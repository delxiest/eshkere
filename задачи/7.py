x=int(input())
dell=0
for i in range(2,x):
    if x%i==0:
        dell+=1
if dell==0:
    print('простое')
else:
    print('не простое')
