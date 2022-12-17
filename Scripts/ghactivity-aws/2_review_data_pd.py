import pandas as pd


path_ghactivity_aws = r'C:\Users\lmman\Documents\GIT\AWS\Lambda\training-aws-lambda-ghactivity\Scripts\ghactivity-aws\data\2022-06-05-0.json.gz'

df = pd.read_json(path_ghactivity_aws, lines = True)

df[0:10]

df.shape

df.columns

df.dtypes

df['org']