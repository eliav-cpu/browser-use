"""Generate a real-estate finance management scaffold for Google Sheets.

The generator creates plain-text artifacts that can be copied into Google Sheets
or Make.com without relying on binary files.  It also creates a local ZIP bundle
for operators who run the script on their own machine, but the committed output
is intentionally text-first because many review/download UIs cannot display ZIPs.
"""

from __future__ import annotations

import csv
import json
import zipfile
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"

TabName = Literal[
    "Income",
    "Expenses",
    "Lists",
    "Category_Map",
    "RAW_Transactions",
    "Transactions_All",
    "Project_Profitability",
    "Tasks_Manager",
    "Dashboard",
]


class TabDefinition(BaseModel):
    """A Google Sheets tab schema and optional seed rows."""

    model_config = ConfigDict(frozen=True)

    name: TabName | str
    headers: list[str] = Field(min_length=1)
    rows: list[list[str]] = Field(default_factory=list)

    @field_validator("rows")
    @classmethod
    def rows_match_header_width(cls, rows: list[list[str]], info: Any) -> list[list[str]]:
        """Validate generated CSV rows so imports do not create shifted columns."""
        headers = info.data.get("headers", [])
        width = len(headers)
        for row_index, row in enumerate(rows, start=1):
            if len(row) != width:
                raise ValueError(f"row {row_index} has {len(row)} cells, expected {width}")
        return rows


class MakeScenario(BaseModel):
    """Make.com scenario blueprint."""

    model_config = ConfigDict(frozen=True)

    name: str
    trigger: str
    modules: list[str] = Field(min_length=1)
    writes_to: str
    duplicate_guard: str


class FinanceSystemBlueprint(BaseModel):
    """All generated assets for the finance system."""

    model_config = ConfigDict(frozen=True)

    workbook_name: str
    tabs: list[TabDefinition]
    make_scenarios: list[MakeScenario]

    @property
    def tab_names(self) -> list[str]:
        """Return tab names in workbook creation order."""
        return [tab.name for tab in self.tabs]


FORMULAS: dict[str, list[tuple[str, str]]] = {
    "Income": [
        ("J2", '=IF(OR(E2="",F2=""),"",E2+F2)'),
        ("K2", '=IF(A2="","",TEXT(A2,"yyyymmdd")&"_"&C2&"_"&E2)'),
        ("L2", '=IF(K2="","",IF(COUNTIF($K:$K,K2)>1,"כפול",""))'),
        ("M2", '=IF(A2="","",IF(OR(E2<=0,F2<0,D2="",C2="",H2=""),"שגיאת הזנה",""))'),
    ],
    "Expenses": [
        ("J2", '=IF(OR(E2="",F2=""),"",E2+F2)'),
        ("K2", '=IF(A2="","",TEXT(A2,"yyyymmdd")&"_"&C2&"_"&E2)'),
        ("L2", '=IF(K2="","",IF(COUNTIF($K:$K,K2)>1,"כפול",""))'),
        ("M2", '=IF(A2="","",IF(OR(E2<=0,F2<0,D2="",C2="",H2=""),"שגיאת הזנה",""))'),
    ],
    "RAW_Transactions": [
        ("O2", '=IF(M2="","",IF(OR(LOWER(M2)="income",LOWER(M2)="credit"),"הכנסה","הוצאה"))'),
        ("R2", '=IF(N2="","ממתין",IF(REGEXMATCH(LOWER(N2),"paid|success|completed"),"שולם","ממתין"))'),
        ("U2", '=IF(D2="","",TEXT(D2,"yyyymmdd")&"_"&E2&"_"&G2&"_"&C2)'),
        ("S2", '=IF(U2="","",IF(COUNTIF($U:$U,U2)>1,"כפול",""))'),
        ("T2", '=IF(OR(D2="",E2="",G2="",O2=""),"שגיאה","")'),
    ],
    "Transactions_All": [
        (
            "A2",
            "="
            "{"
            'FILTER({Income!A2:A,"הכנסה",Income!B2:B,Income!C2:C,Income!D2:D,'
            "Income!E2:E,Income!F2:F,Income!J2:J,Income!G2:G,Income!H2:H,Income!I2:I,Income!K2:K},"
            'Income!A2:A<>"");'
            'FILTER({Expenses!A2:A,"הוצאה",Expenses!B2:B,Expenses!C2:C,Expenses!D2:D,'
            "Expenses!E2:E,Expenses!F2:F,Expenses!J2:J,Expenses!G2:G,Expenses!H2:H,Expenses!I2:I,Expenses!K2:K},"
            'Expenses!A2:A<>"")'
            "}",
        )
    ],
    "Project_Profitability": [
        ("A2", '=UNIQUE(FILTER(Transactions_All!D2:D,Transactions_All!D2:D<>""))'),
        ("B2", '=SUMIFS(Transactions_All!H:H,Transactions_All!D:D,A2,Transactions_All!B:B,"הכנסה")'),
        ("C2", '=SUMIFS(Transactions_All!H:H,Transactions_All!D:D,A2,Transactions_All!B:B,"הוצאה")'),
        ("D2", "=B2-C2"),
        ("E2", '=IF(B2=0,"",D2/B2)'),
    ],
    "Tasks_Manager": [
        ("A2", '="TSK-"&TEXT(ROW(A2)-1,"00000")'),
        ("N2", '=IF(B2="","",TODAY()-B2)'),
        ("O2", '=IF(OR(K2="",L2="הושלם"),"",IF(TODAY()>K2,"באיחור","בזמן"))'),
    ],
    "Dashboard": [
        (
            "B2",
            "=SUMIFS(Transactions_All!H:H,Transactions_All!B:B,"
            '"הכנסה",Transactions_All!A:A,">="&EOMONTH(TODAY(),-1)+1,'
            'Transactions_All!A:A,"<="&EOMONTH(TODAY(),0))',
        ),
        (
            "B3",
            "=SUMIFS(Transactions_All!H:H,Transactions_All!B:B,"
            '"הוצאה",Transactions_All!A:A,">="&EOMONTH(TODAY(),-1)+1,'
            'Transactions_All!A:A,"<="&EOMONTH(TODAY(),0))',
        ),
        ("B4", "=B2-B3"),
        ("B5", '=SUMIFS(Transactions_All!H:H,Transactions_All!J:J,"ממתין")'),
        ("B6", '=COUNTIF(Income!L:L,"כפול")+COUNTIF(Expenses!L:L,"כפול")+COUNTIF(RAW_Transactions!S:S,"כפול")'),
        ("B7", '=COUNTIF(Income!M:M,"שגיאת הזנה")+COUNTIF(Expenses!M:M,"שגיאת הזנה")+COUNTIF(RAW_Transactions!T:T,"שגיאה")'),
    ],
}


BLUEPRINT = FinanceSystemBlueprint(
    workbook_name="Finance_RealEstate_v1",
    tabs=[
        TabDefinition(
            name="Income",
            headers=[
                "תאריך",
                "צד נגדי",
                "פרויקט",
                "קטגוריה",
                "סכום",
                'מע"מ',
                "אמצעי תשלום",
                "סטטוס",
                "הערות",
                "סכום כולל",
                "מזהה תנועה",
                "כפילות?",
                "שגיאה?",
            ],
        ),
        TabDefinition(
            name="Expenses",
            headers=[
                "תאריך",
                "צד נגדי",
                "פרויקט",
                "קטגוריה",
                "סכום",
                'מע"מ',
                "אמצעי תשלום",
                "סטטוס",
                "הערות",
                "סכום כולל",
                "מזהה תנועה",
                "כפילות?",
                "שגיאה?",
            ],
        ),
        TabDefinition(
            name="Lists",
            headers=["Payment_Methods", "Status", "Income_Categories", "Expense_Categories", "Projects"],
            rows=[
                ["העברה בנקאית", "שולם", "מכירת נכס", "שיווק", "Project A"],
                ["אשראי", "ממתין", "שכירות", "תחזוקה", "Project B"],
                ["צ׳ק", "חלקי", "דמי תיווך", "משפטי", "Project C"],
                ["מזומן", "בוטל", "ניהול נכס", 'הנה"ח', "Project D"],
                ["ביט", "", "אחר", "עמלות סליקה", ""],
                ["אחר", "", "", "אחר", ""],
            ],
        ),
        TabDefinition(
            name="Category_Map",
            headers=["keyword", "normalized_category", "type", "notes"],
            rows=[
                ["פייסבוק", "שיווק", "הוצאה", "סיווג הוצאות פרסום"],
                ["עו\"ד", "משפטי", "הוצאה", "סיווג הוצאות משפטיות"],
                ["דמי ניהול", "ניהול נכס", "הכנסה", "זיהוי הכנסות מניהול"],
            ],
        ),
        TabDefinition(
            name="RAW_Transactions",
            headers=[
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
                "unique_key",
            ],
        ),
        TabDefinition(
            name="Transactions_All",
            headers=[
                "תאריך",
                "סוג תנועה",
                "צד נגדי",
                "פרויקט",
                "קטגוריה",
                "סכום",
                'מע"מ',
                "סכום כולל",
                "אמצעי תשלום",
                "סטטוס",
                "הערות",
                "מזהה תנועה",
            ],
        ),
        TabDefinition(name="Project_Profitability", headers=["פרויקט", "הכנסות", "הוצאות", "רווח נקי", "שיעור רווחיות"]),
        TabDefinition(
            name="Tasks_Manager",
            headers=[
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
                "resolved_at",
            ],
        ),
        TabDefinition(
            name="Dashboard",
            headers=["metric", "value", "notes"],
            rows=[
                ["הכנסות החודש", "", "מחושב מ-Transactions_All"],
                ["הוצאות החודש", "", "מחושב מ-Transactions_All"],
                ["רווח נקי", "", "הכנסות פחות הוצאות"],
                ["תשלומים ממתינים", "", "סטטוס ממתין"],
                ["כפילויות פתוחות", "", "Income + Expenses + RAW"],
                ["שגיאות נתונים", "", "Income + Expenses + RAW"],
            ],
        ),
    ],
    make_scenarios=[
        MakeScenario(
            name="ingestion",
            trigger="Webhook / EasyCard / CSV / API",
            modules=[
                "Receive transaction payload",
                "Normalize date, amount, VAT, status, source and external_id",
                "Search RAW_Transactions by external_id and unique_key",
                "Append only new transactions to RAW_Transactions",
                "Route malformed records to an alert path",
            ],
            writes_to="RAW_Transactions",
            duplicate_guard="external_id + unique_key",
        ),
        MakeScenario(
            name="daily_control",
            trigger="Scheduler at 08:00",
            modules=[
                "Search duplicate_flag='כפול' and error_flag='שגיאה'",
                "Create or update Tasks_Manager rows",
                "Send management summary by email / Slack / WhatsApp gateway",
            ],
            writes_to="Tasks_Manager",
            duplicate_guard="related_transaction_id + task_type + status != הושלם",
        ),
    ],
)


REFERENCE_LINKS = [
    "Google Apps Script Spreadsheet service: https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet-app",
    "Google Apps Script Range.setValues / setFormula / setDataValidation: "
    "https://developers.google.com/apps-script/reference/spreadsheet/range",
    "Google Apps Script DataValidationBuilder: "
    "https://developers.google.com/apps-script/reference/spreadsheet/data-validation-builder",
    "Make Webhooks help: https://help.make.com/webhooks",
    "Make Google Sheets app documentation: https://apps.make.com/google-sheets",
]


def write_csv(path: Path, tab: TabDefinition) -> None:
    """Write one tab as a UTF-8 CSV file."""
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(tab.headers)
        writer.writerows(tab.rows)


def formula_markdown() -> str:
    """Render all spreadsheet formulas as copy/paste documentation."""
    sections = ["# Formula Pack (copy/paste into Google Sheets)", ""]
    for sheet_name, formulas in FORMULAS.items():
        sections.extend([f"## {sheet_name}", ""])
        for cell, formula in formulas:
            sections.extend([f"- `{cell}`:", "```excel", formula, "```", ""])
    return "\n".join(sections).rstrip() + "\n"


def setup_he_markdown() -> str:
    """Render Hebrew setup instructions for non-technical operators."""
    tab_list = "\n".join(f"   - `{tab_name}`" for tab_name in BLUEPRINT.tab_names)
    return f"""# מדריך הקמה בעברית - מערכת כספים לחברת נדל\"ן

המטרה: להקים מערכת מקבילה ונקייה ב-Google Sheets, בלי לפגוע בקובץ הקיים.

## הדרך המומלצת - אוטומציה עם Apps Script

1. פתח Google Sheets וצור קובץ חדש בשם `{BLUEPRINT.workbook_name}`.
2. בתפריט העליון לחץ `Extensions` -> `Apps Script`.
3. פתח את הקובץ `setup_google_sheet.gs` מתוך תיקיית `output`.
4. העתק את כל הקוד והדבק אותו בעורך Apps Script.
5. שמור והריץ את הפונקציה `setupRealEstateFinanceSystem`.
6. אשר הרשאות אם Google מבקש.
7. חזור לגיליון ובדוק שכל הטאבים, הכותרות, הנוסחאות והרשימות נוצרו.

## דרך ידנית - אם לא רוצים Apps Script

1. פתח Google Sheets.
2. צור קובץ חדש בשם `{BLUEPRINT.workbook_name}`.
3. צור טאבים לפי הרשימה:
{tab_list}
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
"""


def download_he_markdown() -> str:
    """Render Hebrew instructions for environments that do not support binary ZIP files."""
    files = [f"{tab.name}.csv" for tab in BLUEPRINT.tabs]
    files.extend(["FORMULAS.md", "SETUP_HE.md", "setup_google_sheet.gs", "make_scenario_blueprint.json"])
    files_list = "\n".join(f"{index}. `{file_name}`" for index, file_name in enumerate(files, start=1))
    return f"""# איך להשתמש במערכת הכספים בלי ZIP

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

{files_list}

## הדרך המהירה ביותר להקים

1. פתח Google Sheets חדש בשם `{BLUEPRINT.workbook_name}`.
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
"""


def make_blueprint_json() -> str:
    """Render Make.com implementation blueprint JSON."""
    payload = {
        "name": "real-estate-finance-automation",
        "version": 2,
        "target_workbook": BLUEPRINT.workbook_name,
        "principles": [
            "Write external data only to RAW_Transactions until validation is complete.",
            "Use external_id and unique_key before appending to prevent duplicates.",
            "Create Tasks_Manager rows for exceptions instead of overwriting financial history.",
        ],
        "field_mapping": {
            "external_id": "Provider transaction/payment id",
            "txn_date": "Provider transaction date",
            "counterparty": "Customer / supplier name",
            "amount": "Amount before VAT when available",
            "vat": "VAT amount or zero",
            "direction_raw": "income/credit or expense/debit",
            "status_raw": "paid/success/completed/pending/failed",
        },
        "scenarios": [scenario.model_dump() for scenario in BLUEPRINT.make_scenarios],
    }
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def apps_script_source() -> str:
    """Generate Google Apps Script code that creates the workbook in one click."""
    tab_payload = {tab.name: [tab.headers, *tab.rows] for tab in BLUEPRINT.tabs}
    formulas_payload = FORMULAS
    return f"""// Auto-generated by generate_system.py.
// Creates the real-estate finance workbook structure, formulas, and dropdowns.

const FINANCE_SYSTEM_TABS = {json.dumps(tab_payload, ensure_ascii=False, indent=2)};
const FINANCE_SYSTEM_FORMULAS = {json.dumps(formulas_payload, ensure_ascii=False, indent=2)};

function setupRealEstateFinanceSystem() {{
  const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();

  Object.keys(FINANCE_SYSTEM_TABS).forEach(function(sheetName) {{
    const values = FINANCE_SYSTEM_TABS[sheetName];
    let sheet = spreadsheet.getSheetByName(sheetName);
    if (!sheet) {{
      sheet = spreadsheet.insertSheet(sheetName);
    }}
    sheet.clear();
    sheet.getRange(1, 1, values.length, values[0].length).setValues(values);
    sheet.setFrozenRows(1);
    sheet.autoResizeColumns(1, values[0].length);
  }});

  Object.keys(FINANCE_SYSTEM_FORMULAS).forEach(function(sheetName) {{
    const sheet = spreadsheet.getSheetByName(sheetName);
    if (!sheet) return;
    FINANCE_SYSTEM_FORMULAS[sheetName].forEach(function(item) {{
      sheet.getRange(item[0]).setFormula(item[1]);
    }});
  }});

  applyFinanceDataValidation_(spreadsheet);
  SpreadsheetApp.flush();
}}

function applyFinanceDataValidation_(spreadsheet) {{
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
  if (income) {{
    income.getRange('C2:C1000').setDataValidation(projectRule);
    income.getRange('D2:D1000').setDataValidation(incomeCategoryRule);
    income.getRange('G2:G1000').setDataValidation(paymentRule);
    income.getRange('H2:H1000').setDataValidation(statusRule);
  }}
  if (expenses) {{
    expenses.getRange('C2:C1000').setDataValidation(projectRule);
    expenses.getRange('D2:D1000').setDataValidation(expenseCategoryRule);
    expenses.getRange('G2:G1000').setDataValidation(paymentRule);
    expenses.getRange('H2:H1000').setDataValidation(statusRule);
  }}
}}
"""


def all_in_one_he_markdown() -> str:
    """Render a single Hebrew file containing every generated text artifact."""
    sections = [
        "# כל מערכת הכספים בקובץ אחד",
        "",
        "זה קובץ טקסט אחד שמרכז את כל מה שצריך כדי להקים את המערכת.",
        "אם אין לך אפשרות להוריד ZIP, פתח את הקובץ הזה והעתק ממנו את החלקים הדרושים.",
        "",
        "## הכי חשוב",
        "",
        "כדי להקים את כל המערכת בגוגל שיטס, אתה צריך בעיקר את החלק `setup_google_sheet.gs` למטה.",
        "העתק אותו ל-Google Sheets -> Extensions -> Apps Script והריץ `setupRealEstateFinanceSystem`.",
        "",
    ]

    artifacts = {
        "SETUP_HE.md": setup_he_markdown(),
        "DOWNLOAD_HE.md": download_he_markdown(),
        "FORMULAS.md": formula_markdown(),
        "make_scenario_blueprint.json": make_blueprint_json(),
        "setup_google_sheet.gs": apps_script_source(),
    }

    for tab in BLUEPRINT.tabs:
        csv_lines = []
        import io

        csv_buffer = io.StringIO()
        writer = csv.writer(csv_buffer, lineterminator="\n")
        writer.writerow(tab.headers)
        writer.writerows(tab.rows)
        csv_lines.append(csv_buffer.getvalue())
        artifacts[f"{tab.name}.csv"] = "".join(csv_lines)

    for file_name, content in artifacts.items():
        fence = "json" if file_name.endswith(".json") else "javascript" if file_name.endswith(".gs") else "text"
        sections.extend([f"## {file_name}", "", f"```{fence}", content.rstrip(), "```", ""])

    return "\n".join(sections).rstrip() + "\n"


def references_markdown() -> str:
    """Render references checked while improving this scaffold."""
    lines = ["# References used", "", "The scaffold was reviewed against these primary references:", ""]
    lines.extend(f"- {link}" for link in REFERENCE_LINKS)
    return "\n".join(lines) + "\n"


def create_download_bundle() -> Path:
    """Create a local ZIP bundle containing generated setup artifacts."""
    bundle_path = OUTPUT_DIR / "real_estate_finance_system_bundle.zip"
    generated_files = sorted(path for path in OUTPUT_DIR.iterdir() if path.is_file() and path != bundle_path)

    with zipfile.ZipFile(bundle_path, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
        for path in generated_files:
            bundle.write(path, arcname=path.name)

    return bundle_path


def generate() -> list[Path]:
    """Generate all text artifacts and return their paths."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for old_artifact in OUTPUT_DIR.iterdir():
        if old_artifact.is_file():
            old_artifact.unlink()
    generated_paths: list[Path] = []

    for tab in BLUEPRINT.tabs:
        path = OUTPUT_DIR / f"{tab.name}.csv"
        write_csv(path, tab)
        generated_paths.append(path)

    named_outputs = {
        "FORMULAS.md": formula_markdown(),
        "SETUP_HE.md": setup_he_markdown(),
        "DOWNLOAD_HE.md": download_he_markdown(),
        "ALL_IN_ONE_HE.md": all_in_one_he_markdown(),
        "REFERENCES.md": references_markdown(),
        "setup_google_sheet.gs": apps_script_source(),
        "make_scenario_blueprint.json": make_blueprint_json(),
    }
    for file_name, content in named_outputs.items():
        path = OUTPUT_DIR / file_name
        path.write_text(content, encoding="utf-8")
        generated_paths.append(path)

    create_download_bundle()
    return generated_paths


def main() -> None:
    """CLI entry point."""
    generated_paths = generate()
    print(f"Generated workbook scaffold in: {OUTPUT_DIR}")
    print(f"Generated {len(generated_paths)} text artifacts")
    print(f"Local-only ZIP bundle: {OUTPUT_DIR / 'real_estate_finance_system_bundle.zip'}")


if __name__ == "__main__":
    main()
