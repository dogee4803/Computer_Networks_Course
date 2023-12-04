def menu():
        print("Do you want to send a message to one client or broadcast to all?")
        print("Print 'target' if you want to send to one client and 'all' if you want to send to everyone.")
        print("Print 'pass turn' if you want to make client pass and 'close socket' if you want to close socket")
        choice = input("Answer: ")
        if choice == "target":
            return choice
        elif choice == "all":
            return choice
        elif choice == "pass turn":
            return choice
        elif choice == "close socket":
            return choice
        else:
            return "3"
