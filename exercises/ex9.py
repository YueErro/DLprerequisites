import os
import ex8
import numpy as np
import pandas as pd

spirals, colors = ex8.getSpirals()
dict = {'x': spirals[0,:], 'y': spirals[1,:], 'c': colors}

df = pd.DataFrame(dict)

ex9dir = os.path.dirname(os.path.realpath(__file__))
parentPath = os.path.dirname(ex9dir)

try:
    df.to_csv(parentPath + '/csv/ex9.csv')
except IOError:
    raise Exception("Folder does not exist")
