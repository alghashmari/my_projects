try:
    age = int(input("How old are you?"))
except ValueError:
    print("wrong entry use actual number such as 19")
    age = int(input("How old are you?"))


if age > 18:
 print(f"You can drive at age {age}.")
