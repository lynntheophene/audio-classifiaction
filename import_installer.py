import subprocess
import sys

# List of packages to install
packages = [
    "tensorflow",
    "scikit-learn",
    "numpy",
    "matplotlib",    # Optional, for plotting
    "jupyterlab",    # Optional, for working in notebooks
    "librosa",       # For audio processing
    "pandas",        # For data manipulation
    "tqdm",          # For progress bars
    "resampy",       # For audio resampling
]

def install_packages(package_list):
    for package in package_list:
        print(f"\nInstalling {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    install_packages(packages)
    print("\n✅ All packages installed successfully!\n")

    # Try importing to verify
    import tensorflow as tf
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, Dropout
    from tensorflow.keras.optimizers import Adam
    from sklearn import datasets, model_selection, metrics
    import numpy as np
    import librosa
    import pandas as pd
    from tqdm import tqdm  # Import tqdm
    import resampy  # Import resampy

    print("✅ All modules imported successfully!")

except Exception as e:
    print("\n❌ An error occurred:", e)
