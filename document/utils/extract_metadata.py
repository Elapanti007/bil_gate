import fitz 
import PyPDF2

def extract_pdf_metadata(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            metadata = reader.metadata
            document_info = {
                'Title': metadata.get('/Title', 'Not available'),
                'Author': metadata.get('/Author', 'Not available'),
                'Subject': metadata.get('/Subject', 'Not available'),
                'Keywords': metadata.get('/Keywords', 'Not available'),
                'Creator': metadata.get('/Creator', 'Not available'),
                'Producer': metadata.get('/Producer', 'Not available'),
                'CreationDate': metadata.get('/CreationDate', 'Not available'),
                'ModDate': metadata.get('/ModDate', 'Not available'),
                'Trapped': metadata.get('/Trapped', 'Not available')
            }
            return document_info
    except Exception as e:
        return f"An error occurred: {e}"