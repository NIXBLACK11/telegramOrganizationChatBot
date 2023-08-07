import random
import json

import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
#  This line loads the model's state dictionary with the state dictionary stored in the 'model_state' variable.
model.load_state_dict(model_state)
model.eval()

def resp(sentence):
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    # The line X = torch.from_numpy(X).to(device) converts the numpy array 'X' to a torch tensor and sends it to the specified device (e.g. CPU or GPU)
    X = torch.from_numpy(X).to(device)

    output = model(X)
    # The line _, predicted = torch.max(output, dim=1) gets the maximum value from the 'output' tensor along the 1st dimension and assigns the index of this maximum value to the variable 'predicted'
    _, predicted = torch.max(output, dim=1)
    # The line tag = tags[predicted.item()] gets the tag associated with the index 'predicted' from the 'tags' list
    tag = tags[predicted.item()]
    # he purpose of using the softmax function here is to convert the raw scores or logits in output into probabilities for each class.
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                if(tag=="balance_graph" or tag=="balance_enquiry"):
                    if "graph" in sentence:
                        tag = "balance_graph"
                    else:
                        print("balance enquiry")
                        tag = "balance_enquiry"
                reply =''
                reply = random.choice(intent['responses'])
                # print(f"{reply}")
                return reply, tag
    else:
        return "I do not understand...", None