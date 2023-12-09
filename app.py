import streamlit as st
from PIL import Image
import img2pdf

# Title of the app
st.title('Images to PDF converter')

# Upload images
uploaded_files = st.file_uploader("Choose Images", accept_multiple_files=True)

if st.button('Convert to PDF'):
    if uploaded_files:
        images = [Image.open(uploaded_file) for uploaded_file in uploaded_files]

        # Convert images to PDF
        pdf_bytes = img2pdf.convert([image.filename for image in images])

        # Create a link to download the PDF
        st.download_button(
            label="Download PDF",
            data=pdf_bytes,
            file_name='Image_to_PDF.pdf',
            mime='application/pdf',
        )
    else:
        st.write("No images uploaded")
