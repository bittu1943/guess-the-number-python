import random

def game():
    count = 0
    computer_gen_value = random.randint(1,100)
    
    
    while count<10 :

        user_input = input("enter your guess:")

        try:
            user_input = int(user_input)


            
            if user_input > computer_gen_value:
                print("your guess is way too high.")
                count = count + 1
                print("trials:",count) 
                
            elif user_input < computer_gen_value:
                print ("your guess is way to low")
                count = count + 1
                print("trials:",count)

            elif not(int(user_input)):
                print ('please enter a number.')
                count = count + 1
                print("trials:",count)

            elif user_input == computer_gen_value:
                print('you win')
                count = count + 1
                print("trials:",count)
                print("it took you",count,"trials")
                break

        except ValueError:
            
            print("please enter an integer.")
            count = count + 1
            print("trials:",count)

    else:   
        print("you lose,you have lost all your trials.")
    play_again = input("wanna play again:").lower()
    if play_again == "yes":
        game()
    
            

game()
  
        



