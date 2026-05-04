import pandas as pd

def load_csv():
    df = pd.read_csv(r"data\sales_data_raw.csv")
    return df

def clean_columns(df):
    df.columns = df.columns.str.strip()

    df["order_id"] = df["order_id"].astype(str).str.strip()
    df["customer_id"] = df["customer_id"].astype(str).str.strip()
    df["quantity"] = pd.to_numeric(df["quantity"],errors="coerce")
    df["price"] = pd.to_numeric(df["price"],errors="coerce")
    df["customer_name"] = df["customer_name"].str.strip()
    df["city"] = df["city"].str.strip()
    df["product_category"] = df["product_category"].str.strip()
    df["product_name"] = df["product_name"].str.strip()

    return df

def fix_dates(clean_df):
    clean_df = clean_df.copy()

    clean_df["order_date"] = pd.to_datetime(
        clean_df["order_date"],
        format="mixed",
        errors="coerce",
        dayfirst=True
    )

    return clean_df

def handle_missing_values(clean_df):
    clean_df = clean_df.dropna(subset=["order_id","customer_id","quantity","price"])
    clean_df["city"] = clean_df["city"].fillna("Unknown")

    return clean_df

def remove_duplicates(clean_df):
    clean_df = clean_df.copy()

    clean_df = clean_df.drop_duplicates()

    return clean_df

def business_metrics(clean_df):
    clean_df = clean_df.copy()

    clean_df["revenue"] = (clean_df["quantity"] * clean_df["price"]).round(2)
    clean_df["month"] = clean_df["order_date"].dt.to_period("M").astype(str)

    return clean_df

def save_clean_data(clean_df):
    clean_df.to_csv(r"data\clean_sales_data.csv",index=False)
    print("Clean sales data saved")


df = load_csv()

original_rows = len(df)

clean_df = clean_columns(df)
clean_df = fix_dates(clean_df)
clean_df = handle_missing_values(clean_df)
clean_df = remove_duplicates(clean_df)
clean_df = business_metrics(clean_df)

clean_rows = len(clean_df)

print("Original rows: ",original_rows)
print("Clean rows: ", clean_rows)
print("Removed rows: ", original_rows-clean_rows)

save_clean_data(clean_df)