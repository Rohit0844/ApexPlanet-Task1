# ApexPlanet Data Analytics Internship — Task 1
## Data Immersion & Wrangling

**Dataset:** ApexPlanet_DataAnalytics_Dataset.xlsx  
**Source sheet:** Sales_Dataset  
**Project focus:** Retail / sales transaction data cleaning and preparation  
**Tools:** Python, Pandas, NumPy, Excel

## 1. Objective
The objective is to understand the supplied dataset, document its fields, assess data quality, clean and transform the data, and produce an analysis-ready dataset.

## 2. Dataset overview
- Source records: **1,000**
- Original columns: **12**
- Date range: **2025-01-01 to 2026-01-01**
- Exact duplicate rows: **0**
- Fields: Order_ID, Order_Date, Customer_ID, Customer_Name, Age, Gender, City, Product, Category, Quantity, Unit_Price, Total_Sales.

## 3. Data quality assessment
| Check | Finding | Treatment |
|---|---:|---|
| Missing Age | 20 | Filled with median (41) |
| Missing City | 13 | Replaced with `Unknown` |
| Exact duplicate rows | 0 | No rows removed |
| Extra repeated Order_ID occurrences | 8 | Retained; unique row key added |
| Sales formula mismatches | 0 | Total_Sales recalculated |
| IQR outliers in Total_Sales | 19 | Flagged, not deleted |

**Important identifier finding:** The source contains 1 distinct Order_ID values that occur more than once. Inspection shows that repeated IDs can belong to different customers, dates and products. Therefore, deleting these records would destroy valid-looking transactions. A new unique `Order_Row_ID` is added to identify every source row while preserving the original `Order_ID`.

## 4. Cleaning and transformation steps
1. Loaded the `Sales_Dataset` worksheet using Pandas.
2. Inspected dimensions, data types, unique values, missing values and duplicate rows.
3. Trimmed leading/trailing whitespace from text fields.
4. Converted `Order_Date` to a date type and numeric fields to numeric types.
5. Imputed missing `Age` values with the source median (41).
6. Replaced missing `City` values with `Unknown`.
7. Added `Order_Row_ID` as a unique row-level key.
8. Recalculated `Total_Sales = Quantity × Unit_Price`, rounded to two decimal places.
9. Profiled numerical outliers using the 1.5 × IQR rule. The 19 flagged Total_Sales observations were retained because high values can be legitimate sales transactions and should not be removed without business validation.

## 5. Final output
- `cleaned_sales_dataset.csv` — analysis-ready flat file.
- `cleaned_sales_dataset.xlsx` — workbook containing Cleaned_Data, Data_Dictionary and Quality_Summary.
- `data_dictionary.csv` — field definitions, data types and business relevance.
- `quality_assessment.csv` — findings and cleaning decisions.
- `task1_cleaning.py` — reproducible cleaning script.

## 6. Validation
- All 1,000 source records are preserved.
- Missing values in the cleaned dataset: **0**.
- `Order_Row_ID` is unique for every row.
- `Total_Sales` is recalculated from quantity and unit price.
- Potential outliers are documented rather than silently deleted.

## 7. Conclusion
The supplied sales dataset has been profiled, documented, cleaned and transformed into a structured dataset suitable for the next stage of analysis. The cleaning process preserves transaction-level information and makes data quality decisions transparent and reproducible.

---
**Internship:** ApexPlanet Software Pvt. Ltd. — 60-Day Data Analytics Program  
**Task:** 1 — Data Immersion & Wrangling
