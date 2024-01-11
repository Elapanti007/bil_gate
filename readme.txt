

import os
import csv
import hashlib
import streamlit as st

# Define the path for the CSV file
CSV_FILE_PATH = "uploaded_hashes.csv"

# Check if the CSV file exists, if not, create it
if not os.path.exists(CSV_FILE_PATH):
    with open(CSV_FILE_PATH, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["hash"])

# Load existing hashes from the CSV file into a set
with open(CSV_FILE_PATH, "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    uploaded_hashes = set(row[0] for row in csv_reader if row)  # Ensure there are rows in the CSV

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

        # Add the hash of the uploaded file to the set and the CSV file
        uploaded_hashes.add(hash_of_uploaded_file)
        with open(CSV_FILE_PATH, "a", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([hash_of_uploaded_file])

        # Continue processing the PDF
        metadata = extract_pdf_metadata(file_path)

        # Rest of the processing code...

ji# Initialize an empty set to store the hashes of the uploaded documents
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

        # Rest of the processing code..






import os
import csv
import hashlib
import streamlit as st

# Define the path for the CSV file
CSV_FILE_PATH = "uploaded_hashes.csv"

# Check if the CSV file exists, if not, create it
if not os.path.exists(CSV_FILE_PATH):
    with open(CSV_FILE_PATH, "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["hash"])

# Load existing hashes from the CSV file into a set
with open(CSV_FILE_PATH, "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    uploaded_hashes = set(row[0] for row in csv_reader)

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

        # Add the hash of the uploaded file to the set and the CSV file
        uploaded_hashes.add(hash_of_uploaded_file)
        with open(CSV_FILE_PATH, "a") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([hash_of_uploaded_file])

        # Continue processing the PDF
        metadata = extract_pdf_metadata(file_path)

        # Rest of the processing code...
.
