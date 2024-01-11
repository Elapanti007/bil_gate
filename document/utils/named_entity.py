import spacy
from spacy.matcher import Matcher

# Load the pre-trained spaCy model
nlp = spacy.load("en_core_web_sm")

# Define the text to be analyzed
text = "Service: Excell Broadband InvoiceNumber: 16082956 Invoice Date: 1 Dec 2023 Custnum: 54554 CustomerName: MOSES PRABHAKAR ATHOTA Phone: 9701514514 Amount: Rs. 588.82"

# Process the text with the spaCy model
doc = nlp(text)

# Initialize the spaCy Matcher
matcher = Matcher(nlp.vocab)

# Define the pattern to match the customer name
pattern = [{"LOWER": "customername"}, {"IS_PUNCT": True}, {"ENT_TYPE": "PERSON"}]

# Add the pattern to the matcher
matcher.add("CUSTOMER_NAME", [pattern])

# Apply the matcher to the processed text
matches = matcher(doc)

# Extract the matched spans
for match_id, start, end in matches:
    matched_span = doc[start:end]
    print(matched_span.text)
