import mongoOp
import chatBot

def response(input, id):
    tag: str = chatBot.chat(input)
    resp: str = ""

    if(tag=="balance_graph"):
        if(userExists(id)):
            resp = mongoOp.balance_graph(id)
        else:
            resp = "You need to login first"
    else if(tag=="balance_enquiry"):
        if(userExists(id)):
            resp = mongoOp.balance_graph(id)
        else:
            resp = "You need to login first"
    else if(tag=="latest_updates"):
        resp = mongoOp.latest_updates()
    else if(tag=="interest_rates"):
        resp = mongoOp.interest_rates()
    else if(tag=="TimeQuery"):
        resp = 
    else:
        resp = 


    return resp