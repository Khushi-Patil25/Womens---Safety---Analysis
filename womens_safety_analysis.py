import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("crcCAW_r1.csv")

# First 5 rows
print(df.head())

# Dataset information
print(df.info())

# Number of rows and columns
print("Shape:", df.shape)

print(df["CRIME HEAD"].unique())
x = df[df['STATE/UT'] != 'TOTAL Crime against Women'].copy()

years = [str(y) for y in range(2001, 2013)]

x['CATEGORY_TOTAL'] = x[years].sum(axis=1)

result = x.groupby('CRIME HEAD')['CATEGORY_TOTAL'].sum().sort_values(ascending=False)

print(result)

result.plot(kind="bar", figsize=(12, 6))

plt.xlabel("Crime Category")
plt.ylabel("Total Cases")
plt.title("Crime Against Women - Category Wise Analysis")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

result.plot(kind="bar", figsize=(12, 6))

plt.title("Crime Against Women - Category Wise Total (2001-2012)")
plt.xlabel("Crime Category")
plt.ylabel("Total Cases")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.show()

# Step 2: Year-wise Crime Analysis

years = [str(year) for year in range(2001, 2013)]

# Remove total row
year_data = df[df["STATE/UT"] != "TOTAL Crime against Women"].copy()

# Calculate total crimes for each year
yearly_total = year_data[years].sum()

print("\nYear-wise Total Crimes:")
print(yearly_total)

# Line Chart
plt.figure(figsize=(10, 6))

plt.plot(yearly_total.index, yearly_total.values, marker="o")

plt.title("Crime Against Women - Year-wise Analysis")
plt.xlabel("Year")
plt.ylabel("Total Cases")

plt.grid(True)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Step 3: State-wise Crime Analysis

state_data = df[df["STATE/UT"] != "TOTAL Crime against Women"].copy()

# Calculate total crimes for each state
state_data["STATE_TOTAL"] = state_data[years].sum(axis=1)

# Group by state
state_total = state_data.groupby("STATE/UT")["STATE_TOTAL"].sum()

# Top 10 states
top_10_states = state_total.sort_values(ascending=False).head(10)

print("\nTop 10 States/UTs by Total Crimes:")
print(top_10_states)

# Bar Chart
plt.figure(figsize=(12, 6))

top_10_states.plot(kind="bar")

plt.title("Top 10 States/UTs - Crime Against Women (2001-2012)")
plt.xlabel("State/UT")
plt.ylabel("Total Cases")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.show()

# Step 4: Most Common Crime Category by State

# Remove total row
analysis_data = df[
    df["STATE/UT"] != "TOTAL Crime against Women"
].copy()

# Calculate total cases for each crime category
analysis_data["CATEGORY_TOTAL"] = analysis_data[years].sum(axis=1)

# Find the highest crime category for each state
state_category = (
    analysis_data.loc[
        analysis_data.groupby("STATE/UT")["CATEGORY_TOTAL"].idxmax()
    ]
    [["STATE/UT", "CRIME HEAD", "CATEGORY_TOTAL"]]
    .sort_values("CATEGORY_TOTAL", ascending=False)
)

print("\nMost Common Crime Category by State:")
print(state_category.to_string(index=False))

# Step 5: Crime Category Trend Analysis

# Remove total state and total crime category
trend_data = df[
    (df["STATE/UT"] != "TOTAL Crime against Women") &
    (df["CRIME HEAD"] != "TOTAL CRIMES AGAINST WOMEN")
].copy()

# Calculate total cases for each crime category year-wise
category_yearly = trend_data.groupby("CRIME HEAD")[years].sum()

print("\nCrime Category Trend (2001-2012):")
print(category_yearly)

# Line Chart
plt.figure(figsize=(14, 7))

for category in category_yearly.index:
    plt.plot(
        years,
        category_yearly.loc[category],
        marker="o",
        label=category
    )

plt.title("Crime Category Trends Against Women (2001-2012)")
plt.xlabel("Year")
plt.ylabel("Total Cases")

plt.xticks(rotation=45)
plt.legend(fontsize=8)
plt.grid(True)

plt.tight_layout()  
plt.show()

# Step 6: High-Risk Crime Categories

# Remove total state and total crime category
risk_data = df[
    (df["STATE/UT"] != "TOTAL Crime against Women") &
    (df["CRIME HEAD"] != "TOTAL CRIMES AGAINST WOMEN")
].copy()

# Calculate total cases for each crime category
risk_data["CATEGORY_TOTAL"] = risk_data[years].sum(axis=1)

# Group by crime category
risk_category = (
    risk_data.groupby("CRIME HEAD")["CATEGORY_TOTAL"]
    .sum()
    .sort_values(ascending=False)
)

print("\nHigh-Risk Crime Categories:")
print(risk_category)

# Top 5 High-Risk Categories
top_5_risk = risk_category.head(5)

print("\nTop 5 High-Risk Crime Categories:")
print(top_5_risk)

# Bar Chart
plt.figure(figsize=(12, 6))

top_5_risk.plot(kind="bar")

plt.title("Top 5 High-Risk Crime Categories (2001-2012)")
plt.xlabel("Crime Category")
plt.ylabel("Total Cases")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.show()

# Step 7: State Risk Analysis

# Remove total state and total crime category
state_risk_data = df[
    (df["STATE/UT"] != "TOTAL Crime against Women") &
    (df["CRIME HEAD"] != "TOTAL CRIMES AGAINST WOMEN")
].copy()

# Calculate total cases for each state
state_risk_data["STATE_TOTAL"] = state_risk_data[years].sum(axis=1)

# Group by state
state_risk = (
    state_risk_data.groupby("STATE/UT")["STATE_TOTAL"]
    .sum()
    .sort_values(ascending=False)
)

print("\nState-wise Risk Ranking:")
print(state_risk)

# Top 10 High-Risk States/UTs
top_10_risk_states = state_risk.head(10)

print("\nTop 10 High-Risk States/UTs:")
print(top_10_risk_states)

# Bar Chart
plt.figure(figsize=(12, 6))

top_10_risk_states.plot(kind="bar")

plt.title("Top 10 High-Risk States/UTs (2001-2012)")
plt.xlabel("State/UT")
plt.ylabel("Total Cases")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.show()

# Step 8: State-wise Crime Pattern Analysis

# Remove total state and total crime category
pattern_data = df[
    (df["STATE/UT"] != "TOTAL Crime against Women") &
    (df["CRIME HEAD"] != "TOTAL CRIMES AGAINST WOMEN")
].copy()

# Calculate total cases
pattern_data["CATEGORY_TOTAL"] = pattern_data[years].sum(axis=1)

# Find top crime category for each state
state_pattern = (
    pattern_data.loc[
        pattern_data.groupby("STATE/UT")["CATEGORY_TOTAL"].idxmax()
    ]
    [["STATE/UT", "CRIME HEAD", "CATEGORY_TOTAL"]]
)

print("\nState-wise Most Common Crime Category:")
print(state_pattern.to_string(index=False))

# Count how many states have each crime as their highest category
pattern_count = state_pattern["CRIME HEAD"].value_counts()

print("\nMost Common Crime Category Across States:")
print(pattern_count)

# Bar Chart
plt.figure(figsize=(12, 6))

pattern_count.plot(kind="bar")

plt.title("Most Common Crime Category Across States/UTs")
plt.xlabel("Crime Category")
plt.ylabel("Number of States/UTs")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.show() 

# Step 9: Risk Level Classification

# Remove total state and total crime category
risk_level_data = df[
    (df["STATE/UT"] != "TOTAL Crime against Women") &
    (df["CRIME HEAD"] != "TOTAL CRIMES AGAINST WOMEN")
].copy()

# Calculate total crimes for each state
risk_level_data["STATE_TOTAL"] = risk_level_data[years].sum(axis=1)

# Group by state
state_risk_total = (
    risk_level_data.groupby("STATE/UT")["STATE_TOTAL"]
    .sum()
    .sort_values(ascending=False)
)

# Calculate thresholds
high_threshold = state_risk_total.quantile(0.75)
low_threshold = state_risk_total.quantile(0.25)

# Assign risk level
def classify_risk(value):
    if value >= high_threshold:
        return "High Risk"
    elif value <= low_threshold:
        return "Low Risk"
    else:
        return "Medium Risk"

risk_levels = state_risk_total.to_frame(name="TOTAL_CASES")

risk_levels["RISK_LEVEL"] = risk_levels["TOTAL_CASES"].apply(classify_risk)

print("\nState-wise Risk Level:")
print(risk_levels)

# Count states in each risk level
risk_count = risk_levels["RISK_LEVEL"].value_counts()

print("\nRisk Level Distribution:")
print(risk_count)

# Bar Chart
plt.figure(figsize=(10, 6))

risk_count.plot(kind="bar")

plt.title("State-wise Risk Level Distribution")
plt.xlabel("Risk Level")
plt.ylabel("Number of States/UTs")

plt.xticks(rotation=0)
plt.tight_layout()

plt.show()

# Step 10: Year-wise Crime Trend Analysis

total_row = df[df['CRIME HEAD'] == 'TOTAL CRIMES AGAINST WOMEN']

years = [str(y) for y in range(2001, 2013)]

yearly_total = total_row[years].sum()

print("\nYear-wise Total Crimes Against Women:")
print(yearly_total)

yearly_total.plot(
    kind='line',
    marker='o',
    figsize=(12, 6),
    title='Year-wise Crimes Against Women (2001-2012)'
)

plt.xlabel('Year')
plt.ylabel('Total Crimes')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Step 11: Top 10 States by Total Crimes

state_data = df[
    (df['CRIME HEAD'] == 'TOTAL CRIMES AGAINST WOMEN') &
    (df['STATE/UT'] != 'TOTAL Crime against Women')
].copy()

years = [str(y) for y in range(2001, 2013)]

state_data['TOTAL_CRIMES'] = state_data[years].sum(axis=1)

top_10_states = state_data[
    ['STATE/UT', 'TOTAL_CRIMES']
].sort_values(
    by='TOTAL_CRIMES',
    ascending=False
).head(10)

print("\nTop 10 States/UTs by Total Crimes Against Women:")
print(top_10_states)

top_10_states.set_index('STATE/UT')['TOTAL_CRIMES'].plot(
    kind='bar',
    figsize=(12, 6),
    title='Top 10 States/UTs by Crimes Against Women (2001-2012)'
)

plt.xlabel('State/UT')
plt.ylabel('Total Crimes')
plt.xticks(rotation=45)
plt.show()

# Step 12: Crime Category Trends Over Years

category_data = df[
    df['STATE/UT'] != 'TOTAL Crime against Women'
].copy()

years = [str(y) for y in range(2001, 2013)]

category_yearly = category_data.groupby('CRIME HEAD')[years].sum()

# Remove total crimes category
category_yearly = category_yearly[
    category_yearly.index != 'TOTAL CRIMES AGAINST WOMEN'
]

# Select top 5 crime categories
top_categories = category_yearly.sum(axis=1).sort_values(
    ascending=False
).head(5).index

top_5_trends = category_yearly.loc[top_categories]

print("\nTop 5 Crime Categories:")
print(top_5_trends)

top_5_trends.T.plot(
    figsize=(12, 6),
    marker='o',
    title='Top 5 Crime Categories - Year-wise Trend'
)

plt.xlabel('Year')
plt.ylabel('Number of Crimes')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend(title='Crime Category')
plt.show()

# Step 13: Highest Crime State and Its Crime Categories

highest_state = top_10_states.iloc[0]['STATE/UT']

print("\nHighest Crime State:", highest_state)

state_category_data = df[
    (df['STATE/UT'] == highest_state) &
    (df['CRIME HEAD'] != 'TOTAL CRIMES AGAINST WOMEN')
].copy()

state_category_data['TOTAL_CRIMES'] = state_category_data[years].sum(axis=1)

state_category_data = state_category_data[
    ['CRIME HEAD', 'TOTAL_CRIMES']
].sort_values(
    by='TOTAL_CRIMES',
    ascending=False
)

print("\nCrime Categories in", highest_state)
print(state_category_data.head(10))

state_category_data.head(10).set_index(
    'CRIME HEAD'
)['TOTAL_CRIMES'].plot(
    kind='bar',
    figsize=(12, 6),
    title=f'Top Crime Categories in {highest_state}'
)

plt.xlabel('Crime Category')
plt.ylabel('Total Crimes')
plt.xticks(rotation=45, ha='right')
plt.show()

# Step 14: Crime Growth Percentage (2001 vs 2012)

start_year = yearly_total['2001']
end_year = yearly_total['2012']

growth_percentage = ((end_year - start_year) / start_year) * 100

print("\nCrime Growth Analysis:")
print("Crimes in 2001:", start_year)
print("Crimes in 2012:", end_year)
print("Growth Percentage:", round(growth_percentage, 2), "%")

# Step 15: State-wise Crime Ranking

state_ranking = state_data[
    ['STATE/UT', 'TOTAL_CRIMES']
].sort_values(
    by='TOTAL_CRIMES',
    ascending=False
).reset_index(drop=True)

state_ranking['RANK'] = state_ranking.index + 1

print("\nState-wise Crime Ranking:")
print(state_ranking[['RANK', 'STATE/UT', 'TOTAL_CRIMES']])

# Top 10 State Ranking Chart

top_10_ranking = state_ranking.head(10)

top_10_ranking.plot(
    x='STATE/UT',
    y='TOTAL_CRIMES',
    kind='bar',
    figsize=(12, 6),
    title='State-wise Crime Ranking (Top 10)'
)

plt.xlabel('State/UT')
plt.ylabel('Total Crimes (2001-2012)')
plt.xticks(rotation=45, ha='right')
plt.show()

# Step 16 - Year-wise Crime Trend Analysis

import matplotlib.pyplot as plt

x = df[df['CRIME HEAD'] == 'TOTAL CRIMES AGAINST WOMEN']

years = [str(y) for y in range(2001, 2013)]

trend = x[years].sum()

trend.plot(
    kind='line',
    marker='o',
    figsize=(12, 6)
)

plt.title('Year-wise Crime Against Women Trend (2001-2012)')
plt.xlabel('Year')
plt.ylabel('Total Crimes')
plt.grid(True)
plt.show()

# Step 17 - State-wise Crime Comparison

x = df[
    (df['STATE/UT'] != 'TOTAL Crime against Women') &
    (df['CRIME HEAD'] == 'TOTAL CRIMES AGAINST WOMEN')
].copy()

years = [str(y) for y in range(2001, 2013)]

x['TOTAL'] = x[years].sum(axis=1)

result = x.groupby('STATE/UT')['TOTAL'].sum().sort_values(ascending=False).head(10)

result.sort_values().plot(
    kind='barh',
    figsize=(12, 6)
)

plt.title('Top 10 States/UTs by Total Crimes Against Women (2001-2012)')
plt.xlabel('Total Crimes')
plt.ylabel('State/UT')
plt.tight_layout()
plt.show()

# Step 18: Year-wise Crime Trend

yearly_total = x[years].sum()

print("\nYear-wise Total Crimes Against Women:")
print(yearly_total)

yearly_total.plot(kind='line', marker='o', figsize=(12,6))

plt.title('Year-wise Crime Trend Against Women (2001-2012)')
plt.xlabel('Year')
plt.ylabel('Total Crimes')
plt.grid()
plt.tight_layout()
plt.show()

# Step 19: Top Crime Categories

category_total = x.groupby('CRIME HEAD')[years].sum().sum(axis=1)
category_total = category_total.sort_values(ascending=False).head(8)

print("\nTop 8 Crime Categories:")
print(category_total)

category_total.plot(kind='bar', figsize=(12,6))

plt.title('Top 8 Crime Categories Against Women (2001-2012)')
plt.xlabel('Crime Category')
plt.ylabel('Total Crimes')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# STEP 20: State-wise Crime Analysis

years = [str(y) for y in range(2001, 2013)]

state_data = df[df['STATE/UT'] != 'TOTAL Crime against Women'].copy()

state_data['STATE_TOTAL'] = state_data[years].sum(axis=1)

state_data = state_data.groupby('STATE/UT')['STATE_TOTAL'].sum().sort_values(ascending=False).head(10)

print("\nTop 10 States/UTs - Total Crimes:")

print(state_data)

state_data.plot(kind='bar', figsize=(12,6))

plt.title('Top 10 States/UTs - Crimes Against Women (2001-2012)')
plt.xlabel('State/UT')
plt.ylabel('Total Crimes')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# STEP 21: Year-wise Crime Trend

years = [str(y) for y in range(2001, 2013)]

yearly_total = df[df['CRIME HEAD'] == 'TOTAL CRIMES AGAINST WOMEN'][years].sum()

print("\nYear-wise Crime Trend:")
print(yearly_total)

yearly_total.plot(kind='line', marker='o', figsize=(12,6))

plt.title('Year-wise Crimes Against Women (2001-2012)')
plt.xlabel('Year')
plt.ylabel('Total Crimes')
plt.xticks(rotation=45)

plt.grid(True)
plt.tight_layout()
plt.show()

# STEP 22: Crime Category Comparison

category_data = df[df['CRIME HEAD'] != 'TOTAL CRIMES AGAINST WOMEN'].copy()

category_data['CATEGORY_TOTAL'] = category_data[years].sum(axis=1)

category_total = category_data.groupby('CRIME HEAD')['CATEGORY_TOTAL'].sum().sort_values(ascending=False)

print("\nCrime Category Comparison:")
print(category_total)

category_total.plot(kind='bar', figsize=(12,6))

plt.title('Crime Category Comparison (2001-2012)')
plt.xlabel('Crime Category')
plt.ylabel('Total Cases')
plt.xticks(rotation=75)

plt.tight_layout()
plt.show()

# STEP 23: Top 5 Crime Categories Trend

top_5_categories = category_total.head(5).index

top_5_trend = category_data[
    category_data['CRIME HEAD'].isin(top_5_categories)
].groupby('CRIME HEAD')[years].sum()

print("\nTop 5 Crime Categories Trend:")
print(top_5_trend)

for category in top_5_trend.index:
    plt.plot(
        years,
        top_5_trend.loc[category],
        marker='o',
        label=category
    )

plt.title('Top 5 Crime Categories Trend (2001-2012)')
plt.xlabel('Year')
plt.ylabel('Total Cases')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()

# STEP 24: Highest Crime State Analysis

state_total = df[
    df['CRIME HEAD'] == 'TOTAL CRIMES AGAINST WOMEN'
].copy()

state_total['TOTAL_CRIMES'] = state_total[years].sum(axis=1)

state_total = state_total[
    state_total['STATE/UT'] != 'TOTAL Crime against Women'
]

highest_state = state_total.sort_values(
    'TOTAL_CRIMES',
    ascending=False
).iloc[0]['STATE/UT']

print("\nHighest Crime State:")
print(highest_state)

state_categories = category_data[
    category_data['STATE/UT'] == highest_state
].groupby('CRIME HEAD')['CATEGORY_TOTAL'].sum().sort_values(
    ascending=False
)

print("\nCrime Categories in", highest_state)
print(state_categories)

state_categories.plot(
    kind='bar',
    figsize=(12,6)
)

plt.title(
    f'Crime Categories in {highest_state} (2001-2012)'
)

plt.xlabel('Crime Category')
plt.ylabel('Total Cases')
plt.xticks(rotation=75)

plt.tight_layout()
plt.show()

# STEP 25: Crime Growth Analysis

total_crimes = df[
    df['CRIME HEAD'] == 'TOTAL CRIMES AGAINST WOMEN'
].copy()

year_2001 = total_crimes['2001'].sum()
year_2012 = total_crimes['2012'].sum()

growth_percentage = (
    (year_2012 - year_2001) / year_2001
) * 100

print("\nCrime Growth Analysis:")
print("Crimes in 2001:", year_2001)
print("Crimes in 2012:", year_2012)
print("Growth Percentage:", round(growth_percentage, 2), "%")

# STEP 26: State-wise Crime Ranking

ranking_data = df[
    df['CRIME HEAD'] == 'TOTAL CRIMES AGAINST WOMEN'
].copy()

ranking_data['TOTAL_CRIMES'] = ranking_data[years].sum(axis=1)

ranking_data = ranking_data[
    ranking_data['STATE/UT'] != 'TOTAL Crime against Women'
]

ranking_data = ranking_data.sort_values(
    'TOTAL_CRIMES',
    ascending=False
).reset_index(drop=True)

ranking_data['RANK'] = ranking_data.index + 1

ranking_data = ranking_data[
    ['RANK', 'STATE/UT', 'TOTAL_CRIMES']
]

print("\nState-wise Crime Ranking:")
print(ranking_data)


# STEP 27: State-wise Risk Level Classification

risk_data = ranking_data.copy()

def risk_level(crimes):
    if crimes >= 100000:
        return "High Risk"
    elif crimes >= 10000:
        return "Medium Risk"
    else:
        return "Low Risk"

risk_data['RISK_LEVEL'] = risk_data['TOTAL_CRIMES'].apply(risk_level)

print("\nState-wise Risk Level:")
print(risk_data[['STATE/UT', 'TOTAL_CRIMES', 'RISK_LEVEL']])

print("\nRisk Level Distribution:")
print(risk_data['RISK_LEVEL'].value_counts())

# STEP 28: Year-wise Crime Trend Summary

yearly_data = df[
    df['CRIME HEAD'] == 'TOTAL CRIMES AGAINST WOMEN'
].copy()

yearly_data = yearly_data[
    yearly_data['STATE/UT'] == 'TOTAL Crime against Women'
]

yearly_totals = yearly_data[years].sum()

print("\nYear-wise Crime Trend Summary:")
print(yearly_totals)

print("\nHighest Crime Year:", yearly_totals.idxmax())
print("Lowest Crime Year:", yearly_totals.idxmin())

# STEP 29: Year-over-Year Crime Growth Analysis

yearly_growth = yearly_totals.astype(float).pct_change() * 100

print("\nYear-over-Year Crime Growth (%):")
print(yearly_growth.round(2))

print("\nHighest Year-over-Year Growth:")
print(yearly_growth.idxmax(), ":", round(yearly_growth.max(), 2), "%")

print("\nLowest Year-over-Year Growth:")
print(yearly_growth.idxmin(), ":", round(yearly_growth.min(), 2), "%")

# STEP 30: Crime Trend Interpretation

first_year = int(yearly_totals.iloc[0])
last_year = int(yearly_totals.iloc[-1])

growth_percentage = ((last_year - first_year) / first_year) * 100

print("\n--- CRIME TREND INTERPRETATION ---")

print(f"Starting year (2001) reported cases: {first_year}")
print(f"Ending year (2012) reported cases: {last_year}")
print(f"Overall change in reported cases: {growth_percentage:.2f}%")

if last_year > first_year:
    print("Finding: Reported cases were higher in 2012 than in 2001.")
elif last_year < first_year:
    print("Finding: Reported cases were lower in 2012 than in 2001.")
else:
    print("Finding: Reported cases were the same in both years.")

print("Note: Changes in reported cases do not alone prove changes in actual crime risk.")

# STEP 31: Final Analysis Summary

print("\n========== WOMEN'S SAFETY ANALYSIS ==========")

print("\n1. Overall Crime Growth:")
print(f"Reported cases increased by {growth_percentage:.2f}% from 2001 to 2012.")

print("\n2. Highest Crime Year:")
print(yearly_totals.idxmax())

print("\n3. Lowest Crime Year:")
print(yearly_totals.idxmin())

print("\n4. Most Common Crime Category:")
print(category_total.index[0])

print("\n5. Highest Ranked State/UT:")
print(ranking_data.iloc[0]['STATE/UT'])

print("\n6. Risk Level Distribution:")
print(risk_data['RISK_LEVEL'].value_counts())

print("\n=============================================")

# STEP 32: Dashboard Data Preparation

dashboard_yearly_data = pd.DataFrame({
    'Year': yearly_totals.index.astype(int),
    'Total_Crimes': yearly_totals.values
})

dashboard_yearly_data['Yearly_Change'] = (
    dashboard_yearly_data['Total_Crimes'].diff()
)

dashboard_yearly_data['Growth_Percentage'] = (
    dashboard_yearly_data['Total_Crimes'].pct_change() * 100
)

print("\nDashboard Yearly Data:")
print(dashboard_yearly_data.round(2).to_string(index=False))

# STEP 33: Dashboard State-wise Data Preparation

dashboard_state_data = risk_data[
    ['STATE/UT', 'TOTAL_CRIMES', 'RISK_LEVEL']
].copy()

dashboard_state_data = dashboard_state_data.sort_values(
    'TOTAL_CRIMES',
    ascending=False
).reset_index(drop=True)

print("\nDashboard State-wise Data:")
print(dashboard_state_data.to_string(index=False))

print("\nTotal States/UTs:", len(dashboard_state_data))

# STEP 34: Dashboard Crime Category Data

dashboard_category_data = category_total.reset_index()

dashboard_category_data.columns = [
    'Crime_Category',
    'Total_Cases'
]

dashboard_category_data = dashboard_category_data.sort_values(
    'Total_Cases',
    ascending=False
).reset_index(drop=True)

print("\nDashboard Crime Category Data:")
print(dashboard_category_data.to_string(index=False))

print("\nTotal Crime Categories:", len(dashboard_category_data))

# STEP 35: Export Dashboard Data to CSV

dashboard_yearly_data.to_csv(
    'dashboard_yearly_data.csv',
    index=False
)

dashboard_state_data.to_csv(
    'dashboard_state_data.csv',
    index=False
)

dashboard_category_data.to_csv(
    'dashboard_category_data.csv',
    index=False
)

print("\nDashboard data exported successfully!")

print("1. dashboard_yearly_data.csv")
print("2. dashboard_state_data.csv")
print("3. dashboard_category_data.csv")
                                               









