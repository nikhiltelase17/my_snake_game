from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(230, 270)
        self.hideturtle()
        self.update_score()
        self.show_high_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def show_high_score(self):
        tim = Turtle()
        tim.penup()
        tim.color("White")
        tim.goto(-230, 270)
        tim.hideturtle()
        # opening score file for reading
        o = open("score.txt", "r")
        text = o.read()
        text_str_list = text.split(",")
        text_int_list = []
        for text in text_str_list:
            text_int_list.append(int(text))

        tim.write(f"High score: {max(text_int_list)}", align=ALIGNMENT, font=FONT)
        o.close()

    def game_over(self):
        self.goto(0, 0)
        # opening score file for writing score
        f = open("score.txt", "a")
        f.write(f", {self.score}")
        f.close()

        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
