import streamlit as st

st.set_page_config(page_title="VaayuBot – Ayurvedic Health Scan", layout="centered")

st.title("🌿 VaayuBot – Ayurvedic Health Scanner")
st.write("Simulate your **Prakriti**, **Agni**, **Ama**, and **Vikriti** analysis using traditional Ayurvedic logic.")

# 1. UI for Face Feature Simulation
st.header("👤 Face Features (Simulated)")

face_shape = st.selectbox("Select Face Shape", ["long", "oval", "round"])
skin_type = st.selectbox("Select Skin Type", ["dry", "reddish", "oily"])
eye_type = st.selectbox("Select Eye Type", ["small", "sharp", "large"])
lip_type = st.selectbox("Select Lip Type", ["dry", "medium", "full"])

# 2. UI for Tongue Feature Simulation
st.header("👅 Tongue Features (Simulated)")

tongue_color = st.selectbox("Select Tongue Color", ["pale", "reddish", "normal"])
coating = st.selectbox("Select Tongue Coating", ["none", "thin white", "thick white"])
texture = st.selectbox("Select Tongue Texture", ["smooth", "cracked"])
greasy = st.checkbox("Is the tongue greasy?", value=False)

# 3. Logic Mapping Function
def map_to_ayurvedic_profile(face, tongue):
    # Prakriti Logic
    if face["face_shape"] == "oval" and face["skin_type"] == "reddish":
        prakriti = "🔥 Pitta"
    elif face["face_shape"] == "long" and face["skin_type"] == "dry":
        prakriti = "💨 Vata"
    elif face["face_shape"] == "round" and face["skin_type"] == "oily":
        prakriti = "🌊 Kapha"
    else:
        prakriti = "⚖️ Vata-Pitta (Dual)"

    # Agni Logic
    if tongue["texture"] == "cracked":
        agni = "⚡ Vishama Agni"
    elif tongue["color"] == "reddish" and tongue["coating"] == "none":
        agni = "🔥 Tikshna Agni"
    elif tongue["coating"] == "thick white":
        agni = "❄️ Mandagni"
    else:
        agni = "✅ Sama Agni"

    # Ama Logic
    if tongue["coating"] == "thick white":
        ama = "🚫 High"
    elif tongue["coating"] == "thin white":
        ama = "⚠️ Moderate"
    else:
        ama = "✅ Low"

    # Vikriti Logic
    if tongue["texture"] == "cracked" and face["skin_type"] == "dry":
        vikriti = "💨 Vata Imbalance"
    elif tongue["color"] == "reddish" and face["skin_type"] == "reddish":
        vikriti = "🔥 Pitta Imbalance"
    elif tongue["greasy"]:
        vikriti = "🌊 Kapha Imbalance"
    else:
        vikriti = "✅ Balanced or Mild Fluctuation"

    return prakriti, agni, ama, vikriti

# 4. Analyze Button
if st.button("🔍 Analyze Now"):
    face_data = {
        "face_shape": face_shape,
        "skin_type": skin_type,
        "eye_type": eye_type,
        "lip_type": lip_type
    }
    tongue_data = {
        "color": tongue_color,
        "coating": coating,
        "texture": texture,
        "greasy": greasy
    }

    prakriti, agni, ama, vikriti = map_to_ayurvedic_profile(face_data, tongue_data)

    st.success("✅ Analysis Complete!")
    st.subheader("🧠 Your Ayurvedic Profile")
    st.markdown(f"- **Prakriti:** {prakriti}")
    st.markdown(f"- **Agni Type:** {agni}")
    st.markdown(f"- **Ama Level:** {ama}")
    st.markdown(f"- **Vikriti:** {vikriti}")

    st.subheader("💡 Recommendations")
    if "Vata" in prakriti:
        st.markdown("- Eat warm, moist, grounding foods")
        st.markdown("- Oil massage (Abhyanga) and Vata-balancing herbs like Ashwagandha")
    if "Pitta" in prakriti:
        st.markdown("- Favor cooling, bitter, and sweet foods")
        st.markdown("- Avoid spicy, sour, fermented items")
    if "Kapha" in prakriti:
        st.markdown("- Use light, dry, warming foods")
        st.markdown("- Exercise and stimulate digestion with Trikatu or Pippali")

---

### ✅ How to Run Locally

```bash
pip install streamlit
streamlit run vaayu_chatbot.py
