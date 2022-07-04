title: Creating a Flask App
subtitle: Blogging the Easy Way
author: Philip Mannering
date: 2021-11-22
tags: [flask, python]




# Flask
Create a new Flask app in a new file called `app.py`.


```
from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "Hello World!"
if __name__ == "__main__":
    app.run(debug=True)
```

You can run the app by running `python app.py` from the command line.

```python
for i in range(10):
    print(i)
```

And PowerShell...
```powershell
mkdir new_folder
cd new_folder
```

# Table

| Header 1 | Header 2 | Header 3 |
| -------- | -------- | -------- |
| Cell 1   | Cell 2   | Cell 3   |
| Cell 1   | Cell 2   | Cell 3   |

