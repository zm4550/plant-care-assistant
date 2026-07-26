# 🌿 Plant Care Assistant

A simple Streamlit web app that checks the health of a plant leaf from a photo using a Keras image classification model. Upload a leaf image and get an instant "Healthy" or "Defect Detected" result, along with a suggested care action.

## Features

- Upload a leaf photo (JPG/PNG)
- Runs inference with a pre-trained Keras model (`keras_model.h5`)
- Displays confidence score for the prediction
- Suggests a care action if a defect is detected

## Getting Started

### Prerequisites

- Python 3.9+

### Installation

```bash
git clone https://github.com/<your-username>/plant-care-assistant.git
cd plant-care-assistant
pip install -r requirements.txt
```

### Run the app

```bash
streamlit run app.py
```

Then open the URL shown in your terminal (usually `http://localhost:8501`).

## Project Structure

```
.
├── app.py            # Streamlit application
├── keras_model.h5     # Trained Keras model
├── labels.txt          # Class labels
└── requirements.txt    # Python dependencies
```

## Model

The model was trained to classify leaf images into two classes:

- `Healthy`
- `Sick`

## Tech Stack

- [Streamlit](https://streamlit.io/) — web app framework
- [TensorFlow / Keras](https://www.tensorflow.org/) — model inference
- [Pillow](https://python-pillow.org/) — image processing

## License

This project is open source and available under the [MIT License](LICENSE).
