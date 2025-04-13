from motors import rotate_y_clockwise, rotate_y_counter, grab_prize
from gpiozero import OutputDevice, AngularServo, Servo, Button
from signal import pause
import time

def main():
  LEFT_BUTTON = Button(5, pull_up=False, bounce_time=0.03)
  UP_BUTTON = Button(6, pull_up=False, bounce_time=0.03)
  DOWN_BUTTON = Button(13, pull_up=False, bounce_time=0.03)
  RIGHT_BUTTON = Button(19, pull_up=False, bounce_time=0.03)
  GRAB_BUTTON = Button(26, pull_up=False, bounce_time=0.03)
  import simpleaudio as sa
  filename = 'wavs/sweep1.wav'
  wave_obj = sa.WaveObject.from_wave_file(filename)
  play_obj = wave_obj.play()
  play_obj.wait_done()  # Wait until sound has finished playing
  while True:
    if UP_BUTTON.is_pressed:
      print("up")
      rotate_y_clockwise()
    elif DOWN_BUTTON.is_pressed:
      print("down")
      rotate_y_counter()
    if LEFT_BUTTON.is_pressed:
      print("left")
      rotate_y_counter()
    if RIGHT_BUTTON.is_pressed:
      rotate_y_clockwise()
      print("right ")
      # rotate_x_clockwise()
    elif GRAB_BUTTON.is_pressed:
      print("grab button")
      grab_prize()
    else:
      continue
    # time.sleep(0.05)



if __name__ == "__main__":
  main()
