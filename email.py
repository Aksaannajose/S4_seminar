import numpy as n
import random
import pandas as pd
import gzip
n = 40428967  #total number of records in the clickstream data
sample_size = 1000000
skip_values = sorted(random.sample(range(1,n), n-sample_size))
parse_date = lambda val : pd.datetime.strptime(val, '%y%m%d%H')
with gzip.open('train.gz') as f:
    train = pd.read_csv(f, parse_dates = ['hour'], date_parser = parse_date, dtype=pd, skiprows = skip_values)

