# import Packages
import turtle
import random
import time

#Creating Screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.setup(width=700, height=700)
screen.tracer(0) # এটা Automatic Screen Update কে বন্ধ করে। নিচের while লুপ শেষ হলে তারপর ম্যানুয়েলি update হবে। নাহলে performance খারাপ হবে। 
screen.bgcolor("green")

# Creating border
turtle.speed(0)
turtle.pensize(4)       # কলমের সাইজ ৪
turtle.color("black")     # চারপাশের বেকগ্রাউন্ড তৈরি করা
turtle.penup()          #লেখার জন্য কলম তুলছে
turtle.goto(-310, 250)    # -x অক্ষে ৩১০ ঘর গিয়ে উপরের y এর দিকে 250 ঘর যাবে।  
turtle.pendown()        # এরপর কলম বসাবে লেখার জন্য 
turtle.forward(620)       # ওখান থেকে ৬২০ ঘর লিখবে বা দাগ টানবে। 
turtle.right(90)       # এরপর ওখান থেকে ৯০ ডিগ্রি ডান পাশে কলম ঘুরবে। 
turtle.forward(500)      # সেখান থেকে ৫০০ ঘর দাগ টানবে। 
turtle.right(90)       # আবার ডান পাশে ৯০ ডিগ্রি ঘুরবে। 
turtle.forward(620)      # ওখান থেকে ৬২০ ঘর যাবে। 
turtle.right(90)       # আবার ডান পাশে ৯০ ডিগ্রি ঘুরবে।
turtle.forward(500)      # সেখান থেকে ৫০০ ঘর দাগ টানবে। 
turtle.right(90)       # আবার ডান পাশে ৯০ ডিগ্রি ঘুরে আগের জায়গায় নিয়ে যাবে। যদিও এটা প্রয়োজন নেই। কিন্তু good Practice. 
turtle.penup()           # এরপর কলম তুলে ফেলে আঁকা শেষ করবে। 
turtle.hideturtle()    # শেষে Turtle icon স্ক্রিন থেকে লুকিয়ে ফেলবে। এটা লুকিয়ে না ফেললে স্ক্রিনে একটা তীর চিহ্ন আসবে, যা দেখতে খারাপ লাগবে। 

# Score
score = 0
delay = 0.1

# Snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("red")
snake.penup()
snake.goto(0,0)
snake.direction = "stop" # শুরুতে সাপটি থেমে থাকবে। 

# Food
fruit = turtle.Turtle()
fruit.shape("square")
fruit.speed(0)
fruit.color("white")
fruit.penup()
fruit.goto(30,30)

# List for eating food
old_fruit = []

# Scoring System
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.write("Score: ", align="center", font=("Arial", 24, "bold"))

# Define How to move
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"
        
def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"
        
def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"
        
def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"
        

def sanke_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y+20)     # Up বাটন চাপলে সাপকে ২০ ঘর উপরের দিকে নিয়ে যাবে। 
        
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y-20)      # Down বাটন চাপলে সাপকে ২০ ঘর নিচের দিকে নিয়ে যাবে। 
        
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x-20)      # Left বাটন চাপলে সাপকে ২০ ঘর বাম দিকে নিয়ে যাবে। 
        
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x+20)      # Right বাটন চাপলে সাপকে ২০ ঘর ডান দিকে নিয়ে যাবে। 


# Keyboard Bindings
screen.listen()
screen.onkeypress(snake_go_up,"Up")
screen.onkeypress(snake_go_down,"Down")
screen.onkeypress(snake_go_left,"Left")
screen.onkeypress(snake_go_right,"Right")


# Main Loop
while True:
    screen.update()
    
    # Snake & Fruit Colision 
    if snake.distance(fruit)<20:
        x = random.randint(-290, 290) # নতুন খাবার x অক্ষের ধনাত্মক দিকে ২৯০ ঘর ও ঋণাত্মক দিকে ২৯০ ঘর বরাবর randomly আসবে। 
        y = random.randint(-240,240) # নতুন খাবার y অক্ষের ধনাত্মক দিকে ২৪০ ঘর ও ঋণাত্মক দিকে ২৪০ ঘর বরাবর randomly আসবে।
        fruit.goto(x,y)  # নতুন random পজিশনে খাবার হাজির হবে
        scoring.clear()  # Clear the previous content to avoid overlapping or displaying outdated information.
        score = score + 10
        scoring.write(f"Score: {score}", align="center", font=("Arial", 24, "bold"))
        delay = delay - 0.001
        
        
        # Creating New Foods  || সাপের পেটে গেলে যেমন দেখাবে
        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("square")
        new_fruit.color("yellow")
        new_fruit.penup()
        old_fruit.append(new_fruit)
        
        
    
    # Adding ball to snake
    for index in range(len(old_fruit)-1,0,-1):    #  প্রথমত: " len(old_fruit)-1 " এখানে -1 দেওয়া হয়েছে কারণ list এ ০ থেকে হিসাব হয়।            
                                                  # ফলে একটি লিস্টে যদি [a,b,c,d] চারটি উপাদান থাকে, তাহলে এর len হবে চার। কিন্তু আমরা যদি শেষ উপাদান d কে পেতে চায় তবে, এর ইনডেক্স হবে 3।  দ্বিতীয়ত: ০ এর আগ পর্যন্ত। ০ হলো সাপের মাথা তৃতীয়ত: -1 হলো ইনডেক্স ১ করে কমবে।  
        a = old_fruit[index-1].xcor() 
                                        # এখানে নুতুন আইটেমের স্থানাংক (a,b) এর 'a'বিন্দু follow করবে index-1 এর x coordinate কে। ফলে আগের ইনডেক্সের আইটেমকে নতুন ইনডেক্সের আইটেম অনুসরণ করবে।  
        b = old_fruit[index-1].ycor()   # এখইভাবে, 'b' বিন্দু অনুসরণ করবে index-1 এর y coordinate কে।
        
        old_fruit[index].goto(a,b) # It ensures that the segment follows the one in front, creating the effect of a continuous, moving snake. 
        
                                    # Head -> old_fruit[0] -> old_fruit[1] -> old_fruit[2] -> old_fruit[3]
                                    #Position: (new A)         (A)           (B)                 (C)           (D)

        
        
        
    if len(old_fruit)>0:
        a= snake.xcor()  # 'a' অনুসরণ করবে snake কে, অর্থাৎ head এর x coordinate কে অনুরণ করবে। 
        b = snake.ycor()
        old_fruit[0].goto(a,b) # old_fruit এর ০ ইনডেক্স a,b কে অনুসরণ করবে। 
    sanke_move()
    
    
    # Snake & border Colision
    if snake.xcor()>300 or snake.xcor()<-300 or snake.ycor()>240 or snake.ycor()<-240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("turquoise")
        scoring.goto(0,0)
        scoring.write(f"     সাপ মারা গেছে। \n আপনার স্কোর হলো  {score}", align="center", font=("Arial", 30, "bold"))
        
    # Snake Colision itself
    for food in old_fruit:
        if food.distance(snake)<20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0,0)
            scoring.write(f" সাপতো নিজের লেজে নিজে কামড় দিলো। \n     আপনার স্কোর হলো  {score}", align="center", font=("Arial", 30, "bold"))
            
        
    time.sleep(delay)
    
turtle.Terminator()