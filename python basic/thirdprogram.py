student=["Ibad",92,"A"];   #  list in python
print(student[0]);  # accessing Array index

print(student[0:2]);   # slicing same as string
student[1]= 95;   # list is mutable; however, the string is immutable.
print(student);  


# method for list

list=[1,2,3,4];

list.append(3.4);   # add element at the end of the string.
print(list);        
list.sort();        # print list in the ascending order.
print(list);

list.sort(reverse=True); # sort list in descending order.
print(list);


list.insert(2,6);  # list(idx, element) add element at any index
print(list)