names = names_string.split(", ")
import random
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_will_pay = names[random_choice]
print( person_will_pay + " is going to buy the meal today!")
