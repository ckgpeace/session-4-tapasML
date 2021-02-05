import math
import time

# dictionary of <named parameter> : < function name>
kwargs_map = {'sep' : ['print'],
              'start' : ['squared_power_list'],
              'end' : ['squared_power_list','print'],
              'sides' : ['polygon_area'],
              'temp_given_in' : ['temp_converter'],
              'dist' : ['speed_converter'],
              'time' : ['speed_converter']
    }

# this function calls the argument function 'fn' multiple times.
# the function returns the tuple of :
#    (result of last execution of 'fn' function, # of repitition, and average time taken)

def time_it(fn, *args, repetitons= 1, **kwargs):
    _result = None
    if not args:
        raise ValueError('positional parameter is missing')
    # validate repetitons
    if not isinstance(repetitons, int):
        raise ValueError('repetitons must be integer')
    if repetitons < 0:
        raise ValueError('repetitons must be >= 0')
    if(repetitons != int(repetitons)):
        raise ValueError('repetitons must be integer value')
    
    # validate keyword arguments    
    for key in kwargs:       
        if key not in kwargs_map.keys():
            raise ValueError(f'incorrect named argument {key}')        
        elif fn.__name__ not in kwargs_map[key] :            
            raise NameError(f'incorrect named argument {key} in function {fn.__name__}')    
    
    start = time.perf_counter()     
    for i in range(repetitons):                    
        _result = fn(*args, **kwargs)  # invoke the function for # of repitions
    end = time.perf_counter()
    timetaken = (end - start) / repetitons
    print(f' result and average time taken in {repetitons} invocation is:  {(_result, repetitons, timetaken)}')
    return (_result, repetitons, timetaken)

# calculates power on base and adds to list
def squared_power_list(*args, **kwargs):
    _result=[]
    _base=args[0]
    if (isinstance(_base, int) == False and isinstance(_base, float) == False):
        raise ValueError(f'base {_base} is not int or float')
    _start=kwargs['start']
    _end=kwargs['end']
    if not _start or not _end:
        raise ValueError(f'keyword parameter missing')
    if isinstance(_start, int) == False :
        raise ValueError(f'_start should be an integer')
    if isinstance(_end, int) == False :
        raise ValueError(f'_end should be an integer')
    if _start > _end:
        raise ValueError(f'start  must be <= end')
    for i in range(_start, _end + 1):
        _result.append(pow(_base,i))   
    #print(_result)
    return _result

# calculates area of polygon of equals side length
def polygon_area(*args, **kwargs):
    _side_len = args[0]
    _no_of_sides= kwargs['sides']
    if (isinstance(_side_len, int) == False and isinstance(_side_len, float) == False):
        raise ValueError(f'Side length {_side_len} is not int or float')
    if isinstance(_no_of_sides, int) == False :
        raise ValueError(f'number of sides {_no_of_sides} is not int or float')
        
    if _side_len <= 0:
        raise ValueError(f'side length {_side_len} is not > 0')
    if _no_of_sides < 3:
        raise ValueError(f'no of sides {_no_of_sides} is not >= 3')
    
    
    _perimeter = _side_len * _no_of_sides   
    _apothem = _side_len/ (2 * math.tan(math.pi/_no_of_sides))    
    _area = (_perimeter * _apothem)/2    
    #print('area= ', _area)
    return _area

# convers C to F and vice versa
def temp_converter(*args, **kwargs):
    _base_temp = args[0]
    _unit = kwargs['temp_given_in']
    
    if (isinstance(_base_temp, int) == False and isinstance(_base_temp, float) == False):
        raise ValueError(f'args[0] {_base_temp} is not int or float')
    if _unit not in ('f','F', 'c','C'):
        raise ValueError(f' {_unit} is not valid unit')
    
    if _unit in ('f','F'): # F to C
        _result = 5/9 *(_base_temp - 32)
        
    elif  _unit in ('c','C'): # C to F
        _result = 32 + (9/5 * _base_temp)
     
    #print(_result)
    return _result

# converts /kmph to unit asked for
def speed_converter(*args, **kwargs):    
    if not 'dist' in kwargs.keys():
        raise ValueError(f' named parameter dist is missing')   
    if not 'time' in kwargs.keys():
        raise ValueError(f' named parameter time is missing')
    _kmph = args[0]
    _dist = kwargs.get('dist')
    _time = kwargs.get('time')
    if _kmph < 0:
        raise ValueError(f'speed can not be negative')
    
    
    # distionary for dist_unit : factor of km
    _dist_map = {'km' : 1,
                 'm' : 1000,
                 'ft': 3280.84,
                 'yrd' : 1093.61 }
    
    # distionary for time_unit : factor of hour
    _time_map = {'hr' : 1,
                 'min' : 60,
                 'day' : 1/24,
                 's' : 60,
                 'ms' : 60000,
                 }
    _result = _kmph * _dist_map[_dist] / _time_map[_time]
    #print(_result)
    return _result

#time_it(print, 1, 2, 3, 'hello', sep='-', end= ' ***\n', repetitons=2)
#time_it(squared_power_list, 2, start=3, end=4, repetitons=2) 
#time_it(polygon_area, 15, sides = 6, repetitons=2) 
#time_it(temp_converter, -200.23, temp_given_in = 'C', repetitons=1)
#time_it(speed_converter, 100, dist='km', time='min', repetitons=100) 
#time_it(squared_power_list, 2, start=3, end=4, repetitons=5)
#time_it(temp_converter, -200.23, temp_given_in = 'C')
#time_it(speed_converter, 200, dist='m', time='day', repetitons=100)
#time_it(speed_converter, 200, dist='m')

    
