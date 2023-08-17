
while input!="exit":
 input=input(">")
 if input.lower()=="help":
    print("Star- to start the car "
          "Stop- to stop the car "
          "quit- to exit the game")
 elif input.lower()=="start":
    print("Car started ready to go")
 elif input.lower()=="stop":
    print("Car stopped.")

