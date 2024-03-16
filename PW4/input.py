def get_int_input(message):
  while True:
    try:
      value = int(input(message))
      return value
    except ValueError:
      print("Invalid input. Please enter an integer.")

def get_string_input(message):
  return input(message)
