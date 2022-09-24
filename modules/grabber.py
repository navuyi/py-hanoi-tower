class Grabber:
    def __init__(self, num_of_disks, num_of_sticks):
        self.num_of_disks = num_of_disks
        self.num_of_sticks = num_of_sticks

        self.grabbed_disk = None

    def validate_stick(self, prompt):
        while True:
            value = input(prompt)
            if not value.isnumeric():
                print("Provide a number")
            elif 0 <= int(value)-1 <= self.num_of_sticks - 1:
                return int(value)-1
            else:
                print("This stick does not exist")

    def select_stick_to_put_on(self, sticks):
        while True:
            index = self.validate_stick("Select stick to put on: ")
            # Check if stick can receive grabbed disk
            disk_stack = sticks[index].get_disk_stack()

            if len(disk_stack) == 0:
                self.put_disk(stick=sticks[index])
                return
            elif len(disk_stack) > 0:
                top_disk = disk_stack[len(disk_stack) - 1]
                if self.grabbed_disk < top_disk:
                    self.put_disk(stick=sticks[index])
                    return
                else:
                    print(f"Can not put disk {self.grabbed_disk} on top of disk {top_disk}")

    def select_stick_to_take_from(self, sticks):
        while True:
            # Validate stick number
            index = self.validate_stick("Select stick to take from: ")
            # Check if stick is not empty
            if len(sticks[index].get_disk_stack()) > 0:
                self.take_disk(sticks[index])
                return
            else:
                print("Can not take from empty stick")

    def take_disk(self, stick):
        self.grabbed_disk = stick.take_disk()
        print(f"You have grabbed disk with width: {self.grabbed_disk}")

    def put_disk(self, stick):
        stick.put_disk(self.grabbed_disk)
        self.grabbed_disk = None


