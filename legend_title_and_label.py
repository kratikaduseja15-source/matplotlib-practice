import matplotlib.pyplot as plt
x=[1,2,3]
y=[5,9,6]
x2=[1,2,3]
y2=[10,14,16]
plt.plot(x,y,label='First line')
plt.plot(x2,y2,label='second line')
plt.xlabel('plot number')
plt.ylabel('important var')
plt.title('interesting graph /ncheck it out')
plt.legend
plt.show()