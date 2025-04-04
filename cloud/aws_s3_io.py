import boto3  
import numpy as np  
import io  

def save_npy_to_s3(data, bucket, key):  
    buffer = io.BytesIO()  
    np.save(buffer, data)  
    s3 = boto3.client("s3")  
    s3.put_object(Bucket=bucket, Key=key, Body=buffer.getvalue())  

def load_npy_from_s3(bucket, key):  
    s3 = boto3.client("s3")  
    response = s3.get_object(Bucket=bucket, Key=key)  
    return np.load(io.BytesIO(response["Body"].read()))  

# Example  
arr = np.random.rand(100, 100)  
save_npy_to_s3(arr, "my-bucket", "data.npy")  
loaded = load_npy_from_s3("my-bucket", "data.npy")  
print("Loaded array shape:", loaded.shape)  