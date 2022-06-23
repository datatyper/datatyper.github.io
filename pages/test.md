title: Testing Markdown to HTML Converter
author: Philip Mannering
status: published
date: 2022-01-01

# Test Markdown

This is a paragraph.

* This is item 1
* This is item 2

This is **bold** text  
This is *italic* text  
This is ***bold and italic*** text  

## Table

a | b | c
---|---|---
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9

Here is some code

```python
for i in range(10):
    print(i)
```

Here is some powershell
```powershell
for i in (1..10)
{
    write-host $i
}
```

Here is some Alteryx
```alteryx
datetimeadd(datetimetoday(), 1, 'day')
```

end