"""
ApexPlanet Data Analytics Internship - Task 1
Data Immersion & Wrangling
Run: python task1_cleaning.py
Input: ApexPlanet_DataAnalytics_Dataset.xlsx (same folder)
Outputs: cleaned_sales_dataset.csv, cleaned_sales_dataset.xlsx,
         data_dictionary.csv, quality_assessment.csv
"""
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "ApexPlanet_DataAnalytics_Dataset.xlsx"
SHEET_NAME = "Sales_Dataset"

def build_data_dictionary():
    rows = [
        ("Order_Row_ID", "Unique row-level transaction key added during cleaning", "Text", "Unique record identifier."),
        ("Order_ID", "Source order identifier", "Text", "Not unique in the supplied dataset."),
        ("Order_Date", "Date of transaction", "Date", "Time-based sales analysis."),
        ("Customer_ID", "Customer identifier", "Text", "Customer-level analysis."),
        ("Customer_Name", "Customer display name", "Text", "Customer label/name."),
        ("Age", "Customer age in years", "Numeric", "20 missing values imputed with median."),
        ("Gender", "Customer gender category", "Categorical", "Demographic segmentation."),
        ("City", "Customer city", "Categorical/Text", "13 missing values labelled Unknown."),
        ("Product", "Product name", "Categorical", "Product analysis."),
        ("Category", "Product category", "Categorical", "Category-level analysis."),
        ("Quantity", "Units purchased", "Integer", "Order volume."),
        ("Unit_Price", "Price per unit", "Decimal", "Revenue calculation input."),
        ("Total_Sales", "Total transaction sales", "Decimal", "Quantity multiplied by Unit_Price.")
    ]
    return pd.DataFrame(rows, columns=["Column_Name", "Description", "Data_Type", "Business_Relevance_and_Notes"])

def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Place {INPUT_FILE.name} in {BASE_DIR}")
    df = pd.read_excel(INPUT_FILE, sheet_name=SHEET_NAME)
    original_rows = len(df)

    # Standardize whitespace in text columns
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype("string").str.strip()

    # Convert types
    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
    for col in ["Age", "Quantity", "Unit_Price", "Total_Sales"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Missing-value treatment
    age_median = df["Age"].median()
    df["Age"] = df["Age"].fillna(age_median)
    df["City"] = df["City"].fillna("Unknown")

    # Preserve source records; Order_ID is repeated for different transactions
    df.insert(0, "Order_Row_ID", [f"ROW{i:04d}" for i in range(1, len(df) + 1)])

    # Recompute total sales consistently
    df["Total_Sales"] = (df["Quantity"] * df["Unit_Price"]).round(2)

    dictionary = build_data_dictionary()
    quality = pd.DataFrame({
        "Metric": ["Rows before cleaning", "Rows after cleaning", "Columns after adding row key",
                   "Missing Age before cleaning", "Missing City before cleaning",
                   "Exact duplicate rows before cleaning", "Repeated Order_ID extra occurrences",
                   "Missing values after cleaning"],
        "Value": [original_rows, len(df), len(df.columns),
                  int(pd.read_excel(INPUT_FILE, sheet_name=SHEET_NAME)["Age"].isna().sum()),
                  int(pd.read_excel(INPUT_FILE, sheet_name=SHEET_NAME)["City"].isna().sum()),
                  int(pd.read_excel(INPUT_FILE, sheet_name=SHEET_NAME).duplicated().sum()),
                  int(pd.read_excel(INPUT_FILE, sheet_name=SHEET_NAME)["Order_ID"].duplicated().sum()),
                  int(df.isna().sum().sum())]
    })

    export_df = df.copy()
    export_df["Order_Date"] = export_df["Order_Date"].dt.strftime("%Y-%m-%d")
    export_df.to_csv(BASE_DIR / "cleaned_sales_dataset.csv", index=False)
    with pd.ExcelWriter(BASE_DIR / "cleaned_sales_dataset.xlsx", engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Cleaned_Data", index=False)
        dictionary.to_excel(writer, sheet_name="Data_Dictionary", index=False)
        quality.to_excel(writer, sheet_name="Quality_Summary", index=False)
    dictionary.to_csv(BASE_DIR / "data_dictionary.csv", index=False)
    quality.to_csv(BASE_DIR / "quality_assessment.csv", index=False)
    print("Task 1 cleaning completed.")
    print(f"Rows preserved: {len(df)}")
    print(f"Missing values remaining: {int(df.isna().sum().sum())}")
    print("Created cleaned CSV/XLSX, data dictionary, and quality assessment.")

if __name__ == "__main__":
    main()
