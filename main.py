import os
from time import sleep
from src.Chuck import ChuckNorris

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
        1. get Random number of Jokes
        2. get Specific Joke
        3. get By catagory (only nerdy and explicit)
        4.exit
        """)

        menu = input()
    #    clear()  # clear the screen
        switcher = {
            1: lambda x: ChuckNorris.getJokes(1),
            2: lambda x: ChuckNorris.getJokes(2),
            3: lambda x: ChuckNorris.getJokes(3), #only nerdy and explicit catagories
            4: lambda x: close(),
        }
        switcher.get(int(menu))(0)


if __name__ == "__main__":
    main()
