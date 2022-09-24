from modules.game import Game


def main():
    hanoi = Game(num_of_sticks=3, num_of_disks=4)
    hanoi.start()


if __name__ == "__main__":
    main()
