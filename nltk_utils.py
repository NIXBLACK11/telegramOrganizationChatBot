import numpy as np
import nltk
# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

def tokenize_text(input_text):
    """
    Split input_text into a list of words/tokens.
    A token can be a word, punctuation character, or number.
    """
    return nltk.word_tokenize(input_text)

def stem_word(word):
    """
    Apply stemming to find the root form of a word.
    Example:
    words = ["organize", "organizes", "organizing"]
    stemmed_words = [stem_word(w) for w in words]
    -> ["organ", "organ", "organ"]
    """
    return stemmer.stem(word.lower())

def create_bag_of_words(tokenized_sentence, vocabulary):
    """
    Generate a bag of words array:
    1 for each word in the vocabulary that exists in the tokenized_sentence, 0 otherwise.
    Example:
    tokenized_sentence = ["hello", "how", "are", "you"]
    vocabulary = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bag_of_words = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """
    # Apply stemming to each word in the tokenized sentence
    stemmed_words = [stem_word(word) for word in tokenized_sentence]
    
    # Initialize the bag with zeros for each word in the vocabulary
    bag = np.zeros(len(vocabulary), dtype=np.float32)
    
    # Set corresponding entries to 1 for words present in the tokenized sentence
    for idx, word in enumerate(vocabulary):
        if word in stemmed_words:
            bag[idx] = 1
    
    return bag
