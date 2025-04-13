from gpiozero import OutputDevice, Servo, AngularServo, Button
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
    while True:
        if UP_BUTTON.is_pressed and DOWN_BUTTON.is_pressed:
           continue
        elif UP_BUTTON.is_pressed:
            rotate_y_counter()
        elif DOWN_BUTTON.is_pressed:
            rotate_y_clockwise()
    # steps = 128 # 45 degrees
    # for i in range(steps):
    #     rotate_y_clockwise()
    # time.sleep(1)
    # for i in range(steps):
    #     rotate_y_counter()

if __name__ == "__main__":
    main()
