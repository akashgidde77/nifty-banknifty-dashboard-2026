import pandas as pd
import matplotlib.pyplot as plt

# Load Nifty 50 data
nifty = pd.read_excel(r"A:\Stock Market Project\Nifty50.xlsx")

# Load Bank Nifty data
bank = pd.read_excel(r"A:\Stock Market Project\BankNifty.xlsx")

# Remove extra spaces from column names
nifty.columns = nifty.columns.str.strip()
bank.columns = bank.columns.str.strip()

# Check data
print("Nifty 50 Shape:", nifty.shape)
print("Bank Nifty Shape:", bank.shape)

# Display first 5 rows
print("\nNifty 50 Data:")
print(nifty.head())

print("\nBank Nifty Data:")
print(bank.head())

# Check missing values
print("\nNifty 50 Missing Values:")
print(nifty.isnull().sum())

print("\nBank Nifty Missing Values:")
print(bank.isnull().sum())






# Calculate monthly average daily returns
print("Nifty columns:", nifty.columns.tolist())
print("Bank Nifty columns:", bank.columns.tolist())

nifty["Daily Return %"] = nifty["Close"].pct_change() * 100
bank["Daily Return %"] = bank["Close"].pct_change() * 100

# Ensure dates are in datetime format
nifty["Date"] = pd.to_datetime(nifty["Date"])
bank["Date"] = pd.to_datetime(bank["Date"])

# Sort data by date
nifty = nifty.sort_values("Date")
bank = bank.sort_values("Date")

# Calculate monthly closing prices
nifty_monthly = nifty.groupby(
    nifty["Date"].dt.to_period("M")
)["Close"].agg(["first", "last"])

bank_monthly = bank.groupby(
    bank["Date"].dt.to_period("M")
)["Close"].agg(["first", "last"])

# Calculate monthly returns
nifty_return = (nifty_monthly["last"] / nifty_monthly["first"] - 1) * 100
bank_return = (bank_monthly["last"] / bank_monthly["first"] - 1) * 100

# Compare both indices
comparison = pd.DataFrame({
    "Nifty 50": nifty_return,
    "Bank Nifty": bank_return
})

comparison.index.name = "Month"
comparison.to_csv(r"A:\Stock Market Project\monthly_comparison.csv")

print("\nMonthly Return Comparison:")
print(comparison.round(3))

# Plot graph
comparison.plot(kind="line", marker="o", figsize=(12, 6))
plt.title("Nifty 50 vs Bank Nifty - Monthly Average Daily Returns")
plt.xlabel("Month")
plt.ylabel("Average Daily Return (%)")
plt.grid(True)
plt.tight_layout()
plt.show()

