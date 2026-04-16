import numpy as np

def find_unique_elements(arr):
    unique_elements = np.unique(arr)
    return unique_elements

# Example usage
if __name__ == "__main__":
    arr = np.array([1, 2, 3, 4, 5, 2, 3, 6])
    unique_elements = find_unique_elements(arr)
    print("Unique elements in the array:", unique_elements)