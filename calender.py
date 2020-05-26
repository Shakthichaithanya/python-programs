def monthcode(x):
   s={ "jan": 1,
    "feb":4,
    "mar":4,
    "apr":0,
    "may":2,
    "jun":5,
    "jul":0,
    "aug":3,
    "sep":6,
    "oct":1,
    "nov":4,
    "dec":6}
   return s.get(x,"nothing")
def centurycode(x):
    s={
        "16":6,
        "17":4,
        "18":2,
        "19":0,
        "20":6,
        "21":4,
        "22":2,
        "23":0
        }
    return s.get(x,"nothing")
def daycode(n):
    s={
        1:"sunday",
        2:"monday",
        3:"tuesday",
        4:"wednesday",
        5:"thursday",
        6:"friday",
        0:"saturday"
        }
    return s.get(n,"nothing")
for i in range(0,7):
   a=input("Enter the day-month-year in this format: ")
   l=a.split('-')
   d=l[0]
   m=l[1]
   y=l[2]
   o=str(y)
   c=monthcode(m)
   f=centurycode(o[0:2])
   m=int(y[2:])//4
   result=int(d)+int(c)+int(f)+int(y[2:])+m
   r=result%7
   k=daycode(r)
   print(k)
