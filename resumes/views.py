import os
from django.shortcuts import render
from django.conf import settings
from pypdf import PdfReader
import pandas as pd


def upload_pdf(request):
    if request.method == 'POST':
        pdf_files = request.FILES.getlist('pdf_files')
        combined_dataset = pd.DataFrame(columns=["Text"])

        for pdf_file in pdf_files:
            try:
                # Save the uploaded file temporarily
                file_path = os.path.join(settings.MEDIA_ROOT, pdf_file.name)
                with open(file_path, 'wb') as file:
                    for chunk in pdf_file.chunks():
                        file.write(chunk)

                # Read the PDF file and extract text
                with open(file_path, "rb") as file:
                    pdf_reader = PdfReader(file)
                    page_texts = [page.extract_text() for page in pdf_reader.pages]

                # Decide whether it's a CV or JD based on filename or other criteria
                is_cv = "resume" in pdf_file.name.lower() or "cv" in pdf_file.name.lower()

                # Create a row for the combined dataset
                row = {"Text": ''.join(page_texts)}
                combined_dataset = pd.concat([combined_dataset, pd.DataFrame([row])], ignore_index=True)

            except Exception as e:
                # Handle errors (e.g., PDF parsing error)
                print(f"Error processing {pdf_file.name}: {str(e)}")

            finally:
                # Delete the temporary file
                if os.path.exists(file_path):
                    os.remove(file_path)

        # Save the combined dataset to a CSV file
        csv_file_path = os.path.join(settings.MEDIA_ROOT, 'combined_dataset.csv')
        combined_dataset.to_csv(csv_file_path, mode='a', header=False, index=False)  # Append data
        return render(request, 'result.html', {'csv_file_path': csv_file_path})

    return render(request, 'upload.html')


def home(request):
    return render(request, 'upload.html')

