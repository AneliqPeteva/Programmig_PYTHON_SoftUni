from collections import deque
from datetime import datetime, timedelta

robot = {}

for rob in input().split(";"):
    name, time_needed = rob.split("-")
    robot[name] = [int(time_needed), 0]

factory_time = datetime.strptime(input(), "%H:%M:%S")
products = deque()

while True:
    product = input()

    if product == "End":
        break

    product.append(products)

while products:
    factory_time += timedelta(0, 1)
    product = products.popleft()

    free_robots = []

    for name, value in robot.items():
        if value[1] != 0:
            robot[name][1] -= 1

print(factory_time)