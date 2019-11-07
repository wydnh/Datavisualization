import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    a = RandomWalk(5000)
    a.fill_walk()
    point_numbers = list(range(a.num_point))
    plt.plot(a.x_points, a.y_points, linewidth=1)
    plt.scatter(0, 0, c='green', s=100)
    plt.scatter(a.x_points[-1], a.y_points[-1], c='red', s=100)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    # plt.figure(figsize=(5, 3))
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
