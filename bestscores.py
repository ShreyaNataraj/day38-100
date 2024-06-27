#BruteForceApproch
def first_second(mylist):
    mylist1 =max(mylist)
    print(mylist1)
    mylist.remove(mylist1)
    return max(mylist)
mylist = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
print(first_second(mylist))
#optimal solution
def first_second(mylist):
  num1,num2 =float('-inf'), float('-inf')
  for num in mylist:
    if num>num1:
      num2 =num1
      num1 =num
    elif num>num2 and num!=num1:
      num2 = num
  return num1,num2
mylist = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
print(first_second(mylist))      
      