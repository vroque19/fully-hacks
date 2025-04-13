from gpiozero import OutputDevice, Button
import time

control_pins_y = [OutputDevice(pin) for pin in [17, 18, 27, 22]]
control_pins_x = [OutputDevice(pin) for pin in [23, 24, 25, 8]]
control_pins_z = [OutputDevice(pin) for pin in [10, 9, 11, 8]]
control_pins_grab = [OutputDevice(pin) for pin in [26, 16, 20, 21]]

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

def step_motor(pins, steps=16, direction=1):
    sequence = STEP_SEQUENCE if direction > 0 else list(reversed(STEP_SEQUENCE))
    for _ in range(steps):
        for halfstep in sequence:
            for pin, val in zip(pins, halfstep):
                pin.value = val
            time.sleep(0.001)


def rotate_y_clockwise(): 
    step_motor(control_pins_y, direction=1)

def rotate_y_counter(): 
    step_motor(control_pins_y, direction=-1)

def rotate_x_clockwise(): 
    step_motor(control_pins_x, direction=1)

def rotate_x_counter(): 
    step_motor(control_pins_x, direction=-1)

def rotate_z_clockwise(): 
    step_motor(control_pins_z, direction=1)

def rotate_z_counter(): 
    step_motor(control_pins_z, direction=-1)

def grab_prize():
    step_motor(control_pins_grab, direction=1, steps=128) # open
    print("going down...")
    rotate_z_clockwise(steps=1024) # down
    step_motor(control_pins_y, direction=-1, steps=128) # close
    rotate_z_counter(steps=1024) # up
    print("going up...")
    

def open_and_close():
    step_motor(control_pins_y, direction=1, steps=256)
    step_motor(control_pins_y, direction=-1, steps=256)
    step_motor(control_pins_y, direction=1, steps=256)


def main():
    ...
    # open_and_close()
    # time.sleep(1)
    
if __name__ == "__main__":
    main()
