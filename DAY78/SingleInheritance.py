class Animal:

    def make_sound(self):
        print("Animal makes sound")

    def move(self):
        print("Animla Moves")

    def jumps(self):
        print("Animal Jumps")

class Cat(Animal):

    def make_sound(self):
        print("Cat makes Meow_Meow sound")

    def move(self):
        print("Cat moves quickly")

    def jumps(self):
        print("Cat jumps high")

animal = Animal()
animal.make_sound()
animal.move()             # this is the default definations of the functions of Animal class
animal.jumps()

cat = Cat()
cat.make_sound()
cat.move()             # These are the redefined functions for the Cat class
cat.jumps()
