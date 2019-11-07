from random import choice

import matplotlib.pyplot as plt


class RandomWalk(object):
    def __init__(self, num_point=5000):
        self.num_point = num_point
        self.x_points = [0]
        self.y_points = [0]

    def fill_walk(self):
        while len(self.x_points) < self.num_point:
            x_direction = choice([1])
            x_step = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            x_distance = x_direction * x_step

            y_direction = choice([1])
            y_setp = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            y_distance = y_direction * y_setp

            if x_distance == 0 and y_distance == 0:
                continue

            x_next = self.x_points[-1] + x_distance
            y_next = self.y_points[-1] + y_distance

            self.x_points.append(x_next)
            self.y_points.append(y_next)


while True:
    a = RandomWalk(50000)
    a.fill_walk()
    point_numbers = list(range(a.num_point))
    plt.scatter(a.x_points, a.y_points, s=1, c=point_numbers, cmap=plt.cm.Blues)
    plt.scatter(0, 0, c='green', s=100)
    plt.scatter(a.x_points[-1], a.y_points[-1], c='red', s=100)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    # plt.figure(figsize=(5, 3))
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
