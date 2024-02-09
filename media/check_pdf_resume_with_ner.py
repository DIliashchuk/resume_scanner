import spacy
import PyPDF2

# Replace 'path/to/trained_model' with the actual path to your trained model directory
model_path = '/Users/dmytroiliashchuk/LearnML/ML_AI/resume_project/media'

# Load the trained model
nlp = spacy.load(model_path)

# Function to extract text from PDF using PyPDF2
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)  # Use len(pages) instead of numPages
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]  # Use pages instead of getPage
            text += page.extract_text()
    return text

# Example: Process text from a PDF file
pdf_path = 'CV4.pdf'
pdf_text = extract_text_from_pdf(pdf_path)


# Process the text with the trained model directly
doc = nlp(pdf_text)

# Access named entities in the processed document
for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")

