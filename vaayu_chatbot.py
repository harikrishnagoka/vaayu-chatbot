import streamlit as st
from PIL import Image
import random

# ---- RULE-BASED MOCK MAPPING ---- #

def analyze_face(image):
    # Dummy logic: detect face shape by image name keyword
    image = image.convert("RGB")
    return {
        "face_shape": "long",
        "skin_type": "dry",
        "eye_type": "small"
    }

def analyze_tongue(image):
    # Dummy logic: detect color and coating
    image = image.convert("RGB")
    return {
        "color": "red",
        "coating": "thick white",
        "texture": "cracked"
    }

def map_to_dosha(face, tongue):
    prakriti = "Vata-Pitta" if face["face_shape"] == "long" and tongue["texture"] == "cracked" else "Kapha"
    agni = "Vishama" if tongue["texture"] == "cracked" else "Sama"
    ama = "Moderate" if tongue["coating"] == "thick white" else "Low"
    vikriti = "Vata imbalance" if face["skin_type"] == "dry" else "None"
    return prakriti, agni, ama, vikriti

# ---- STREAMLIT UI ---- #

st.set_page_config(page_title="VaayuBot – Ayurveda Chatbot", layout="centered")

st.title("VaayuBot – Ayurvedic Health Scanner")
st.write("Get your **Prakriti**, **Agni**, and **Ama** evaluated using face and tongue scan!")

face_img = st.file_uploader("Upload your face photo", type=["jpg", "jpeg", "png"])
tongue_img = st.file_uploader("Upload your tongue photo", type=["jpg", "jpeg", "png"])

if st.button("Analyze Now"):
    if face_img and tongue_img:
        with st.spinner("Analyzing with Ayurvedic intelligence..."):
            face_data = analyze_face(Image.open(face_img))
            tongue_data = analyze_tongue(Image.open(tongue_img))
            prakriti, agni, ama, vikriti = map_to_dosha(face_data, tongue_data)

        st.success("Analysis Complete!")
        st.subheader("Your Ayurvedic Profile")
        st.markdown(f"- **Prakriti:** {prakriti}")
        st.markdown(f"- **Agni Type:** {agni}")
        st.markdown(f"- **Ama Level:** {ama}")
        st.markdown(f"- **Vikriti:** {vikriti}")

        st.subheader("Next Steps")
        st.markdown("- Try warm, grounding meals to balance Vata.")
        st.markdown("- Avoid raw/cold foods if agni is Vishama.")
        st.markdown("- Consider herbs like Trikatu or Pippali.")
    else:
        st.warning("Please upload both face and tongue images.")
