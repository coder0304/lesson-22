import array as arr
array_num=arr.array('i',[1,3,5,3,7,9,3])
print("og array: ",str(array_num))
print("number of occurences of the nos 3 in the said array:"+str(array_num.count(3)))

array_num.reverse()
print("Reverse the order of the item:")
print(str(array_num))