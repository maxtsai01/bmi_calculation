height = input("身高:")
height = float(height)
weight = input('體重:')
weight = float(weight)

bmi = weight / (height/100)**2

if bmi <18.5 :
    print('體重過輕', 'BMI:', round(bmi,2))
elif bmi >=18.5 and bmi <24:
    print('正常範圍', 'BMI:', round(bmi,2))
elif bmi >=24 and bmi <27:
    print('過重', 'BMI:', round(bmi,2))
elif bmi >=27 and bmi <30:
    print('輕度肥胖', 'BMI:', round(bmi,2))
elif bmi >=30 and bmi <35:
    print('中度肥胖', 'BMI:', round(bmi,2))
else:
    print('重度肥胖', 'BMI:', round(bmi,2))