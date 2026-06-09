# התחלה מהירה בעברית - בלי להוריד ZIP

אם אתה שואל "איך אני מוריד את הכל?" — בגלל שהמערכת לא תומכת בקבצים בינאריים, לא משתמשים ב-ZIP מתוך הדיפ. במקום זה עובדים עם קבצי הטקסט שכבר נמצאים בריפו.

## הדרך הכי קלה להקים את כל המערכת

אם אתה רוצה "את הכל" בקובץ אחד, פתח:

```text
examples/use-cases/real_estate_finance_system/output/ALL_IN_ONE_HE.md
```

אבל כדי להקים את השלד בגוגל שיטס בפועל, מספיק קובץ אחד:

```text
examples/use-cases/real_estate_finance_system/output/setup_google_sheet.gs
```

### שלבים

1. פתח Google Sheets.
2. צור קובץ חדש בשם:
   `Finance_RealEstate_v1`
3. בתפריט העליון לחץ:
   `Extensions` -> `Apps Script`
4. פתח בריפו את הקובץ:
   `examples/use-cases/real_estate_finance_system/output/setup_google_sheet.gs`
5. העתק את כל התוכן של הקובץ.
6. הדבק אותו ב-Apps Script במקום הקוד הקיים.
7. לחץ Save.
8. בחר להריץ את הפונקציה:
   `setupRealEstateFinanceSystem`
9. אשר הרשאות אם Google מבקש.
10. חזור לגוגל שיטס — הטאבים, הכותרות, הנוסחאות והרשימות ייווצרו אוטומטית.

## אם אתה רוצה להעתיק ידנית במקום Apps Script

פתח את התיקייה:

```text
examples/use-cases/real_estate_finance_system/output/
```

פתח כל קובץ CSV, העתק את התוכן שלו, והדבק אותו בתא `A1` בטאב המתאים בגוגל שיטס.

הקבצים המרכזיים הם:

- `Income.csv`
- `Expenses.csv`
- `Lists.csv`
- `Category_Map.csv`
- `RAW_Transactions.csv`
- `Transactions_All.csv`
- `Project_Profitability.csv`
- `Tasks_Manager.csv`
- `Dashboard.csv`

אחרי זה פתח:

- `FORMULAS.md` — להדבקת נוסחאות.
- `SETUP_HE.md` — להמשך בדיקות והפעלה.
- `make_scenario_blueprint.json` — לחיבור Make בהמשך.

## אם אתה עובד במחשב עם הריפו מקומית

אפשר ליצור ZIP מקומי אצלך במחשב:

```bash
python3 examples/use-cases/real_estate_finance_system/generate_system.py
```

אחרי ההרצה, הקובץ יופיע כאן:

```text
examples/use-cases/real_estate_finance_system/output/real_estate_finance_system_bundle.zip
```

אבל אם הממשק שלך רושם `Binary files are not supported`, אל תנסה לפתוח את ה-ZIP דרך הדיפ. השתמש בקבצי הטקסט או ב-Apps Script.
