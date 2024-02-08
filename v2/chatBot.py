from laser_encoders import LaserEncoderPipeline
import torch
import json

model = torch.load('./model.pth', map_location=torch.device('cpu'))
encoder = LaserEncoderPipeline(lang="eng_Latn")

with open('intents.json') as file:
    data = json.load(file)

def chat(user_input):
    user_input = user_input.lower()
    input_bag = encoder.encode_sentences([user_input])[0]

    input_bag = torch.tensor(input_bag, dtype=torch.float32).to(device)
    input_bag = input_bag.unsqueeze(0)

    results = model(input_bag)
    results_index = torch.argmax(results).item()
    tag = labels[results_index]

    for intent in data['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])