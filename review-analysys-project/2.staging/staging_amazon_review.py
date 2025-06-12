import pandas as pd

file_path = r'C:\Repositorios\Data-Analysis-Track\data-analysys-project\raw_data\amazon.csv'

def get_staging_data():

    df = pd.read_csv(file_path)


    df = df.drop_duplicates()


    df.rename(columns={
        'product_id'         : 'dim_prdt_tk',
        'product_name'       : 'product_title',
        'category'           : 'product_category',
        'discounted_price'   : 'discounted_value',
        'actual_price'       : 'original_price',
        'discount_percentage': 'vp_discount',
        'rating'             : 'customer_rating',
        'rating_count'       : 'customer_reviews_count',
        'about_product'      : 'product_summary',
        'user_id'            : 'dim_cstm_tk',
        'user_name'          : 'customer_name',
        'review_id'          : 'dim_revw_tk',
        'review_title'       : 'review_title',
        'review_content'     : 'review_details',
        'img_link'           : 'img_url',
        'product_link'       : 'product_url'
    }, inplace=True)


    return df
