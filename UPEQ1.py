'''
Write a python code to remove tuples from list of tuples if greater than n. Given a list of a
tuple, the task is to remove all the tuples from list, if it’s greater than n (say 100).
'''
tuple = [('a', 100), ('b', 200), ('c', 45),('d', 876), ('e', 75)]
  
print("given_list", str(tuple))

result = [i for i in tuple if i[1] <= 100]

print ("Filtered tuple list: ", str(result))