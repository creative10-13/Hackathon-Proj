import time

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    
def end_day(score):
    slow_print("The day is over. Let's see how you did...")
    if score > 30:
        slow_print("You had a super productive day! Time to relax.")
    elif score > 0:
        slow_print("Not bad! A solid day of coding.")
    else:
        slow_print("Rough day...but there's always tomorrow!")