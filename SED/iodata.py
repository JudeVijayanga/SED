import h5py
import numpy as np


def save_checkpoint(array: np.ndarray, filename: str):
    """
    Save a NumPy array to an HDF5 (.h5) file using h5py.
    """
    with h5py.File(f"{filename}.h5", "w") as hf:
        hf.create_dataset("data", data=array)
    print(f"Checkpoint saved to {filename}.h5")


def load_checkpoint(filename: str) -> np.ndarray:
    """
    Load a NumPy array from an HDF5 (.h5) file using h5py.
    """
    with h5py.File(f"{filename}.h5", "r") as hf:
        array = hf["data"][:]
    print(f"Checkpoint loaded from {filename}.h5")
    return array
