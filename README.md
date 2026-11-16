# ApexPlanet Data Analytics Internship — Task 1
## Data Immersion & Wrangling

This repository contains the Task 1 deliverables built from the supplied `ApexPlanet_DataAnalytics_Dataset.xlsx`.

### Project structure
- `task1_cleaning.py` — reproducible Pandas cleaning workflow
- `cleaned_sales_dataset.csv` — cleaned dataset
- `cleaned_sales_dataset.xlsx` — cleaned data, dictionary and quality summary
- `data_dictionary.csv` — field-level documentation
- `quality_assessment.csv` — data quality findings and decisions
- `TASK1_PROJECT_REPORT.md` — project report
- `ApexPlanet_DataAnalytics_Dataset.xlsx` — original input dataset (include this in your private working copy; only publish if permitted)

### Run locally
```bash
pip install pandas openpyxl
python task1_cleaning.py
```
Keep the source Excel workbook in the same folder as the script.

### Key methodology
- Missing Age: median imputation
- Missing City: `Unknown`
- Repeated Order_ID values: preserve rows and add unique Order_Row_ID
- Total_Sales: recalculate from Quantity × Unit_Price
- IQR outliers: flag and document; do not automatically delete

See `TASK1_PROJECT_REPORT.md` for the full methodology and findings.
