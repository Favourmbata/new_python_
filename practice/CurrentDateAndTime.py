# from datetime import  date
# today = date.today()
# print("Todays day is :",today)



import datetime
now = datetime.datetime.now()
print("current date and time:")
print(now.strftime("%Y-%m-%d %H:%M:%s"))