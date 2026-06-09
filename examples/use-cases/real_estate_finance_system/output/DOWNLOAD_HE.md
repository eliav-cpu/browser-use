# איך להשתמש במערכת הכספים בלי ZIP

אם אתה רואה הודעה כמו:

```text
Binary files are not supported
```

זה אומר שהממשק שבו אתה נמצא לא מאפשר לפתוח או להציג קובץ ZIP בינארי.
לכן כל קבצי המערכת נשמרים גם כקבצי טקסט רגילים (`.csv`, `.md`, `.json`, `.gs`)
שאפשר לפתוח, להעתיק או להוריד אחד-אחד.

## הדרך הכי פשוטה

פתח את התיקייה:

```text
examples/use-cases/real_estate_finance_system/output/
```

אם אתה רוצה קובץ אחד שמרכז הכל, פתח קודם:

```text
examples/use-cases/real_estate_finance_system/output/ALL_IN_ONE_HE.md
```

או השתמש בקבצים האלה:

1. `Income.csv`
2. `Expenses.csv`
3. `Lists.csv`
4. `Category_Map.csv`
5. `RAW_Transactions.csv`
6. `Transactions_All.csv`
7. `Project_Profitability.csv`
8. `Tasks_Manager.csv`
9. `Dashboard.csv`
10. `FORMULAS.md`
11. `SETUP_HE.md`
12. `setup_google_sheet.gs`
13. `make_scenario_blueprint.json`

## הדרך המהירה ביותר להקים

1. פתח Google Sheets חדש בשם `Finance_RealEstate_v1`.
2. לחץ `Extensions` -> `Apps Script`.
3. פתח את `setup_google_sheet.gs` והעתק את כל הקוד.
4. הדבק ב-Apps Script והריץ את `setupRealEstateFinanceSystem`.
5. חזור לגיליון ובדוק שהמערכת נוצרה.

## אם אתה מעדיף ידנית

1. צור טאבים לפי שמות קבצי ה-CSV, בלי הסיומת `.csv`.
2. פתח כל CSV.
3. העתק את התוכן.
4. הדבק בתא `A1` בטאב המתאים.
5. פתח `FORMULAS.md` והדבק נוסחאות.
6. פתח `SETUP_HE.md` והמשך לפי שלבי הבדיקה.

## אם אתה בכל זאת רוצה ZIP

אפשר ליצור אותו מקומית במחשב שלך על ידי הרצת:

```bash
python3 examples/use-cases/real_estate_finance_system/generate_system.py
```

הקובץ ייווצר כאן:

```text
examples/use-cases/real_estate_finance_system/output/real_estate_finance_system_bundle.zip
```

חשוב: ה-ZIP נוצר מקומית, אבל לא נשמר כקובץ PR/דיפ רגיל כי הוא בינארי וחלק מהממשקים לא תומכים בו.
