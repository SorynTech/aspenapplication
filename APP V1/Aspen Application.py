#Code for Aspen
import requests
import time as Rabbit
import datetime
import random
def compmatch():
    return random.randint(90,100)
    #testing ignore
print(compmatch)
now = datetime.datetime.now()
#testing ignore 
print(now)
TARGET_DATE = datetime.datetime(2026, 3, 20)
print("Please put all answers in Lowercase")

user=input("What username/name do you want to be refered to as")
if user == "Aspen":
    print("Identity Confirmed Please type continue to continue")
    continue_user=input("Do you want to continue")
    if continue_user == "continue":
        print("Ok welcome to The Program that Soryn Made for you")
        Rabbit.sleep(3)
        ASPNquestion1=input("What is your favourite colour?")
        if ASPNquestion1 == "purple":
            print("See told you", referal,"I knew your fav colour")
        elif ASPNquestion1 == "black":
           print("See told you", referal,"I knew your fav colour")
        else:
            print("Sowee i didnt know your fav colour")
            Rabbit.sleep(3)
        ASPNquestion2=input("Is your OC species a xoltulum?")
        if ASPNquestion2 == "yes":
            print("well they are the most adorable xoltulum I know :3 <3")
        else:
            print("stop lyingggg")
        ASPNquestion3 = input("How do you feel about soryn")
        
    #for testing not real webhook
    webhook_url = "https://discord.com/api/webhooks/1445185110210252891/bv55IvhK6VdnwyO-W5of0NBfMcIHzM6vOk6hkECITL5N1NQO9jKdkt35PDDVw4a2SYC1"
    print("message sent to Webhook to soryn :3")
    Rabbit.sleep(3)
    data={"content": f'💕 **Aspen answered your third question as:** "{ASPNquestion3}"'}
    requests.post(webhook_url, json=data)
    #continuing quesitons from here
    Rabbit.sleep(3)
    if now.date() == TARGET_DATE.date():
        ASPNquestion4=input("Did you Know its Soryn's Birthday")
        if ASPNquestion4 == "yes":
            print("I knew you wouldnt forget")
        else:
            print("Awh you forgot :c")
    #incase not bday
    ASPNquestion4a= input("Whats Soryn's Fav colour")
    if ASPNquestion4a == "blue":
        print("See you know me so well")
    else:
        print("wowwww didnt even know my fav colour")
    ASPNquestion5 = int(input("how much do you think soryn Loves you"))
    if ASPNquestion5 > 100:
        print("The number has to be between 1 and 100")
    else:
        #for testing not real webhook
        webhook_url= "https://discord.com/api/webhooks/1445185110210252891/bv55IvhK6VdnwyO-W5of0NBfMcIHzM6vOk6hkECITL5N1NQO9jKdkt35PDDVw4a2SYC1"
        data={"content": f'💕 **Aspen said that he thinks you love him  out of % as :** "{ASPNquestion5}"'}
        requests.post(webhook_url,json=data)
    #Questions mainly about soryn with new variable names
    sQ1=input("What do you think is soryn's Fav Animal")
    if sQ1 == "ferret":
        print("Yesss")
        Rabbit.sleep(1)
        SQ1a=input("How many Ferrets does Soyrn own")
        if SQ1a == "2":
            print("Yayyy you know Soryn So well")
        else:
            print("you dont know soryn that well")
        Rabbit.sleep(1)
        sqa1b= input("What are the ferrets names")
        if sqa1b == "Ozzy and Ollie":
            print("Yay you know soyrn the best", referal)
    Rabbit.sleep(1)
    sQ2=input("Whats soryn's MAIN species for OC")
    if sQ2 == "Demon":
        print("You two must Know each other great")
    else:
        print("its Demon sillies but I know theres a lot")
    print("A: Python")
    Rabbit.sleep(2)
    print("B: C++")
    Rabbit.sleep(2)
    print("C: PHP")
    Rabbit.sleep(2)
    print("D: C#")
    Rabbit.sleep(2)
    Sq3=input("Whats soryn's main programming langauge")
    if Sq3 == "a":
        print("Holy Fuck you Know soryn so well")
    else:
        print("not suprised you didnt know but its python")
    #compatibility check:
    compatibility_score=compmatch()
    compmatch=int
    if compatibility_score < 95:
        Compatibility = "Wow you are", compatibility_score, "%" "compatible this is good for you two and soryn is working on making it better"
    elif compatibility_score > 95:
        Compatibility = "WOW you and Soryn are", compatibility_score,"%", "compatible this is amazing it means you two are great together"
    print(compatibility_score, "%")
    print(Compatibility)
#Question 2 section
#Variable naming conventions:
#a=aspen s=soryn
q2a=input("what is your Fav game to play with Soryn")
if q2a == "Marvel Rivals":
    print("Oh thats the best choice :3")
else:
    print("thats also a really good choice and im sure soryn would love it :3")
q2s=input("Whats soryn's Fav Marvel Rivals character (If you say Jeff refer to him as Shark)")
if q2s == "shark":
    print("You know Soryn the best i see why your compatibile")
else:
    print("I see why you would say that as they also play", q2s, "a lot")
q3a = input("Whats your favourite animal")
if q3a == "Axolotl":
    print("OMG axolotls are soooo cute ")
else:
    print("OMG they are so cute too")
q3s = input("What is soryn's 2nd fav animal")
if q3s == "shark":
    print("Sharks are amazing but you are more amazing <3")
else:
    print("well even though that animal is amazing your better :3c")

q4s=input("If you and soryn where to be stranded what would happen")
while q4s == "":
    print("Please enter text into the text box (try again)")
    if q4s != "":
        break
#discord again
webhook_url="https://discord.com/api/webhooks/1445185110210252891/bv55IvhK6VdnwyO-W5of0NBfMcIHzM6vOk6hkECITL5N1NQO9jKdkt35PDDVw4a2SYC1"
data={"content:"f'💞 ** Aspen said that if you 2 where stranded that:"{q4s} would happen"'}
requests.post(webhook_url,data)

Rabbit.sleep(5)
    
q4a=input("What do you think soryn feels about you (you can be honest)")
#input validation
while q4a == "":
    print("please enter somthing")
    if q4a != "":
        break
Rabbit.sleep(5)
#discord again
webhook_url="https://discord.com/api/webhooks/1445185110210252891/bv55IvhK6VdnwyO-W5of0NBfMcIHzM6vOk6hkECITL5N1NQO9jKdkt35PDDVw4a2SYC1"
data=("content:"f'💞 ** Aspen said that he feels like you feel :"{q4a} about him"')
requests.post(webhook_url,data)

Rabbit.sleep(0.5)
specialintrestsaspn=input("Whats your special intrest")
while specialintrestsaspn == "":
    print("please enter somthing")
    if specialintrestsaspn != "":
        break

ocspecies=input("Why is your oc a xoltulm")
while ocspecies == "":
    print("Please enter text")
    if ocspecies != "":
        break

webhook_url= "https://discord.com/api/webhooks/1445185110210252891/bv55IvhK6VdnwyO-W5of0NBfMcIHzM6vOk6hkECITL5N1NQO9jKdkt35PDDVw4a2SYC1"
data={"content:"f'💞 ** Aspen said answered :"{specialintrestsaspn} to the Specialintrests question"'}
requests.post(webhook_url,json=data)
Rabbit.sleep(10)
webhook_url= "https://discord.com/api/webhooks/1445185110210252891/bv55IvhK6VdnwyO-W5of0NBfMcIHzM6vOk6hkECITL5N1NQO9jKdkt35PDDVw4a2SYC1"
data={"content:"f'💞 ** Aspen said answered :"{ocspecies} to the oc species question"'}
requests.post(webhook_url,json=data)

favfood=input("what is your favourite food")
while favfood == "":
    print("Please enter some text")
    if favfood != "":
        break
    
webhook_url= "https://discord.com/api/webhooks/1445185110210252891/bv55IvhK6VdnwyO-W5of0NBfMcIHzM6vOk6hkECITL5N1NQO9jKdkt35PDDVw4a2SYC1"
data={"content": f'💕 **Aspen said his fav food is :** "{favfood}"'}

favplacetoeat=input("Out of any resteraunt where would you like to eat the most")
while favplacetoeat == "":
    print("Please enter somthing")
    if favplacetoeat != "":
        break
webhook_url= "https://discord.com/api/webhooks/1445185110210252891/bv55IvhK6VdnwyO-W5of0NBfMcIHzM6vOk6hkECITL5N1NQO9jKdkt35PDDVw4a2SYC1"
data={"content": f'💕 **Aspen said his fav place to eat  is :** "{favplacetoeat}"'}

requests.post(webhook_url,json=data)

favanimatedmovie=input("whats your favourite animated movie")
while favanimatedmovie == "":
    print("Please Enter somthing")
    if favanimatedmovie != "":
        break 
webhook_url= "https://discord.com/api/webhooks/1445185110210252891/bv55IvhK6VdnwyO-W5of0NBfMcIHzM6vOk6hkECITL5N1NQO9jKdkt35PDDVw4a2SYC1"
data={"content": f'💕 **Aspen said his fav Animted movie is :** "{favanimatedmovie}"'}


#ADD MORE QUESTIONS AT SOME POINT



finalquestion=input("send a message to soryn about if you want to be with him")
#for testing not real webhook
webhook_url= "https://discord.com/api/webhooks/1445185110210252891/bv55IvhK6VdnwyO-W5of0NBfMcIHzM6vOk6hkECITL5N1NQO9jKdkt35PDDVw4a2SYC1"
data={"content": f'💕 **Aspen said about wanting to be with you:** "{finalquestion}"'}
requests.post(webhook_url,json=data)






#To close the terminal once needed
exit()
print("Program Terminated")
