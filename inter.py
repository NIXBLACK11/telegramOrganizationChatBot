import chat
import mongoOp

id = "NULL"

def response(input, l):
    global id
    if(l==True):
        id = mongoOp.caller(input, "do")
        if(id=="-1"):
            return "Unable to login press /login and put correct username and password ex:test test@123"
        else:
            return "Successfully logged in!" 
    else:
        res, tag = chat.resp(input)
        if(tag=="balance_enquiry" and id=="NULL"):
            return "First you need to login to login type /login"
        elif(tag=="balance_enquiry" and id!="NULL"):
            return mongoOp.caller(tag, id)
        elif(tag=="latest_updates"):
            return mongoOp.caller(tag, "")
        elif(tag=="interest_rates"):
            return mongoOp.caller(tag, "")
        elif(tag=="quit"):
            id="NULL"
            return(res)
        else:
            return(res)

# while(True):
#     ques = input("input->")
#     output = response(ques, True)
#     print(output)
#     ques = input("input->")
#     output = response(ques, False)
#     print(output)