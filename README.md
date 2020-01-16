# BAS.Python

Python embedded implementation for Browser Automation Studio (BAS)

## Documentation
##### 1. Language name: Python
##### 2. Language version: 3.8.1
##### 3. Module search:

Use this url for getting package information (latest stable release):
```
http://pypi.python.org/pypi/<project_name>/json
```
###### Example: http://pypi.python.org/pypi/pyuv/json

Use this url for getting package information (specific release):
```
http://pypi.python.org/pypi/<project_name>/<version>/json
```
###### Example: http://pypi.python.org/pypi/pyuv/1.4.0/json

##### 4. Method by which you can add functions:
```
Create file '/distr/src/custom/<function_name>.py' contents of which
identical to the function code.
```

###### Example:
```python
def get_sum(a, b):
    return a + b
```
##### 5. Method by which you can add files:
```
Create file '/distr/src/<file_name>.py' contents of which 
identical to the file code.
```

###### Example:
```python
def get_sum(a, b):
    return a + b
```
##### 6. The sequence of actions for installing modules:
```
Run '/distr/python.exe -m pip install <package-name>'
```

##### 7. The sequence of actions necessary to start the process in which operates built-in language:
```
Run '/distr/python.exe /distr/src/main.py'
```