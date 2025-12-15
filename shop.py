import streamlit as st
import os
import time

# Page config
st.set_page_config(page_title="Amasoft", page_icon="💻")

# Logo
st.image("images/icon.png", width=300)

# Loading effect
with st.spinner("Starting Amasoft..."):
    time.sleep(1)

# Title
st.markdown(
    "<h1 style='text-align:center;'>💻 Amasoft</h1>",
    unsafe_allow_html=True
)

# Typing effect
text = "Welcome to Amasoft "
placeholder = st.empty()
output = ""

for char in text:
    output += char
    placeholder.markdown(f"### {output}")
    time.sleep(0.05)

st.divider()

if st.button("Survive game"):
    st.session_state.page = "home"






# Info
st.write("📁 You can download games (more coming later)")
st.write("🎮 You can now play Dagu or try the demo")
st.write("❤️ Do you like my games?")

# Debug / info
st.write("Current directory:")
st.code(os.getcwd())

st.write("Files in games/:")
st.code(os.listdir("games"))

# Download button
zip_path = os.path.join("games", "dagu_demo.zip")

if os.path.exists(zip_path):
    with open(zip_path, "rb") as file:
        st.download_button(
            label="⬇️ Download for macOS",
            data=file,
            file_name="dagu_demo.zip",
            mime="application/zip"
        )
else:
    st.error("dagu_demo.zip not found!")

