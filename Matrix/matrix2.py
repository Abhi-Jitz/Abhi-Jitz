import random
from termcolor import colored
set = ""
colors = ["grey", "red", "green", "yellow", "blue", "magenta", "cyan"]
while True:
    line = [random.randint(0,1) for i in range(118)]
    for deck in line:
        set+= colored(str(deck),random.choice(colors)) + " "
    set +="\n"
    print(set)
