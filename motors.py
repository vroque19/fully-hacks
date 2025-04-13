from gpiozero import OutputDevice, AngularServo, Servo, Button
from math import sin

import time


STEP_SEQUENCE = [
        [1, 0, 0, 1],
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1]
    ]

def servo_sin():
   s = AngularServo(25, min_angle=-90, max_angle=90)
   elapsed = 0.0
   delay = 0.05
   while True:
      time.sleep(delay)
      elapsed += delay
      s.value = sin(elapsed)


def servo_calibrate():
   #factory = PiGPIOFactory()
   print('calibrating servo...')
   min_angle = -30
   max_angle = 30
   s = AngularServo(25, min_angle=min_angle, max_angle=max_angle)
   angle = 0
   s.angle = angle
   while True:
      angle = int(input("degrees: ").strip())
      s.angle = angle
      print('actual angle: ', s.angle, flush=True)
      time.sleep(0.5)


def rotate_y_counter():
  steps = 128
  control_pins = [17, 18, 27, 22]
  pins = [OutputDevice(pin) for pin in control_pins]
  for halfstep in reversed(STEP_SEQUENCE):  # reverse the sequence
      for pin in range(4):
          pins[pin].value = halfstep[pin]
      time.sleep(0.001)

def rotate_y_clockwise():
  control_pins = [17, 18, 27, 22]
  pins = [OutputDevice(pin) for pin in control_pins]
  steps = 128 # 45 degrees

  for halfstep in STEP_SEQUENCE:  # reverse the sequence
    for pin in range(4):
        pins[pin].value = halfstep[pin]
    time.sleep(0.001)

def open_and_close():
    for i in range(128):
        rotate_y_clockwise()
    time.sleep(1)
    for i in range(128):
        rotate_y_counter()
    time.sleep(1)
# def rotate_x_counter():
#   control_pins = [23, 24, 25, 8]
#   pins = [OutputDevice(pin) for pin in control_pins]
#   for halfstep in reversed(STEP_SEQUENCE):  # reverse the sequence
#       for pin in range(4):
#           pins[pin].value = halfstep[pin]
#       time.sleep(0.001)

# def rotate_x_clockwise():
#   control_pins = [23, 24, 25, 8]
#   pins = [OutputDevice(pin) for pin in control_pins]
#   steps = 64 # 45 degrees
#   for halfstep in STEP_SEQUENCE:  # reverse the sequence
#       for pin in range(4):
#           pins[pin].value = halfstep[pin]
#       time.sleep(0.001)

def main():
    UP_BUTTON = Button(5, pull_up=False)
    DOWN_BUTTON = Button(6, pull_up=False)
    # servo = Servo(25)
    # servo_calibrate()
    while True:
        # if UP_BUTTON.is_pressed:
        #     rotate_y_clockwise()
        # elif DOWN_BUTTON.is_pressed:
        #    rotate_y_counter()
        open_and_close()

        
    
if __name__ == "__main__":
    main()
    # servo_sin()
    # servo_calibrate()
