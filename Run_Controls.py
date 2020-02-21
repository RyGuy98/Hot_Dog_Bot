from time import sleep
import RPi.GPIO as GPIO

#servo
servo = 3
frequency = 50
dc = 0

DIRZ = 20
STEPZ = 21
DIRY = 6
STEPY = 12⁸
DIRX = 14
STEPX = 4
CW = 1
CCW = 0
SPR = 200 #steps per rotation


GPIO.setmode(GPIO.BCM)
GPIO.setup(DIRX, GPIO.OUT)
GPIO.setup(STEPX, GPIO.OUT)
GPIO.setup(DIRY, GPIO.OUT)
GPIO.setup(STEPY, GPIO.OUT)
GPIO.setup(DIRZ, GPIO.OUT)
GPIO.setup(STEPZ, GPIO.OUT)


#servo
GPIO.setup(servo, GPIO.OUT)
pwm = GPIO.PWM(servo, frequency)
pwm.start(dc) 

 
step_count = SPR
delay = .0012


def run_servo(degree):
  cycle = degree/18+2
  #2 - servo lowest available value(may be changed)
  GPIO.output(servo, True)
  pwm.ChangeDutyCycle(cycle)
  sleep(1)
  GPIO.output(servo, False)
  pwm.ChangeDutyCycle(0)
  


def run_motor(sprx, spry, sprz):
    x = 0
    y = 0
    z = 0
    print("Clockwise")
    GPIO.output(DIRX, CW)
    GPIO.output(DIRY, CW)
    GPIO.output(DIRZ, CW)
    print(sprx, " run x ccw")
    print(spry, " run y ccw")
    print(sprz, " run z ccw")
    while (x <= sprx or y <= spry or z <= sprz):
        if x <= sprx:
            GPIO.output(STEPX, GPIO.LOW)
        if y <= spry:
            GPIO.output(STEPY, GPIO.LOW)
        if z <= sprz:
            GPIO.output(STEPZ, GPIO.LOW)
        sleep(delay)   
        if x <= sprx:
            GPIO.output(STEPX, GPIO.HIGH)
            x=x+1
        if y <= spry:
            GPIO.output(STEPY, GPIO.HIGH)
            y=y+1
        if z <= sprz:
            GPIO.output(STEPZ, GPIO.HIGH)
            z=z+1
        sleep(delay)
    
    sleep(.1)    
    
    x = 0
    y = 0
    z = 0
    print("counterclockwise")
    GPIO.output(DIRX, CCW)
    GPIO.output(DIRY, CCW)
    GPIO.output(DIRZ, CCW)
    print(sprx, " run x ccw")
    print(spry, " run y ccw")
    print(sprz, " run z ccw")
    while (x <= sprx or y <= spry or z <= sprz):
        if x <= sprx:
            GPIO.output(STEPX, GPIO.LOW)
        if y <= spry:
            GPIO.output(STEPY, GPIO.LOW)
        if z <= sprz:
            GPIO.output(STEPZ, GPIO.LOW)
        sleep(delay)            
        if x <= sprx:
            GPIO.output(STEPX, GPIO.HIGH)
            x=x+1
        if y <= spry:
            GPIO.output(STEPY, GPIO.HIGH)
            y=y+1
        if z <= sprz:
            GPIO.output(STEPZ, GPIO.HIGH)
            z=z+1
        sleep(delay)    
    sleep(.5)
       

while(1):
    try:
        mode = int(input('Enter Mode: '))
        if mode == 1:
            for t in range(5):
                run_motor(200, 200, 200)
        elif mode == 2:
            run_motor(400, 400, 400)
        elif mode == 3:
            run_motor(800, 800, 800)
        elif mode == 4:
            run_motor(200, 300, 500)
        elif mode == 5:
            run_motor(600, 700, 800)
        elif mode == 6:
            run_motor(1000, 600, 300)
        elif mode == 7:
            run_motor(2000, 1500, 1000)
        elif mode == 8:
            run_motor(3000, 4000, 5000)
        elif mode == 9:
            run_servo()
        
        else: 
            print("Not a valid mode.")
    except ValueError:
        print("Not a mode.")
    
    
