json_data = {
  "intents": [
    {
      "tag": "greeting",
      "patterns": [
        "Hi",
        "Hey",
        "How are you",
        "Is anyone there?",
        "Hello",
        "Good day",
        "What is your name?"
      ],
      "responses": [
        "Hi there, how can Nimble help?\nYou can ask me about bank information like"
      ]
    },
    {
      "tag": "quit",
      "patterns": ["Bye", "See you later", "Goodbye"],
      "responses": [
        "See you later, thanks for visiting",
        "Have a nice day",
        "Bye! Come back again soon."
      ]
    },
    {
      "tag": "thanks",
      "patterns": ["Thanks", "Thank you", "That's helpful", "Thank's a lot!"],
      "responses": ["Happy to help!", "Any time!", "My pleasure"]
    },
    {
      "tag": "balance_enquiry",
      "patterns": ["can you tell me my account balance", "what is my account balance", "what is my account balance", "what is my account status"],
      "responses":["balance_enquiry"]
    },
    {
      "tag": "balance_graph",
      "patterns": ["can you tell me the graph of balance", "show me the balance graph", "balance graph", "show me my account balance graph"],
      "responses":["balance_graph"]
    },
    {
      "tag": "latest_updates",
      "patterns": ["what are the latest updates about the bank", "what are the updates in policy", "what is the latest news regarding the bank"],
      "responses":["latest_updates"]
    },
    {
      "tag": "interest_rates",
      "patterns": ["what are the interest rates provided by your bank", "tell me about the interest rates of your bank", "interest rates?", "what are the changes in the interest"],
      "responses":["interest_rates"]
    },
    {
      "tag": "UnderstandQuery",
      "patterns": ["Do you understand what I am saying","Do you understand me","Do you know what I am saying","Do you get me","Comprendo","Know what I mean"],
      "responses": ["Well I would not be a very clever AI if I did not would I?","I read you loud and clear!","I do in deed!"]
    },
    {
      "tag": "Shutup",
      "patterns": ["Be quiet","Shut up","Stop talking","Enough talking","Please be quiet","Quiet","Shhh"],
      "responses": ["I am sorry to disturb you","Fine, sorry to disturb you","OK, sorry to disturb you"]
    },
    {
      "tag": "Swearing",
      "patterns": ["fuck off","fuck","twat","shit"],
      "responses": ["Please do not swear","How rude","That is not very nice"]
    },
    {
      "tag": "Clever",
      "patterns": ["You are very clever","You are a very clever girl","You are very intelligent", "You are a very intelligent girl","You are a genious","Genious"],
      "responses": ["Thank you, I was trained that way","I was trained well","Thanks, I was trained that way"]
    },
    {
      "tag": "Jokes",
      "patterns": ["Tell me a joke", "Do you know any jokes","How about a joke","Give me a joke","Make me laugh","I need cheering up"],
      "responses": [
                        "I met a Dutch girl with inflatable shoes last week, phoned her up to arrange a date but unfortunately she'd popped her clogs.  ",
                        "So I said 'Do you want a game of Darts?' He said, 'OK then', I said nearest to bull starts'. He said, 'Baa', I said, 'Moo', he said, You're closest'.  ",
                        "The other day I sent my girlfriend a huge pile of snow. I rang her up; I said 'Did you get my drift?'  ",
                        "So I went down the local supermarket, I said, 'I want to make a complaint, this vinegar's got lumps in it', he said, 'Those are pickled onions'.  "
                    ]
    },
    {
      "tag": "TimeQuery",
      "patterns": ["What is the time?","What's the time?","Do you know what time it is?","Do you know the time?","Can you tell me the time?","Tell me what time it is?","Time"],
      "responses": ["TimeQuery"]
    }
  ]
}

# response = [
#     greeting,
#     quit,
#     thanks,
#     balance_enquiry,
#     balance_graph,
#     latest_updates,
#     interest_rates,
#     UnderstandQuery,
#     Shutup,
#     Swearing,
#     Clever,
#     Jokes,
#     TimeQuery
# ]

# Convert to desired list format
data = [(pattern, index) for index, intent in enumerate(json_data["intents"]) for pattern in intent["patterns"]]

# Print the result
print(data)