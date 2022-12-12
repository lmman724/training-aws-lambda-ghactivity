import pandas as pd


path_ghaactivity_aws = r'C:\Users\admin\OneDrive\Documents\Git\Udemy\AWS\AWS_Lambda\Personal_code\ghactivity-aws\data\2022-06-05-0.json.gz'

df = pd.read_json(path_ghaactivity_aws, lines = True)

df.shape

df.columns

df.dtypes

df['org']