import pandas as pd

sales = [120, 135, 150, 160, 180, 200, 210]
series = pd.Series(sales)

employee_performance = {
    'Employee': ['Alaa', 'Mona', 'Khaled'],
    'Performance Score': [88, 92, 79]
}
dataFrame = pd.DataFrame(employee_performance)

series
dataFrame