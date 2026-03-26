# Living Planet Data Analysis Script
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
plt.style.use('seaborn-v0_8')

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv("global-living-planet-index.csv")
df.head()

# -----------------------------
# 2. DATA CLEANING
# -----------------------------
df = pd.read_csv("heart.csv")
print(df.head())
print(df.info())

df = df.rename(columns={
    'Entity': 'Region',
    'Living Planet Index': 'LPI',
    'Upper confidence interval of Living Planet Index': 'LPI_upper',
    'Lower confidence interval of Living Planet Index': 'LPI_lower'
})
df.head()

df['Year']= pd.to_numeric(df['Year'], errors='coerce').astype(int)
df['LPI']= pd.to_numeric(df['LPI'], errors='coerce')
df['LPI_upper']= pd.to_numeric(df['LPI_upper'], errors='coerce')
df['LPI_lower']= pd.to_numeric(df['LPI_lower'], errors='coerce')

# -----------------------------
# 3. BASIC INFO
# -----------------------------
print(f"Regions ({df['Region'].nunique()}):")
print(df['Region'].unique())

print(f"\nYear range : {df['Year'].min()}-{df['Year'].max()}")

# -----------------------------
# 4. PLOT: LPI BY REGION
# -----------------------------
plt.figure(figsize=(12, 6))

for region in df['Region'].unique():
    sub = df[df['Region']== region]
    plt.plot(sub['Year'], sub['LPI'], label=region)
plt.title("Living Planet Index by Region (1970–2020)")
plt.xlabel("Year")
plt.ylabel("LPI")
plt.legend()
plt.grid(True)
plt.show()

# -----------------------------
# 5. GLOBAL TREND
# -----------------------------
world=df[df['Region']== 'World']
plt.figure(figsize=(12,6))
plt.plot(world['Year'], world['LPI'], linewidth=3)
plt.xlabel("Year")
plt.ylabel("LPI")
plt.grid(True)
plt.show()

# -----------------------------
# 6. CONFIDENCE INTERVAL
# -----------------------------
plt.figure(figsize=(12, 6))

plt.plot(world['Year'], world['LPI'], label='LPI')

plt.fill_between(
    world['Year'],
    world['LPI_lower'],
    world['LPI_upper'],
    alpha=0.2,
    label='Confidence interval'
)

plt.title("Global LPI with Confidence Interval")
plt.xlabel("Year")
plt.ylabel("LPI")

plt.legend()
plt.grid(True)

plt.show()

# -----------------------------
# 7. BOXPLOT
# -----------------------------
sns.boxplot(x='Region', y='LPI', data=df)
plt.title("Distribution of LPI by Region")
plt.xticks(rotation=45)
plt.show()

# -----------------------------
# 8. SMOOTHING
# -----------------------------
world = df[df['Region'] == 'World'].copy()

world['LPI_smooth']=world['LPI'].rolling(window=5).mean()

plt.figure(figsize=(12,6))
plt.plot(world['Year'], world['LPI'], alpha=0.4, label='Original')
plt.plot(world['Year'], world['LPI_smooth'], linewidth=3, label='Smoothed')
plt.legend()
plt.title("Smoothed Global LPI Trend")
plt.show()

# -----------------------------
# 9. BARPLOT (2020)
# -----------------------------
latest=df[df['Year']==2020]
plt.figure(figsize=(12,6))
sns.barplot(x='Region', y='LPI', hue='Region', data=latest, palette='pastel')
plt.xticks(rotation=45)
plt.title("LPI by Region in 2020")
plt.show()

# -----------------------------
# 10. CORRELATION
# -----------------------------
correlation=df[['LPI', 'LPI_upper', 'LPI_lower']].corr()

plt.figure(figsize=(12,6))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# -----------------------------
# 11. CONCLUSION
# -----------------------------
- Global biodiversity has declined significantly since 1970
- The rate of decline varies across regions
- Confidence intervals indicate increasing uncertainty
- Data smoothing reveals long-term trends clearly