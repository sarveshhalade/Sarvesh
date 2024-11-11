import matplotlib.pyplot as plt
x=[40,80,50,90,95]
e=[0,0,0,0,0.1]
plt.pie(x,explode=e)
plt.title("Pie Plot")
plt.show()