from random import Random


class Abdullah:
    def __init__(self, kid,age,character = "funny"):
        self.kid= kid
        self.age = age
        self.character = character
        self.followers = 0
        self.following = 0

    def follow(self,kid):
        kid.followers +=1
        self.following +=1



kid_1 = Abdullah("Rand", 7, "smart")
kid_2 = Abdullah("Deem", 5 )
kid_3 = Abdullah("Omar", 1, "tall")


print(f"Kid's Name: {kid_1.kid}, Age: {kid_1.age}, Character: {kid_1.character}")
print(f"Kid's Name: {kid_2.kid}, Age: {kid_2.age}, Character: {kid_2.character}")
print(f"Kid's Name: {kid_3.kid}, Age: {kid_3.age}, Character: {kid_3.character}")