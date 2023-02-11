# Creating Sample Data to Analyze 

import math
import pandas as pd
import numpy as np

from pathlib import Path
from matplotlib import pyplot as plt


def create_wave(num_data_points, sampling_frequency, waveAdder):
    
    # Used Parameters 
    # num_data_points, sampling_frequency, waveAdder are all used directly in the function. 
    # The waveAdder is in the format of [frequency, magnitude, starting time]

    # Unused Parameters 
    sampling_time = num_data_points / sampling_frequency

    # Time Array 
    time_array = np.arange(num_data_points)
    time_array = time_array / sampling_frequency

    sample = np.zeros(num_data_points)

    for wave in waveAdder:
        for i in range(num_data_points):
            if (i / sampling_frequency < wave[2]):
                sample[i] = sample[i] + 0
            else:
                sample[i] = sample[i] + wave[1] * np.sin(2 * math.pi * wave[0] * (i / sampling_frequency - wave[2]))

    return [time_array, sample]