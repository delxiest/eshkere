x=int(input())
if x>1000:
    sk=0.1
elif x>500:
    sk=0.05
else:
    sk=0
itog=x-(x*sk)
print(itog)
