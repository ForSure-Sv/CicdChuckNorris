import os
from time import sleep
from src.Chuck import ChuckNorris
import random

#def clear():
#    sleep(3)
#    os.system('clear')


def close():
#    clear()
    print("program has been closed")
    sleep(1)
    exit(0)


def main():
    while True:
        print("""
        1. get Joke
        2. get Specific Joke
        3. get By catagory
        4.exit
        """)

        menu = input()
    #    clear()  # clear the screen
        num = random.randint(1,10)
        switcher = {
            1: lambda x: ChuckNorris.getJoke(num),
            2: lambda x: ChuckNorris.getSpecificJoke(),
            3: lambda x: ChuckNorris.getByCatagory(), #only nerdy and explicit catagories
            4: lambda x: close(),
        }
        switcher.get(int(menu))(0)


if __name__ == "__main__":
    main()
