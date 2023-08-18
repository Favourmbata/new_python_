import  time


current_time = time.time()

total_seconds = int(current_time)

current_second = total_seconds % 60

total_minutes = total_seconds // 60

current_minute = total_minutes % 60

total_hours = total_minutes // 60

current_hour = total_hours % 24

print("current_time is",current_hour,":",current_minute,";",current_second,"GMT")