import PyPDF2
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def extract_text_from_pdf(pdf_path):
   
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)
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
    tokens = [token for token in tokens if token.isalnum()]
    tokens = [token for token in tokens if len(token) > 1]
    lemmatized_tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens]
    return lemmatized_tokens


def tokenize_text(text):
    return word_tokenize(text)


# tech_skills = ['java', 'data', 'analysis', 'analytics', 'html', 'javascript', 'looker']
tech_skills = ['postman', 'incorta', 'looker', 'java', 'mocha', 'javascript', 'git', 'playwright']


def search_pdf_by_tokens(pdf_folder, tech_skills):
    matched_pdfs = []
    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, filename)
            pdf_text = extract_text_from_pdf(pdf_path)
            pdf_tokens = set(tokenize_text(pdf_text.lower()))
            stop = remove_stop_words(pdf_tokens)
            lemma = tokenize_and_lemmatize(stop)
            # "If there is at least one tech skill present in the lemmatized tokens of the PDF,
            # then consider this PDF as a match and add it to the list of matched PDFs."
            if set(tech_skills).intersection(lemma):
                matched_pdfs.append(pdf_path)
    return matched_pdfs


pdf_folder = './Resumes'
matched_pdf = search_pdf_by_tokens(pdf_folder, tech_skills)

# Create a dictionary to store the count of each skill
skill_count = {skill: 0 for skill in tech_skills}
print(skill_count)
print(type(skill_count))
print(matched_pdf)
# Iterate through all lemmatized tokens from matched PDFs
for pdf in matched_pdf:
    tokens = tokenize_and_lemmatize(remove_stop_words(tokenize_text(extract_text_from_pdf(pdf))))

    # Count the occurrences of each skill in the tokens
    for skill in tech_skills:
        if skill in tokens:
            skill_count[skill] += 1

print(skill_count)
fig, ax = plt.subplots()
bars = ax.bar(skill_count.keys(), skill_count.values())
ax.set_xlabel('Skills')
ax.set_ylabel('Number of Members')
ax.set_title('Number of Members with Each Skill')

# Add data labels on the bars
for bar in bars:
    # Gets the height of the current bar.
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')

plt.show()

df = pd.DataFrame(list(skill_count.items()), columns=['Skill', 'Count'])

# Plot the histogram using Seaborn
plt.figure(figsize=(10, 6))
ax = sns.barplot(x='Skill', y='Count', data=df, palette='viridis')
# Add data labels on the bars
for bar in ax.patches:
    # Gets the height of the current bar.
    yval = bar.get_height()
    # Add the count label on the top of the bar.
    ax.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')
plt.xlabel('Skills')
plt.ylabel('Number of Members')
plt.title('Number of Members with Each Skill')
plt.show()

# Convert skill_count dictionary to a DataFrame
df = pd.DataFrame(list(skill_count.items()), columns=['Skill', 'Count'])

# Plot displot for the distribution of counts
plt.figure(figsize=(12, 6))
sns.set(style="whitegrid")
sns.displot(df['Count'], bins=10, kde=True)

plt.xlabel('Number of Members')
plt.ylabel('Frequency')
plt.title('Distribution of Number of Members for Each Skill')
plt.show()

# print("HIstooo")
# # Plot distribution of counts for each skill
# # plt.figure(figsize=(12, 6))
# # sns.set(style="whitegrid")
# # ax=sns.histplot(data=df, x='Count', bins=10, kde=True, hue='Skill', multiple='stack', palette='viridis')
# # for bar in ax.patches:
# #     height = bar.get_height()
# #     width = bar.get_x() + bar.get_width() / 2
# #     ax.text(width, height, f'{int(height)}', ha='center', va='bottom', fontsize=8)
# #
# # plt.xlabel('Number of Members')
# # plt.ylabel('Frequency')
# # plt.title('Distribution of Number of Members for Each Skill')
# # plt.legend(title='Skills', bbox_to_anchor=(1.05, 1), loc='upper left')
# # plt.show()


