PASCUALyes = input("TYPE YOUR NAME: ") .title()
PASCUALno = input("TYPE YOUR JOB POSITION = JANITOR, CLERK, CASHIER OR MANAGER: ") .title()
PASCUALmaybe = int(input("TYPE HOURS WORKED: "))

match pascualpos:
    case "janitor":
        pascualmnth = 18000
    case "clerk":
        pascualmnth = 22000
    case "cashier":
        pascualmnth = 24000
    case "manager":
        pascualmtnh = 40000
    case _:
        pascualmtnh = 0

 if pascualmtnh > 0:
     pascualbasic = pascualmnth / 2
     pascualhourly = pascualmnth /88
     if pascualhours < 88:
         pascualabsent = 88 - pascualhours
         pascualabsdeduc = pascualabsent * pascualhourly
         pascualovertime = 0
         pascualovertimepay = 0
     else:
         pascualabsent = 0
         pascualabsdeduc = 0
         pascualovertime = pascualhours - 88
         pascualovertimerate = pascualhourly * 1.25
         pascualotp = pascualovertime * pascualovertimerate

     pascualnet = pascualbasic - pascualabsdeduc + pascualovertimepay
     print("EMPLOYEE NAME: " ,PASCUALyes)
     print("JOB POSITION: " ,PASCUALno)
     print("JOB  HOURS: " ,PASCUALmaybe)
     print("MONTHLY PAY: " ,pascualmtnh)
     print("BHMS: " ,pascualbasic)
     print("MONTHLY SALARY: " ,round(pascualhourly, 2))
     print("ABSENT HOURS: " ,pascualabsent)
     print("ABSENT DEDUCTION: " ,round(pascualabsdeduc, 2))
     print("OVERTIME HOURS: " ,pascualovertime)
     print("OVERTIME PAY: " ,round(pascualovertimepay, 2))
     print("HALF MONTH SALARY: " ,round(pascualnet, 2))
else:
    print("INVALID CHOICE!")
