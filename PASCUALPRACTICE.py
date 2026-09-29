while True:
    pascual_yes = input("TYPE YOUR NAME: ").title()
    pascual_no = input("TYPE YOUR JOB POSITION = JANITOR, CLERK, CASHIER OR MANAGER: ").title()
    pascual_maybe = int(input("TYPE HOURS WORKED: "))

    match pascual_no:
        case "Janitor":
            pascual_mnth = 18000
        case "Clerk":
            pascual_mnth = 22000
        case "Cashier":
            pascual_mnth = 24000
        case "Manager":
            pascual_mnth = 40000
        case _:
            pascual_mnth = 0

    if pascual_mnth > 0:
        pascual_basic = pascual_mnth / 2
        pascual_hourly = pascual_mnth / 88

        if pascual_maybe < 88:
            pascual_absent = 88 - pascual_maybe
            pascual_absdeduc = pascual_absent * pascual_hourly
            pascual_overtime = 0
            pascual_overtimepay = 0
        else:
            pascual_absent = 0
            pascual_absdeduc = 0
            pascual_overtime = pascual_maybe - 88
            pascual_overtimerate = pascual_hourly * 1.25
            pascual_overtimepay = pascual_overtime * pascual_overtimerate

        pascual_net = pascual_basic - pascual_absdeduc + pascual_overtimepay

        print("\n" + "=" * 30)
        print("EMPLOYEE NAME:", pascual_yes)
        print("JOB POSITION:", pascual_no)
        print("JOB HOURS:", pascual_maybe)
        print("MONTHLY PAY:", pascual_mnth)
        print("BHMS:", pascual_basic)
        print("HOURLY RATE:", round(pascual_hourly, 2))
        print("ABSENT HOURS:", pascual_absent)
        print("ABSENT DEDUCTION:", round(pascual_absdeduc, 2))
        print("OVERTIME HOURS:", pascual_overtime)
        print("OVERTIME PAY:", round(pascual_overtimepay, 2))
        print("HALF MONTH SALARY:", round(pascual_net, 2))
    else:
        print("INVALID CHOICE!")




    again = input("\nDO WISH TO TRY AGAIN? (YES/NO)?")
    if again.upper() != "YES":
        print("THANK YOU FOR YOUR TIME!")
        break