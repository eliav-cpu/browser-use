# Real-Estate Finance Management System (Google Sheets + Make)

This guide defines a full production-ready operating model for a real-estate company that already manages finances in Excel/Sheets and wants to improve incrementally without replacing the existing process.

## 1) Goals and constraints

- Improve the existing income/expense process in phases.
- Do **not** replace the current workbook without approval.
- Keep all changes backward-compatible and reversible.
- Support daily operations, executive visibility, and automation.

## 2) Sheet architecture

Create a parallel workbook (recommended name: `Finance_RealEstate_v1`) with the tabs below:

1. `Income`
2. `Expenses`
3. `Lists`
4. `Category_Map`
5. `RAW_Transactions`
6. `Transactions_All`
7. `Project_Profitability`
8. `Tasks_Manager`
9. `Dashboard`

## 3) Data schema

### 3.1 Income and Expenses (core input)

Common columns (same order in both tabs):

1. `תאריך`
2. `צד נגדי` (client for income, supplier for expense)
3. `פרויקט`
4. `קטגוריה`
5. `סכום`
6. `מע"מ`
7. `אמצעי תשלום`
8. `סטטוס`
9. `הערות`
10. `סכום כולל` (formula)
11. `מזהה תנועה` (formula)
12. `כפילות?` (formula)
13. `שגיאה?` (formula)

### 3.2 Lists

Reference lists for validation:

- Payment methods: `העברה בנקאית`, `אשראי`, `צ׳ק`, `מזומן`, `ביט`, `אחר`
- Status: `שולם`, `ממתין`, `חלקי`, `בוטל`
- Income categories: `מכירת נכס`, `שכירות`, `דמי תיווך`, `ניהול נכס`, `אחר`
- Expense categories: `שיווק`, `תחזוקה`, `משפטי`, `הנה"ח`, `עמלות סליקה`, `אחר`
- Projects: active projects list

### 3.3 RAW_Transactions (automation input)

1. `created_at`
2. `source`
3. `external_id`
4. `txn_date`
5. `counterparty`
6. `description`
7. `amount`
8. `vat`
9. `currency`
10. `payment_method`
11. `project_raw`
12. `category_raw`
13. `direction_raw`
14. `status_raw`
15. `normalized_type`
16. `normalized_category`
17. `normalized_project`
18. `status_normalized`
19. `duplicate_flag`
20. `error_flag`
21. `unique_key`

## 4) Core formulas

> Notes:
> - Formulas assume row 1 is headers and data starts at row 2.
> - Replace column letters if your sheet layout differs.

### 4.1 Income/Expenses formulas

`סכום כולל`:

```excel
=IF(OR(E2="",F2=""),"",E2+F2)
```

`מזהה תנועה`:

```excel
=TEXT(A2,"yyyymmdd")&"_"&C2&"_"&E2
```

`כפילות?`:

```excel
=IF(K2="","",IF(COUNTIF($K:$K,K2)>1,"כפול",""))
```

`שגיאה?`:

```excel
=IF(A2="","",IF(OR(E2<=0,F2<0,D2="",C2="",H2=""),"שגיאת הזנה",""))
```

### 4.2 RAW normalization

`normalized_type`:

```excel
=IF(M2="","",IF(OR(LOWER(M2)="income",LOWER(M2)="credit"),"הכנסה","הוצאה"))
```

`status_normalized`:

```excel
=IF(N2="","ממתין",IF(REGEXMATCH(LOWER(N2),"paid|success|completed"),"שולם","ממתין"))
```

`unique_key`:

```excel
=IF(D2="","",TEXT(D2,"yyyymmdd")&"_"&E2&"_"&G2&"_"&C2)
```

`duplicate_flag`:

```excel
=IF(U2="","",IF(COUNTIF($U:$U,U2)>1,"כפול",""))
```

`error_flag`:

```excel
=IF(OR(D2="",E2="",G2="",O2=""),"שגיאה","")
```

### 4.3 Unified transactions

In `Transactions_All!A2`:

```excel
={
  FILTER({Income!A2:A,"הכנסה",Income!B2:B,Income!C2:C,Income!D2:D,Income!E2:E,Income!F2:F,Income!J2:J,Income!G2:G,Income!H2:H,Income!I2:I,Income!K2:K},Income!A2:A<>"");
  FILTER({Expenses!A2:A,"הוצאה",Expenses!B2:B,Expenses!C2:C,Expenses!D2:D,Expenses!E2:E,Expenses!F2:F,Expenses!J2:J,Expenses!G2:G,Expenses!H2:H,Expenses!I2:I,Expenses!K2:K},Expenses!A2:A<>"")
}
```

## 5) Dashboard KPIs

- Current month income
- Current month expense
- Net profit
- Pending payments
- Month-over-month change
- Open data quality issues
- Open duplicates

Current month income:

```excel
=SUMIFS(Transactions_All!H:H,Transactions_All!B:B,"הכנסה",Transactions_All!A:A,">="&EOMONTH(TODAY(),-1)+1,Transactions_All!A:A,"<="&EOMONTH(TODAY(),0))
```

Current month expense:

```excel
=SUMIFS(Transactions_All!H:H,Transactions_All!B:B,"הוצאה",Transactions_All!A:A,">="&EOMONTH(TODAY(),-1)+1,Transactions_All!A:A,"<="&EOMONTH(TODAY(),0))
```

Pending payments:

```excel
=SUMIFS(Transactions_All!H:H,Transactions_All!J:J,"ממתין")
```

## 6) Project profitability

In `Project_Profitability`:

- `A`: project name list
- `B`: income by project
- `C`: expense by project
- `D`: net
- `E`: margin

Project list:

```excel
=UNIQUE(FILTER(Transactions_All!D2:D,Transactions_All!D2:D<>""))
```

Income by project:

```excel
=SUMIFS(Transactions_All!H:H,Transactions_All!D:D,A2,Transactions_All!B:B,"הכנסה")
```

Expense by project:

```excel
=SUMIFS(Transactions_All!H:H,Transactions_All!D:D,A2,Transactions_All!B:B,"הוצאה")
```

Net:

```excel
=B2-C2
```

Margin:

```excel
=IF(B2=0,"",D2/B2)
```

## 7) Tasks manager

Columns:

1. `task_id`
2. `created_at`
3. `task_type`
4. `priority`
5. `related_project`
6. `related_counterparty`
7. `related_transaction_id`
8. `task_title`
9. `task_description`
10. `owner`
11. `due_date`
12. `status`
13. `sla_days`
14. `aging_days`
15. `is_overdue`
16. `resolution_note`
17. `resolved_at`

Key formulas:

`task_id`

```excel
="TSK-"&TEXT(ROW(A2)-1,"00000")
```

`aging_days`

```excel
=IF(B2="","",TODAY()-B2)
```

`is_overdue`

```excel
=IF(OR(K2="",L2="הושלם"),"",IF(TODAY()>K2,"באיחור","בזמן"))
```

## 8) Make.com scenarios

### 8.1 Ingestion scenario (realtime/batch)

1. Trigger: Webhook / scheduled pull from EasyCard/API/CSV.
2. Normalize fields (date, amount, status).
3. Check duplicates by `external_id` in `RAW_Transactions`.
4. Append new rows only.
5. Alert on malformed payloads.

### 8.2 Daily control scenario

1. Scheduled daily run (e.g., 08:00).
2. Detect transactions with:
   - `duplicate_flag="כפול"`
   - `error_flag="שגיאה"`
   - pending status beyond SLA
3. Create/update rows in `Tasks_Manager`.
4. Send summary to management (email/Slack/WhatsApp gateway).

## 9) Rollout plan

### Phase 1 (day 1)

- Create workbook structure.
- Implement validation lists.
- Implement core formulas.
- Build minimal dashboard.

### Phase 2 (day 2-3)

- Add Make ingestion from one source.
- Validate duplicate/error controls.
- Add project profitability view.

### Phase 3 (day 4-5)

- Add tasks manager automation.
- Add daily management summary.
- Final UAT and handoff.

## 10) Governance

- Keep `Lists` and `Category_Map` editable only by finance owner.
- Archive monthly snapshots before major formula changes.
- Never delete historical rows; use status lifecycle.
- Document every mapping rule change with date and owner.
