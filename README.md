# Industrial Casting Product Defect Detection

## 🚀 Live Demo

👉 [Try the Live Streamlit App](https://casting-appuct-defect-detection-lmbsrntnnzwoav4jwrafeh.streamlit.app/)

Upload a casting product image and get a prediction of **Defective** or **Normal** with confidence.

A CNN-based deep learning project that classifies industrial casting products as **Defective** or **Normal** using computer vision.

## Problem Statement

In manufacturing industries, detecting defective casting products is an important quality-control task. Manual inspection can be time-consuming and may lead to inconsistent results.

This project uses a Convolutional Neural Network (CNN) to automatically classify casting product images into two categories:

- Defective
- Normal

## Dataset

The project uses the **Real-Life Industrial Dataset of Casting Product**.

- Training images: 6,633
- Test images: 715
- Total images: 7,348
- Training split: 80% training, 20% validation

## Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Google Colab

## CNN Architecture

- Input: 128 × 128 × 3
- Conv2D: 32 filters
- MaxPooling2D
- Conv2D: 64 filters
- MaxPooling2D
- Conv2D: 128 filters
- MaxPooling2D
- Flatten
- Dense: 128 neurons
- Dropout: 0.5
- Output: 1 neuron with Sigmoid activation

## Results

**Test Accuracy: 98.74%**

| Actual / Predicted | Defective | Normal |
|---|---:|---:|
| Defective | 449 | 4 |
| Normal | 5 | 257 |

## Streamlit Application

The application allows a user to upload a casting image and receive a prediction of **Defective** or **Normal**, along with a confidence score.

## Project Workflow

```text
Casting Image
      ↓
Image Preprocessing
      ↓
CNN Model
      ↓
Feature Extraction
      ↓
Classification
      ↓
Defective / Normal
      ↓
Confidence Score
```

## Project Structure

```text
casting-product-defect-detection/
├── app.py
├── README.md
├── requirements.txt
└── casting_cnn_model.keras
```

## Future Improvements

- Data augmentation
- Transfer learning with models such as MobileNetV2, EfficientNet or ResNet
- Grad-CAM explainability
- Testing on more diverse real-world images
- Deployment to a cloud platform

## Conclusion

This project demonstrates the use of CNN-based computer vision for automated industrial casting quality inspection. The model achieved **98.74% test accuracy** and was integrated with Streamlit for image-based predictions.
