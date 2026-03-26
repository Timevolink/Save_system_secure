from Save import *

my_data = "level:1;niveau:1"
data = Save(my_data)
data.save()
print(data.load())