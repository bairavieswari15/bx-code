import math
ab = int(input())
bc = int(input())
angle_rad = math.atan2(ab, bc)
angle_deg = math.degrees(angle_rad)
print(str(int(round(angle_deg))) + "\u00b0")
