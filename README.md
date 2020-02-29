# commons
easy, common stuff

#### 1. How to install third party modules in Python
1. create text file requirements.txt
2. File should have the module names and versions as key value pairs, example:
    ```
    delorean==1.0.0
    requests==2.18.4
    ```
3. Then run 
    ```pip install -r requirements.txt```
4. pip searches for the modules and the respecive version at pypi.org and will install them
5. To view all modules+dependencies, run 
    ```pip -freeze > requirements.txt```
    
#### 2. String Fomratting in Python
Format spec language from the docs:
format_spec ::=  [[fill]align][sign][#][0][width][,][.precision][type]
fill        ::=  <any character>
align       ::=  "<" | ">" | "=" | "^"
sign        ::=  "+" | "-" | " "
width       ::=  integer
precision   ::=  integer
type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
    
remember:
1. fill is needed only if there is an alignment
```
print("{:*20,}".format(5000000))   # ValueError: Invalid format specifier
print("{:*>20,}".format(5000000))  # added right alignment
***********5,000,000
```
2. sign (if any) comes after align and before width
```
print("{:*>+20,}".format(5000000))
**********+5,000,000
```

3. alignment without specifying width doesnt have any impact
```
print("{:*>+,}".format(5000000))        # no width, right align
+5,000,000
print("{:*>+20,}".format(5000000))      # width=20, rihgt align
**********+5,000,000
```

4. , is for seperator in numeric values
```print("{}".format(5000000))
5000000
print("{:,}".format(5000000))
5,000,000
```

5. .precision is number of digits before decimal point + number of digits after the decimal
```
print("{:}".format(22/7))       # no precision is set
3.142857142857143

print("{:.3}".format(22/7))    # precision set
3.14
```


6. type can be used for conversion to types like binary, hex, octal, etc. the type % calculates percentage
```
print("{:b}".format(10))
1010
print("{:X}".format(10))
A
print("{:x}".format(10))
a
```




