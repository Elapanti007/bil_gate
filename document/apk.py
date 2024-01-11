import streamlit as st
import os
import io
import hashlib

from utils.document_hash import calculate_hash
from utils.document_upload import upload_document
from utils.extract_gstin import extract_gstin
from utils.extract_text import extract_text_from_pdf
from utils.extract_metadata import extract_pdf_metadata
from utils.metadata_checker import check_metadata
from utils.qr_code_extractor import extract_images_and_decode_qr
from utils.qr_code_name_extractor import find_name_in_qr_data
# Set the upload folder and maximum content length
UPLOAD_FOLDER = 'uploads/'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB upload limit
os.makedirs(UPLOAD_FOLDER, exist_ok=True)



# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()  # Read bytes directly
    hash_of_uploaded_file = hashlib.sha256(bytes_data).hexdigest()

    # Check if file with the same hash exists
    is_duplicate = any(
        hash_of_uploaded_file == calculate_hash(os.path.join(UPLOAD_FOLDER, existing_filename))
        for existing_filename in os.listdir(UPLOAD_FOLDER)
    )

    if is_duplicate:
        st.error("This document already exists.")
    else:
        file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)

        # Save the uploaded PDF if it's not a duplicate
        with open(file_path, 'wb') as f:
            f.write(bytes_data)

        # Continue processing the PDF
        metadata = extract_pdf_metadata(file_path)

        # Check if metadata is available
        if all(value == 'Not available' for value in metadata.values()):
            st.write("No metadata available for this document.")
        else:
            st.json(metadata)
        is_good = check_metadata(metadata)
        qr_contents = extract_images_and_decode_qr(file_path, UPLOAD_FOLDER)
        pdf_text = extract_text_from_pdf(file_path)
        name_from_qr = find_name_in_qr_data(qr_contents)
        gstin = extract_gstin(pdf_text)
        

        # Display extracted name
        st.write("Name from QR Code Data:")
        st.write(name_from_qr)

        # Check if the extracted name is in the PDF text
        if name_from_qr in pdf_text:
            st.success("Name from QR code is present in the PDF text.")
        else:
            st.warning("Name from QR code is NOT present in the PDF text.")



        # Display results
        st.success("Document uploaded successfully.")
        st.json(metadata)

        if is_good:
            st.success("Metadata is good.")
        else:
            st.warning("Metadata check failed.")

        st.write("QR Contents:")
        st.write(qr_contents)

        st.write("Extracted Text:")
        st.write(pdf_text)

        if gstin:
            st.write("Extracted GSTIN:")
            st.write(gstin)
