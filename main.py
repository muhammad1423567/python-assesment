from random import randint
from time import time
  
  #Asking user's if they want to know the rules of game?
def rules():
    rules = input("Do you want to read the rules? press 'y' for rules or 'n' to continue : ")
    if rules == 'yes' or rules == 'y':
        print("To play you will be ask how many rounds you would want to play. /n Once you have \nchosen your rounds you will recive questions to answer./nEvery question you get \ncorrect you will earn 1 point if you get any question incorrect you wont recive any points. Enjoy the game!")
    else:
        print("You may continue without the rules.")
#asking user how many round they would like to play
def get_range():
    global num, total #where are you using these to determine no of rounds?
    while True:
        try:
            num = int(input("Please enter the amount of rounds you'd like to play : "))
            if 0<num<= 6:
                total=num
                print("got it.")              
                break
            else:
                print("The max is 6 and the minimum is 1")
        except:
            pass

          
#Asking users name.
print("welcome to my quiz")
#Ask for name
while True:
    name = input("Enter your name : ")
    if name.isalpha():
        break
    print("please enter characters A-Z only")

print('hello',name)
rules()

#Asking the user if they are ready for the quiz
ready=input("Are you ready for the quiz?:press y to continue or any other key to exit:")
if ready=="y" or ready=="yes":
   print("Let's continue")
else:
   print('thank you')
   exit()
       
get_range()


print('Enjoy a math quiz.')
num_right = +1
num_wrong = 0
sum_answer_time = 0

while True:
    num1 = randint(2, 9)
    num2 = randint(11, 99)
    product = num1 * num2
    total -=1 # this is to take away a qustion from the rounds chosen each time a question is asked
    start_time = time()
    response = input(f'What is {num1} * {num2}? ')
    #if not response: #why do you break the loop if user doesnt enter an answer? you should only break if rounds are down to 0
    if total == 0:
        break
    try:
        answer = int(response)
        elapsed = time() - start_time
        if answer == product:
            print(f'Right, in {elapsed:.2f} seconds')
            num_right += 1
            sum_answer_time += elapsed
        else:
            print(f'Wrong, the answer was {product}')
            num_wrong += 1
    except ValueError:
        print('You entered something other than an integer')

print('You got ' + str(num_right) + ' right and ' + str(num_wrong) + ' wrong. Average time for right answers: ' + str(sum_answer_time / num_right))
please_enter = input("Press q to exit:") 
