#import os    #From Stack Overflow

#Planning types of questions asked:
  #Store hours
  #Location
  #Type of products/availability
  #Prices of products

#Chatbot introduction
print("Hello there! ")
print("Thank you for visiting our store's website. ")
print("\nI'm Chatsy, a chatbot designed to answer questions regarding our business. ")

#Chatbot instuctions
#def question():
print("\n\n")
prompt = print("What are you needing inquiry about?", end='') #end= From Stack Overflow
userQuestion = input(": ")
#question()

#Checking for keywords
def answer():
  #Store hours
  if(userQuestion == "What are the business hours?"):
    print("\nOur business operates from 9AM to 8PM, Monday through Saturday.\nOn Sundays, we operate from 12PM to 7PM.")

answer()

#Defining continuation options
userChoice = input('\nDo you have any more questions? \nType "C" or "c" to ask a question. \nOr type "Q" or "q" to quit. \n:')

def qOrC():
  if userChoice == "C" or "c":
    print("\nWhat is your next question?")
    #os.system('clear')    #From Stack Overflow
    #question()
  elif userChoice == "Q" or "q":
    print("Thank you for your time. Goodbye! ")
qOrC()

#while word in question == "hour" || "hours":
  