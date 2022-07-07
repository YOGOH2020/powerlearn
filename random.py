import random
gaze =int(input("Type the highest number you want "))
if gaze <=0:
    print('Please type a number larger than 0 ')
    quit()
else:
    random_number=random.randint(0,gaze)
    print(random_number)
