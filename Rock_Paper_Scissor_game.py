import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_img=[rock,paper,scissors]
com_mark=0

user_mark=0

def play():
  user=int(input("what do u choose?\n 0 for Rock \n 1 for Paper\n 2 for Scissors"))
  print(game_img[user])
  com=random.randint(0,2)
  print("computer has chosen")
  print(game_img[com])
  global com_mark
  global user_mark
  if(user==0 and com==2):
    user_mark+=1
    print("user won")
  elif(user==2 and com==0):
    com_mark+=1
    print("com won")
  elif(user==2 and com==1):
      user_mark+=1
      print("user won")
  elif(user==1 and com==2):
      com_mark+=1
      print("com won")
  elif(user==1 and com==0):
      user_mark+=1
      print("user won")
  elif(user==0 and com==1):
      com_mark+=1
      print("com won")
  elif(user==com):
      print("draw")

  global ques
  ques=input("Do You wish to continue the game?")
play()
while(ques=="yes"):
  play()
if(ques=="no"):
  print("your results are here!","\n","Here is user's score : ",user_mark,"\n","Here is computer's score :",com_mark)
