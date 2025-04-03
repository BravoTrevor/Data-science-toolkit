import numpy as np  
import time  

# Benchmark: Vectorized vs. Loop  
def pure_python_sum(size):  
    data = list(range(size))  
    return sum(data)  

def numpy_sum(size):  
    data = np.arange(size)  
    return np.sum(data)  

# Test  
size = 10_000_000  
start = time.time()  
pure_python_sum(size)  
print(f"Python loop: {time.time() - start:.4f}s")  

start = time.time()  
numpy_sum(size)  
print(f"NumPy vectorized: {time.time() - start:.4f}s")  