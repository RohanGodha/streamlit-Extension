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
plt.bar(df['Category'], df['Value'], color='skyblue', alpha=0.7)  # Customize color and transparency
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart in Power BI')

# Add labels to the bars
for i, value in enumerate(df['Value']):
    plt.text(i, value + 1, str(value), ha='center', va='bottom', fontsize=12)

# Customize the axis labels and title
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Category', fontsize=14)
plt.ylabel('Value', fontsize=14)
plt.title('Bar Chart in Power BI', fontsize=16)

# Display the plot
plt.grid(axis='y', linestyle='--', alpha=0.5)  # Add a horizontal grid
plt.tight_layout()  # Ensure labels fit within the figure
plt.show()
