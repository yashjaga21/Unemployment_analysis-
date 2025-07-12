import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('unemployment_data.csv')

# Basic info
print(df.info())
print(df.describe())

# Handling missing values (if any)
df = df.dropna()

# Plot unemployment rate over time
plt.figure(figsize=(10, 5))
sns.lineplot(x='Date', y='Unemployment Rate', data=df)
plt.title('Unemployment Rate Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
