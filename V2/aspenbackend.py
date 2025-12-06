#create email list for the emailJS
import time as Rabbit
from datetime import datetime
import random
questionscore=0
now=datetime.now
print("Todays date is", now)
TARGET_DATE = datetime.datetime(2026, 3, 20)
#will use email JS in a html frontend to email me the open ended responses
compatibility_score=random.randint(90,100)
if compatibility_score <=95:
    compatibility_text = "The compatibility is close to a good state Soryn is working to make it better"
elif compatibility_score >= 95:
    compatibility_text = "WOW the compatibility is off the charts"
        #email the compatibility answer to me via EmailJS (will be in the HTML file)
print("This website was made By soryntech on Github please do not steal")
psswd=input("What is the Password to accsess this Website")
password = "Shark123"
while psswd != password:
    print("Inccorect password ❌")
    if psswd == password:
        print("Welcome Aspen")
        break
truefalse=input("would you like to continue Y/N")
#questions will follow a while q != answer loop
Rabbit.sleep(2)
#Open ended questions for EmailJS will utilise Openquestion[num] where as normal questions will be AQ or SQ (A = Aspen S=Soryn)
#open ended (EmailJS list) Questions section
Openquestion1=input("How do you feel about soryn in a loving way")
if Openquestion1 == "":
    print("incorrect format please enter somthing")
    Openquestion1=input("How do you feel about soryn in a loving way")
elif Openquestion1 != "":
    print("Confirmed")
    #after ending loop add to the email list
openquestion2 = input("What is your fav thing about soryn?")
if openquestion2 == "":
    print("incorrect format please enter somthing")
    openquestion2=input("How do you feel about soryn in a loving way")
elif openquestion2 != "":
    print("Confirmed")
    #after ending loop add to the email list
#soryn section
Sorynq1=input("What is soryns fav animal")
sorynq1a="Shark"
if Sorynq1 != sorynq1a:
    print("Incorrect answer")
    Rabbit.sleep(1)
    Sorynq1=input("What is soryns fav animal")
elif Sorynq1 == sorynq1a:
    print("Correct answer")
    questionscore=questionscore+1
sorynq2 = input("what is soryn's fav past time")
sorynq2a= "Coding" or "Gaming"
if sorynq2 != sorynq2a:
    print ("Incorrect answer")
elif sorynq2 == sorynq2a:
    print("Correct")
    questionscore=questionscore+1
sorynq3=input("What is Soryn's Special Intrest (we have RPed it before)")
sorynq3a = "Hypnosis"
if sorynq3 != sorynq3a:
    print("Incorrect answer")
    print("hint: its a form of losing control")
    sorynq3=input("What is Soryn's Special Intrest (we have RPed it before)")
elif sorynq3 == sorynq3a:
    print("Correct")
    questionscore = questionscore+1
sorynquestion4=input("Soryn has 2 ferrets what are thier names")
sorynquestion4a="Ozzy and Ollie" or "Ozzie and Ollie" or "Ozzy and Olly" or "Ozzie and Olly"
if sorynquestion4!= sorynquestion4a:
    print("Oh so close")
    print("hint: Oz** and Oll**")
elif sorynquestion4 == sorynquestion4a:
    print("Correct :3")
    questionscore=questionscore+1
#Aspen questions will be questions about Aspen that are open ended (so need to be added to email JS) but about himself
Rabbit.sleep(0.5)
print("these are the questions about you aspen")
Aspnq1=input("Whats your fav food")
if Aspnq1 == "":
    print("Please enter some text")
elif Aspnq1 != "":
    Rabbit.sleep(3)
    print("confirmed")
ASPN_q2=input("Whats your fav place to eat at (like place out to eat at)")
if ASPN_q2 == "":
    print("Invalid answer please enter some text")
elif ASPN_q2 != "":
    Rabbit.sleep(2)
    print("confirmed")
Rabbit.sleep(0.5)
aspen_question3=input("What is your special intrest")
if aspen_question3 == "":
    print("Invalid answer please enter somthing")
elif aspen_question3 != "":
    print("confirmed")
#this is a seperate bday section
if now == TARGET_DATE:
    Sorynbdayq=input("Would you like to wish Soryn a Happy Birthday (Y/N)")
    if Sorynbdayq == "Y":
        print("Sending the happy birthday message")
    elif Sorynbdayq == "N":
        print("Ok :c")
        Rabbit.sleep(1)
if now!=TARGET_DATE:
    print("its not Soryn's birthday")
    #add this to email JS

#testing qscore and comp check
print(questionscore)
print(compatibility_score)
print(compatibility_text)
