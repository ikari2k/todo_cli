import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

uploaded_file = st.file_uploader('Upload image')

with st.expander('Start Camera'):
    # Start the camera 
    camera_image = st.camera_input('Camera')

if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    gray_img = img.convert('L')

    # Render the grayscale image on the webpage
    st.image(gray_img)

if uploaded_file:
    img = Image.open(uploaded_file)
    gray_img = img.convert('L')
    st.image(gray_img)