import streamlit as st
import os
import time

st.image("        images/icon.png", width=450)
time.sleep(1)


st.title("                💻 Amasoft")


text = "Welcome to Dagu Game"

placeholder = st.empty()
output = ""

for char in text:
    output += char
    placeholder.markdown(output)
    time.sleep(0.05)


st.write("Current directory:")
st.write("You can down load games with will be added latter")
st.write("You can now play dagu or open dagu demo")
st.write("Do you like my games")
st.write(os.getcwd())

st.write("Files in games/:")
st.write(os.listdir("games"))

zip_path = os.path.join("games", "dagu_demo.zip")

with open(zip_path, "rb") as file:
    st.download_button(
        label="Download for macOS",
        data=file,
        file_name="dagu_demo.zip",
        mime="application/zip"
    )

