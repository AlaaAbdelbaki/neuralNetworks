import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import make_interp_spline

# Get a list of files in the losses directory
files = os.listdir('losses')

for file in files:
    # Load the CSV file
    # Replace 'file.csv' with your actual file path
    filePath = os.path.join('losses', file)
    data = pd.read_csv(filePath)

    # Check the first few rows to ensure correct loading
    print(data.head())
    # Generate a smooth curve using spline interpolation
    x = data['epoch']
    y = data['loss']

    # Create more x-points for smoothing
    x_smooth = np.linspace(x.min(), x.max(), 500)
    spline = make_interp_spline(x, y, k=3)  # k=3 for cubic spline
    y_smooth = spline(x_smooth)

    # Plot the loss chart
    plt.figure(figsize=(10, 6))
    plt.plot(x_smooth, y_smooth, label='Loss',
             color='b', linestyle='-', linewidth=2)
    plt.title('Loss vs. Epoch', fontsize=16)
    plt.xlabel('Epoch', fontsize=14)
    plt.ylabel('Loss', fontsize=14)
    plt.grid(True)
    plt.legend(fontsize=12)
    output_image = file.replace('.csv', '') + '_image.png'
    plt.savefig(f'loss_charts/{output_image}')
    # plt.show()
