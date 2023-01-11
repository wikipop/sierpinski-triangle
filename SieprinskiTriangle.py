import random
import matplotlib.pyplot as plt
import numpy as np


def midpoint(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


fig, ax = plt.subplots()
ax.set_aspect(1)

points = [(0, 0), (1, 0), (0.5, np.sqrt(3) / 2)]

ax.plot(*zip(*points, (0, 0)), color='black')

chosen_points = random.sample(points, 2)

ax.scatter(*midpoint(*chosen_points), color='red', s=10)

third_point = random.choice([p for p in points if p not in chosen_points])

ax.scatter(*midpoint(third_point, midpoint(*chosen_points)), color='red', s=10)
act_point = midpoint(third_point, midpoint(*chosen_points))

for i in range(3000):
    new_point = midpoint(random.choice(points), act_point)
    ax.scatter(*new_point, color='red', s=10)
    act_point = new_point
    print(i)

plt.show()
