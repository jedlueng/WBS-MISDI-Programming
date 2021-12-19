import pandas as pd
from datetime import datetime as dt
from datetime import timedelta as delta
import re


# Open CSV's
df = pd.read_csv('rooms.csv')
booking_df = pd.read_csv('Bookings.csv')

booking_df['start'] = pd.to_datetime(booking_df['start'])
booking_df['end'] = pd.to_datetime(booking_df['end'])


def capacity_finder(df):
  '''Shows rooms which are currently free'''
  qty = int(input('Enter capacity requirement: '))
  free_rooms = df.loc[df.Capacity >= qty]

  print('Rooms with your capacity needs: \n')
  
  for row in free_rooms.itertuples():
    print('Room ID: {}, Capacity: {}, at: {}\n'.format(row.room_id,
                                                     row.Capacity,
                                                     row.Location))

#.loc = locate
def show_free_rooms(df):
  '''Shows rooms which are currently free'''
  free_rooms = df.loc[df.Availability == True]

  print('Rooms with availability: \n')

  for row in free_rooms.itertuples():
    print('Room ID: {}, Capacity: {}, at: {}\n'.format(row.room_id,
                                                     row.Capacity,
                                                     row.Location))


def date_entry():
  choose_date = input('Enter date as dd-mm-yyyy ')
  choose_time = input('Enter time as hh:mm ')
  time_and_date = choose_time + ' ' + choose_date 
  pattern = re.compile(r'\d\d:\d\d \d\d-\d\d-\d{4}')

  while not re.search(pattern, time_and_date):
    print('Data entered incorrectly, try again')
    choose_date = input('Re-enter date as dd-mm-yyyy ')
    choose_time = input('Re-enter time as hh:mm ')
  else:
    time_and_date = choose_time + ' ' + choose_date
    start_time = dt.strptime(time_and_date, '%H:%M %d-%m-%Y')
    return start_time


def hour_selector(start_time):
  choose_hour = float(input('How many hour? '))
  while choose_hour > 3: 
    choose_hour = int(input('Try again, 3 or less: '))
  else:
    end_time = start_time + delta(hours=choose_hour)
    if (int(end_time.hour) * 60) + int(end_time.minute) <= 1260:
      print('Allowed!', end_time)
      return end_time
    else:
      print('Booking is too late')
      hour_selector(start_time)


def show_bookable_rooms(df):
  free_rooms = dict(enumerate(df.loc[df.Availability == True]['room_id']))

  print('Bookable rooms are as follows: ')
  for k,v in free_rooms.items():
    print('Press {} for room {}'.format(k,v))

  choice = int(input('Enter Choice: '))
  print('You Chose room: {}'.format(free_rooms[choice]))

  bookings = booking_df.loc[booking_df.room_id == free_rooms[choice]]
  print('There are {} existing bookings for your choice:'.format(len(bookings)))
  print(bookings[['start', 'end']], '\n\n')


  start = date_entry()
  end = hour_selector(start)
  print(start, end)


#Filtering 
def filter_loc(df): 
  wbs = df.loc[df.Location == 'WBS']
  lib = df.loc[df.Location == 'Library']
  eng = df.loc[df.Location == 'Engineering']
  wmg = df.loc[df.Location == 'WBS']
  print(''' 
  Choose your location 
  Press 1 for WBS 
  Press 2 for library 
  Press 3 for Engineering
  Press 4 for WMG
  ''')
  us_int = int(input())
  if us_int == 1:
    for row in wbs.itertuples():
      print('Room ID: {}, Capacity: {}, at: {}\n'.format(row.room_id,
                                                     row.Capacity,
                                                     row.Location))
  elif us_int == 2: 
    for row in lib.itertuples():
      print('Room ID: {}, Capacity: {}, at: {}\n'.format(row.room_id,
                                                     row.Capacity,
                                                     row.Location))
  elif us_int == 3:
    for row in eng.itertuples(): 
            print('Room ID: {}, Capacity: {}, at: {}\n'.format(row.room_id,
                                                     row.Capacity,
                                                     row.Location))
  elif us_int ==4: 
    for row in wmg.itertuples(): 
      print('Room ID: {}, Capacity: {}, at: {}\n'.format(row.room_id,
                                                     row.Capacity,
                                                     row.Location))
                                            
def filter_eq(df):
  com = df.loc[df.Computer == True]
  printer = df.loc[df.Printer ==  True]
  projector = df.loc[df.Projector == True]
  print(''' 
  Choose avaiable things 
  Press 1 for Computer
  Press 2 for Printer 
  Press 3 for Projector
  ''')
  us_int = int(input())
  if us_int == 1:
    for row in com.itertuples():
      print('Room ID: {}, Capacity: {}, at: {}\n'.format(row.room_id,
                                                     row.Capacity,
                                                     row.Location))
  elif us_int == 2: 
    for row in printer.itertuples():
      print('Room ID: {}, Capacity: {}, at: {}\n'.format(row.room_id,
                                                     row.Capacity,
                                                     row.Location))
  elif us_int == 3:
    for row in projector.itertuples(): 
            print('Room ID: {}, Capacity: {}, at: {}\n'.format(row.room_id,
                                                     row.Capacity,
                                                     row.Location))

#Filtering 
def filter_main(df):
  print('''
  Press 1 for filtering by location 
  Press 2 for filtering by equitment
  ''')
  us_input = int(input())
  if us_input == 1: 
    filter_loc(df)
  elif us_input == 2: 
    filter_eq(df) 

loop_text = '''
        Welcome, {}
        Press 1 to see all rooms
        Press 2 to find rooms with your capacity
        Press 3 to make a booking
        Press 4 to for location and equtment filtering 
        Press Q to quit
          '''.format('John')

def main_loop():
  while True:
    print(loop_text)
    
    user_input = input('Enter Choice: ').lower()
    if user_input == '1':
      show_free_rooms(df)

    if user_input == '2':
      capacity_finder(df)

    if user_input == '3':
      show_bookable_rooms(df)

    if user_input == '4':
      filter_main(df)

    if user_input == 'q':
      print('Quitting')
      break



main_loop()
##############################



# start_time = date_entry()
# hour_selector(start_time)