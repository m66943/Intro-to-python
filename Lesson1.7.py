# Read an integer:
# a = int(input())
# Print a value:
# print(a)
h1=int(input())
m1=int(input())
s1=int(input())
h2=int(input())
m2=int(input())
s2=int(input())
t1=(h1*3600 + m1*60 +s1)
t2=(h2*3600 + m2*60 +s2)
dif=t2-t1
print(dif)
