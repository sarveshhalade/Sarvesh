import matplotlib.pyplot as plt
plt.plot([1,2,3],[4,5,6])
plt.xlim(1,5)
plt.ylim(1,6)
plt.subplot(2,2,1)

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.title("Demo Graph")
plt.legend("Values")

x = [3,1,3,12,2,4,4]
y = [3,2,1,4,5,6,7]
plt.subplot(2,2,2)

plt.bar(x,y)

import matplotlib.pyplot as plt
x=[1,2,3,4]
e=[0.1,0,0,0]
plt.subplot(2,2,3)
plt.pie(x,explode=e)
plt.title("Pie Plot")
plt.show()
