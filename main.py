import os
import pandas as pd
import json
import numpy as np
import sys
import pickle

n_col = None
n_row = None
stats = None
msg = None

database_uri = os.getenv('DATABASE_URI','no_database_uri')

if os.path.exists(database_uri):

  try:
    test = pd.read_csv(database_uri)

    column_names = test.columns
    summary = test.describe()
    stats = summary.to_json()
    
    n_col = len(column_names)
    n_row = len(test)
    # cols = {}
    # for col in summary.keys():
    #     values = summary[col]
        # cols[col] = {
        #     "count": values["count"],
        #     "mean": values["mean"],
        #     "std": values["std"],
        #     "min": values["min"],
        #     "q1": values["25%"],
        #     "median": values["50%"],
        #     "q3": values["75%"],
        #     "max": values["max"]
        # }
    #print(test['Age'].mean())

    #test = test.set_index(['Age'], inplace = True)
    #print(test["Age"]
  except:
    msg = sys.exc_info()[0]
  
else:
  msg = f"File {database_uri} not found"


result = {
    'Number of columns': n_col,
    'Number of rows': n_row,
    'statistics': stats,
    'msg' : msg,
    'test' : "This is not the right version"
}

# # Write output to file

output_file = os.environ["OUTPUT_FILE"]

with open(output_file, 'wb') as f:
    f.write(pickle.dumps(result))