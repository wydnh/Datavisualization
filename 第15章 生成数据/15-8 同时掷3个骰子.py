import pygal

from die import Die

die1 = Die()
die2 = Die()
die3 = Die()

result = [die1.roll() + die2.roll() + die3.roll() for i in range(1000000)]

frequencies = [result.count(i) for i in range(3, die1.num_sides + die2.num_sides + die3.num_sides + 1)]

hist = pygal.Bar()
hist.title = "两个 d6 掷1000次筛子的结果"
hist.x_labels = list(range(3, die1.num_sides + die2.num_sides + die3.num_sides + 1))
hist.x_title = "result"
hist.y_title = "frequency of result"
hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')
