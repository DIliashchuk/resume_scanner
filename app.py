import streamlit as st
from PyPDF2 import PdfReader
import openai


openai.api_key = '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'

def extract_text_from_pdf(pdf_file):
    text = ''
    pdf_reader = PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text += page.extract_text() or ''
    return text


st.title('Resume Analyzer')

resume_file = st.file_uploader("Upload Resume (PDF)", type=['pdf'])
jd_file = st.file_uploader("Upload Job Description (PDF)", type=['pdf'])


@st.cache_data
def analyze_resume_with_job_description(cv_text, jd_text):
    prompt = f"Analyze this resume against the job description: \n\nJob Description:\n{jd_text}\n\nResume:\n{cv_text}\n\nProvide a percentage match and recommendations for improvement."

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
            {"role": "system", "content": "You are a helpful assistant."}
        ]
    )

    return response.choices[0].message.content


    return completion_text


# Process files and display analysis
if resume_file and jd_file:
    with st.spinner('Analyzing...'):
        cv_text = extract_text_from_pdf(resume_file)
        jd_text = extract_text_from_pdf(jd_file)

        cv_text_clean = ' '.join(cv_text.split())
        jd_text_clean = ' '.join(jd_text.split())

        analysis_result = analyze_resume_with_job_description(cv_text_clean, jd_text_clean)

        st.write(analysis_result)
