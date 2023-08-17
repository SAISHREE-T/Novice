secret_num=9
trial_num=1

while trial_num<=3:
  guess=int(input("Guess:"))
  if guess==secret_num:
   print("You win!")
   break

  trial_num+=1
else:
    print("You lose!")
