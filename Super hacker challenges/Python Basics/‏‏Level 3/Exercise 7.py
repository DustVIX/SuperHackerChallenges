#  Write a function that removes duplicates from a list.

str_list = ["ddd","ddd","ddd","ff"] 

def removes_duplicates(a_list):
    print("The Original List: ", a_list)
    unique_list = []
    for i in a_list:
        if i not in unique_list: 
            unique_list.append(i)  
    print("The List After Removing Duplicates: ", unique_list)



removes_duplicates(str_list)