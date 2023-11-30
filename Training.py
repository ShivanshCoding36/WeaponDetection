print("Started")
from os import listdir
print('Library Imported')
import cv2
print('Library Imported')
from numpy import array
print('Library Imported')
from keras import Sequential
print('Library Imported')
from keras.layers import Dense, Flatten, MaxPool2D, Conv2D
print('Library Imported')

#Data Preparation
Xtrain = []
Ytrain = []
# Knives = 1
# Pistols = 0
for k in listdir('Knife'):
    img_path = f'Knife/{k}'
    img = cv2.imread(img_path)
    
    if img is not None:
        data = img / 255.0
        Xtrain.append(data)
        Ytrain.append(1)
print("First")
# Similarly for the 'Pistol' directory
for p in listdir('Pistol'):
    img_path = f'Pistol/{p}'
    img = cv2.imread(img_path)
    
    if img is not None:
        data = img / 255.0
        Xtrain.append(data)
        Ytrain.append(0)
print("Second")
#print(Xtrain)
#print(Ytrain)
#Evaluation Data Preparation
Xtest = []
Ytest= []

#Knifes = 1
#Pistols = 0

for k in listdir('eval_Knife'):
    img_path = f'eval_Knife/{k}'
    img = cv2.imread(img_path)
    
    if img is not None:
        data = img / 255.0
        Xtrain.append(data)
        Ytrain.append(1)
print("Third")
# Similarly for the 'Pistol' directory
for p in listdir('eval_pistol'):
    img_path = f'eval_pistol/{p}'
    img = cv2.imread(img_path)
    
    if img is not None:
        data = img / 255.0
        Xtrain.append(data)
        Ytrain.append(0)
print("Fourth")
print(len(Xtrain))
print(len(Ytrain))
print(len(Xtest))
print(len(Ytest))
print("Building Model")
model = Sequential([
    Conv2D(filters=16, kernel_size=(3,3), activation='relu', input_shape=(250,250,3)),
    MaxPool2D((5,5)),
    Conv2D(filters=32, kernel_size=(3,3), activation='relu'),
    MaxPool2D((3,3)),
    Flatten(),
    Dense(64,activation='relu'),
    Dense(1, activation='sigmoid')
])
print("Compiling Model")
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)
print("Training Model")
x = array(Xtrain).astype(float)
y = array(Ytrain).astype(int)
model.fit(x, y, epochs=5) #Ranned twice
print("Evaluating Model")
XEval = array(Xtest).astype(float)
YEval = array(Ytest).astype(int)
if XEval and YEval:
    model.evaluate(XEval,YEval)
predicted = model.predict(x).flatten()
predicted[predicted >= 0.6] = 1
predicted[predicted < 0.4] = 0
predicted[(0.6 > predicted) & (predicted > 0.4)] = 2

model.save("WeaponIdentifier.h5")
print("Model saved as WeaponIdentifier.h5")


print("Done\nBye")