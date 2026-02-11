n=int(input('enter no of marks:'))
marks=[0]*n
for i in range(n):
    marks[i]=int(input('enter mark:'))
print(marks)
name=input('enter name:')
if len(name)%2 != 0:
    for i in range(len(marks)):
        if(marks[i]+2 > 100):
            marks[i]=100
        else:
         marks[i]=marks[i] + 2
else:
    for i in range(len(marks)):
        if marks[i] - 2 <0:
            marks[i]=0
        else:
            marks[i]=marks[i] - 2
print("marks has been updated due to personalisation")
print(marks)
count=0
failed_count=0
for i in range(len(marks)):
    if marks[i]>=90 and marks[i]<=100:
        print(marks[i],"-> Excellent")
        count=count+1
    elif marks[i]>=75 and marks[i]<=89:
        print(marks[i],"-> Very Good")
        count = count + 1
    elif marks[i]>=60 and marks[i]<=74:
        print(marks[i],"-> Good")
        count = count + 1
    elif marks[i]>=40 and marks[i]<=59:
        print(marks[i],"-> Average")
        count = count + 1
    elif marks[i]>=0 and marks[i]<=39:
        print(marks[i],"-> Fail")
        count = count + 1
        failed_count = failed_count + 1
    else:
        print(marks[i],"-> Invalid")
print('Total valid students:',count)
print('Total failed students:',failed_count)




