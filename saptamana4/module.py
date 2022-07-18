# from test import test_function
# from test import *
# import test


var_1 = 10
var_2 = 20
var_3 = 30
#
# result_modul = test_function(var_1, var_2, var_3)
# print(result_modul)

import sys, os
print(sys,os)
BASE = os.path.dirname((os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,BASE)

print(sys.path)

from saptamana3.functii import test_function
result_modul = test_function(var_1, var_2, var_3)
print(result_modul)