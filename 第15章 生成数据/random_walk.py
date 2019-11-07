from random import choice


class RandomWalk(object):
    def __init__(self, num_point=5000):
        self.num_point = num_point
        self.x_points = [0]
        self.y_points = [0]

    def fill_walk(self):
        while len(self.x_points) < self.num_point:
            x_direction = choice([1, -1])
            x_step = choice([0, 1, 2, 3, 4, 5])
            x_distance = x_direction * x_step

            y_direction = choice([1, -1])
            y_setp = choice([0, 1, 2, 3, 4, 5])
            y_distance = y_direction * y_setp

            if x_distance == 0 and y_distance == 0:
                continue

            x_next = self.x_points[-1] + x_distance
            y_next = self.y_points[-1] + y_distance

            self.x_points.append(x_next)
            self.y_points.append(y_next)


# a = RandomWalk()
# a.fill_walk()
# print(len(a.x_points))
# print(len(a.y_points))
