import turtle
t=turtle.Turtle()
t.shape("turtle")


def square(length):
        for i in range(4):
                   t.forward(length)
                   t.left(90)
                           
                   
length=int(input("변의 길이를 입력하시오:"))
square(length)
length=int(input("변의 길이를 입력하시오:"))
square(length)
length=int(input("변의 길이를 입력하시오:"))
square(length)
