import pandas as pd  

def process_large_csv(file_path, chunk_size=10_000):  
    for chunk in pd.read_csv(file_path, chunksize=chunk_size):  
        # Example: Filter rows  
        filtered = chunk[chunk["value"] > 0.5]  
        yield filtered  

# Simulate a 10GB CSV  
results = pd.concat(process_large_csv("fake_large_data.csv"))  
print("Processed rows:", len(results))  