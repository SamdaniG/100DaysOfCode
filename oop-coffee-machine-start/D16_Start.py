#This is Day16 of 100DaysOfPython 
"""
import turtle

timmy=turtle.Turtle()
print(timmy)
timmy.shape("turtle")


my_screen=turtle.Screen()

timmy.forward(100)
print(my_screen.canvheight)
my_screen.exitonclick()


"""
import mmap
import prettytable
my_table=prettytable.PrettyTable()
my_table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])

my_table.add_column("Type",["Electric","Water","Fire"])
print(my_table.align)
my_table.align="r"
print(my_table)