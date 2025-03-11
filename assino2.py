"""
Create an empty list called my_list.
Append the following elements to my_list: 10, 20, 30, 40.
Insert the value 15 at the second position in the list.
Extend my_list with another list: [50, 60, 70].
Remove the last element from my_list.
Sort my_list in ascending order.
Find and print the index of the value 30 in my_list.

"""
#empty list
my_list=[]
my_list.extend([10,20,30,40])#appended values
#print(my_list)
my_list.insert(1,15)
#print(my_list)
thisList=[50,60,70]
#extend my_list
my_list.extend(thisList)
#print(my_list)
my_list.remove(70)
#print(my_list)
my_list.sort()
#print(my_list)
print(my_list.index(30))#index of 30

