class Stick:
    def __init__(self, index, num_of_disks):
        self.disk_stack = []
        self.index = index
        self.num_of_disks = num_of_disks

        self.__prepare()

    def __prepare(self):
        # Prepare first stick with all the disks
        if self.index == 0:
            for i in range(self.num_of_disks):
                self.disk_stack.append(i+1)
            self.disk_stack.reverse()
        else:
            # Rest of sticks are empty
            self.disk_stack = []
    
    def get_disk_stack(self):
        return self.disk_stack
    
    def get_index(self):
        return self.index

    def take_disk(self):
        return self.disk_stack.pop()

    def put_disk(self, disk):
        self.disk_stack.append(disk)