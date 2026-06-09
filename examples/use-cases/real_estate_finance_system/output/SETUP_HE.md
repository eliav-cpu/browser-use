# מדריך הקמה בעברית - מערכת כספים לחברת נדל"ן

המטרה: להקים מערכת מקבילה ונקייה ב-Google Sheets, בלי לפגוע בקובץ הקיים.

## הדרך המומלצת - אוטומציה עם Apps Script

1. פתח Google Sheets וצור קובץ חדש בשם `Finance_RealEstate_v1`.
2. בתפריט העליון לחץ `Extensions` -> `Apps Script`.
3. פתח את הקובץ `setup_google_sheet.gs` מתוך תיקיית `output`.
4. העתק את כל הקוד והדבק אותו בעורך Apps Script.
5. שמור והריץ את הפונקציה `setupRealEstateFinanceSystem`.
6. אשר הרשאות אם Google מבקש.
7. חזור לגיליון ובדוק שכל הטאבים, הכותרות, הנוסחאות והרשימות נוצרו.

## דרך ידנית - אם לא רוצים Apps Script

1. פתח Google Sheets.
2. צור קובץ חדש בשם `Finance_RealEstate_v1`.
3. צור טאבים לפי הרשימה:
   - `Income`
   - `Expenses`
   - `Lists`
   - `Category_Map`
   - `RAW_Transactions`
   - `Transactions_All`
   - `Project_Profitability`
   - `Tasks_Manager`
   - `Dashboard`
4. פתח כל קובץ CSV בתיקיית `output`.
5. העתק את התוכן והדבק בתא `A1` בטאב המתאים.
6. פתח את `FORMULAS.md` והדבק את הנוסחאות בתאים שמצוינים שם.

## הגדרת רשימות בחירה

אם השתמשת ב-Apps Script, הרשימות מוגדרות אוטומטית. אם עבדת ידנית:

- `Income!G:G` ו-`Expenses!G:G` מתוך `Lists!A:A`.
- `Income!H:H` ו-`Expenses!H:H` מתוך `Lists!B:B`.
- `Income!D:D` מתוך `Lists!C:C`.
- `Expenses!D:D` מתוך `Lists!D:D`.
- `Income!C:C` ו-`Expenses!C:C` מתוך `Lists!E:E`.

## בדיקה לפני עבודה אמיתית

הכנס 3 שורות ניסיון ב-`Income` ו-3 שורות ניסיון ב-`Expenses`.

בדוק ש:

- `סכום כולל` מחושב אוטומטית.
- `מזהה תנועה` נוצר.
- `כפילות?` מזהה רשומה כפולה.
- `שגיאה?` מזהה שורה חסרה או לא תקינה.
- `Transactions_All` מציג גם הכנסות וגם הוצאות.
- `Project_Profitability` מציג רווחיות לפי פרויקט.
- `Dashboard` מציג מדדים חודשיים.

## חיבור Make / EasyCard

1. פתח Make.
2. צור Scenario חדש.
3. השתמש ב-`make_scenario_blueprint.json` כמפת עבודה.
4. חבר טריגר ראשון: Webhook / EasyCard / CSV / API.
5. ודא שכל תנועה נכנסת קודם ל-`RAW_Transactions`.
6. אל תכתוב אוטומציה ישירות ל-`Income` או `Expenses` לפני בדיקות.

## כלל חשוב

הקובץ החדש הוא סביבת עבודה מקבילה. לא מוחקים, לא משנים ולא מחליפים את הקובץ הקיים עד שהמערכת החדשה נבדקה ואושרה.
