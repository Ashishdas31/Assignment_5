#Ans. 2  
Dict={"foo":42}
print(Dict["foo"])

""""#Ans. 4.
spam = {'bar': 100}
print(spam["foo"])"""

spam = {'bar': 100}
spam.setdefault('color', 'black')
print(spam)  # output: {'bar': 100, 'color': 'black'}
