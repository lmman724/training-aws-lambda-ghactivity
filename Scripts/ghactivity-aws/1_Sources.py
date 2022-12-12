import requests

res = requests.get('https://data.gharchive.org/2022-06-05-0.json.gz')

#type(res)

type(res.content)

#file_name = '2022-06-05-0.json.gz'

path = r'C:\Users\admin\OneDrive\Documents\Git\Udemy\AWS\AWS_Lambda\Personal_code\ghactivity-aws\data\2022-06-05-0.json.gz'

file = open(path, 'wb')

#
file.write(res.content)

file.close()
#print(type(file))

