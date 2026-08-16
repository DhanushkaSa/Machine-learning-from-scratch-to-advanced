import numpy as np
import pandas as pd

# Q1 Load and inspect the dataset
df = pd.read_csv('customers_messy_500.csv')


print(df.head())

print(df.tail())

print(df.shape)

print(list(df.columns))

print(df.dtypes)

print(df.info())

print(df.describe(include='all'))
# 1. There are missing values in several columns.
# 2. The data has consistency problems: city appears in different formats like Colombo and COLOMBO, and purchased mixes values such as 0, 1, and false.
# 3. Dataset has duplicates and missing values.

# Q2 Measure missingness
print(df.isna().sum())

print(df.isnull().sum()/len(df)*100)

# The most incomplete column is 'age' column
# The mostly complete column is 'customer_id' column
# Because Pandas only detects NaN, None, or <NA> as missing values. An empty string ("" or "   ") is a valid string object with length ≥ 0, so isna() returns False.
empty_count = (df['city'].str.strip() == '').sum()


# Q3 Practice loc and iloc selection
first10_loc = df.loc[df.index[:10], ["customer_id", "age", "city", "score"]]
print(first10_loc)

print(df.iloc[0:10, 0:4])

data_series = df['score']
print(data_series)

data_frame = df[["age", "score"]]
print(data_frame)

# loc selects data by label (column/row names), while iloc selects data by integer position (index numbers), regardless of the actual labels.

# Q4 Fix data types(age,score,income)
df['age'] = pd.to_numeric(df['age'], errors='coerce')

# Score arrives in two formats: plain decimals like "0.728" (already 0-1)
# and percent strings like "47%" (need to become 0.47). Track which rows
# had a "%" BEFORE stripping it, so we only divide those by 100 -
# dividing every row by 100 would wrongly shrink the already-decimal ones.
raw_score = df['score'].astype(str).str.strip()
had_percent = raw_score.str.contains('%', na=False)

df['score'] = (
    raw_score
    .str.replace('%', '', regex=False)
    .str.strip()
)
df['score'] = pd.to_numeric(df['score'], errors='coerce')
df['score'] = np.where(had_percent, df['score'] / 100, df['score'])


df['income'] = (
    df['income']
    .astype(str)
    .str.replace('LKR', '', regex=False)
    .str.replace(',', '', regex=False)
    .str.strip()
)
df['income'] = pd.to_numeric(df['income'], errors='coerce')

print(df[["age", "score", "income"]].dtypes)


# Q5 Standardise city names
df["city"] = df["city"].str.strip()

df["city"] = df["city"].str.title()

df["city"] = df["city"].replace({
    "Colmbo": "Colombo",
    "Gale": "Galle"
})

df['city'] = df['city'].replace('', np.nan)

print(df["city"].value_counts())

# Q6 Handle missing values
df = df.dropna(subset=['customer_id'])
key_fields = ['age', 'score', 'income', 'city']
df = df.dropna(subset=key_fields, thresh=len(key_fields) - 2)

df["age"] = df["age"].fillna(df["age"].median())

df["score"] = df["score"].fillna(df["score"].median())

df["income"] = df["income"].fillna(df["income"].median())

df["city"] = df["city"].fillna(df["city"].mode()[0])
# I filled missing city values with the mode because city is likely to have a dominant/common category

print(df.isna().sum())

# Q7 Filter invalid values
rows_before = df.shape[0]

df = df[(df["age"] >= 18) & (df["age"] <= 80)]

df = df[(df["score"] >= 0) & (df["score"] <= 1)]

df = df[(df["purchases"].notna()) & (df["purchases"] >= 0)]

row_after = df.shape[0]

removed_row = rows_before - row_after
print(removed_row)

print(df.shape[0])

# Q8 Clean the purchased column and remove duplicates
purchased_map = {
    'Yes': 1, 'YES': 1, 'yes': 1, 'true': 1, 'True': 1, 'TRUE': 1, 'y': 1, 'Y': 1, '1': 1, 1: 1,
    'No': 0, 'NO': 0, 'no': 0, 'false': 0, 'False': 0, 'FALSE': 0, 'n': 0, 'N': 0, '0': 0, 0: 0
}

df['purchased'] = df['purchased'].map(purchased_map)

df = df.dropna(subset=['purchased'])

df['purchased'] = df['purchased'].astype(int)

rows_before_dup = df.shape[0]
df = df.drop_duplicates()

dup_customer_ids = df['customer_id'].duplicated().sum()
print(f"Duplicate customer_id count (before resolving): {dup_customer_ids}")

df = df.drop_duplicates(subset=['customer_id'], keep='first')

print(f"Rows removed by full-row duplicates: {rows_before_dup - df.shape[0]}")
print(f"Final number of rows: {df.shape[0]}")

# Q9 Create features and sort
df["score_pct"] = df["score"]*100
print(df.head(10))

df["high_value"] = df["income"] > df["income"].median()
print(df.head(10))

df = df.sort_values("score", ascending=False)
print(df.head(10))

filtered = df[(df["city"] == "Colombo") & (
    df["score"] >= 0.7) & (df["purchased"] == 1)]
print(filtered)
print(filtered.shape[0])

# Q10 Explore with value_counts and groupby
df["city"].value_counts()
df["purchased"].value_counts()

purchased_balance = df['purchased'].value_counts(normalize=True) * 100
print("\nPurchased class balance (%):")
print(purchased_balance)

print(df.groupby("city")["score"].mean())

print(df.groupby("city")[["income", "purchases"]].mean())

print(
    df.groupby("city").agg(
        row_count=("city", "count"),
        mean_age=("age", "mean"),
        mean_score=("score", "mean"),
        purchase_rate=("purchased", "mean")
    )
)

# Findings for a future ML model

# Score is a strong predictor — it correlates fairly well with purchases (r ≈ 0.54), with purchasers averaging a score of ~0.75 vs ~0.53 for non-purchasers.
# Target is imbalanced — only ~31% of customers purchased vs 69% who didn't, so future models should use F1-score or ROC-AUC instead of accuracy.
# Age and income are weak linear predictors (r ≈ 0.01 and 0.07), suggesting non-linear models like XGBoost would capture their effects better.
# City matters — Negombo has the highest purchase rate (~39.4%), Jaffna the lowest (~26.3%), so city should be included as an encoded categorical feature.
