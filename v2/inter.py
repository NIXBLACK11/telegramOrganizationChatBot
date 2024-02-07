import mongoOp
# import chatBot
from datetime import datetime

def response(input, id):
    # tag: str = chatBot.chat(input)
    tag = "time_query"
    resp: str = ""

    if(tag=="balance_graph"):
        if(mongoOp.userExists(id)):
            resp = mongoOp.balanceGraph(id)
        else:
            resp = "You need to login first"
    elif(tag=="balance_enquiry"):
        if(mongoOp.userExists(id)):
            resp = mongoOp.balance(id)
        else:
            resp = "You need to login first"
    elif(tag=="latest_updates"):
        resp = mongoOp.updates()
    elif(tag=="interest_rates"):
        resp = mongoOp.interest()
    elif(tag=="time_query"): 
        resp = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    else:
        resp = "noooo"


    return resp