from selenium import webdriver
from tkinter import *

"""
************************
* 12.08.20. GUI added. *
************************
"""

root = Tk()
root.geometry("700x500")
root.title("Game price checker")


go = Button(text="Print results", bg="green", command=lambda: console()).pack(side=TOP)
button = Button(text="Exit", fg="white", bg= "red", command=root.destroy).pack(side=BOTTOM)
push = Button(text="RUN", bg="yellow", command=lambda: funk()).pack(side=TOP)


output = Text(width=100, height=60)
output.pack()


# console function takes text from txt file and prints it out into the text window


def console():
    f = open(" result.txt")
    output.insert(1.0, f.read())
    f.close()

    
# funk is a main finction. It works with webdriver, searches the information on web site and pushes in into a txt file.


def funk():
    driver = webdriver.Firefox()
    driver.minimize_window()
    out = open(' result.txt', 'w')
    data_array = ["https://hot-game.info/game/Death-Stranding",
                  "https://hot-game.info/game/Thronebreaker-The-Witcher-Tales",
                  "https://hot-game.info/game/Cyberpunk-2077",
                  "https://hot-game.info/game/Desperados-III",
                  "https://hot-game.info/game/Remnant-From-the-Ashes",
                  "https://hot-game.info/game/Mafia-Definitive-Edition",
                  "https://hot-game.info/game/The-Outer-Worlds",
                  "https://hot-game.info/game/Quantum-Break"]
    for link in data_array:
        driver.get(link)
        search = driver.find_elements_by_class_name("price-value")
        temp = link.split('/')
        print('\n', temp[-1], file= out)
        for i in search:
            print(i.text, end=' ', file= out)
    out.close()
    driver.quit()


root.mainloop()
