import turtle
import random
import time

# Ekranı oluştur
screen = turtle.Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")

# Turtle nesnesi oluştur
t = turtle.Turtle()
t.color("light blue")
t.speed(0)  # Maksimum hız
t.shape("turtle")

# Puan başlangıç değeri
score = 0

# Puan tablosu (scoreboard) oluştur
score_display = turtle.Turtle()
score_display.speed(0)
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 220)
score_display.color("white")
score_display.write(f"Puan: {score}", align="center", font=("Courier", 24, "normal"))

def update_score():
    global score
    score += 1
    score_display.clear()
    score_display.write(f"Puan: {score}", align="center", font=("Courier", 24, "normal"))

# Turtle tıklama işlevi
def click(x, y):
    if t.distance(x, y) < 20:  # Eğer Turtle'a tıkladıysanız (ayarlayabilirsiniz)
        update_score()
        # Rastgele yeni bir konum seç
        new_x = random.randint(-250, 250)
        new_y = random.randint(-250, 250)
        t.penup()
        t.goto(new_x, new_y)
        t.pendown()

# Turtle'a tıklamayı dinle
t.onclick(click)

while True:
    # Rastgele bir x ve y koordinatı oluştur
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)

    # Turtle'ı belirtilen konuma ışınlamak
    t.penup()
    t.goto(x, y)
    t.pendown()

    # 1 saniye beklet
    time.sleep(1)

    # Turtle'ı temizle (kaybolmasını sağla)
    t.clear()



screen.mainloop()
