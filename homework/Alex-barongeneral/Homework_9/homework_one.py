from datetime import datetime

date_string = "Jan 15, 2023 - 12:05:33"
date_object = datetime.strptime(date_string, "%b %d, %Y - %H:%M:%S")
full_month = date_object.strftime("%B")
print(full_month)
formatted_date = date_object.strftime("%d . %m . %Y , %H : %M")
print(formatted_date)
