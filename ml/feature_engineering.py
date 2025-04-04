import pandas as pd  
from sklearn.preprocessing import StandardScaler  

def preprocess_data(df):  
    # Handle missing values  
    df = df.fillna(df.median())  

    # One-hot encode categoricals  
    df = pd.get_dummies(df, columns=["category"])  

    # Scale numerical features  
    scaler = StandardScaler()  
    df[["age", "income"]] = scaler.fit_transform(df[["age", "income"]])  
    return df  

# Example  
data = {"age": [25, 30, None], "income": [50000, 80000, 60000], "category": ["A", "B", "A"]}  
df = pd.DataFrame(data)  
processed_df = preprocess_data(df)  
print(processed_df)  