from datetime import datetime
from upper_case import capitalize
@capitalize
def greetings():

    current_time=datetime.now()
    current_hour=current_time.hour
    if(5<=current_hour<12):
        return("good morning")
    elif(12<=current_hour<18):
        return("good after noon")
    else:
        return("good evening")

print(greetings())
    

