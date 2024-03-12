import PyPDF2
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import os


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as pdf_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Get the number of pages in the PDF
        num_pages = len(pdf_reader.pages)

        # Extract text from each page
        text = ""
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    return text


def remove_stop_words(tokens):
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    return filtered_tokens


def tokenize_and_lemmatize(tokens):
    lemmatizer = WordNetLemmatizer()
    # tokens = word_tokenize(text)
    tokens = [token for token in tokens if token.isalnum()]
    # Remove single alphabet tokens
    tokens = [token for token in tokens if len(token) > 1]
    lemmatized_tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens]
    return lemmatized_tokens


def tokenize_text(text):
    # Tokenize the text using NLTK
    return word_tokenize(text)


user_input = input("Enter skills (comma-separated): ")
input_skills = set(skill.strip().lower() for skill in user_input.split(','))


def search_pdf_by_tokens(pdf_folder, input_skills):
    # Iterate through each file in the specified folder
    matched_pdfs = []
    for filename in os.listdir(pdf_folder):
        # Check if the file is a PDF
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, filename)

            # Extract text from the PDF
            pdf_text = extract_text_from_pdf(pdf_path)

            # Tokenize the text and convert to lowercase for case-insensitive matching
            pdf_tokens = set(tokenize_text(pdf_text.lower()))
            print(pdf_tokens)
            print(len(pdf_tokens))
            stop = remove_stop_words(pdf_tokens)
            print(f"length of tokens without stop words {len(stop)}")
            lemma = tokenize_and_lemmatize(stop)

            print(f"length of lemma words {len(lemma)}")

            # Check if the input tokens are a subset of PDF tokens
            if set(input_skills).issubset(lemma):
                matched_pdfs.append(pdf_path)
                for ln in lemma:
                    print(ln)
                # return pdf_path  # Return the matched PDF path

    return matched_pdfs


pdf_folder = './vz_data'
# Search for a matching PDF
matched_pdf = search_pdf_by_tokens(pdf_folder, input_skills)

# Display the result
if matched_pdf:
    print("Matching PDFs found:")
    for pdf in matched_pdf:
        print(f"Matching PDF found: {pdf}")
else:
    print("No matching PDF found.")
