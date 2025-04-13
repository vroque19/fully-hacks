from gpiozero import OutputDevice
import keyboard
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
  control_pins = [17, 18, 27, 22]
  pins = [OutputDevice(pin) for pin in control_pins]
  for halfstep in reversed(STEP_SEQUENCE):  # reverse the sequence
      for pin in range(4):
          pins[pin].value = halfstep[pin]
      time.sleep(0.001)

def rotate_y_clockwise():
  control_pins = [17, 18, 27, 22]
  pins = [OutputDevice(pin) for pin in control_pins]
  steps = 64 # 45 degrees
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
    # while True:
    #     if keyboard.is_pressed("up"):
    #         rotate_y_counter()
    #     if keyboard.is_pressed("down"):
    #         rotate_y_clockwise()
    rotate_y_clockwise()
    rotate_y_counter()

if __name__ == "__main__":
    main()
