from modules.stick import Stick
from modules.grabber import Grabber


class Game:
    def __init__(self, num_of_sticks=3, num_of_disks=3):
        self.running = False
        self.num_of_disks = num_of_disks
        self.num_of_sticks = num_of_sticks

        self.expected_final_stick = []
        
        self.sticks = []

        self.grabber = Grabber(num_of_disks=self.num_of_disks, num_of_sticks=self.num_of_sticks)



    def __prepare_sticks(self):
        # Create first stick (containing all the disks)
        self.sticks.append(Stick(index=0, num_of_disks=self.num_of_disks))
        for i in range(1, self.num_of_sticks):
            self.sticks.append(Stick(index=i, num_of_disks=self.num_of_disks))

        self.expected_final_stick = self.sticks[0].get_disk_stack()[:]

    def __print_sticks(self):
        for stick in self.sticks:
            print(f"#{stick.get_index()+1} {stick.get_disk_stack()}")

    def __check_for_win(self):
        last_stick = self.sticks[len(self.sticks)-1]
        last_disk_stack = last_stick.get_disk_stack()

        if last_disk_stack == self.expected_final_stick:
            print("Success!")
            self.running = False

    def start(self):
        self.__prepare_sticks()

        print("Welcome to Hanoi Tower game :)")
        self.__print_sticks()

        self.running = True
        # Start game loop
        while self.running:
            self.grabber.select_stick_to_take_from(self.sticks)
            self.__print_sticks()
            self.grabber.select_stick_to_put_on(self.sticks)
            self.__print_sticks()

            self.__check_for_win()







