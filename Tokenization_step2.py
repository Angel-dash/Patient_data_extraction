# the data is stored as a list of sintences where each sentence is a list of tokens
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import re
import nltk

nltk.download('punkt')


# Load the stop words
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Initialize the stemmer
stemmer = PorterStemmer()

# Define a function to preprocess the text


def preprocess(text):
    # Convert the text to lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(r'[^\w\s]', '', text)

    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Tokenize each sentence into words and remove stop words and stem the tokens
    preprocessed_sentences = []
    for sentence in sentences:
        tokens = word_tokenize(sentence)
        tokens = [stemmer.stem(token)
                  for token in tokens if token not in stop_words]
        preprocessed_sentences.append(tokens)

    # Return the preprocessed text as a list of sentences where each sentence is a list of tokens
    return preprocessed_sentences


# Read data from a .txt file
with open('Medical_data.txt', 'r') as file:
    text = file.read()

# Preprocess the text data
preprocessed_text = preprocess(text)
print(preprocessed_text)
# Open a new file in write mode
with open('preprocessed_data.txt', 'w') as file:
    # Write the preprocessed text to the file
    for sentence in preprocessed_text:
        file.write(' '.join(sentence) + '\n')
