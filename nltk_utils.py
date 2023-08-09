import numpy as np
import nltk
# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

def tokenize(sentence):
    """
    Split a sentence into an array of words/tokens.
    A token can be a word, punctuation character, or number.
    """
    return nltk.word_tokenize(sentence)

def stem(word):
    """
    Apply stemming to find the root form of a word.
    Example:
    words = ["organize", "organizes", "organizing"]
    stemmed_words = [stem(w) for w in words]
    -> ["organ", "organ", "organ"]
    """
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, words):
    """
    Generate a bag of words array:
    1 for each known word that exists in the tokenized_sentence, 0 otherwise.
    Example:
    tokenized_sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bag = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """
    # Apply stemming to each word in the tokenized sentence
    sentence_words = [stem(word) for word in tokenized_sentence]
    
    # Initialize the bag with zeros for each word in the vocabulary
    bag = np.zeros(len(words), dtype=np.float32)
    
    # Set corresponding entries to 1 for words present in the tokenized sentence
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1
    
    return bag
