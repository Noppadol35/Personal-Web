#<---------------------------------------------------->
#discount with a filter (parameter)

# dis_rate = 5

# price = eval(input("Enter the price of the item: "))

# def calculate(price, dis_rate):
#     discount = price * dis_rate / 100
#     return discount

# if price > 0:
#     disc = calculate(price, dis_rate)
#     net = price - disc
#     print("Discount:{} \nNet:{}". format (disc,net))
# else:
#     print("Invalid price")
#<---------------------------------------------------->

#<---------------------------------------------------->
#Grading.py (not parameter)

# def youSC():
#     AmountSC = ComProMidSC + ComProFinalSC
#     return AmountSC

# ComProMidSC = eval(input('Enter Midterm score: '))
# ComProFinalSC = eval(input('Enter Final score: '))


# GPAcomPro = youSC()

# if GPAcomPro >= 80:
#     Grade = 'A'
# elif GPAcomPro >= 70:
#     Grade = 'B'
# elif GPAcomPro >= 60:
#     Grade = 'B'
# elif GPAcomPro >= 50:
#     Grade = 'B'
# else:
#     Grab = 'F'
    
# print('MID: {} Final: {} Total score: {} --> Grade: {}'. format(ComProMidSC, ComProFinalSC, GPAcomPro, Grade))
#<---------------------------------------------------->

#<---------------------------------------------------->
#Tuple.py

# students = ('Purm', 'new', 'max', 'view', 'ohm', 'friend', 'fluke')    #Tupleรายชื่อ

# for std in students[0:7]:       #ระบุช่วง
#     print(std)

# for std in students[:3]:        #ระบุช่วง
#     print(std)
    
# for std in students[4:7]:       #ระบุช่วง
#     print(std)

# for std in students[4:1]:       #ระบุช่วง(ไม่สามารถบอกช่วงอยู่น้อยกว่าได้) / ถ้ามีติดลบจะเป็นการนับจากหลังมาหน้า
#     print(std)

# for std in students[-7]:        #ระบุช่วง และ แสดงผลที่ละตัว F O O K 
#     print(std)
#<---------------------------------------------------->

#<---------------------------------------------------->
#ws; dict1

# dict1 = {}

# dict1['NP101'] = 'Mac'
# dict1['NP102'] = 'Iphone'
# dict1['NP103'] = 'Ipad'
# dict1['NP104'] = 'Airpods'
# dict1['NP105'] = 'applewatch'

# for key in dict1:
#     print(key,dict1[key])
#<---------------------------------------------------->

#<---------------------------------------------------->
#WS1:list given total element

mylist = []

total_element = eval(input('Enter number of products: '))

for i in range(total_element):
    grade = eval(input('value grade'+str(i)+":"))
    mylist.append(grade)

print(mylist)

if grade >= 80:
    Grade = 'A'
    all_grade_A = mylist.count(grade)
elif grade >= 70:
    Grade = 'B'
    all_grade_B = mylist.count(grade)
elif grade >= 60:
    Grade = 'C'
    all_grade_C = mylist.count(grade)
elif grade >= 50:
    Grade = 'D'
    all_grade_D = mylist.count(grade)
else:
    Grade = 'F'
    all_grade_F = mylist.count(grade)

amount = sum(mylist)
print('{}product(s)in Your cart. Total={}THB'. format(len(mylist),amount))
print('Grade: {} {} product(s)'. format(Grade,all_grade_A))
print('Grade: {} {} product(s)'. format(Grade,all_grade_B))
print('Grade: {} {} product(s)'. format(Grade,all_grade_C))
print('Grade: {} {} product(s)'. format(Grade,all_grade_D))
print('Grade: {} {} product(s)'. format(Grade,all_grade_F))

#<---------------------------------------------------->

#<---------------------------------------------------->
#list_Example.py

# score = [15,12,6,87,4]  #ประกาศสร้างlistพร้อมกำหนดข้อมูล
# score.append(17)           #เพิ่มข้อมูลเข้าlist    .append(metond)
# score.append(19)           #เพิ่มข้อมูลเข้าlist
# score.append(44)           #เพิ่มข้อมูลเข้าlist

# print(type(score))         #ข้อมูลในscore
# print(score)
#<---------------------------------------------------->

#<---------------------------------------------------->
#Tuple_workshop.py

# students = ('Purm', 'new', 'max', 'view', 'ohm', 'friend', 'fluke', 'Ice', 'Fairy')
# score = (30,25,21,28,26,30,25,21,21)

# total = sum(score)
# numStudent = len(score)
# avg = total/numStudent
# i = 0

# for z in students:         #วนรอบ ระบุช่วง
#     print('{} {:6} => {:5}'. format(i+0,z,score[i]))
#     i +=1

# print(type(students))
# print('Totla:{:8}'. format(total))
# print('Max Score:',max(score))
# print('Min Score:', min(score))
# print("Avg Score:{:6.2f}". format(avg))
#<---------------------------------------------------->

#<---------------------------------------------------->
#teach.py

# for i in range(5,1,2):
#     print(i)    #none value
    
# for i in range(5,1,-1):
#     print(i)    #5 4 3 2 (value -1 ;step back)
#<---------------------------------------------------->

#<---------------------------------------------------->
#teach.py

# while True:
#     age = eval(input("Enter your age: "))
#     if age >= 60:
#         break
#     else:
#         print("plase enter age again!")

# if age >= 60 and age <= 65:
#     bonus = 500
# elif age >= 66 and age <= 70:
#     bonus = 600
# elif age >= 71 and age <= 75:
#     bonus = 800
# elif age >= 76 and age <= 80:
#     bonus = 900
# else:
#     if age >= 81:
#         bonus = 1000
# print("Bonus salary: {:.2f}" . format(bonus))
#<---------------------------------------------------->

#<---------------------------------------------------->
#teach.py

# import turtle as tt

# distance = 50

# leg = 30

# y = 0

# tt.pensize(4)

# tt.pencolor("red")

# for m in range(6):
#     for k in range(4):
#         tt.pendown()
#         tt.forward(leg)

#         for i in range(3):
#             tt.left(90)
#             tt.forward(leg)

#         tt.penup()
#         tt.setheading(0)
#         tt.forward(distance)
#         tt.speed(300)

#     y += distance

#     tt.goto(0,y)
#<---------------------------------------------------->

#<---------------------------------------------------->
#teach.py

# while True:
#     rad = eval(input("Enter rad: "))
#     if rad > 0:
#         break

# area = 3.14* (rad**2)

# print("%10.2f" %(area))
#<---------------------------------------------------->

#<---------------------------------------------------->
#teach.py

# amt = eval(input("Enter amount: "))


# vat_rate = 7

# #calculate vat+price

# net_vat = amt *(vat_rate/100)
# net_price = amt + net_vat

# print("total:{:.2f} \nvat7%:{:.2f}". format(net_price, net_vat))
#<---------------------------------------------------->

#<---------------------------------------------------->
#discont.py

# pro = 5       #ส่วนลด
# price = 100   #ราคาสินค้า

# discount = price * pro/100   #คำนวณส่วนลด

# net_price = price - discount  #ราคาสินค้าลดแล้ว

# bg = str(net_price)

# print(type(net_price))
# print("ราคาสุทธิ:{}". format (net_price))
#<---------------------------------------------------->

#<---------------------------------------------------->
#plush_number.py

# count = 0

# sum = 0

# while count < 50:
#     sum = sum + 1

#     print(sum)

#     count = count + 1
#<---------------------------------------------------->
