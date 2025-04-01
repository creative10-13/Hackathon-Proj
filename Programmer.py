from _Functions import slow_print
from _Functions import end_day

def start_day():
    slow_print("You wake up to your alarm. It's time to start your day as a programmer!")
    choice = input("Do you: \n1. Hit snooze \n2. Get up immediately\n> ")
    if choice == "1":
        slow_print("You slept in and now you're late! You rush to your computer.")
        return -10
    else:
        slow_print("You feel fresh and ready to start coding.")
        return 10

def breakfast():
    slow_print("Time for breakfast!")
    choice = input("Do you: \n1. Make a healthy breakfast \n2. Just grab coffee\n> ")
    if choice == "1":
        slow_print("Good choice! Your brain will thank you later.")
        return 10
    else:
        slow_print("Caffeine is great, but you're running on fumes.")
        return -5

def coding_session():
    slow_print("Time to start coding! What do you focus on?")
    choice = input("Do you: \n1. Work on your feature \n2. Procrastinate on social media\n> ")
    if choice == "1":
        slow_print("You're making great progress and feeling accomplished!")
        return 20
    else:
        slow_print("Oops, an hour just disappeared...and now you feel guilty.")
        return -10

def bug_fix():
    slow_print("A critical bug appears! How do you handle it?")
    choice = input("Do you: \n1. Debug systematically \n2. Panic and start rewriting code randomly\n> ")
    if choice == "1":
        slow_print("Nice! You solved it efficiently.")
        return 15
    else:
        slow_print("Oh no, now things are worse than before!")
        return -15
    
def run():
    score = 0
    score += start_day()
    score += breakfast()
    score += coding_session()
    score += bug_fix()
    end_day(score)