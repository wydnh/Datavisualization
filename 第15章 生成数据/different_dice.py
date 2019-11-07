import pygal

from die import Die

die1 = Die(6)
die2 = Die(10)

while True:
    result = [die1.roll() + die2.roll() for i in range(50000)]
    frequencies = [result.count(i) for i in range(2, die1.num_sides + die2.num_sides + 1)]

    hist = pygal.Bar()
    hist.title = "d6和d10 掷50000次筛子的结果"
    hist.x_labels = [x for x in range(2, die1.num_sides + die2.num_sides + 1)]
    hist.x_title = "result"
    hist.y_title = "frequency of result"
    hist.add('D6 + D10', frequencies)
    hist.render_to_file('die_visual.svg')

    panduan = input("y/n? ")
    if panduan == "n":
        break