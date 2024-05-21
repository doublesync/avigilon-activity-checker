from datetime import datetime, timedelta

def extract_panel_dates(input_string):
    panel_dates = []
    try:
        input_lines = input_string.split('\n')
        for line in input_lines:
            if not line:
                continue
            values = line.split('\t')
            if len(values) > 1:
                date_str = values[1].split()[0]
                datetime_obj = datetime.strptime(date_str, '%Y-%m-%d')
                formatted_date = datetime_obj.strftime('%Y-%m-%d')
                panel_dates.append(formatted_date)
    except Exception as e:
        print(f"Error extracting panel dates: {e}")

    return panel_dates

try:
    with open('log.txt', 'r') as file:
        input_string = file.read()
    panel_dates = extract_panel_dates(input_string)
except FileNotFoundError:
    print("File 'log.txt' not found. Please make sure the file exists in the correct location.")
except Exception as e:
    print(f"Error: {e}")

dates = [
    datetime.strptime(date, "%Y-%m-%d").strftime("%m-%d")
    for date in panel_dates
]

day_count = {
  "September": {
      "Monday": 0,
      "Tuesday": 0,
      "Wednesday": 0,
      "Thursday": 0,
      "Friday": 0,
      "Saturday": 0,
      "Sunday": 0
  },
  "October": {
      "Monday": 0,
      "Tuesday": 0,
      "Wednesday": 0,
      "Thursday": 0,
      "Friday": 0,
      "Saturday": 0,
      "Sunday": 0
  },
  "November": {
      "Monday": 0,
      "Tuesday": 0,
      "Wednesday": 0,
      "Thursday": 0,
      "Friday": 0,
      "Saturday": 0,
      "Sunday": 0
  },
  "December": {
      "Monday": 0,
      "Tuesday": 0,
      "Wednesday": 0,
      "Thursday": 0,
      "Friday": 0,
      "Saturday": 0,
      "Sunday": 0
  },
  "January": {
      "Monday": 0,
      "Tuesday": 0,
      "Wednesday": 0,
      "Thursday": 0,
      "Friday": 0,
      "Saturday": 0,
      "Sunday": 0
  },
  "February": {
      "Monday": 0,
      "Tuesday": 0,
      "Wednesday": 0,
      "Thursday": 0,
      "Friday": 0,
      "Saturday": 0,
      "Sunday": 0
  },
}

used_dates = []
for date in dates:
  if date == "02-29":
    day_of_week = "Friday"
    month = "February"
  else:
    dt_obj = datetime.strptime(date, "%m-%d")
    day_of_week = dt_obj.strftime("%A")
    month = dt_obj.strftime("%B")
  if not date in used_dates:
    day_count[month][day_of_week] += 1

  used_dates.append(date)

for month, days in day_count.items():
  print(month)
  for day, count in days.items():
    if day != "Saturday" and day != "Sunday":
      print(f"  {day}: {count}")
