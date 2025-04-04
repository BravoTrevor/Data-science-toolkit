import tensorflow as tf  
import pandas as pd  
from sklearn.model_selection import train_test_split  

def create_tf_dataset(df, target_col, batch_size=32):  
    features = df.drop(columns=[target_col])  
    labels = df[target_col]  
    X_train, X_val, y_train, y_val = train_test_split(features, labels, test_size=0.2)  

    train_dataset = tf.data.Dataset.from_tensor_slices((X_train.values, y_train.values))  
    train_dataset = train_dataset.shuffle(1000).batch(batch_size)  

    val_dataset = tf.data.Dataset.from_tensor_slices((X_val.values, y_val.values))  
    val_dataset = val_dataset.batch(batch_size)  

    return train_dataset, val_dataset  

# Example  
df = pd.DataFrame({"feature1": [1, 2, 3], "feature2": [4, 5, 6], "target": [0, 1, 0]})  
train_ds, val_ds = create_tf_dataset(df, "target")  

model = tf.keras.Sequential([  
    tf.keras.layers.Dense(10, activation="relu"),  
    tf.keras.layers.Dense(1, activation="sigmoid")  
])  

model.compile(optimizer="adam", loss="binary_crossentropy")  
model.fit(train_ds, validation_data=val_ds, epochs=5)  