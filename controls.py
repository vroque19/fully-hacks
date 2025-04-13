from gpiozero import Button


forward = Button(5, pull_up=False)
backward = Button(6, pull_up=False)

while True:
  if forward.is_pressed:
    print("forward pressed")
  if backward.is_pressed:
    print("backward pressed")
