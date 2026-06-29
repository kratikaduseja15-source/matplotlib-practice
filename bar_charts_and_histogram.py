import matplotlib.pyplot as plt

x=[2,4,6,8,10]
y=[6,7,8,5,6]

x2=[1,3,5,7,9]
y2=[6,8,5,7,1]

plt.bar(x,y, label='bar1' , color='r')
plt.bar(x2,y2, label='bar2' , color='c')

plt.xlabel('plot number')
plt.ylabel('important var')
plt.title('interesting graph')
plt.legend
plt.show()

