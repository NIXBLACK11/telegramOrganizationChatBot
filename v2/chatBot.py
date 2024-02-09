import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import random
import json
import pickle
from laser_encoders import LaserEncoderPipeline

encoder = LaserEncoderPipeline(lang="eng_Latn")

with open('sizes.pkl', 'rb') as file:
    sizes = pickle.load(file)


with open('lables.pkl', 'rb') as file:
    labels = pickle.load(file)

with open('intents.json') as file:
    data = json.load(file)

input_size = sizes[0]
output_size = sizes[1]
hidden_size = sizes[2]

class ChatbotModel(nn.Module):
  def __init__(self, input_size, hidden_size, output_size):
    super(ChatbotModel, self).__init__()
    self.l1 = nn.Linear(input_size, hidden_size)
    self.l2 = nn.Linear(hidden_size, hidden_size)
    self.l3 = nn.Linear(hidden_size, output_size)
    self.relu = nn.ReLU()

  def forward(self, x):
    out = self.l1(x)
    out = self.relu(out)
    out = self.l2(out)
    out = self.relu(out)
    out = self.l3(out)
    return out

state_dict = torch.load('model.pth')
model = ChatbotModel(input_size, hidden_size, output_size)
model.load_state_dict(state_dict)
model.eval()


def chat(user_input):
    user_input = user_input.lower()
    input_bag = encoder.encode_sentences([user_input])[0]

    input_bag = torch.tensor(input_bag, dtype=torch.float32)
    input_bag = input_bag.unsqueeze(0)  # Add a batch dimension

    results = model(input_bag)
    results_index = torch.argmax(results).item()
    tag = labels[results_index]

    for intent in data['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
