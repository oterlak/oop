from datetime import datetime

name = "Олег"
location = "Kyiv"
activity = "learning Python"

print(f"{name} started {activity} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}. {location} is a wonderful place!")
