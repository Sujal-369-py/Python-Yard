instruction = ""
while True :
    instruction = input("> ").lower()
    if instruction == "help" :
        print("""
start - to start the car
stop - to stop the car
quit - to exit
              """)
    elif instruction == "start"  :
        print("Car is started...")
    elif instruction == "stop" :
        print("Car is Stoppped")
    elif instruction == "quit" :
        break
    else :
       print("I don't understand")