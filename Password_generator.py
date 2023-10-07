logo='''
  _______          _______     _____                           _             
 |  __ \ \        / /  __ \   / ____|                         | |            
 | |__) \ \  /\  / /| |  | | | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 |  ___/ \ \/  \/ / | |  | | | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |      \  /\  /  | |__| | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 |_|       \/  \/   |_____/   \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
'''
print(logo)
import random
alphabets=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=["!","@","#","$","%","^","&","*","(",")","_"]
letters=int(input("How many Letters you want in the Password?"))
num=int(input("How many Numbers you want in the Password?"))
symbol=int(input("How many Symbols you want in the Password?"))
pwd_list=[]
for i in range(1,letters+1):
  pwd_list.append(random.choice(alphabets))
for i in range(1,num+1):
  pwd_list.append(random.choice(numbers))
for i in range(1,symbol+1):
  pwd_list.append(random.choice(symbols))
random.shuffle(pwd_list)
emp=""
for ch in pwd_list:
  emp+=ch
print(f"Your Password is {emp}")
