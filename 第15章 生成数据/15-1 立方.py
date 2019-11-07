import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, s=40, c=y_values, cmap=plt.cm.BuGn)
# plt.scatter(x_values, y_values, s=40)

plt.title("x'sancifang", fontsize=24)
plt.xlabel("x", fontsize=14)
plt.ylabel("x*3", fontsize=14)
plt.tick_params(axis='both', labelsize=14)

plt.axis([0, 5000, 0, 5000**3])


plt.savefig("sancifang.png", bbox_inches='tight')
plt.show()