def getMonthName(monthCode):
    monthNames = ['January','February','March','April','May','June','July','August','September','October','November','December']
    return monthNames[monthCode]

def printHeadline(month,year):
    monthName = getMonthName(month-1)
    nSpaces = 19 - len(monthName) - len(str(year))
    spaces = ''
    for i in range(nSpaces):
        spaces = spaces + ' '
    line = '  '+ monthName + spaces + str(year)
    print(line)
    
def printWeekdays():
    print('  M  T  W  T  F  S  D')
    print('----------------------')

def getDayStr(day):
    return str(day)+' ' if (day>=10) else ' '+str(day)+' '

def printLine(init,end,pad):
    line = ' '
    for i in range(pad):
        line = line + '   '
    for i in range(init,end+1):
        line = line + getDayStr(i)
    print(line)

def printMonth(year,month,diffFromMonday,daysInMonth):
    print('')
    printHeadline(month,year)
    printWeekdays()
    dayInit = 1
    dayEnd = dayInit + 6 - diffFromMonday
    while (dayInit <= daysInMonth):
        printLine(dayInit,dayEnd,diffFromMonday)
        dayInit = dayEnd + 1
        dayEnd = dayInit + 6 if (dayInit + 6)<daysInMonth else daysInMonth
        diffFromMonday = 0
    