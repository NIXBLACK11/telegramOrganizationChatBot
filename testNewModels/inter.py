import mongoOp
import chatBot

def response(input, id):
    tag: str = chatBot.chat(input)
    resp: str = ""
    if(tag.split(" ")[1]!="backend"):
        resp = tag.random()
    else:
        if(tag bina login):
            resp = mongoOp.func()
        else:
            if(mongoOp.userExists(id)):
                if(tag==""):
            else:
                resp = "For this you need to login first"


    return resp