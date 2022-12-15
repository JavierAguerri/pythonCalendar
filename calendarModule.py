import calendarDateValidation as dateValidation

def exit():
    print('Exit the program.')
    
def lapYear(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 500 == 0):
                return True
            return False
        return True
    return False
    
def daysInYear(year):
    if lapYear(year):
        return 366
    else:
        return 365
    
def daysInMonth(month,year):
    shortMonths = [4,6,9,11]
    if month == 2:
        days = 28
        if lapYear(year):
            days = 29
    elif month in shortMonths:
        days = 30
    else: 
        days = 31
    return days
    
def cummulativeDaysMonth(month,year):
    totalDays = 0
    # from i=0 to month
    for i in range(month):
        totalDays = totalDays + daysInMonth(i+1,year)
    return totalDays

def cummulativeDaysYear(year):
    totalDays = 0
    for i in range(1900,year+1):
        totalDays = totalDays + cummulativeDaysMonth(12,i)
    return totalDays

def getDiffFromMonday(year,month,day):
    totalDaysfromEpoch = cummulativeDaysYear(year-1) + cummulativeDaysMonth(month-1,year) + day-1
    return totalDaysfromEpoch % 7

def getWeekdayName(dayCode):
    dayNames = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    return dayNames[dayCode]

def weekday():
    print('Print the week day for a certain date.')
    dateInput = input('Input the date. Use format: YYYY/MM/DD: ')
    while not dateValidation.isValidDateInput(dateInput):
        print ('Invalid entry. Please input a valid date from 1900/01/01 onwards.')
        dateInput = input('Input the date. Use format: YYYY/MM/DD: ')
    # get day, month, year variables as int from the input string
    dateInputArr = dateInput.split('/')
    year = int(dateInputArr[0])
    month = int(dateInputArr[1])
    day = int(dateInputArr[2])
    diffFromMonday = getDiffFromMonday(year,month,day)
    weekdayName = getWeekdayName(diffFromMonday)
    print(f'On date {dateInput} it was (or it will be) {weekdayName} ')
    
def monthly():
    print('Print the monthly calendar for a certain year.')

def yearly():
    print('Print the yearly calendar for a certain year.')  
    
functionsList = [yearly,monthly,weekday,exit]