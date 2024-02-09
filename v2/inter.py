import mongoOp
import chatBot
import photoWork
from datetime import datetime

def response(input, id):
    resp: str = chatBot.chat(input)

    if(resp=="balance_graph"):
        if(mongoOp.userExists(id)):
            values = [int(i) for i in mongoOp.balanceGraph(id).split(",")]
            resp = photoWork.create_plot(values, id)
        else:
            resp = "You need to login first"
    elif(resp=="balance_enquiry"):
        if(mongoOp.userExists(id)):
            resp = mongoOp.balance(id)
        else:
            resp = "You need to login first"
    elif(resp=="latest_updates"):
        resp = mongoOp.updates()
    elif(resp=="interest_rates"):
        resp = mongoOp.interest()
    elif(resp=="time_query"): 
        resp = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    elif(resp=="documents"):
        resp = mongoOp.documents()

    return resp