test_dict={'codingal':2,'is': 2,'best':2,'for':2,'coding':1}
print("the orginal dictionary:"+str(test_dict))
k=2
res=0
for key in test_dict:
    if test_dict[key]:
        res=res+1
print("frequency of k is:"+str(test_dict))