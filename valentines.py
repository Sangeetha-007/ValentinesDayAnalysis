import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller

# reading the dataset using read_csv
df = pd.read_csv("/Users/sangeetha/Downloads/archive/historical_spending.csv")

print(df.head())

# Manually adding values for 2023-2025
new_data = pd.DataFrame({
    'Year': [2023, 2024, 2025],
    'PercentCelebrating': [52.0, 53.0, 56.0]  # Replace with actual values you want
})

# Append the new data
df = pd.concat([df, new_data], ignore_index=True)

# Assuming df is your DataFrame
sns.set(style="whitegrid")  # Setting the style to whitegrid for a clean background
# Calculate EMA
#span = 25
df['EMA_20'] = df['PercentCelebrating'].ewm(span=20, adjust=False).mean()  # Use a longer span

plt.figure(figsize=(12, 10))  # Setting the figure size
sns.lineplot(data=df, x='Year', y='PercentCelebrating', label='Percent Celebrating', color='red', linewidth=2.5)
sns.lineplot(data=df, x='Year', y='EMA_20', label='Smoothed EMA (20-year span)', color='purple', linewidth=2.5)

# Adding labels and title
plt.xlabel('Date', fontweight='bold')
plt.ylabel('Spending Percentage', fontweight='bold')
#plt.plot(df['EMA'], label=f'EMA (span={span})', color='orange')
plt.title('Valentines Day Celebrating Over Time')




plt.xticks(df['Year'], rotation=45) 
plt.show()