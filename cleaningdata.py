from nltk.tokenize import word_tokenize
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

    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stop words and stem the tokens
    tokens = [stemmer.stem(token)
              for token in tokens if token not in stop_words]

    # Return the preprocessed text
    return ' '.join(tokens)


# Read data from a .txt file
with open('Medical_data.txt', 'r') as file:
    text = file.read()

# Preprocess the text data
preprocessed_text = preprocess(text)
print(preprocessed_text)
# Open a new file in write mode
with open('preprocessed_data.txt', 'w') as file:
    # Write the preprocessed text to the file
    file.write(preprocessed_text)
