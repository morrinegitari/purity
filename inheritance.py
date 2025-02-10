#parent/

class animal:
    def speak(self):
        print("animal is speaking")

  #chile class/sub class/derived class
class Dog(animal) :
    def bark(self):
        print("dog is barking")

class cat(dog) :
    def meow(self):
        print("cat is meowing")

a = animal()

b = Dog()
c = cat()