
import math
def paint_calc(height, width, cover):
  num_cans = (height*width) / cover
  round_up_can = math.ceil(num_cans)
  print(f"You'll need {round_up_can} cans of paint.")

test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)