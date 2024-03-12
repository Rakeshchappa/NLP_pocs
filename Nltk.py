text = """Here’s to the crazy ones, the misfits, the rebels, the troublemakers, 
the round pegs in the square holes. The ones who see things differently — they’re not fond of 
rules. You can quote them, disagree with them, glorify
or vilify them, but the only thing you can’t do is ignore them because they
change things. They push the human race forward, and while some may see them
as the crazy ones, we see genius, because the ones who are crazy enough to think
that they can change the world, are the ones who do."""

print(text.split())
print(type(text.split()))
#  split() method doesn’t consider punctuation symbols as a separate token.
#  This might change your project results.
# 2nd Method Using nltk module
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
# . Its primary purpose is to convert a collection of text documents into a matrix of token counts
# Text Vectorization: It transforms a collection of text documents into a sparse matrix representation where each row corresponds to a document, each column corresponds to a unique word (token), and the matrix's values represent the word frequencies in each document.
#
# Feature Extraction: The resulting matrix can be used as input for machine learning models, such as classifiers. Each document's word frequencies become features that the model can use to learn patterns and make predictions.
#
# Word Tokenization: It automatically tokenizes input text into words. It handles common tasks like removing punctuation, converting text to lowercase, and breaking text into individual words.
#
# Stop Words Removal: The stop_words parameter allows you to specify a list of common words (stop words) that should be excluded from the tokenization process. This can help focus on more meaningful words.
from sklearn.feature_extraction.text import CountVectorizer

word_tokenizes = word_tokenize(text)
print(type(word_tokenize(text)))
print(len(word_tokenize(text)))
print("HIHIHIHHIH")
print(word_tokenizes)
# df = pd.DataFrame({'author': ['jobs', 'gates'], 'text':text})
# print(f"Rakesh df:{df.to_string()}")
# cv = CountVectorizer(stop_words='english')
# print(f"cv means{cv}")
#
# cv_matrix = cv.fit_transform(df['text'])
# print(f"cv_matrix{cv_matrix}")
# df_dtm = pd.DataFrame(cv_matrix.toarray(), index=df['author'].values, columns=cv.get_feature_names_out())
# print(df_dtm.to_string())
# frequncy of this tokens


Fdist = FreqDist()
for i in word_tokenizes:
    Fdist[i] = Fdist[i] + 1
print(type(Fdist))
# Convert FreqDist items to a list of tuples
result_list = list(Fdist.items())

# Print the list of tuples
print(result_list)
# for word, frequency in Fdist.items():
#     print(f"{word}: {frequency}")
top_10 = Fdist.most_common(10)
print(top_10)

# stemming
# it is the process of reducing a word to its word stem by cutting off the begining or the end
from nltk.stem import PorterStemmer

pst = PorterStemmer()
print(pst.stem("Winning"), pst.stem("buying"), pst.stem("studies"))

# Lemmatisation is a process of reducing words into their lemma (a meaning full) or dictionary
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
words_to_lemma = ['studies', 'giving', 'cats', 'geese']
for i in words_to_lemma:
    print(lemmatizer.lemmatize(i))

#  the pos_tag function to perform part-of-speech tagging on a list of words.
# identifiy the parts of speeachs list of words
from nltk import pos_tag

text = "This is RakeshChappa I am working as a dataAnalyst in Feuji in vizag."
words = word_tokenize(text)
pos_tags = pos_tag(words)
print(pos_tags)
nouns = []
for word, pos in pos_tags:
    if pos in ['NN', 'NNS', 'NNP', 'NNPS']:
        nouns.append(word)

print(f"nouns{nouns}")
from nltk import ne_chunk

from nltk.corpus import stopwords

text1 = "This is RakeshChappa i am working in Vishakapatanam."
words = word_tokenize(text1)
pos_tags1 = pos_tag(words)
entity_named = ne_chunk(pos_tags1)
print(entity_named)


def remove_stop_words(tokens):
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in tokens if word not in stop_words]

    return filtered_words


data = remove_stop_words(words)
stop_words_removed = [word for word in words if word not in data]

print(f" stop words {stop_words_removed}")
print(f"without stop words {data}")
stop_words = set(stopwords.words('english'))
stop_words1 = stopwords.words('english')
print(len(stop_words1))
print(len(stop_words))
print(f"list of stop words are:{stop_words}")


