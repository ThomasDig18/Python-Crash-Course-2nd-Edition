import matplotlib.pyplot as plt 


x_values = range(1, 501)
y_values = [x**2 for x in x_values]


plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=24)
ax.set_ylabel("Square of Value", fontsize=14)

ax.scatter(x_values, y_values, c="red", s=10)

ax.tick_params(axis='both', labelsize = 14)
ax.axis([0, 1100, 0, 500000])

plt.show()


