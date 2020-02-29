# commons
easy, common stuff

#### 1. How to install third party modules in Python
1. create text file requirements.txt
2. File should have the module names and versions as key value pairs, example:
    delorean==1.0.0
    requests==2.18.4
3. Then run 
    pip install -r requirements.txt
4. pip searches for the modules and the respecive version at pypi.org and will install them
5. To view all modules+dependencies, run 
    pip -freeze > requirements.txt



