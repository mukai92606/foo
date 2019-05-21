import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft

class Mother:
    def __init__(self,start,stop,interval):
        self.start=start
        self.stop=stop
        self.interval=interval
    def display(self):
        a = np.arange(self.start, self.stop, self.interval)
        b=np.sin(a)
        c=np.cos(a)
        d=np.tan(a)/10
        plt.plot(a,b)
        plt.plot(a,c)
        plt.plot(a,d)
        e = b+c+d
        plt.plot(a, e, linewidth=6)
        f=fft(b+c+d)/10
        plt.plot(a, f, linewidth=6, color='y')
        plt.show()

mot1=Mother(-10,10,0.1)
mot1.display()

#mot2 = Mother(-10, 10,1)
#mot2.display()
# ggggggggggg
# hhhhhhhh