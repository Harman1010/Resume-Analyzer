import pdfplumber

def read_pdf(file_input):
    text = ""
    try:
        if file_input is None:
            return ""

        # Works for both file path and Gradio file object
        pdf = pdfplumber.open(file_input)

        with pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

    except Exception as e:
        print("PDF ERROR:", e)
        return ""

    return text