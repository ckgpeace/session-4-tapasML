import pytest
import random
import string
import os
import inspect
import re
import math
import session_4
from session_4 import *


#Happy path
def test_print1():
    result = time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitons=2)
    assert result[2] > 0, 'should return timings value'

def test_print2():
    result = time_it(print, 1, 2, 3, ('a','b''c'), sep='-', end= ' ***\n', repetitons=2)
    assert result[1] == 2, 'should return timings value'
    
def test_print_3():
    with pytest.raises(ValueError):
        time_it(print, 1, 2, 3, 'hello', separator='-', end= ' ***\n', repetitons=2)
    
def test_print_4():
    with pytest.raises(NameError):
        time_it(printFunc, 1, 2, 3, 'hello', sep='-', end= ' ***\n', repetitons=2)  

def test_print_5():
    with pytest.raises(ValueError):
        time_it(print, 1, 2, 3, 'hello', myparam=100, sep='-', end= ' ***\n', repetitons=2)             



########################################

# happy path: no error
def test_squared_power_list_happypath():
    result =  time_it(squared_power_list, 2, start=3, end=4, repetitons=1)
    assert result[2] > 0, 'should return timings value'

# invoke 5 times: no error
def test_squared_power_list_5_repitition():
    result = time_it(squared_power_list, 2, start=3, end=4, repetitons=5)
    assert result[0] == [8,16], 'incorrect value returned'
    assert result[1] == 5, 'incorrect value returned'

# incorrect keyword parameter
def test_squared_power_list_3():
    with pytest.raises(ValueError):
        time_it(squared_power_list, 2, start=3, ending=4, repetitons=5)
    
def test_squared_power_list_4():
    with pytest.raises(ValueError):
        time_it(squared_power_list, '2.0', start=0, end=51, repetitons=5)
        
def test_squared_power_list_5():
    with pytest.raises(ValueError):
        time_it(squared_power_list, -3, start=0, end=2, repetitons=5)
        
########################################

def test_polygon_area_happypath():
    result = time_it(polygon_area, 15, sides = 6, repetitons=2) 
    assert int(result[0]) == 584, 'incorrect area value'

def test_polygon_area_2():
    with pytest.raises(ValueError):
        result = time_it(polygon_area, 10, sides = 2, repetitons=2) 

# side = -10    
def test_polygon_area_3():
    with pytest.raises(ValueError):
        result = time_it(polygon_area, -10, sides = 2, repetitons=2)   

# repetitons='2'
def test_polygon_area_4():
    with pytest.raises(ValueError):
        result = time_it(polygon_area, -10, sides = 2, repetitons='2') 
# param missing        
def test_polygon_area_5():
    with pytest.raises(ValueError):
        result = time_it(polygon_area, -10, repetitons='2')  

###################################################

def test_temp_converter_happypath():    
    result = time_it(temp_converter, 212, temp_given_in = 'F', repetitons=1)
    assert(result[0] == 100)
    
def test_temp_converter_happypath2():    
    result = time_it(temp_converter, -200.23, temp_given_in = 'C', repetitons=1)
    assert(int(result[0]) == -328)
 
# invalid parameter value for temp unit
def test_temp_converter_3(): 
    with pytest.raises(ValueError):
        result = time_it(temp_converter, 212, temp_given_in = 'K', repetitons=5)

# missing positional arg
def test_temp_converter_4(): 
    with pytest.raises(ValueError):
        result = time_it(temp_converter, temp_given_in = 'C', repetitons=5)
        
# default keyword arg not supplied
def test_temp_converter_5():     
     result = time_it(temp_converter, -200.23, temp_given_in = 'C')
     assert(int(result[1]) == 1)

####################################################

def test_speed_converter_happypath():
    result = time_it(speed_converter, 100, dist='km', time='min', repetitons=100) 
    assert(round(result[0], 2) == 1.67), 'incorrect result'
    
def test_speed_converter_happypath2():
    result = time_it(speed_converter, 200, dist='m', time='day', repetitons=100)
    assert(round(result[0], 2) == 4800000), 'incorrect result'

# default keyword arg not supplied
def test_speed_converter_happypath3():
    result = time_it(speed_converter, 200, dist='m', time='day')
    assert(round(result[0], 2) == 4800000), 'incorrect result'

# negative speed
def test_speed_converter_error4():
    with pytest.raises(ValueError):
        result = time_it(speed_converter, -200, dist='m', time='day')

def test_speed_converter_error5():
    with pytest.raises(ValueError):
        result = time_it(speed_converter, 200, dist='m')