# DSeL - a DSL for Event Log Generation

DSL for simple Event Log Generation. 
It's pronounced _Diesel_.

## Syntax 

```
GENERATE [LOG|DF]
OUTPUT <filepath>
ACTIVITIES 
	<a_name> : <a_id>
	... 
TRACES 
	<a_name> [- <a_name>] ... 
	...
[COLUMN <c_name> TYPE <c_type>]...
CASES <n_cases>

```

- It generates an _Event Log_ with `<n_cases>`.
- Activities _names_ and _ids_ are declared in `ACTIVITIES`.
- Each case follows one of the declared `TRACES`.
- Each record has the default columns : _CaseID_, _ActivityID_, _Activity_.
 - Extra columns can be defined using `COLUMN`. 
Each column can be of one of these types: `Timestamp`, `Int`, `Number` and `String`.

_Example.dsel_

```
GENERATE LOG 
OUTPUT example.csv
ACTIVITIES 
    a : _1
    b : _2 
    c : _3
TRACES 
    a - b - c
    a - c
COLUMN timestamp TYPE Timestamp 
COLUMN var0 TYPE Int
COLUMN var1 TYPE Int
CASES 2
```

Generates the following _example.csv_ :
```
CaseID,ActivityID,Activity,timestamp,var0,var1
1, _1, a, 0, 10, 20 
1, _3, c, 4, 10, 30 
2, _1, a, 0, 10, 13
2, _2, b, 5, 23, 30 
2, _3, c, 9, 34, 12 
```

## Types 

For now, there are the following data types: 

- **Timestamp** 
Timestamp of a given activity. 
Random value. 
Incremental within cases.
For now it is basically an Int.
- **Int**
Integer. 
Random value between 0-100.
- **Number** 
Float. 
Random value between 0-100.
- **String**
	String.
	Random String.

## Try it yourself 

Use the example file or generate your own _Event Log_ using:

```
python3 dsel.py <filepath>
```