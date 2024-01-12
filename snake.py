from turtle import Turtle
import pygame
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

#  SOUND EFFECTS
pygame.mixer.init()
turning_sound = pygame.mixer.Sound("turning sound.mp3")

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            pygame.mixer.Sound.play(turning_sound)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            pygame.mixer.Sound.play(turning_sound)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            pygame.mixer.Sound.play(turning_sound)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            pygame.mixer.Sound.play(turning_sound)
