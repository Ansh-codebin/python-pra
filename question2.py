


studentattendance= int(input("enter your attendace"))
totalclass=int(input("totalclass"))
requires=(studentattendance/totalclass)*100
if requires > 75:
    print("ok for exam")
    print(requires)
