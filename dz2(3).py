month = input('Введите номер месяца: ')
winter = ['1', '2', '12']
spring = ['3', '4', '5']
summer = ['6', '7', '8']
autumn = ['9', '10', '11']
if month in winter:
    print('Зима')
elif month in spring:
    print('Весна')
elif month in summer:
    print('Лето')
else:
    print('Осень')


