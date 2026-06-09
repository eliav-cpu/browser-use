# Real-Estate Finance System Generator

This package generates a ready-to-run Google Sheets finance system for a real-estate business. It produces plain-text files (`.csv`, `.md`, `.json`, `.gs`) so the setup works even in review tools that cannot open binary ZIP files.

## Hebrew quick start

If you need the simplest Hebrew instructions, start with `QUICK_START_HE.md`. If you want everything in one text file, open `output/ALL_IN_ONE_HE.md`.

## Best setup path

Use the generated Apps Script file:

1. Create a new Google Sheet named `Finance_RealEstate_v1`.
2. Open `Extensions` -> `Apps Script`.
3. Copy the content from `output/setup_google_sheet.gs` into Apps Script.
4. Run `setupRealEstateFinanceSystem`.
5. Review the generated tabs, formulas, and dropdown validations.

## What the generator creates

After running the generator, `output/` contains:

- `Income.csv`
- `Expenses.csv`
- `Lists.csv`
- `Category_Map.csv`
- `RAW_Transactions.csv`
- `Transactions_All.csv`
- `Project_Profitability.csv`
- `Tasks_Manager.csv`
- `Dashboard.csv`
- `FORMULAS.md`
- `ALL_IN_ONE_HE.md` (single Hebrew text bundle with all generated artifacts)
- `SETUP_HE.md`
- `DOWNLOAD_HE.md`
- `REFERENCES.md`
- `setup_google_sheet.gs`
- `make_scenario_blueprint.json`

The generator also creates `real_estate_finance_system_bundle.zip` locally, but the ZIP is intentionally not committed because some review/download UIs show `Binary files are not supported`.

## Run

```bash
python3 examples/use-cases/real_estate_finance_system/generate_system.py
```

If your local project environment is already synced, this also works:

```bash
uv run python examples/use-cases/real_estate_finance_system/generate_system.py
```

## Manual Google Sheets setup

If you do not want to use Apps Script:

1. Create a new workbook: `Finance_RealEstate_v1`.
2. Create tabs with the CSV file names, without `.csv`.
3. Copy each CSV into cell `A1` of the matching tab.
4. Copy formulas from `FORMULAS.md`.
5. Configure data validation in `Income` / `Expenses` from `Lists`.
6. Use `make_scenario_blueprint.json` as the Make.com automation map.

## References checked

The generated Apps Script and Make plan were reviewed against primary documentation listed in `output/REFERENCES.md`.

## Notes

- This does **not** replace your current workbook.
- Roll out in parallel, validate, then migrate gradually.
