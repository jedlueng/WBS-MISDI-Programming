import pandas as pd
from datetime import datetime as dt
from datetime import timedelta as delta
import re

#Open CSV
df = pd.read_csv('rooms.csv')

# Show the first n rows (defaults to 5)
# print(df.head())

# Shows a basic summary
# Check for missing values
# Check types
# df.info()

#print('manual')

#user_input = str(input('Give me input'))

# if user_input == 'something': 
#   #run function 
#     return None



def capacity_finder(df, qty):
  return df.loc[df.capacity >= qty]

#.loc = locate
def show_free_rooms(df):
  '''Shows rooms which are currently free'''
  return df.loc[df.Availability == True]


# print(show_free_rooms(df))

# print(capacity_finder(df, 5))


# START
# start = '2021-10-11 11:00'
# end = '2021-10-11 11:30'
# start_time = dt.strptime(start, '%Y-%m-%d %H:%M')
# print(start_time)
# print(start_time + delta(hours=1))
loop_text = '''
        Press 1 to see free rooms
        Press 2 to find rooms with your capacity
        Press Q to quit
          '''
# while True:
#   print(loop_text)
  
#   user_input = input('Enter Choice: ').lower()
#   if user_input == '1':
#     print('Free Rooms: \n')
#     print(show_free_rooms(df))

#   if user_input == 'q':
#     print('Quitting')
#     break




##############################

cols = ['booking_id', 'room_id', 'start', 'end']
booking_df = pd.DataFrame(columns=cols)

booking_df.at[0] = [1,
                    'R1',
                    '2021-12-14 16:00:00',
                    '2021-12-14 17:00:00']

# Converting columns from strings to 'datetimes'
booking_df['start'] = pd.to_datetime(booking_df['start'])
booking_df['end'] = pd.to_datetime(booking_df['end'])

booking_df.info()
booking_df.to_csv('Bookings.csv')


# 13:00 13-12-2021
# 15:00 13-12-2021
# start_time = dt.strptime('%Y-%m-%d')

#Date 
choose_date = input('Enter date as dd-mm-yyyy ')

#Time 
choose_time = input('Enter time as hh:mm ')

#Combine 
time_and_date = choose_time + ' ' + choose_date 


pattern = re.compile(r'\d\d:\d\d \d\d-\d\d-\d{4}')

while not re.search(pattern, time_and_date):
  print('Data entered incorrectly, try again')
  choose_date = input('Re-enter date as dd-mm-yyyy ')
  choose_time = input('Re-enter time as hh:mm ')
else:
  print('Accepted!')
  time_and_date = choose_time + ' ' + choose_date
  date_time = dt.strptime(time_and_date, '%H:%M %d-%m-%Y')
  print(date_time)