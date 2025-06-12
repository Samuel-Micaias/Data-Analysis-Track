import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'staging')))

from staging_amazon_review import get_staging_data

df_staging = get_staging_data()
df_dim_product = df_staging[['dim_prdt_tk','product_category','product_title','product_summary','img_url','product_url']].drop_duplicates(subset='dim_prdt_tk')

output_dir = 'data_cleaned'
os.makedirs(output_dir, exist_ok=True)  # Cria a pasta se não existir
df_dim_product.to_csv(os.path.join(output_dir, 'dim_product.csv'), index=False)