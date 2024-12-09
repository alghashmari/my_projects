import random

#
# # creating a list
# ops = ["+", "-", "*", "/"]
# num = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
# # computer choosing ops
# c_c1 = random.randint(0,3)
# print(ops[c_c1])
#
# # computer choosing numbers
# c_n_c1 = random.randint(0,9)
# print(num[c_n_c1])
# c_n_c2 = random.randint(0,9)
# print(num[c_n_c2])
#
# # asking user to solve
# answer = input(f"solve {num[c_n_c1]} {ops[c_c1]} {num[c_n_c2]}\n ")
#
# # evaluating the correct answer
# correct_answer = eval(f"{num[c_n_c1]} {ops[c_c1]} {num[c_n_c2]}")
#
# if float(answer )== correct_answer:
#     print("great job!")
# else:
#     print("tough luck ! try again")

# creating lists
option = ["Odd, Even"]
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# computer choosing
cpu = random.randint(0,9)
print(num[cpu])
# user guessing
answer = input(f"guess if the number is odd or even\n")
print(f"{answer}.{option}")
if int(num) % 2 == 0:
    print("you win")
else:
    print("You lose!")









