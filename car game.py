
input1=""
started=False
while True:
    input1 = input("> ").lower()
    if input1 == "start":
        if started:
            print("The car has already started!")
        else:
            started=True
            print("The car has started and is ready to go!!")
    elif input1 == "stop":
        if not started:
            print("The car is already stopped!!")
        else:
            started= False
            print("The car has stopped!")
    elif input1 == "help":
        print("""
start - To start the car
stop - To stop the car
exit - To exit""")
    elif input1 == "exit":
        break

    else:
        print("I don't understand...")









