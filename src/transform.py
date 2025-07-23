import pandas as pd
import os

# Load raw CSV
df = pd.read_csv("data/raw/banking_raw.csv")
before_count = len(df)

# Transformations
df.columns = df.columns.str.lower()
df['transactiondate'] = pd.to_datetime(df['transactiondate'])

# Remove rows with 0 transaction amount
df = df[df['transactionamount'] != 0]

# Balance after transaction logic
df['balanceaftertransaction'] = df.apply(
    lambda row: row['balance'] - row['transactionamount']
    if row['transactiontype'].lower() == 'debit'
    else row['balance'] + row['transactionamount'],
    axis=1
)

# Drop duplicates if any
df = df.drop_duplicates()

after_count = len(df)

# Save to processed directory
os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/banking_cleaned.csv", index=False)

# Print summary
print(f"Rows before: {before_count}, Rows after: {after_count}")