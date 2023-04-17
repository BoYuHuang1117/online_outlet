- [Create a virtual environment]

```Powershell
python -m venv env
.\env\Scripts\activate
```

```bash
python3.10 -m venv env
source env/bin/activate
```

Update pip install and install
```Powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

```bash
pip3 install -r requirements.txt
```

- [Start a BE development environment on port 8000]

```Powershell
py manage.py runserver
```

```bash
python3 manage.py runserver
```
