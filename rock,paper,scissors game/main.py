import  random

while True: 
   choices = ["R", "P", "S"]

   computer = random.choice(choices)
   user = None

   while user not in choices:
    user= input( f' Pick an option between "R", "P","S":')
    user= user.upper()
    if  user == "R" or user == "P" or user == "S":
    
      print(f"user({user.upper()}): Computer({computer.upper()})")
         
    else: 
        print(" Error:The character you entered is not recognised")
        continue

  

    if user == computer:
     
      print ("Tie! restart")
      continue

    elif user == "R" :
      if computer == "P":
         
         print ("Computer won! Paper beats Rock")
         print ("Game over")

      if computer =="S":
         
        print ("You win! Rock beats Scissors")
        print ("Game over")

    elif user == "S" :
      if computer == "R":
        
        print ("Computer won! Rock beats Scissors")
        print ("Game over")

      if computer =="P":
        
        print ("You win! Scissors beats paper")
        print ("Game over")

    elif user == "P" :
      if computer == "S":
         
         print ("Computer won! Scissors beats Paper")
         print ("Game over")
         
      if computer =="R":
        
        print ("You win! Paper beats Rock")
        print ("Game over")    

    play_again = input("play again?(yes/no):").lower()

   
   if play_again!= "yes":
    break

    
print ("bye,Thank you!")
