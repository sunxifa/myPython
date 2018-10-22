class Animal(object):
    def run(self):
        print 'Animal is running...'


class Dog(Animal):
    # def run(self):
    #     print 'Dog is running...'
    pass


class Cat(Animal):
    def run(self):
        print 'Cat is running...'


a = Animal()
a.run()
dog = Dog()
dog.run()
isinstance(a, Animal)
isinstance(dog, Animal)
