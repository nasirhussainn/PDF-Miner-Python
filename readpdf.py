from pdfminer.high_level import extract_text

# Path to the PDF file
pdf_path = r'C:\Users\Nasir\Documents\Django\Nasir Hussain Resume.pdf'

# Extract text from the PDF
text = extract_text(pdf_path)

# Print the extracted text
print(text)
