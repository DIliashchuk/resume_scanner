import PyPDF2
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy

nltk.download('punkt')
nltk.download('stopwords')


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    return text


def extract_frequent_words(text, min_frequency=5):
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalpha() and word not in stop_words]


    word_counts = nltk.FreqDist(words)
    frequent_words = {word for word, count in word_counts.items() if count > min_frequency}

    return frequent_words

def compute_nlp_similarity(text1, text2):
    nlp = spacy.load("en_core_web_sm")

    doc1 = nlp(text1)
    doc2 = nlp(text2)

    # Compute similarity between two documents (ranges from 0 to 1)
    similarity = doc1.similarity(doc2)
    return similarity

def extract_words_and_similarity(job_description_pdf_path, resume_pdf_path, min_frequency=5):
    job_description_text = extract_text_from_pdf(job_description_pdf_path)
    resume_text = extract_text_from_pdf(resume_pdf_path)

    job_description_words = extract_frequent_words(job_description_text, min_frequency)
    resume_words = extract_frequent_words(resume_text, min_frequency)

    # Calculate NLP similarity for frequent words
    nlp_similarity = compute_nlp_similarity(job_description_text, resume_text)

    return job_description_words, resume_words, nlp_similarity

# Example usage for job description and resume from PDFs
job_description_pdf_path = "JD.pdf"
resume_pdf_path = "CV3.pdf"

job_description_words, resume_words, nlp_similarity = extract_words_and_similarity(job_description_pdf_path, resume_pdf_path)

print("Job Description Frequent Words:", job_description_words)
print("Resume Frequent Words:", resume_words)
print(f"NLP Similarity for Frequent Words: {nlp_similarity:.2%}")
