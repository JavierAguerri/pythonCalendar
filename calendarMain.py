import calendarModule as calendar
import calendarUnitTesting as calendarUT

def menuInput():
    print('Pick an option:')
    print('1. Yearly calendar')
    print('2. Monthly calendar')
    print('3. Which weekday is...?')
    print('4. Exit')
    print('')
    return input('Choose an option: ')

def isValidOptionInput(str):
    if str == "1":
        return True
    elif str == "2":
        return True
    elif str == "3":
        return True
    elif str == "4":
        return True
    else:
        return False

def menu():
    option = 0
    while not option==4:
        optionInput = menuInput()
        if (not isValidOptionInput(optionInput)):
            print ('Invalid entry. Please input a number from 1 to 4.')
            print('')
        else:
            option = int(optionInput)
            #print (f'option is of type {type(option)}')
            #print (f'You have chosen option {option}')
            calendar.functionsList[option-1]()
            print('')

menu()
#calendarUT.calendarTests()
#calendarUT.inputValidationDatesTests_n3()
#calendarUT.inputValidationDatesTests_n2()
#calendarUT.inputValidationDatesTests_n1()
