import calendarModule as calendar

def isValidDay(year,month,day):
    dayArr = list(day)
    # must be two digit 
    if len(dayArr) != 2:
        return False
    # check that all characters are numbers
    for n in dayArr:
        if n<'0' or n>'9':
            return False
    # parse as int and check if matches the expected number of days for such month and year
    dayInt = int(day)
    if dayInt < 1 or dayInt>calendar.daysInMonth(month,year):
        return False
    return True

def isValidMonth(month):
    monthArr = list(month)
    # must be two digit 
    if len(monthArr) != 2:
        return False
    # check that all characters are numbers
    for n in monthArr:
        if n<'0' or n>'9':
            return False
    # parse as int and check if it is <1 or >12
    monthInt = int(month)
    if monthInt<1 or monthInt>12:
        return False
    return True

def isValidYear(year):
    yearArr = list(year)
    # must be four digit 
    if len(yearArr) != 4:
        return False
    # check that all characters are numbers
    for n in yearArr:
        if n<'0' or n>'9':
            return False
    # parse as int and check if it is <1900
    yearInt = int(year)
    if yearInt<1900:
        return False
    return True

def isValidDateInput(dateInput,items):
    dateInputArr = dateInput.split('/')
    #print(f'dateInputArr: {dateInputArr}')
    if len(dateInputArr) != items:
        return False
    if not isValidYear(dateInputArr[0]):
        return False
    if items >=2:
        if not isValidMonth(dateInputArr[1]):
            return False
    if items >=3:
        # year and month are checked at this point so we can int() them
        if not isValidDay(int(dateInputArr[0]),int(dateInputArr[1]),dateInputArr[2]):
            return False
    return True