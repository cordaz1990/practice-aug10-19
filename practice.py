#Looping Dictionaries 

def print_hist(h):
    for c in h:
        print(c, h[c])
        
       
>>> h = histogram('parrot')
>>> print_hist(h)
a 1
p 1
r 2
t 1
o 1

for key in sorted(h):
    print(key, h[key])
    
a 1
o 1
p 1
r 2
t 1 
