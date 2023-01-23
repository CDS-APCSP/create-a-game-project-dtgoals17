# Variables
mountain_location = "start"
has_flashlight = False
has_climbingpicks = False

# Start function
def start():
  global mountain_location
  print("You find yourself in a mountain with two paths .")
  mountain_explore()

# End function
def end():
  print("Congratulations! You have successfully navigated the mountain and found your way down.")

# mountain explore function
def mountain_explore():
  global mountain_location
  global has_flashlight
  global has_climbingpicks
  
  if mountain_location == "start":
    print("To the left, the path leads down the mountain.")
    print("To the right, the path leads you up the mountain where you see a small cottage.")
    choice = input("Which direction do you want to go? (left/right) ")
    if choice == "left":
      mountain_location = "down mountain"
      mountain_explore()
    elif choice == "right":
      mountain_location = "cottage"
      cottage_explore()

# Cottage explore function
def cottage_explore():
  global cave_location
  global has_flashlight
  global has_climbingpicks
  
  print("You find yourself in a small cottage.")
  if not has_flashlight:
    print("You see a flashlight on the ground.")
    choice = input("Do you want to pick up the flashlight? (yes/no) ")
    if choice == "yes":
      has_flashlight = True
      print("You have picked up the flashlight.")
  if not has_climbingpicks:
    print("You see climbing picks on the wall.")
    choice = input("Do you want to take the climbing picks? (yes/no) ")
    if choice == "yes":
      has_climbingpicks = True
      print("You have taken the climbing picks.")
  choice = input("Do you want to go back to the paths or continue exploring the cottage? (back/continue) ")
  if choice == "back":
    mountain_location = "start"
    mountain_explore()
  elif choice == "continue":
    cottage_explore()

# Check win function
def check_win():
  global has_flashlight
  global has_climbingpicks
  
  if has_flashlight and has_climbingpicks:
    end()
  else:
    print("You Died from not having the right tools to get down the mountain.")

# Run game
start()
check_win()
