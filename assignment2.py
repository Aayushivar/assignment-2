SET -> unorderd collection of data type , {}

books={"statistics","mathematics","pyhsics","chemistry","biology"}
print(books)
print(len(books))
{'chemistry', 'pyhsics', 'biology', 'mathematics', 'statistics'}
5

books.add("economics")
print(books)
{'chemistry', 'pyhsics', 'biology', 'mathematics', 'economics', 'statistics'}

books.remove("biology")
print(books)
{'chemistry', 'pyhsics', 'mathematics', 'economics', 'statistics'}

dataset1={'45','55','65','85','89'}
dataset2={'40','45','85','75','65'}
dataset3=dataset1|(dataset2)
print(dataset3)
{'40', '85', '45', '65', '75', '89', '55'}

dataset1={'45','55','65','85','89'}
dataset2={'40','45','85','75','65'}
dataset3=dataset1&(dataset2)
print(dataset3)
{'45', '65', '85'}

dataset1.clear()
print(dataset1)
set()

student1= 400
student2= 485
print((student1)>=(student2))
print((student1)<=(student2))
print((student1)==(student2))
print((student1)!=(student2))
False
True
False
True

frozen set<-
data=frozenset(["aayushi","rishab"])
print(data)
frozenset({'aayushi', 'rishab'})
data.add("add")
print(data)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Input In [18], in <cell line: 1>()
----> 1 data.add("add")
      2 print(data)

AttributeError: 'frozenset' object has no attribute 'add'

​
