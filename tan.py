import matplotlib.pyplot as plt
plt.style.use('dark_background')
x=np.arange(0,2*np.pi, 0.1)
y=np.tan(x)
plt.figure(figsize=(6,6))
plt.plot(x,y,'r')
plt.title('tan curve')
plt.show()
