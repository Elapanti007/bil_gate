import re

def find_name_in_qr_data(qr_data):
    name_patterns = [r'CustomerName:\s{0,2}(\b[A-Z\s]+\b)', r'name=\s*([A-Za-z\s]+)',r'Name=\s*([A-Za-z\s]+)',r'customername=\s*([A-Za-z\s]+)']
    for pattern in name_patterns:
        for data in qr_data:
            match = re.search(pattern, data)
            if match:
                return match.group(1)
    return "No name found"

def find_total_amount_in_qr_data(qr_data):
    amount_patterns = [r'Amount:\s*Rs\.\s*\d+\.\d{2}', r'TotalInvAmt=\d+\.\d{2}',]
    for pattern in amount_patterns:
        for data in qr_data:
            match = re.search(pattern, data)
            if match:
                return match.group()
    return "No amount found"
