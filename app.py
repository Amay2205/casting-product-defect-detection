import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

st.title("Casting Product Defect Detection")
st.write("Upload a casting product image to predict whether it is defective or normal.")

model_path = "/content/drive/MyDrive/CNN_project/casting_cnn_model.keras"
model = tf.keras.models.load_model(model_path)

st.success("Model loaded successfully!")

uploaded_file = st.file_uploader("Upload a casting image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image")

    image = image.resize((128, 128))
    image_array = np.array(image)
    image_array = np.expand_dims(image_array, axis=0)

    prediction = model.predict(image_array, verbose=0)[0][0]

    if prediction >= 0.5:
        result = "Normal"
        confidence = prediction
    else:
        result = "Defective"
        confidence = 1 - prediction

    st.subheader(f"Prediction: {result}")
    st.write(f"Confidence: {confidence * 100:.2f}%")
