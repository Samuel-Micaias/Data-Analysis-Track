import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'staging')))

from staging_amazon_review import get_staging_data

df_staging = get_staging_data()
df_dim_customers = df_staging[['dim_cstm_tk', 'customer_name']].drop_duplicates(subset='dim_cstm_tk')

output_dir = 'data_cleaned'
os.makedirs(output_dir, exist_ok=True)  # Cria a pasta se não existir
df_dim_customers.to_csv(os.path.join(output_dir, 'dim_customers.csv'), index=False)

