print("lets perform a simple ")
x=[1,2,3,4,5,6,7,8,9,0,"+","-","*","/","="]
logi = '''                                                          
           | |          | |     | | (_)            
   ___ __ _| | ___ _   _| | __ _| |_ _  ___  _ __  
  / __/ _` | |/ __| | | | |/ _` | __| |/ _ \| '_ \ 
 | (_| (_| | | (__| |_| | | (_| | |_| | (_) | | | |
  \___\__,_|_|\___|\__,_|_|\__,_|\__|_|\___/|_| |_|


                                                       '''
print(logi)
for c in range(1):
  print("\t\t\t"," -------",)
for c in range(1):
  print("\t\t\t","|",x[c],x[c+1],x[c+2],"|")
for c in range(1):
 print("\t\t\t","|",x[c+3],x[c+4],x[c+5],"|")
for c in range(1):
 print("\t\t\t","|",x[c+6],x[c+7],x[c+8],"|")
for c in range(1):
 print("\t\t\t","|",x[c+9],x[c+10],x[c+11],"|")
for c in range(1):
  print("\t\t\t","|",x[c+12],x[c+13],x[c+14],"|")
for c in range(1):
  print("\t\t\t"," -------",)
def calc():
  a=int(input("Enter a number"))
  b=int(input("Enter another number"))
  op=input("Enter the Arithemetic operation + or - or * or /")
  if(op=="+"):
      print(a+b)
  if(op=="-"):
      print(a-b)
  if(op=="*"):
      print(a*b)
  if(op=="/"):
      print(round(a/b,2))
  global ques
  ques=input("Do you wanna continue the calculation?")
ques="yes"
calc()
while(ques=="yes"):
  calc()
if(ques=="no"):
  print("Thank you!")
