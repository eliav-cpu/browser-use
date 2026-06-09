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
