# Import the necessary libraries
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [10, 25, 15, 30]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Create a bar chart
plt.figure(figsize=(8, 4))  # Adjust the figure size if needed
plt.bar(df['Category'], df['Value'])
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart in Power BI')

# Display the plot
plt.show()
