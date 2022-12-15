import calendarModule as calendar
import calendarDateValidation as dateValidation

def daysInYear(year,expected):
    passed = True
    print(f'test for daysInYear - year: {year}')
    result = calendar.daysInYear(year)
    resultStr = ''
    if (result != expected):
        resultStr = '** NOT ** '
        passed = False
    print(f'Test {resultStr}successful: result is {result} vs expected {expected}')
    print('')
    return passed

def daysInMonth(year,month,expected):
    passed = True
    print(f'test for daysInMonth - year: {year}, month: {month}')
    result = calendar.daysInMonth(month,year)
    resultStr = ''
    if (result != expected):
        resultStr = '** NOT ** '
        passed = False
    print(f'Test {resultStr}successful: result is {result} vs expected {expected}')
    print('')
    return passed

def cummulativeDaysMonth(year,month,expected):
    passed = True
    print(f'test for cummulativeDaysMonth - year: {year}, month: {month}')
    result = calendar.cummulativeDaysMonth(month,year)
    resultStr = ''
    if (result != expected):
        resultStr = '** NOT ** '
        passed = False
    print(f'Test {resultStr}successful: result is {result} vs expected {expected}')
    print('')
    return passed
        
def cummulativeDaysYear(year,expected):
    passed = True
    print(f'test for cummulativeDaysYear - year: {year}')
    result = calendar.cummulativeDaysYear(year)
    resultStr = ''
    if (result != expected):
        resultStr = '** NOT ** '
        passed = False
    print(f'Test {resultStr}successful: result is {result} vs expected {expected}')
    print('')
    return passed
        
def getDiffFromMonday(year,month,day,expected):
    passed = True
    print(f'test for diffFromMonday - year: {year}, month: {month}, day: {day}')
    result = calendar.getDiffFromMonday(year,month,day)
    resultStr = ''
    if (result != expected):
        resultStr = '** NOT ** '
        passed = False
    print(f'Test {resultStr}successful: result is {result} vs expected {expected}')
    print('')
    return passed
      
def calendarTests():
    nTests = 0
    nPassed = 0
    # getDiffFromMonday
    tests =[
        [1900,1,1,0],
        [2022,12,12,0],
        [2023,1,1,6],
        [1904,1,1,4],
        [2022,12,15,3]
    ]
    for d in tests:
        nTests = nTests + 1
        if (getDiffFromMonday(d[0],d[1],d[2],d[3])):
            nPassed = nPassed + 1
    
    # cummulativeDaysYear
    tests = [
        [1900,365],
        [1901,365*2],
        [1902,365*3],
        [1903,365*4],
        [1904,365*5+1],
        [1905,365*6+1]
    ]
    for d in tests:
        nTests = nTests + 1
        if (cummulativeDaysYear(d[0],d[1])):
            nPassed = nPassed + 1
        
    # cummulativeDaysMonth
    tests = [
        [2020,2,60],
        [1900,2,59],
        [2000,2,60],
        [2022,12,365],
        [2020,12,366],
        [2020,1,31],
        [2022,6,181],
        [2003,0,0],
        [1904,12,366]
    ]
    for d in tests:
        nTests = nTests + 1
        if (cummulativeDaysMonth(d[0],d[1],d[2])):
            nPassed = nPassed + 1
    
    # daysInMonth
    tests = [
        [1900,2,28],
        [1901,2,28],
        [1902,2,28],
        [1903,2,28],
        [1904,2,29],
        [2000,2,29]
    ]
    for d in tests:
        nTests = nTests + 1
        if (daysInMonth(d[0],d[1],d[2])):
            nPassed = nPassed + 1
            
    # daysInYear 
    tests = [
        [1900,365],
        [1901,365],
        [1904,366],
        [2000,366],
        [2003,365],
        [2008,366]
    ]
    for d in tests:
        nTests = nTests + 1
        if (daysInYear(d[0],d[1])):
            nPassed = nPassed + 1
        
    # final count
    print(f'Number of tests executed: {nTests}')
    print(f'Number of tests passed: {nPassed}')
    
def isValidDateInput(date,expected):
    passed = True
    print(f'test for isValidDateInput - date: {date}')
    result = dateValidation.isValidDateInput(date)
    resultStr = ''
    if (result != expected):
        resultStr = '** NOT ** '
        passed = False
    print(f'Test {resultStr}successful: result is {result} vs expected {expected}')
    print('')
    return passed

def inputValidationDatesTests():
    nTests = 0
    nPassed = 0
    
    # isValidDateInput
    
    # negatives
    negTests = [
        '',
        '1020/02/03',
        '0000/10/10',
        '200/10/10',
        '23.5/10/10',
        '1899/10/10',
        '2000/02/30',
        '2000/04/31',
        '2000/10/33',
        '2000/13/02',
        '2000/00/02',
        '2000/05/0',
        '2000/3/2',
        '2000/05/',
        '2000//10',
        '2000//',
        '2000//12',
        '2000/-3/12',
        '2000/ad/10',
        '21,0/ad/10',
        '1900/02/29'     
    ]    
    
    for d in negTests:
        nTests = nTests + 1
        if isValidDateInput(d,False):
            nPassed = nPassed + 1           
    
    # positives
    posTests = [
        '1900/01/01',
        '2000/02/29',
        '5202/11/29',
        '1900/02/28',
        '9999/12/31'
    ]
    
    for d in posTests:
        nTests = nTests + 1
        if isValidDateInput(d,True):
            nPassed = nPassed + 1
            
    # final count
    print(f'Number of tests executed: {nTests}')
    print(f'Number of tests passed: {nPassed}')