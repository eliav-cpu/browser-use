# כל מערכת הכספים בקובץ אחד

זה קובץ טקסט אחד שמרכז את כל מה שצריך כדי להקים את המערכת.
אם אין לך אפשרות להוריד ZIP, פתח את הקובץ הזה והעתק ממנו את החלקים הדרושים.

## הכי חשוב

כדי להקים את כל המערכת בגוגל שיטס, אתה צריך בעיקר את החלק `setup_google_sheet.gs` למטה.
העתק אותו ל-Google Sheets -> Extensions -> Apps Script והריץ `setupRealEstateFinanceSystem`.

## SETUP_HE.md

```text
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
```

## DOWNLOAD_HE.md

```text
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
```

## FORMULAS.md

```text
# Formula Pack (copy/paste into Google Sheets)

## Income

- `J2`:
```excel
=IF(OR(E2="",F2=""),"",E2+F2)
```

- `K2`:
```excel
=IF(A2="","",TEXT(A2,"yyyymmdd")&"_"&C2&"_"&E2)
```

- `L2`:
```excel
=IF(K2="","",IF(COUNTIF($K:$K,K2)>1,"כפול",""))
```

- `M2`:
```excel
=IF(A2="","",IF(OR(E2<=0,F2<0,D2="",C2="",H2=""),"שגיאת הזנה",""))
```

## Expenses

- `J2`:
```excel
=IF(OR(E2="",F2=""),"",E2+F2)
```

- `K2`:
```excel
=IF(A2="","",TEXT(A2,"yyyymmdd")&"_"&C2&"_"&E2)
```

- `L2`:
```excel
=IF(K2="","",IF(COUNTIF($K:$K,K2)>1,"כפול",""))
```

- `M2`:
```excel
=IF(A2="","",IF(OR(E2<=0,F2<0,D2="",C2="",H2=""),"שגיאת הזנה",""))
```

## RAW_Transactions

- `O2`:
```excel
=IF(M2="","",IF(OR(LOWER(M2)="income",LOWER(M2)="credit"),"הכנסה","הוצאה"))
```

- `R2`:
```excel
=IF(N2="","ממתין",IF(REGEXMATCH(LOWER(N2),"paid|success|completed"),"שולם","ממתין"))
```

- `U2`:
```excel
=IF(D2="","",TEXT(D2,"yyyymmdd")&"_"&E2&"_"&G2&"_"&C2)
```

- `S2`:
```excel
=IF(U2="","",IF(COUNTIF($U:$U,U2)>1,"כפול",""))
```

- `T2`:
```excel
=IF(OR(D2="",E2="",G2="",O2=""),"שגיאה","")
```

## Transactions_All

- `A2`:
```excel
={FILTER({Income!A2:A,"הכנסה",Income!B2:B,Income!C2:C,Income!D2:D,Income!E2:E,Income!F2:F,Income!J2:J,Income!G2:G,Income!H2:H,Income!I2:I,Income!K2:K},Income!A2:A<>"");FILTER({Expenses!A2:A,"הוצאה",Expenses!B2:B,Expenses!C2:C,Expenses!D2:D,Expenses!E2:E,Expenses!F2:F,Expenses!J2:J,Expenses!G2:G,Expenses!H2:H,Expenses!I2:I,Expenses!K2:K},Expenses!A2:A<>"")}
```

## Project_Profitability

- `A2`:
```excel
=UNIQUE(FILTER(Transactions_All!D2:D,Transactions_All!D2:D<>""))
```

- `B2`:
```excel
=SUMIFS(Transactions_All!H:H,Transactions_All!D:D,A2,Transactions_All!B:B,"הכנסה")
```

- `C2`:
```excel
=SUMIFS(Transactions_All!H:H,Transactions_All!D:D,A2,Transactions_All!B:B,"הוצאה")
```

- `D2`:
```excel
=B2-C2
```

- `E2`:
```excel
=IF(B2=0,"",D2/B2)
```

## Tasks_Manager

- `A2`:
```excel
="TSK-"&TEXT(ROW(A2)-1,"00000")
```

- `N2`:
```excel
=IF(B2="","",TODAY()-B2)
```

- `O2`:
```excel
=IF(OR(K2="",L2="הושלם"),"",IF(TODAY()>K2,"באיחור","בזמן"))
```

## Dashboard

- `B2`:
```excel
=SUMIFS(Transactions_All!H:H,Transactions_All!B:B,"הכנסה",Transactions_All!A:A,">="&EOMONTH(TODAY(),-1)+1,Transactions_All!A:A,"<="&EOMONTH(TODAY(),0))
```

- `B3`:
```excel
=SUMIFS(Transactions_All!H:H,Transactions_All!B:B,"הוצאה",Transactions_All!A:A,">="&EOMONTH(TODAY(),-1)+1,Transactions_All!A:A,"<="&EOMONTH(TODAY(),0))
```

- `B4`:
```excel
=B2-B3
```

- `B5`:
```excel
=SUMIFS(Transactions_All!H:H,Transactions_All!J:J,"ממתין")
```

- `B6`:
```excel
=COUNTIF(Income!L:L,"כפול")+COUNTIF(Expenses!L:L,"כפול")+COUNTIF(RAW_Transactions!S:S,"כפול")
```

- `B7`:
```excel
=COUNTIF(Income!M:M,"שגיאת הזנה")+COUNTIF(Expenses!M:M,"שגיאת הזנה")+COUNTIF(RAW_Transactions!T:T,"שגיאה")
```
```

## make_scenario_blueprint.json

```json
{
  "name": "real-estate-finance-automation",
  "version": 2,
  "target_workbook": "Finance_RealEstate_v1",
  "principles": [
    "Write external data only to RAW_Transactions until validation is complete.",
    "Use external_id and unique_key before appending to prevent duplicates.",
    "Create Tasks_Manager rows for exceptions instead of overwriting financial history."
  ],
  "field_mapping": {
    "external_id": "Provider transaction/payment id",
    "txn_date": "Provider transaction date",
    "counterparty": "Customer / supplier name",
    "amount": "Amount before VAT when available",
    "vat": "VAT amount or zero",
    "direction_raw": "income/credit or expense/debit",
    "status_raw": "paid/success/completed/pending/failed"
  },
  "scenarios": [
    {
      "name": "ingestion",
      "trigger": "Webhook / EasyCard / CSV / API",
      "modules": [
        "Receive transaction payload",
        "Normalize date, amount, VAT, status, source and external_id",
        "Search RAW_Transactions by external_id and unique_key",
        "Append only new transactions to RAW_Transactions",
        "Route malformed records to an alert path"
      ],
      "writes_to": "RAW_Transactions",
      "duplicate_guard": "external_id + unique_key"
    },
    {
      "name": "daily_control",
      "trigger": "Scheduler at 08:00",
      "modules": [
        "Search duplicate_flag='כפול' and error_flag='שגיאה'",
        "Create or update Tasks_Manager rows",
        "Send management summary by email / Slack / WhatsApp gateway"
      ],
      "writes_to": "Tasks_Manager",
      "duplicate_guard": "related_transaction_id + task_type + status != הושלם"
    }
  ]
}
```

## setup_google_sheet.gs

```javascript
// Auto-generated by generate_system.py.
// Creates the real-estate finance workbook structure, formulas, and dropdowns.

const FINANCE_SYSTEM_TABS = {
  "Income": [
    [
      "תאריך",
      "צד נגדי",
      "פרויקט",
      "קטגוריה",
      "סכום",
      "מע\"מ",
      "אמצעי תשלום",
      "סטטוס",
      "הערות",
      "סכום כולל",
      "מזהה תנועה",
      "כפילות?",
      "שגיאה?"
    ]
  ],
  "Expenses": [
    [
      "תאריך",
      "צד נגדי",
      "פרויקט",
      "קטגוריה",
      "סכום",
      "מע\"מ",
      "אמצעי תשלום",
      "סטטוס",
      "הערות",
      "סכום כולל",
      "מזהה תנועה",
      "כפילות?",
      "שגיאה?"
    ]
  ],
  "Lists": [
    [
      "Payment_Methods",
      "Status",
      "Income_Categories",
      "Expense_Categories",
      "Projects"
    ],
    [
      "העברה בנקאית",
      "שולם",
      "מכירת נכס",
      "שיווק",
      "Project A"
    ],
    [
      "אשראי",
      "ממתין",
      "שכירות",
      "תחזוקה",
      "Project B"
    ],
    [
      "צ׳ק",
      "חלקי",
      "דמי תיווך",
      "משפטי",
      "Project C"
    ],
    [
      "מזומן",
      "בוטל",
      "ניהול נכס",
      "הנה\"ח",
      "Project D"
    ],
    [
      "ביט",
      "",
      "אחר",
      "עמלות סליקה",
      ""
    ],
    [
      "אחר",
      "",
      "",
      "אחר",
      ""
    ]
  ],
  "Category_Map": [
    [
      "keyword",
      "normalized_category",
      "type",
      "notes"
    ],
    [
      "פייסבוק",
      "שיווק",
      "הוצאה",
      "סיווג הוצאות פרסום"
    ],
    [
      "עו\"ד",
      "משפטי",
      "הוצאה",
      "סיווג הוצאות משפטיות"
    ],
    [
      "דמי ניהול",
      "ניהול נכס",
      "הכנסה",
      "זיהוי הכנסות מניהול"
    ]
  ],
  "RAW_Transactions": [
    [
      "created_at",
      "source",
      "external_id",
      "txn_date",
      "counterparty",
      "description",
      "amount",
      "vat",
      "currency",
      "payment_method",
      "project_raw",
      "category_raw",
      "direction_raw",
      "status_raw",
      "normalized_type",
      "normalized_category",
      "normalized_project",
      "status_normalized",
      "duplicate_flag",
      "error_flag",
      "unique_key"
    ]
  ],
  "Transactions_All": [
    [
      "תאריך",
      "סוג תנועה",
      "צד נגדי",
      "פרויקט",
      "קטגוריה",
      "סכום",
      "מע\"מ",
      "סכום כולל",
      "אמצעי תשלום",
      "סטטוס",
      "הערות",
      "מזהה תנועה"
    ]
  ],
  "Project_Profitability": [
    [
      "פרויקט",
      "הכנסות",
      "הוצאות",
      "רווח נקי",
      "שיעור רווחיות"
    ]
  ],
  "Tasks_Manager": [
    [
      "task_id",
      "created_at",
      "task_type",
      "priority",
      "related_project",
      "related_counterparty",
      "related_transaction_id",
      "task_title",
      "task_description",
      "owner",
      "due_date",
      "status",
      "sla_days",
      "aging_days",
      "is_overdue",
      "resolution_note",
      "resolved_at"
    ]
  ],
  "Dashboard": [
    [
      "metric",
      "value",
      "notes"
    ],
    [
      "הכנסות החודש",
      "",
      "מחושב מ-Transactions_All"
    ],
    [
      "הוצאות החודש",
      "",
      "מחושב מ-Transactions_All"
    ],
    [
      "רווח נקי",
      "",
      "הכנסות פחות הוצאות"
    ],
    [
      "תשלומים ממתינים",
      "",
      "סטטוס ממתין"
    ],
    [
      "כפילויות פתוחות",
      "",
      "Income + Expenses + RAW"
    ],
    [
      "שגיאות נתונים",
      "",
      "Income + Expenses + RAW"
    ]
  ]
};
const FINANCE_SYSTEM_FORMULAS = {
  "Income": [
    [
      "J2",
      "=IF(OR(E2=\"\",F2=\"\"),\"\",E2+F2)"
    ],
    [
      "K2",
      "=IF(A2=\"\",\"\",TEXT(A2,\"yyyymmdd\")&\"_\"&C2&\"_\"&E2)"
    ],
    [
      "L2",
      "=IF(K2=\"\",\"\",IF(COUNTIF($K:$K,K2)>1,\"כפול\",\"\"))"
    ],
    [
      "M2",
      "=IF(A2=\"\",\"\",IF(OR(E2<=0,F2<0,D2=\"\",C2=\"\",H2=\"\"),\"שגיאת הזנה\",\"\"))"
    ]
  ],
  "Expenses": [
    [
      "J2",
      "=IF(OR(E2=\"\",F2=\"\"),\"\",E2+F2)"
    ],
    [
      "K2",
      "=IF(A2=\"\",\"\",TEXT(A2,\"yyyymmdd\")&\"_\"&C2&\"_\"&E2)"
    ],
    [
      "L2",
      "=IF(K2=\"\",\"\",IF(COUNTIF($K:$K,K2)>1,\"כפול\",\"\"))"
    ],
    [
      "M2",
      "=IF(A2=\"\",\"\",IF(OR(E2<=0,F2<0,D2=\"\",C2=\"\",H2=\"\"),\"שגיאת הזנה\",\"\"))"
    ]
  ],
  "RAW_Transactions": [
    [
      "O2",
      "=IF(M2=\"\",\"\",IF(OR(LOWER(M2)=\"income\",LOWER(M2)=\"credit\"),\"הכנסה\",\"הוצאה\"))"
    ],
    [
      "R2",
      "=IF(N2=\"\",\"ממתין\",IF(REGEXMATCH(LOWER(N2),\"paid|success|completed\"),\"שולם\",\"ממתין\"))"
    ],
    [
      "U2",
      "=IF(D2=\"\",\"\",TEXT(D2,\"yyyymmdd\")&\"_\"&E2&\"_\"&G2&\"_\"&C2)"
    ],
    [
      "S2",
      "=IF(U2=\"\",\"\",IF(COUNTIF($U:$U,U2)>1,\"כפול\",\"\"))"
    ],
    [
      "T2",
      "=IF(OR(D2=\"\",E2=\"\",G2=\"\",O2=\"\"),\"שגיאה\",\"\")"
    ]
  ],
  "Transactions_All": [
    [
      "A2",
      "={FILTER({Income!A2:A,\"הכנסה\",Income!B2:B,Income!C2:C,Income!D2:D,Income!E2:E,Income!F2:F,Income!J2:J,Income!G2:G,Income!H2:H,Income!I2:I,Income!K2:K},Income!A2:A<>\"\");FILTER({Expenses!A2:A,\"הוצאה\",Expenses!B2:B,Expenses!C2:C,Expenses!D2:D,Expenses!E2:E,Expenses!F2:F,Expenses!J2:J,Expenses!G2:G,Expenses!H2:H,Expenses!I2:I,Expenses!K2:K},Expenses!A2:A<>\"\")}"
    ]
  ],
  "Project_Profitability": [
    [
      "A2",
      "=UNIQUE(FILTER(Transactions_All!D2:D,Transactions_All!D2:D<>\"\"))"
    ],
    [
      "B2",
      "=SUMIFS(Transactions_All!H:H,Transactions_All!D:D,A2,Transactions_All!B:B,\"הכנסה\")"
    ],
    [
      "C2",
      "=SUMIFS(Transactions_All!H:H,Transactions_All!D:D,A2,Transactions_All!B:B,\"הוצאה\")"
    ],
    [
      "D2",
      "=B2-C2"
    ],
    [
      "E2",
      "=IF(B2=0,\"\",D2/B2)"
    ]
  ],
  "Tasks_Manager": [
    [
      "A2",
      "=\"TSK-\"&TEXT(ROW(A2)-1,\"00000\")"
    ],
    [
      "N2",
      "=IF(B2=\"\",\"\",TODAY()-B2)"
    ],
    [
      "O2",
      "=IF(OR(K2=\"\",L2=\"הושלם\"),\"\",IF(TODAY()>K2,\"באיחור\",\"בזמן\"))"
    ]
  ],
  "Dashboard": [
    [
      "B2",
      "=SUMIFS(Transactions_All!H:H,Transactions_All!B:B,\"הכנסה\",Transactions_All!A:A,\">=\"&EOMONTH(TODAY(),-1)+1,Transactions_All!A:A,\"<=\"&EOMONTH(TODAY(),0))"
    ],
    [
      "B3",
      "=SUMIFS(Transactions_All!H:H,Transactions_All!B:B,\"הוצאה\",Transactions_All!A:A,\">=\"&EOMONTH(TODAY(),-1)+1,Transactions_All!A:A,\"<=\"&EOMONTH(TODAY(),0))"
    ],
    [
      "B4",
      "=B2-B3"
    ],
    [
      "B5",
      "=SUMIFS(Transactions_All!H:H,Transactions_All!J:J,\"ממתין\")"
    ],
    [
      "B6",
      "=COUNTIF(Income!L:L,\"כפול\")+COUNTIF(Expenses!L:L,\"כפול\")+COUNTIF(RAW_Transactions!S:S,\"כפול\")"
    ],
    [
      "B7",
      "=COUNTIF(Income!M:M,\"שגיאת הזנה\")+COUNTIF(Expenses!M:M,\"שגיאת הזנה\")+COUNTIF(RAW_Transactions!T:T,\"שגיאה\")"
    ]
  ]
};

function setupRealEstateFinanceSystem() {
  const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();

  Object.keys(FINANCE_SYSTEM_TABS).forEach(function(sheetName) {
    const values = FINANCE_SYSTEM_TABS[sheetName];
    let sheet = spreadsheet.getSheetByName(sheetName);
    if (!sheet) {
      sheet = spreadsheet.insertSheet(sheetName);
    }
    sheet.clear();
    sheet.getRange(1, 1, values.length, values[0].length).setValues(values);
    sheet.setFrozenRows(1);
    sheet.autoResizeColumns(1, values[0].length);
  });

  Object.keys(FINANCE_SYSTEM_FORMULAS).forEach(function(sheetName) {
    const sheet = spreadsheet.getSheetByName(sheetName);
    if (!sheet) return;
    FINANCE_SYSTEM_FORMULAS[sheetName].forEach(function(item) {
      sheet.getRange(item[0]).setFormula(item[1]);
    });
  });

  applyFinanceDataValidation_(spreadsheet);
  SpreadsheetApp.flush();
}

function applyFinanceDataValidation_(spreadsheet) {
  const lists = spreadsheet.getSheetByName('Lists');
  if (!lists) return;

  const paymentRule = SpreadsheetApp.newDataValidation()
    .requireValueInRange(lists.getRange('A2:A100'), true)
    .setAllowInvalid(false)
    .build();
  const statusRule = SpreadsheetApp.newDataValidation()
    .requireValueInRange(lists.getRange('B2:B100'), true)
    .setAllowInvalid(false)
    .build();
  const incomeCategoryRule = SpreadsheetApp.newDataValidation()
    .requireValueInRange(lists.getRange('C2:C100'), true)
    .setAllowInvalid(false)
    .build();
  const expenseCategoryRule = SpreadsheetApp.newDataValidation()
    .requireValueInRange(lists.getRange('D2:D100'), true)
    .setAllowInvalid(false)
    .build();
  const projectRule = SpreadsheetApp.newDataValidation()
    .requireValueInRange(lists.getRange('E2:E100'), true)
    .setAllowInvalid(false)
    .build();

  const income = spreadsheet.getSheetByName('Income');
  const expenses = spreadsheet.getSheetByName('Expenses');
  if (income) {
    income.getRange('C2:C1000').setDataValidation(projectRule);
    income.getRange('D2:D1000').setDataValidation(incomeCategoryRule);
    income.getRange('G2:G1000').setDataValidation(paymentRule);
    income.getRange('H2:H1000').setDataValidation(statusRule);
  }
  if (expenses) {
    expenses.getRange('C2:C1000').setDataValidation(projectRule);
    expenses.getRange('D2:D1000').setDataValidation(expenseCategoryRule);
    expenses.getRange('G2:G1000').setDataValidation(paymentRule);
    expenses.getRange('H2:H1000').setDataValidation(statusRule);
  }
}
```

## Income.csv

```text
תאריך,צד נגדי,פרויקט,קטגוריה,סכום,"מע""מ",אמצעי תשלום,סטטוס,הערות,סכום כולל,מזהה תנועה,כפילות?,שגיאה?
```

## Expenses.csv

```text
תאריך,צד נגדי,פרויקט,קטגוריה,סכום,"מע""מ",אמצעי תשלום,סטטוס,הערות,סכום כולל,מזהה תנועה,כפילות?,שגיאה?
```

## Lists.csv

```text
Payment_Methods,Status,Income_Categories,Expense_Categories,Projects
העברה בנקאית,שולם,מכירת נכס,שיווק,Project A
אשראי,ממתין,שכירות,תחזוקה,Project B
צ׳ק,חלקי,דמי תיווך,משפטי,Project C
מזומן,בוטל,ניהול נכס,"הנה""ח",Project D
ביט,,אחר,עמלות סליקה,
אחר,,,אחר,
```

## Category_Map.csv

```text
keyword,normalized_category,type,notes
פייסבוק,שיווק,הוצאה,סיווג הוצאות פרסום
"עו""ד",משפטי,הוצאה,סיווג הוצאות משפטיות
דמי ניהול,ניהול נכס,הכנסה,זיהוי הכנסות מניהול
```

## RAW_Transactions.csv

```text
created_at,source,external_id,txn_date,counterparty,description,amount,vat,currency,payment_method,project_raw,category_raw,direction_raw,status_raw,normalized_type,normalized_category,normalized_project,status_normalized,duplicate_flag,error_flag,unique_key
```

## Transactions_All.csv

```text
תאריך,סוג תנועה,צד נגדי,פרויקט,קטגוריה,סכום,"מע""מ",סכום כולל,אמצעי תשלום,סטטוס,הערות,מזהה תנועה
```

## Project_Profitability.csv

```text
פרויקט,הכנסות,הוצאות,רווח נקי,שיעור רווחיות
```

## Tasks_Manager.csv

```text
task_id,created_at,task_type,priority,related_project,related_counterparty,related_transaction_id,task_title,task_description,owner,due_date,status,sla_days,aging_days,is_overdue,resolution_note,resolved_at
```

## Dashboard.csv

```text
metric,value,notes
הכנסות החודש,,מחושב מ-Transactions_All
הוצאות החודש,,מחושב מ-Transactions_All
רווח נקי,,הכנסות פחות הוצאות
תשלומים ממתינים,,סטטוס ממתין
כפילויות פתוחות,,Income + Expenses + RAW
שגיאות נתונים,,Income + Expenses + RAW
```
