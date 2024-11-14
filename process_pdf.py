import requests

def download_pdf(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open("downloaded.pdf", "wb") as f:
            f.write(response.content)
        print("PDF downloaded successfully.")
    else:
        print("Failed to download PDF.")
        return

    # Add your text extraction code here if needed
    # This can use a library like PyMuPDF or pdfminer.six
    # For example:
    extracted_text = "Sample extracted text from PDF"
    print(extracted_text)
    return extracted_text
