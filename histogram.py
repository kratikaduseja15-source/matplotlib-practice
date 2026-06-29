import matplotlib.pyplot as plt
population_age= [22,56,88,99,4,5,7,75,48,12,45,9,15,62,58,25,55,5,5,52,5,5,5,2,65,52,2,66,5,5,110,17,121,130]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(population_age, bins, histtype='bar' ,rwidth=0.8)
plt.xlabel('plot number')
plt.ylabel('important var')
plt.title('interesting graph /ncheck it out')
plt.legend
plt.show()

