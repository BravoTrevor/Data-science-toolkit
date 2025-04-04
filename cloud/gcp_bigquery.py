from google.cloud import bigquery  
import pandas as pd  

def query_to_dataframe(project_id, query):  
    client = bigquery.Client(project=project_id)  
    return client.query(query).to_dataframe()  

def dataframe_to_table(df, project_id, dataset_id, table_id):  
    client = bigquery.Client(project=project_id)  
    df.to_gbq(f"{dataset_id}.{table_id}", project_id=project_id, if_exists="replace")  

# Example: Query public dataset and convert to Pandas  
df = query_to_dataframe("bigquery-public-data", "SELECT * FROM `samples.shakespeare` LIMIT 100")  
print(df.head())  

# Example: Upload a DataFrame to BigQuery  
dataframe_to_table(df, "your-gcp-project", "your_dataset", "your_table")  