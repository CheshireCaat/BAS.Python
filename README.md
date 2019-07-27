# BAS.Python
Python embedded implementation for Browser Automation Studio

## Answers to questions for the BAS developer
##### 1. Python
##### 2. 3.7.4
##### 3. Module search:

Use this url for getting package information:
```
http://pypi.python.org/pypi/<package_name>/json
```

Use this url for getting package information for specific release:
```
http://pypi.python.org/pypi/<package_name>/<version>/json
```

##### 4. Method by which you can add functions:
```
Create file '/distr/src/custom/<function-name>.py' contents of which
identical to the function code.
```

##### 6. The sequence of actions for installing modules:
```
Run '/distr/python.exe -m pip install <package-name>'
```

##### 7. The sequence of actions necessary to start the process in which operates built-in language:
```
Run '/distr/python.exe /distr/src/main.py'
```