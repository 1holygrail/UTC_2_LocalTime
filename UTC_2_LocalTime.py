#Uses get method from requests library
#imports date time library
from requests import get as Get #If you dont have requests library install using 'pip install requests'
import datetime

#value variable in this context holds the UTC datetime format
value = "2020-01-01T20:05:39.2254815Z" #Your "UTC_Time_Goes_Here" e.g. "2020-01-01T20:05:39.2254815Z"

#Removes decimal values from 'seconds' in the time
#Change the characters as per your UTC fraction in seconds. If you e.g. in "2020-01-01T20:05:39.2254815Z" if you have 9 characters after and including the period [.] you would use '-9'
value = value[:-9]


#Adds last character 'Z' to rearrange variable with correct format. This is useful before adding/subtracting the off-set time for final output
add_last_char = 'Z'
value = value + add_last_char

#Uses strptime method, to convert the UTC datetime from 'value' into the below format, e.g. 2020-01-01 20:05:39
value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")

#Getting the UTC offset time hours when compared to your local Time. e.g. "America/Port_of_Spain"
#For a full list of all time zones check here "https://worldtimeapi.org/api/timezone/"
timezone_check = Get('https://worldtimeapi.org/api/timezone/America/Port_of_Spain') #change this timezone as per your requirement
UTC_offset_time = timezone_check.json().get('utc_offset')

#Uses the first 3 characters only from the result for easy calculations, e.g. -04 from original value -04:00
UTC_offset_time = UTC_offset_time[:3]

#Adds/subtracts the time difference to the original UTC value
Local_Time = value + datetime.timedelta(hours=int(UTC_offset_time))

#Converts the result into human friendly readable format, using strftime method
Local_Time = Local_Time.strftime("%d %b %Y, %I:%M %p")

#Displays the result output
print(Local_Time)