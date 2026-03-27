from Save import *
from Load import *

my_data = "level:1;niveau:1"
recuperation = Load("save.dat")
recuperation.test_if_modified()