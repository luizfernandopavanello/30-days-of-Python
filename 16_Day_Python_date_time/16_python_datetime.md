<div align="center">
  <h1> 30 Days Of Python: Day 16 - Python Data Time</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/fernandovicentinpavanello/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/nandovicentin">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/nandovicentin?style=social">
  </a>

  <sub>Author:
  <a href="https://www.linkedin.com/in/fernandovicentinpavanello/" target="_blank">Fernando Vicentin Pavanello</a><br>
  <small> First Edition: March, 2022</small>
  </sub>
</div>

[<< Day 15](../15_Day_Python_type_errors/15_python_type_errors.md) | [Day 17 >>](../17_Day_Exception_handling/17_exception_handling.md)

<img src="../Images/python_TreviIT.png" alt="30 Days of Python">
</div>

- [📘 Day 16](#-day-16)
  - [Python *datetime*](#python-datetime)
    - [Getting *datetime* Information](#getting-datetime-information)
    - [Formatting Date Output Using *strftime*](#formatting-date-output-using-strftime)
    - [String to Time Using *strptime*](#string-to-time-using-strptime)
    - [Using *date* from *datetime*](#using-date-from-datetime)
    - [Time Objects to Represent Time](#time-objects-to-represent-time)
    - [Difference Between Two Points in Time Using](#difference-between-two-points-in-time-using)
    - [Difference Between Two Points in Time Using *timedelata*](#difference-between-two-points-in-time-using-timedelata)

# 📘 Day 16

## Python *datetime*

Python has got _datetime_ module to handle date and time.

```py
import datetime
print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
```

With dir or help built-in commands it is possible to know the available functions in a certain module. As you can see, in the datetime module there are many functions, but we will focus on _date_, _datetime_, _time_ and _timedelta_. Let se see them one by one.

### Getting *datetime* Information

```py
from datetime import datetime
now = datetime.now()
print(now)                      # 2022-03-27 10:03:34.094907
day = now.day                   # 27
month = now.month               # 3
year = now.year                 # 2022
hour = now.hour                 # 10
minute = now.minute             # 3
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}') # 27/3/2022 10:03
```

Timestamp or Unix timestamp is the number of seconds elapsed from 1st of January 1970 UTC.

### Formatting Date Output Using *strftime*

```py
from datetime import datetime
new_year = datetime(2021, 1, 1)
print(new_year)     # 2021-01-01 00:00:00
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute) # 1 1 2021 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}') # 1/1/2021, 0:0
```

Formatting date time using *strftime* method and the documentation can be found [here](https://strftime.org/).

```py
from datetime import datetime
# current date and time 
now = datetime.now()
t = now.strftime('%H:%M:%S')
print('time:', t)
time_one = now.strftime('%m/%d/%Y, %H:%M:%S')
# mm/dd/YY H:M:S format
print('time one:', time_one)
time_two = now.strftime('%d/%m/%Y, %H:%M:%S')
# dd/mm/YY H:M:S format
print("time two:", time_two)
```

```sh
time: 10:23:02
time one: 03/27/2022, 10:23:02
time two: 27/03/2022, 10:23:02
```

### String to Time Using *strptime*

Here is a [documentation](https://www.programiz.com/python-programming/datetime/strptimet) hat helps to understand the format. 

```py
from datetime import datetime
date_string = "23 March, 2022"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
```

```sh
date_string = 23 March, 2022
date_object = 2022-03-23 00:00:00
```

### Using *date* from *datetime*

```py
from datetime import date
d = date(2022, 1, 1)
print(d)
print('Current date:', d.today())    # 2022-27-03
# date object of today's date
today = date.today()
print("Current year:", today.year)   # 2022
print("Current month:", today.month) # 3
print("Current day:", today.day)     # 27
```

### Time Objects to Represent Time

```py
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)
```

output  
a = 00:00:00  
b = 10:30:50  
c = 10:30:50  
d = 10:30:50.200555

### Difference Between Two Points in Time Using

```py
today = date(year=2022, month=3, day=27)
new_year = date(year=2023, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear) # Time left for new year:  280 days, 0:00:00

t1 = datetime(year = 2022, month = 3, day = 27, hour = 10, minute = 30, second = 0)
t2 = datetime(year = 2023, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 279 days, 13:30:00
```

### Difference Between Two Points in Time Using *timedelata*

```py
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
```

```sh
    t3 = 86 days, 22:56:50
```

[<< Day 15](../15_Day_Python_type_errors/15_python_type_errors.md) | [Day 17 >>](../17_Day_Exception_handling/17_exception_handling.md)