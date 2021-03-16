# 1 - Understand difference between objects and classes.
# 2 - Understand how classes are defined
# 3 - Understand how objects are initialized
# 4 - Understand instance variables and instance methods
# 5 - Understand class variables and class methods
# 6 - Utilize the self keyword
# 7 - Understand method chaining in a class

car = {
    "make": "Rolls Royce",
    "model": "Ghost",
    "color": "white"
}
car['make'] # Rolls Royce
car.get('make') # Rolls Royce

class CoffeeCup():
  def __init__(self, capacity): # similar to constructor in js
    self.capacity = capacity
    self.amount = 0

  def __str__(self):
    return f"Coffee Cup that is {self.capacity}oz"

  def fill(self): # method on CoffeeCup
    self.amount = self.capacity # 12

  def empty(self): # method on CoffeeCup
    self.amount = 0

  def drink(self, amount): # method
    self.amount -= amount # 12 - 12 = 0
    if (self.amount == 0): # 0 == 0
      self.fill() # run this method

steves_cup = CoffeeCup(12)  # a fancy latte.
seans_cup = CoffeeCup(16)    # gas station drip.
brandis_cup = CoffeeCup(2)  # a quick espresso.

steves_cup.fill() # dot notation when using methods
steves_cup.drink(12) # method chaining...
print(steves_cup.amount)
print(steves_cup) # print the instance of steves_cup
print(help(steves_cup)) # seeing the methods that are on this instance