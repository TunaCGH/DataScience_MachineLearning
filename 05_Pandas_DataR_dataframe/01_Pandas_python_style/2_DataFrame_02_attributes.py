'''
Flow of contents:

1. Shape and Size attributes:
   + df.shape: Returns a tuple (rows, columns)
   + df.size: Returns total number of elements (rows * columns)
   + df.ndim: Returns number of dimensions (always 2 for DataFrame)

2. Data types and Structure attributes:
   + df.dtypes: Returns data types of each column
   + df.columns: Returns column labels
   + df.index: Returns row labels
   + df.axes: Returns a list of both row and column labels

3. Data Access attributes:
   + df.values: Returns the underlying numpy array of the DataFrame
   + df.T: Returns the transpose of the DataFrame
   + df.empty: Returns True if DataFrame is empty, else False

4. Memory and Performance attributes:
   + df.info(memory_usage = 'deep'): Provides a concise summary of the DataFrame
   + df.memory_usage(deep = True): Returns memory usage of each column

5. Advanced attributes:
   + df.attrs: Dictionary for storing custom metadata
   + df.style: Returns a Styler object for HTML/CSS formatting
   + df.flags: Configuration object controlling DataFrame behavior. 
'''

import pandas as pd