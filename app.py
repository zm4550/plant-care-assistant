import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import random

# --- STYLE SETTINGS ---
st.set_page_config(page_title="Plant Care Assistant", layout="centered")

# Custom CSS for Sage Green background and nicer fonts
st.markdown("""
    <style>
    .stApp {
        background-color: #DAE5D0;
    }
    h1, h2, h3, p, span, div {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #3A4D39;
    }
    .stButton>button {
        background-color: #4F6F52;
        color: white;
        border-radius: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATA ---
potential_fixes = [
    "Apply organic Neem Oil spray to the leaves in the evening.",
    "Gently wipe the leaves with a mixture of mild soap and filtered water.",
    "Prune the affected leaves to prevent further spread.",
    "Use a copper-based fungicide according to the package directions.",
    "Add a small dose of balanced liquid fertilizer to the soil.",
    "Inspect the undersides of the leaves for pests and remove manually.",
    "Improve air circulation by moving the plant to a more open area.",
    "Check soil moisture; consider reducing watering frequency."
]

@st.cache_resource
def load_my_model():
    model = tf.keras.models.load_model("keras_model.h5", compile=False)
    with open("labels.txt", "r") as f:
        # Removes numbers from labels (e.g., "0 Healthy" becomes "Healthy")
        labels = [line.strip().split(' ', 1)[-1] for line in f.readlines()]
    return model, labels

model, labels = load_my_model()

# --- UI LAYOUT ---
st.title("plant care🌿")
st.write("Upload a photo below for an instant health check.")

file = st.file_uploader("Choose a leaf image", type=["jpg", "png", "jpeg"])

if file:
    # Keep image smaller (300 pixels wide)
    image = Image.open(file).convert("RGB")
    st.image(image, width=300)
    
    if st.button("Analyze Health"):
        # Image Processing
        size = (224, 224)
        img_input = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
        img_array = np.asarray(img_input)
        normalized_image_array = (img_array.astype(np.float32) / 127.5) - 1
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        data[0] = normalized_image_array

        # Prediction
        prediction = model.predict(data)
        index = np.argmax(prediction)
        result_name = labels[index]
        
        # Get the percentage (Confidence)
        confidence = prediction[0][index] * 100

        st.markdown("---")

        # Display Result with Percentage
        if "Healthy" in result_name:
            st.success(f"Result: **HEALTHY** ({confidence:.1f}% confidence)")
            st.write("Recommended Action: Keep maintaining current care routine.")
        else:
            st.error(f"Result: **DEFECT DETECTED** ({confidence:.1f}% confidence)")
            # Picks one solution from the list
            suggested_fix = random.choice(potential_fixes)
            st.info(f"**Recommended Action:** {suggested_fix}")