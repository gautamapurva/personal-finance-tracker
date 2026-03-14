import pandas as pd


def load_transactions():

    try:
        df = pd.read_csv("transactions.csv")
    except:
        df = pd.DataFrame(columns=["Date", "Description", "Category", "Amount"])

    if not df.empty:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    return df


def save_transaction(date, desc, category, amount):

    new = pd.DataFrame({
        "Date": [date],
        "Description": [desc],
        "Category": [category],
        "Amount": [amount]
    })

    new.to_csv("transactions.csv", mode="a", header=False, index=False)


def monthly_totals(df):

    if df.empty:
        return pd.DataFrame()

    monthly = df.groupby(df["Date"].dt.to_period("M"))["Amount"].sum().reset_index()
    monthly["Date"] = monthly["Date"].astype(str)

    return monthly


def category_totals(df):

    if df.empty:
        return pd.DataFrame()

    return df.groupby("Category")["Amount"].sum().reset_index()