import chat

def response(input):
    if(input=="login"):
        return("connect to backend")
    else:
        res, tag = chat.resp(input)
        if(tag=="balance_enquiry"):
            return("connect to backend")
        elif(tag=="latest_updates"):
            return("connect to backend")
        elif(tag=="interest_rates"):
            return("connect to backend")
        elif(tag=="bye"):
            return(res)
        else:
            return(res)

while(True):
    ques = input("input->")
    output = response(ques)
    print(output)