# from turtle import Turtle, Screen
#
# print(Turtle)
#
# timmy = Turtle()
# timmy.color("pink")
# timmy.shape("turtle")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

import prettytable

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pockemon Name",["Pickatch", "squiertale", "Charmander"])
table.add_column("type",["elictric", "water", "fire"])
table.add_column("cuteness",["very", "eh", "no"])


table.align = "l"


print(table)






