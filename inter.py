import chat
import mongoOp

l = False
id = -1

def response(input):
    if(input=="login" or l == True):
        pass
        # if l==False:
        #     l = True
        #     return "Enter the login and password\nexamlpe:\ntest\ntest@123"
        # else:
        #     id = mongoOp.caller(input)
        #     if(id!=-1):
        #         return "insert the correct credentials"
    else:
        res, tag = chat.resp(input)
        if(tag=="balance_enquiry"):
            return mongoOp.caller(input)
        elif(tag=="latest_updates"):
            return mongoOp.caller(input)
        elif(tag=="interest_rates"):
            return mongoOp.caller(input)
        elif(tag=="bye"):
            return(res)
        else:
            return(res)

while(True):
    ques = input("input->")
    output = response(ques)
    print(output)