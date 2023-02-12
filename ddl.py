import yaml
import pandas as pd

# from database import ENGINE


with open("config/config.yaml") as config_file:
    config = yaml.safe_load(config_file)
    config_data = config.get("DATA_PATH")

print(config_data)


if __name__ == "__main__":

    for table_name, path in config_data.items():
        print(table_name, path)
        # df = pd.read_parquet(path)
        # df.to_sql(table_name, con=ENGINE)
