#!/usr/bin/env python
# coding: utf-8

# In[ ]:


{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "abff74a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "from scipy import signal\n",
    "\n",
    "\n",
    "class Generator():\n",
    "    \n",
    "    def __init__(self, freq, Sampling_freq, duration, Amplitude):  \n",
    "        self.freq = freq\n",
    "        self.Sampling_freq = Sampling_freq\n",
    "        self.duration = duration\n",
    "        self.Amplitude = Amplitude\n",
    "        self.count = 0\n",
    "        \n",
    "        #Гармонический  \n",
    "    def CreateSignal_Harmonic(self,duration):\n",
    "        self.xn=np.arange(0, duration, 1./self.Sampling_freq)\n",
    "        for i in range(len(self.xn)):\n",
    "            yield(self.Amplitude*np.cos(self.xn[i]*self.freq))\n",
    "       \n",
    "        #Треугольник  \n",
    "    def CreateSignal_triangle(self,duration):\n",
    "        if duration<=0:\n",
    "            duration=self.duration\n",
    "        xn=np.arange(0,duration,1./self.Sampling_freq)\n",
    "        self.yn=self.Amplitude*signal.sawtooth(2*np.pi*self.freq*xn)\n",
    "        \n",
    "        return self.yn\n",
    "        #ШИМ\n",
    "    def CreateSignal_SHIM(self,duration,cycles):\n",
    "        if duration<=0:\n",
    "            duration=self.duration\n",
    "        \n",
    "        percent=cycles\n",
    "        d_dur=1./self.Sampling_freq\n",
    "        \n",
    "        xn=np,arange(0,duration,d_dur)\n",
    "        self.yn=self.Amplitude*xn%(1./self_freq)<(1./self.freq)*percent/100\n",
    "        \n",
    "        return self.yn\n",
    "    \n",
    "        #Пила\n",
    "    def CreateSignal_Saw(self,duration):\n",
    "        if duration<=0:\n",
    "            duration=self.duration\n",
    "            \n",
    "        xn=np.arange(0,duration,1./self.Sampling_freq)\n",
    "        yn=np.exp((complex(-0.5,self.freq))*xn)\n",
    "        self.yn=np.arange(yn)*self.Amplitude/3\n",
    "        \n",
    "        return self.yn\n",
    "        \n",
    "        #Возвращает по номеру\n",
    "    def get_sample_n(self,n):\n",
    "        return self.yn[n]\n",
    "        \n",
    "        #Возвращает весь сигнал\n",
    "    def get_sample_duration(self,duration):\n",
    "        print(len(self.yn))\n",
    "        print(duration*self.Sampling_freq)\n",
    "        \n",
    "        return self.yn[duration*self.Sampling_freq]\n",
    "    \n",
    "        #Возвращает следующую выборку\n",
    "    def generator(self,duration):\n",
    "        xn=np.arange(self.xn[len(self.xn)-1],self.xn[len(self.xn)-1]+t,1./self.Sampling_freq)\n",
    "        for i in range(len(xn)):\n",
    "            yield(self.Amplitude*np.cos(xn[i]*self.freq))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c23da0db",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

