import random
#1 option
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
name = random.choice(friends)
print(name)
#2 option
random_pick = random.randint(0,4)
print(friends[random_pick])
