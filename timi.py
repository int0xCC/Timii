from datetime import *

print("====12 & 24 Hour Time====")

t_now = '11:35 PM'

print("Time = ",t_now)

t_now = datetime.strptime(t_now, '%I:%M %p')

print("24 hour-ified Time = ",t_now)
