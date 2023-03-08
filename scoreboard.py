from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.goto(-220, 260)
        self.level += 1
        message = "Level: " + str(self.level)
        self.write(message, align="center", font=FONT)

    def game_over(self):
        """This is function to print game over while detect a collision"""
        self.goto(0,0) # I don't clear screen to show how much point user reach
        self.write("GAME OVER", align="center", font=FONT)