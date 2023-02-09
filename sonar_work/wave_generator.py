# Creating Sample Data to Analyze 

import math
import pandas as pd
import numpy as np

from pathlib import Path
from matplotlib import pyplot as plt


def create_wave():
    print("hello world")

# Parameters 
N = 1000000
sampling_frequency = 500000
sampling_time = N / sampling_frequency

# Time Array 
time_array = np.arange(N)
time_array = time_array / sampling_frequency

# The waveAdder is in the format of [frequency, magnitude, starting time]
waveAdder = [[50000, 1, 0.5], [20000, 2, 1]]

sample = np.zeros(N)

for wave in waveAdder:
    for i in range(N):
        if (i / sampling_frequency < wave[2]):
            sample[i] = sample[i] + 0
        else:
            sample[i] = sample[i] + wave[1] * np.sin(2 * math.pi * wave[0] * (i / sampling_frequency - wave[2]))

plt.plot(time_array, sample)