import random

user_choice = ""

while(user_choice != "q"):
    user_choice = input("What do you pick?: ").lower()
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    log_dic = {"user": user_choice, "computer": computer_choice}
    winner = ""

    if user_choice in choices:
        if computer_choice == user_choice:
            print("Draw!")
        elif "scissors" in log_dic.values() and "rock" in log_dic.values():
            list_dkey =[key for key, val in log_dic.items() if val == "rock"]
            stringd_key = "".join(list_dkey)
            print("You chose:", user_choice, "Computer chose:", computer_choice)
            print(stringd_key, "wins")
        elif "scissors" in log_dic.values() and "paper" in log_dic.values():
            list_dkey =[key for key, val in log_dic.items() if val == "scissors"]
            stringd_key ="".join(list_dkey)
            print("You chose:", user_choice, "Computer chose:", computer_choice)
            print(stringd_key, "wins")
        elif "paper" in log_dic.values() and "rock" in log_dic.values():
            list_dkey =[key for key, val in log_dic.items() if val == "paper"]
            stringd_key ="".join(list_dkey)
            print("You chose:", user_choice, "Computer chose:", computer_choice)
            print(stringd_key, "wins")
    else:
        print("Put in a valid variable, ROCK, PAPER OR SCISSORS")
        
