months = ["JAN, FEB, MAR, APR, MAY. JUN, JULY, AUG, SEP, OCT, NOV,DEC"]
days = ["MON, TUE, WED, THU, FRI, SAT, SUN"]

for x in months:
    print(x)
for b in days:
    print(b)

ML = [("SUPERVISED", "DECISION TREE"),
      ("SUPERVISED", "RANDOM FOREST"),
      ("UNSUPERVISED", "K-MEANS"),
      ("UNSUPERVISED", "GAWSSIAN MIXTURE ,MODEL")
      ]
print("Learning Type: ", ML[0][0])
for item in ML:
    if item[0] == "SUPERVISED":
        print(item[1])
print("LEARNING TYPE:", ML[2][0])
for y in ML:
    if  y[0] == "UNSUPERVISED":
        print(y[1])




