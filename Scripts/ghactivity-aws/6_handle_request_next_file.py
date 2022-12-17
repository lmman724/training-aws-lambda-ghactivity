from datetime import datetime as dt

dt.now()

type(dt.now())

dt.strftime(dt(2022, 12, 17, 15, 19, 44, 365), "%Y-%m-%d %H:%m")

from datetime import timedelta as td

current_next_1hour = dt(2022, 12, 17, 15, 19, 44, 365) + td(hours= 1)

type(current_next_1hour)


#name file
#'2022-06-05-7.json.gz'
#'2022-06-05-8.json.gz'

# dt.strftime(dt.strptime('2022-06-05-7', '%Y-%m-%d-%H') + td(hours=1),'%Y-%m-%d-%H')

next_file = f"{dt.strftime(dt.strptime('2022-06-05-7', '%Y-%m-%d-%H') + td(hours=1),'%Y-%m-%d-%H')}.json.gz"

import requests

res = requests.get(f'https://data.gharchive.org/{next_file}')

file = open(f'C:/Users/lmman/Documents/GIT/AWS/Lambda/training-aws-lambda-ghactivity/Scripts/ghactivity-aws/data/{next_file}', 'wb')

file.write(res.content)
file.close()