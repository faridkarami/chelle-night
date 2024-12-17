from astral import LocationInfo
from astral.sun import sun
from datetime import date, timedelta

city = LocationInfo("Tehran", "Iran", "Asia/Tehran", 35.6892, 51.3890)
year = 2024

def calculate_night_duration(day, month, year):
    s = sun(city.observer, date=date(year, month, day))
    sunset = s['sunset']
    sunrise = s['sunrise'] + timedelta(days=1)
    night_duration = sunrise - sunset
    return night_duration

all_nights = []
for month in range(1, 13):
    for day in range(1, (date(year, month, 1) - timedelta(days=1)).day + 1):
        try:
            duration = calculate_night_duration(day, month, year)
            all_nights.append((month, day, duration))
        except Exception as e:
            print(f"Error on {month}/{day}/{year}: {e}")

longest_night = max(all_nights, key=lambda x: x[2])

for night in all_nights:
    print(f"Night duration on {night[1]}/{night[0]}/{year}: {night[2]}")

print(f"The longest night is on {longest_night[1]}/{longest_night[0]}/{year} with a duration of {longest_night[2]}.")
