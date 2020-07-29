from selenium import webdriver

driver = webdriver.Firefox()
driver.minimize_window()
out = open(' result.txt', 'w')

# This main function does multiple things: goes to the link, you've passed it, prints game's name, which is always in the end of the link
# finds and prints all actual game prices from lowest to highest. Output adds to the result.txt, but the code could be rewrited to print it all out to the console.

def funk(link):
    driver.get(link)
    search = driver.find_elements_by_class_name("price-value")
    temp = link.split('/')
    print('\n', temp[-1], file= out)
    for i in search:
        print(i.text, end=' ', file= out)


# Here you can just run function funk with any link to hot-game resource, you want
# If it exists, it will work. But ofc it requires a webdriver installation and adding it to PATH

funk("https://hot-game.info/game/Death-Stranding")

funk("https://hot-game.info/game/Thronebreaker-The-Witcher-Tales")

funk("https://hot-game.info/game/Cyberpunk-2077")

funk("https://hot-game.info/game/Desperados-III")

funk("https://hot-game.info/game/Remnant-From-the-Ashes")

funk("https://hot-game.info/game/Mafia-Definitive-Edition")

out.close()
driver.quit()

