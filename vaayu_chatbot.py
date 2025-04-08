import streamlit as st
from PIL import Image
import random

# ---- RULE-BASED MOCK MAPPING ---- #

def analyze_face(image):
    # Simulated rules based on facial observation (mock logic)
    return {
        "face_shape": "oval",
        "skin_type": "reddish",
        "eye_type": "sharp",
        "lip_type": "medium"
    }

def analyze_tongue(image):
    # Simulated tongue features
    return {
        "color": "reddish",
        "coating": "thin white",
        "texture": "cracked",
        "greasy": False
    }

def map_to_dosha(face, tongue):
    # Prakriti estimation
    if face["face_shape"] == "oval" and face["skin_type"] == "reddish":
        prakriti = "Pitta"
    elif face["face_shape"] == "long" and face["skin_type"] == "dry":
        prakriti = "Vata"
    elif face["face_shape"] == "round" and face["skin_type"] == "oily":
        prakriti = "Kapha"
    else:
        prakriti = "Vata-Pitta"

    # Agni detection
    if tongue["texture"] == "cracked":
        agni = "Vishama Agni"
    elif tongue["color"] == "reddish" and tongue["coating"] == "none":
        agni = "Tikshna Agni"
    elif tongue["coating"] == "thick white":
        agni = "Mandagni"
    else:
        agni = "Sama Agni"

    # Ama level
    if tongue["coating"] == "thick white":
        ama = "High"
    elif tongue["coating"] == "thin white":
        ama = "Moderate"
    else:
        ama = "Low"

    # Vikriti detection
    if tongue["texture"] == "cracked" and face["skin_type"] == "dry":
        vikriti = "Vata imbalance"
    elif tongue["color"] == "reddish" and face["skin_type"] == "reddish":
        vikriti = "Pitta imbalance"
    elif tongue["greasy"]:
        vikriti = "Kapha imbalance"
    else:
        vikriti = "Mild dosha fluctuation"

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
