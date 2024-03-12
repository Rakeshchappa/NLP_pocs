import PyPDF2
from nltk.tokenize import word_tokenize


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

    # Print the extracted text
    return text


def tokenize_text(text):
    # Tokenize the text using NLTK
    return word_tokenize(text)


path = './Resumes/Rakesh_resume_Feuji.pdf'

# Extract text from the PDF
pdf_text = extract_text_from_pdf(path)

# Tokenize the text and convert to lowercase for case-insensitive matching
pdf_tokens = set(tokenize_text(pdf_text.lower()))


# print("Extracted Text:", pdf_text)
#
# # Print the tokens
# print("PDF Tokens:", pdf_tokens)


def find_matching_tokens(pdf_tokens, input_skills):
    # Find tokens that match the input skills
    matching_tokens = set(token for token in pdf_tokens if token.lower() in input_skills)
    non_matching_tokens = set(skills for skills in input_skills if skills.lower() not in pdf_tokens)

    return matching_tokens,non_matching_tokens


# def find_matching_tokens(pdf_tokens, input_skills):
#     # Find tokens that match the input skills
#     matching_tokens = set()
#     non_matching_tokens = []
#
#     for token in pdf_tokens:
#         is_match = False
#         for skill in input_skills:
#             if token == skill:
#                 matching_tokens.add(token)
#                 is_match = True
#
#                 break  # Break out of the inner loop once a match is found
#
#         if not is_match:
#          non_matching_tokens.append(skill)
#     print(f" not matched tokens:{non_matching_tokens}")
#     print(f" matched tokens:{matching_tokens}")
#     return matching_tokens, non_matching_tokens


user_input = input("Enter skills (comma-separated): ")
input_skills = set(skill.strip().lower() for skill in user_input.split(','))

m_tokens, non_m_tokens = find_matching_tokens(pdf_tokens, input_skills)
print(m_tokens)
if m_tokens:
    print("Matching Tokens:", m_tokens)
else:
    print("No matching tokens found.")

if non_m_tokens:
    print("Non-Matching Tokens:", non_m_tokens)
else:
    print("All tokens matched with input skills.")

# m_tokens = find_matching_tokens(pdf_tokens, input_skills)
#
# if m_tokens:
#     print("Matching Tokens:", m_tokens)
# else:
#     print("No matching tokens found.")
# non_matching_tokens incorta,low,html,linux,rakesh,ramesh,rajesh,vinod
#***********************************************************************
