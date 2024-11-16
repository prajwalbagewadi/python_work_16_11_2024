# single line comment
"""
this is
a
multi line comment
"""
x=10 # global variable

def my_fun():
    y=200 # local variable
    print(y) # view local var
    print(x) # view global var

print(x) # view global var
my_fun() # view local var