n, p, h = input("TYPE YOUR NAME: ").title(), input("TYPE YOUR JOB POSITION = JANITOR, CLERK, CASHIER OR MANAGER: ").title(), int(input("TYPE HOURS WORKED: "))
m = {"Janitor": 18000, "Clerk": 22000, "Cashier": 24000, "Manager": 40000}.get(p, 0)
b, hr = m / 2, m / 88 if m else 0
ad, op = max(0, 88 - h) * hr, max(0, h - 88) * hr * 1.25
net = b - ad + op
print("INVALID CHOICE!" if not m else f"\n" + "="*30 + f"\nEMPLOYEE NAME: {n}\nJOB POSITION: {p}\nJOB HOURS: {h}\nMONTHLY PAY: {m}\nBHMS: {b}\nHOURLY RATE: {hr:.2f}\nABSENT HOURS: {max(0, 88-h)}\nABSENT DEDUCTION: {ad:.2f}\nOVERTIME HOURS: {max(0, h-88)}\nOVERTIME PAY: {op:.2f}\nHALF MONTH SALARY: {net:.2f}")