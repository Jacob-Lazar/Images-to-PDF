import streamlit as st
from PIL import Image
import img2pdf
import io

# Title of the app
st.title('Image to PDF converter')

# Upload images
uploaded_files = st.file_uploader("Choose Images", accept_multiple_files=True)

if st.button('Convert to PDF'):
    if uploaded_files:
        # Convert images to RGB mode
        images = [Image.open(uploaded_file).convert('RGB') for uploaded_file in uploaded_files]

        # Convert images to PDF
        pdf_bytes = img2pdf.convert([image.tobytes() for image in images])

        # Create a link to download the PDF
        st.download_button(
            label="Download PDF",
            data=pdf_bytes,
            file_name='output.pdf',
            mime='application/pdf',
        )
    else:
        st.write("No images uploaded")
