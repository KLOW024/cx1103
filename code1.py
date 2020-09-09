from sense_hat import SenseHat
import time
from random import randint, randrange
#sense = SenseHat()
#sense.show_message("hello") #print msg on pi
#sense.set_rotation(180) #rotato potato
#sense.show_message("hello", text_colour = (225,225, 0), back_colour = (225,0,0), scroll_speed=0.5)

sense = SenseHat()
y = (255, 255, 0)
b = (0, 0, 0 )
red = (255, 0, 0)
image_pixel = [b, b, b, b, b, b, b, b,
                b, b, b, y, y, b, b, b,
                b, b, b, y, y, b, b, b,
                b, b, b, y, y, b, b, b,
                b, b, b, y, y, b, b, b,
                b, b, b, y, y, b, b, b,
                b, y, y, y, y, y, y, b,
                b, y, y, y, y, y, y, b]
sense.set_pixels(image_pixel)
sense.clear()
'''
for i in range(7, -1, -1):
    print(i)
    sense.set_pixel(3, i, red)
    sense.set_pixel(4, i, red)
    time.sleep(0.2)
    sense.set_pixels(image_pixel)
while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    x_axis = round(x, 0)
    y_axis = round(y, 0)
    print("y is ", y)
    print("x is", x)
    print("z is", z)
    time.sleep(0.5)
'''

def exec_5a():
    while True :
        listX = []
        listY = []
        while len(listX) <= 3 or len(listY) <= 3 :
            x = randint(0,7)
            if x not in listX :
                listX.append(x)
            else :
                x1 = randint(0,7)
            y = randint(0,7)
            if y not in listY :
                listY.append(y)
            else :
                y1 = randint(0,7)
        print(listX, listY)
        sense.set_pixel(listX[0],listY[0], red)
        sense.set_pixel(listX[1],listY[1], red)
        sense.set_pixel(listX[2],listY[2], red)
        sense.set_pixel(listX[3],listY[3], red)
        time.sleep(1)
        print("clearing")
        sense.clear()

def exec_5b():
    image_pixel = [
                b, b, b, b, b, b, b, b,
                b, b, b, y, y, b, b, b,
                b, b, b, y, y, b, b, b,
                b, b, b, y, y, b, b, b,
                b, b, b, y, y, b, b, b,
                b, b, b, y, y, b, b, b,
                b, y, y, y, y, y, y, b,
                b, y, y, y, y, y, y, b]
    sense.set_pixels(image_pixel)
    for i in range(7, -1, -1):
        print(i)
        sense.set_pixel(3, i, red)
        sense.set_pixel(4, i, red)
        time.sleep(0.2)
        sense.set_pixels(image_pixel)
    sense.clear()

def exec_5c():
    x = 0
    while True :
        r = randint(0,255)
        gre = randint(0,255)
        blue = randint(0,255)
        y = (r, gre, blue)
        image_pixel = [
                    b, b, b, b, b, b, b, b,
                    b, b, b, y, y, b, b, b,
                    b, b, b, y, y, b, b, b,
                    b, b, b, y, y, b, b, b,
                    b, b, b, y, y, b, b, b,
                    b, b, b, y, y, b, b, b,
                    b, y, y, y, y, y, y, b,
                    b, y, y, y, y, y, y, b]
        sense.set_pixels(image_pixel)
        time.sleep(2)
        if x >= 270 :
            x =0
        else :
            x += 90
        sense.set_rotation(x)
    
def exec_5d():
    sense.show_message("Start", text_colour = (225,225, 0), back_colour = (0,0,0), scroll_speed=0.1)
    score = 0
    while True :
        acceleration = sense.get_accelerometer_raw()
        x_raw = acceleration['x']
        y_raw = acceleration['y']
        x_axis = round(x_raw, 0)
        y_axis = round(y_raw, 0)
        print("y is ", y_raw)
        print("y_axis :", y_axis)
        print("x is", x_raw)
        print("x_axis :", x_axis)
        time.sleep(0.5)
        Coordy = 90
        arrow = randrange(0,270,90)
        sense.set_rotation(arrow)
        image_pixel = [
                b, b, b, b, b, b, b, b,
                b, b, b, y, y, b, b, b,
                b, b, y, y, y, y, b, b,
                b, y, b, y, y, b, y, b,
                b, b, b, y, y, b, b, b,
                b, b, b, y, y, b, b, b,
                b, b, b, y, y, b, b, b,
                b, b, b, y, y, b, b, b]
        sense.set_pixels(image_pixel)
        time.sleep(2)
        if abs(x_raw) > abs(y_raw):
            if x_raw > 0 :
                Coordx =270
            elif x_raw< 0 :
                Coordx = 90
            Coord = Coordx
        elif abs(y_raw) > abs(x_raw) :
            if y_raw < 0 :
                Coordy = 180 
            elif y_raw > 0 :
                Coordy = 0
            Coord = Coordy
        
        sense.set_rotation(arrow)
        print(Coord)
        print(arrow)
        
        if Coord == arrow :
            sense.set_pixels(image_pixel)
            score += 1
        elif Coord != arrow :
            sense.show_message("score:" + str(score), text_colour = (225,225, 0), back_colour = (225,0,0), scroll_speed=0.5)
            break
        time.sleep(0.5)
        print(score)
        
exec_5d()
        
