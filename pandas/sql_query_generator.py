import pandas as pd  

def pandas_to_sql(df, table_name):  
    columns = ", ".join(df.columns)  
    values = []  
    for row in df.itertuples(index=False):  
        vals = ", ".join(f"'{x}'" if isinstance(x, str) else str(x) for x in row)  
        values.append(f"({vals})")  
    return f"INSERT INTO {table_name} ({columns}) VALUES {', '.join(values)};"  

# Example  
df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [25, 30]})  
print(pandas_to_sql(df, "users"))  