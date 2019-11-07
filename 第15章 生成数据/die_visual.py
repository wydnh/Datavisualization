import pygal

from die import Die

die = Die()

result = [die.roll() for i in range(1000)]
frequencies = [result.count(i) for i in range(1, die.num_sides + 1)]

hist = pygal.Bar()
hist.title = "d6 掷1000次筛子的结果"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "result"
hist.y_title = "frequency of result"
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')