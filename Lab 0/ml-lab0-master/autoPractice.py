import numpy as np
import pandas as pd

data = pd.read_fwf("auto-mpg.data")

# data.info()
# print(data.head(10))

data.columns = (["mpg", "cylinders", "displacement", "horsepower", 
"weight", "acceleration", "model year", "origin", "car name"])
print(data.head(5))