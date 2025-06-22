import pandas as pd

df = pd.read_csv('/content/sample_data/mnist_test.csv')
type(df)

df.head() 

df.tail(2)

df.shape #num of rows and columns

df.columns

df.info() # each column dataType, non-null count