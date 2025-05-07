from game import Game

while 1:
    g = Game()
    g.setup()
    g.play()
    restart = input("Play again? (y/n): ")
    if restart != "y":
        break