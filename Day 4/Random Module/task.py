# import random
# import my_module
import random

random_number= random.randint(1,10)
print(random_number)
print(my_module.my_favourite_number)
random_number_2 = random.random() * 10
print(random_number_2)

heads = 1
tails = 2
head_or_tail = random.randint(1,2)
if head_or_tail == 1:
    print("head")
else:
    print("tails")

