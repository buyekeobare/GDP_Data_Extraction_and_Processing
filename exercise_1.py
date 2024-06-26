import numpy as np
import pandas as pd

# You can also use this section to suppress warnings generated by your code:
def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

# Extract tables from webpage using Pandas. Retain table number 3 as the required dataframe.
tables = pd.read_html("https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29")
df = tables[3]

# Replace the column headers with column numbers
df.columns = range(df.shape[1])

# Retain columns with index 0 and 2 (name of country and value of GDP quoted by IMF)
df = df[[0, 2]]

# Retain the Rows with index 1 to 10, indicating the top 10 economies of the world.
df = df.iloc[1:11, :]

# Assign column names as "Country" and "GDP (Million USD)"
df.columns = ['Country', 'GDP (Million USD)']

# Print the resulting dataframe to verify the results
print(df)


