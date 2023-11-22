import random

def guess(x):
    
    random_number = random.randint(1, x)
    number_guess = 0
    while number_guess != random_number:
        number_guess = int(input(f"Enter a number between 1 and {x}:"))
        if number_guess < random_number:
            print("Too low")
        elif number_guess > random_number:
            print("Too high")
    print(f'You have got the jackpot the random number was{random_number}')
    
def computer_gess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
      
        feedback = input(f' Is {guess} too high (H), too low (L) or correct(L)'.lower())
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay! The computer guessed your number {guess} correctly ')
    
def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's' ])
    
    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user, computer):
        return f'Congratulations you won this round with {computer}'
    return "Sorry you lost this time!"

def  is_win(player, oppoent):
    if (player== 'r' and oppoent == 's') or (player == 's' and oppoent == 'p')\
        or (player == 'p' and oppoent == 'r'):
            
     return True
print(play())
    
        


            