from pywinauto import Desktop, Application

Tzatziki = Application().start('Calc.exe ')

TzatzikiTzatziki = Desktop(backend = "uia").Calculator

a = 155

while ( True) :
    b = str(a)
    print (b)
    a = a - 1
    TzatzikiTzatziki.type_keys(b)
    
    if (a <=0) :
        TzatzikiTzatziki.type_keys('=')
        break
    else:
        TzatzikiTzatziki.type_keys('*')

print ("Hey!!")
