import matplotlib.pyplot as plt 

num1 = [1, 2, 3, 4, 5]
cubes1 = [x**3 for x in num1]
fig, ax = plt.subplots()


plt.style.use('seaborn-dark')

ax.scatter(num1, cubes1, s=10)
ax.plot(num1, cubes1, linewidth=1)



ax.set_title("Cube Graph", fontsize=24)
ax.set_xlabel("Value", fontsize=16)
ax.set_ylabel("Cubed Numbers", fontsize=16)



plt.show()