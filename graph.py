import matplotlib.pyplot as plt
plt.style.use('dark_background')
xsin=np.arange(0,2*np.pi, 0.1)
ysin=np.sin(xsin)
print(ysin)
xcos=np.arange(0,2*np.pi, 0.1)
ycos=np.cos(xcos)
print(ycos)
xtan=np.arange(0,2*np.pi, 0.1)
ytan=np.tan(xtan)
print(ytan)
xcot=np.arange(0,2*np.pi, 0.1)
ycot=1/np.tan(xcot)
print(ycot)
plt.figure(figsize=(6,6))
plt.subplot(2,2,1)
plt.plot(xsin,ysin,'r--')
plt.title('sin curve')
plt.subplot(2,2,2)
plt.plot(xcos,ycos,'b--')
plt.title('cos curve')
plt.subplot(2,2,3)
plt.plot(xtan,ytan,'g--')
plt.title('tan curve')
plt.subplot(2,2,4)
plt.plot(xcot,ycot,'w--')
plt.title('cot curve')
plt.show()