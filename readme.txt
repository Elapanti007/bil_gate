# Predefined lists of valid metadata attributes
valid_authors = ["Not available", "Bharti Airtel Limited"]
valid_creators = [
    "Chromiue", "Bharti Airtel Limited",
    "JasperReports Library version 6.14.0-2ab0d8625be255bf609c78e1181801213e51db8f",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
    "dvips(k) S.95a Copyright 2005 Radical Eye Software", "Not available"
]
valid_producers = [
    "GPL Ghostscript 8.78", "Skia/PDF #119",
    "OpenPDF 1.3.28", "Not available",
    "1Text 2.1.7 by 1T3XT; modified using iText 7.1.12 02000-2020 1Text Group IV (AGPL-version)"
]

def check_metadata(metadata):
    # Extracting necessary metadata fields
    author = metadata.get('Author', 'Not available')
    creator = metadata.get('Creator', 'Not available')
    producer = metadata.get('Producer', 'Not available')
    creation_date = metadata.get('CreationDate', '')
    mod_date = metadata.get('ModDate', '')

    # Initialize a list to store failure reasons
    failure_reasons = []

    # Checking metadata validity
    dates_match = creation_date == mod_date
    author_ok = author in valid_authors
    creator_ok = creator in valid_creators
    producer_ok = producer in valid_producers

    # Check each condition and add failure reason if necessary
    if not dates_match:
        failure_reasons.append("Creation and modification dates do not match")
    if not author_ok:
        failure_reasons.append(f"Invalid author: {author}")
    if not creator_ok:
        failure_reasons.append(f"Invalid creator: {creator}")
    if not producer_ok:
        failure_reasons.append(f"Invalid producer: {producer}")

    # Return overall result and failure reasons
    return author_ok and creator_ok and producer_ok and dates_match, failure_reasons

# Example usage
metadata_example = {
    'Author': 'Bharti Airtel Limited',
    'Creator': 'Invalid Creator',
    'Producer': 'GPL Ghostscript 8.78',
    'CreationDate': '20230101',
    'ModDate': '20230101'
}

result, reasons = check_metadata(metadata_example)
print("Check result:", result)
print("Failure reasons:", reasons)


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
