import os,time
name=str(input("Enter your name "))
print(f"Welcome {name} to my computer game")
time.sleep(2)
if os.name=='nt':
    os.system('cls')
else:
    os.system('clear')
playing=input("Do you want to play my game? ")
time.sleep(2)
if playing !="yes":
    quit()
print(f"Okay {name} lets play ") 
if os.name=='nt':
    os.system('cls')
else:
    os.system('clear')
print("All answers should be in lower cases")
time.sleep(2)
if os.name=='nt':
    os.system('cls')
else:
    os.system('clear')
ans=str(input(' Are you vaccinated? '))
time.sleep(2)
if os.name=='nt':
    os.system('cls')
else:
    os.system('clear')
if playing !="yes":
    print('Youre protected ')
else:
    print(f'You should get vaccinated {name} ')
if os.name=='nt':
    os.system('cls')
else:
    os.system('clear')
quiz_one=str(input(f'What is cpu? {name}'))
time.sleep(2)
if os.name=='nt':
    os.system('cls')
else:
    os.system('clear')
if quiz_one=='central processing unit':
    print('CORRECT!')
else:
    print('Wrong?')

