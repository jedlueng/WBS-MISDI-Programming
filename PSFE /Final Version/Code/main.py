#Made by Jedlueng during 15 December 2021 to 10 January 2022
#Import every essential models 
import pandas as pd
from datetime import datetime as dt
from datetime import timedelta as delta
import re

# Open CSV's
#Open 2 dataframe > room-database and booking-database 
df = pd.read_csv('rooms.csv')
booking_df = pd.read_csv('Bookings.csv')


#Change start and end time to datetime variable 
booking_df['start'] = pd.to_datetime(booking_df['start'])
booking_df['end'] = pd.to_datetime(booking_df['end'])


#Filter based on capacity 
def capacity_finder(df):
  
  '''
  Shows rooms which are currently free

  Print dataframe base on given capacity
  
  '''

  qty = int(input('Enter capacity requirement: '))
  free_rooms = df.loc[df.Capacity >= qty] #Filtering with more or equal to this capacity 

  print('Rooms with your capacity needs: \n')
  
  for row in free_rooms.itertuples():#Print free_rooms with string format
    print('Room ID: {}, Capacity: {}, at: {}\n'.format(row.room_id,
                                                     row.Capacity,
                                                     row.Location))


#Filter based on avaivility
def show_free_rooms(df):
  '''
  Shows rooms which are currently free

  Freeroom = True 

  Show Freeroom
  
  '''
  free_rooms = df.loc[df.Availability == True] #Filter avaiabiltiy 

  print('Rooms with availability: \n')

  for row in free_rooms.itertuples(): #Print free_rooms + string formatting 
    print('Room ID: {}, Capacity: {}, at: {}\n'.format(row.room_id,
                                                     row.Capacity,
                                                     row.Location))

#Data Entry for entering datetime
def date_entry():
  '''
  Use regular expression to categorize datetime variable 
  
  '''
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

#Limit time selected from 9am to 9om 
#Cannot book more than 3 hours 
def hour_selector(start_time):
  '''
  
  Limit time selected from 9am to 9om 
  Cannot book more than 3 hours 

  if book more than 3 hours book again 

  if booking after 9pm = too late and need to book again
  
  '''
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

#Show bookable room, choose hours, combined csv file. 
def show_bookable_rooms(df):
  '''
  This function shows free rooms 

  Then let user choose room to book 

  After that, user can choose hours 

  After that using Pandas, python code will combined new data frame with booking.csv automatically 
  
  
  '''
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

  new_room_id = free_rooms[choice] # Get the Room ID
  new_booking_id = booking_df.iloc[-1, 0] + 1 # Generate a Booking ID

  # Data for one new row,
  new_data_to_write = [new_booking_id, new_room_id, start, end]

  # Create new Dataframe to hold the new booking
  single_booking = pd.DataFrame([new_data_to_write], columns=booking_df.columns)

  # Join the existing bookings with the new bookings
  df_to_be_saved = pd.concat([booking_df, single_booking])

  df_to_be_saved.to_csv('Bookings.csv', index=False) #Save to csv



#Filltering for location 
def filter_loc(df): 
  '''
  This function access location forum in the datafram. 

  Then return 
  
  
  '''
  wbs = df.loc[df.Location == 'WBS']
  lib = df.loc[df.Location == 'Library']
  eng = df.loc[df.Location == 'Engineering']
  wmg = df.loc[df.Location == 'WMG']
  print(''' 
  Choose your location 
  Press 1 for WBS 
  Press 2 for library 
  Press 3 for Engineering
  Press 4 for WMG
  ''')
  us_int = int(input())
  if us_int == 1:
    for row in wbs.itertuples():#print wbs
      print('Room ID: {}, Capacity: {}, at: {}\n'.format(row.room_id,
                                                     row.Capacity,
                                                     row.Location))
  elif us_int == 2: 
    for row in lib.itertuples():#print library 
      print('Room ID: {}, Capacity: {}, at: {}\n'.format(row.room_id,
                                                     row.Capacity,
                                                     row.Location))
  elif us_int == 3:
    for row in eng.itertuples(): #print Engineering 
            print('Room ID: {}, Capacity: {}, at: {}\n'.format(row.room_id,
                                                     row.Capacity,
                                                     row.Location))
  elif us_int == 4: 
    for row in wmg.itertuples(): #print wmg 
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
    for row in com.itertuples(): #print computer 
      print('Room ID: {}, Capacity: {}, at: {}\n'.format(row.room_id,
                                                     row.Capacity,
                                                     row.Location))
  elif us_int == 2: 
    for row in printer.itertuples(): #print printer 
      print('Room ID: {}, Capacity: {}, at: {}\n'.format(row.room_id,
                                                     row.Capacity,
                                                     row.Location))
  elif us_int == 3:
    for row in projector.itertuples(): #print projector 
            print('Room ID: {}, Capacity: {}, at: {}\n'.format(row.room_id,
                                                     row.Capacity,
                                                     row.Location))

#Filtering 
def filter_main(df):
  """Defines a main loop which enables user to
    enter a choice between 1 and 4 to determine
    which action to take
    
  Parameters
  ----------  
  df: pd.DataFrame

  Returns
  -------
  None
  """
  print('''
  Press 1 for filtering by location 
  Press 2 for filtering by equitment
  ''')
  us_input = int(input())
  if us_input == 1: 
    filter_loc(df)
  elif us_input == 2: 
    filter_eq(df) 


#Loop text for main loop
loop_text = '''
        Welcome,
        Press 1 to see all rooms
        Press 2 to find rooms with your capacity
        Press 3 to make a booking
        Press 4 to for location and equipment filtering 
        Press Q to quit
          '''

#Enables user to enter choice, loop back when after some functions and quit
def main_loop():
  """Defines a main loop which enables user to
      enter a choice between 1 and 4 to determine
      which action to take

  Parameters
  ----------  
  None

  Returns
  -------
  None
  """

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


#Read mainloop until quit 
main_loop()
