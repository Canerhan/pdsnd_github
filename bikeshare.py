import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }







def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('We got {} as locations.'.format(sorted(CITY_DATA.keys())))
    city = str(input('Which city you want to explore?')).lower()
    while city not in (list(CITY_DATA.keys())):
        print("Sorry, we don\'t have data for that location.")
        city = str(input('Which city you want to explore?')).lower()
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = input('Which month you want to explore? Please return the month as a text. Your options are : {} . If you want want to consider all months, type all '.format(months)).lower()
    if month != 'all':
        while (month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']):
                print('Please enter the month again.')
                month = input('Which month you want to explore? Please return the month as a text. Your options are : {} . If you want want to consider all months, type all '.format(months)).lower()     
        month = months.index(month) + 1
    day = str(input('Which day of the Week you want to explore? Please return the day-name like Monday or Tuesday.\ If you want want to consider all weeks, type all')).lower()
    if day != 'all':
            while(day not in ['monday','tuesday','wednesday', 'thursday', 'friday', 'saturday', 'sunday']):
                print('Please enter the day again.')
                day = str(input('Which day of the Week you want to explore? Please return the day-name like Monday or Tuesday.\ If you want want to consider all weeks, type all')).lower()
            day = day.title()
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day]  
    return df


def show_data(df):
    pd.set_option('display.max_columns',200)
    show_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while show_data == 'yes':
        print(df.iloc[start_loc:(start_loc+6)])
        start_loc += 5
        show_data = input('Do you wish to continue?: ').lower()

    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    try:
        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time.time()
    except:
        pass
 
    print('---------------------------------')

# TO DO: display the most common month
    try:
        print('Display the most common Month')
        print('The Month is {} '.format(df['month'].value_counts().idxmax()))
        print('and the value is {}'.format(df['month'].value_counts().max()))
    except:
        pass
    
    print('---------------------------------')    
    
    # TO DO: display the most common day of week
    try:
        print('Display the most common day of week')
        print('The day is {} '.format(df['hour'].value_counts().idxmax()))
        print('The value is {} '.format(df['day_of_week'].value_counts().max()))
    except:
        pass
    
    print('---------------------------------')
    
    # TO DO: display the most common start hour
    try:
        print('Display the most common start hour')
        print('The start hour is {} '.format(df['hour'].value_counts().idxmax()))
        print('And it was used {} times'.format(df['hour'].value_counts().max()))
    except:
        pass
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    try:
        print("What is the most commonly used start station?")
        print('The start station is {} '.format(df['Start Station'].value_counts().idxmax()))        
        print('The station was used {} times'.format(df['Start Station'].value_counts().max()))    
    except:
        pass
    
    print('---------------------------------')
    # TO DO: display most commonly used end station
    
    try:
        print("What is the most commonly used end station?")
        print('The station is {} .'.format(df['End Station'].value_counts().idxmax()))
        print('The station was used {} times.'.format(df['End Station'].value_counts().max()))
    except:
        pass
    
    print('---------------------------------')
    # TO DO: display most frequent combination of start station and end station trip
    try:
        print('What is the most frequent combination of start station and end station trip')
        print(df.groupby(['Start Station','End Station']).size().reset_index().rename(columns={0:'count'}).max())
    except:
        pass
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    try:
        print("What was our customers total travel time?")
        print(df['Trip Duration'].sum())
    except:
        pass
    
    print('---------------------------------')
    # TO DO: display mean travel time
    
    print('What was our customers median travel time?')
    print(df['Trip Duration'].median())
    print('---------------------------------')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    try:
        print('What are the numbers for each user type ?')
        print(df['User Type'].value_counts())
    except:
        pass
    
    try:
        print('What are the genders of our customers?')
        print(df['Gender'].value_counts())
    except:
        pass
    
    try:
        print("What are the numbers for each user type and gender?")
        print(df.groupby('User Type')['Gender'].value_counts())
    except:
        pass
    
    try:
        print('What ist earliest, most recent, and most common year of birth?')
        print('The earliest birth year is {}'.format(df['Birth Year'].min()))
        print('The most recent birth year is {}'.format(df['Birth Year'].max()))
        print('The most common birth year is {}'.format(df['Birth Year'].median()))
    except:
        pass
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        show_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
    return

if __name__ == "__main__":
	main()
