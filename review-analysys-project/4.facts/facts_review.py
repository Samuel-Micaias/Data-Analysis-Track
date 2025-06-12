import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'staging')))


from staging_amazon_review import get_staging_data


df_staging = get_staging_data()
df_facts_review = df_staging[['dim_prdt_tk','dim_cstm_tk','dim_revw_tk','discounted_value','original_price','vp_discount','customer_rating','customer_reviews_count','review_title']]

output_dir = 'data_cleaned'
os.makedirs(output_dir, exist_ok=True)  # Cria a pasta se não existir
df_facts_review.to_csv(os.path.join(output_dir, 'facts_review.csv'), index=False)