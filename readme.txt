# Initialize an empty set to store the hashes of the uploaded documents
uploaded_hashes = set()

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()  # Read bytes directly
    hash_of_uploaded_file = hashlib.sha256(bytes_data).hexdigest()

    # Check if the hash of the uploaded file already exists in the set of uploaded hashes
    if hash_of_uploaded_file in uploaded_hashes:
        st.error("This document already exists.")
    else:
        file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)

        # Save the uploaded PDF if it's not a duplicate
        with open(file_path, 'wb') as f:
            f.write(bytes_data)

        # Add the hash of the uploaded file to the set of uploaded hashes
        uploaded_hashes.add(hash_of_uploaded_file)

        # Continue processing the PDF
        metadata = extract_pdf_metadata(file_path)

        # Rest of the processing code...
