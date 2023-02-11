import pandas as pd
from sqlalchemy import create_engine


CONNECTION = "poastgres://postgres:postgres@root:postgres/db"
CON = create_engine(CONNECTION)
path_data_dict = {
    "post_info": path_post_info,
    "user_info": path_user_info,
    "feed_data": path_feed_data,
    "like_post": path_like_post
}


if __name__ == "__main__":

    for table_name, path in path_data_dict.items():
        df = pd.read_parquet(path)
        df.to_sql(table_name, con=CON)
