print("Started")
import cv2
import numpy as np
from keras.models import load_model
print("Library Imported")
# Load the trained model
model = load_model("WeaponIdentifier.h5")
print("Model Loaded")
# Function to preprocess the image for prediction
def preprocess_image(image_path):
    img = cv2.imread(image_path)  # Read the image
    img = cv2.resize(img, (250,250))  # Resize to the model's input shape
    img = img / 255.0  # Normalize pixel values
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

# Function to make predictions
def predict_image(image_path):
    print("Predicting...")
    preprocessed_img = preprocess_image(image_path)
    prediction = model.predict(preprocessed_img)[0, 0]  # Get the predicted probability
    return prediction
print("Functions Defined")
# Path to the image you want to test
image_path_to_test = "eval_Knife/009.jpg"

# Make a prediction
prediction_result = predict_image(image_path_to_test)

# Threshold for binary classification
threshold = 0.5

# Convert probability to class label
if prediction_result >= threshold:
    class_label = 1
    obj = "Knife"
else:
    class_label = 0
    obj = "Pistol"

# Print the result
print("Predicted Probability:", prediction_result)
print("Predicted Class:", class_label)
print("Predicted object is :{}".format(obj))