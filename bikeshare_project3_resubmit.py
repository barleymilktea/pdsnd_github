# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 11:13:31 2020

@author: kk240
"""


import time
import pandas as pd
import numpy as np

## adding comments here for refactoring

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    class Error(Exception):
        """Base class for other exceptions"""
        pass
    
    class CityError(Error):
        """raise when city input is not chicago, new york city, or washington """
        pass
    
    class MonthError(Error):
        """raise when month input is not all, january, february.... june"""
        pass
    
    class DayError(Error):
        """raise when day input is not all, Monday, Tuesday... Sunday"""
        pass
    
    while True:
        try:
            city = input('Key in one of the following cities (chicago, new york city, washington): ')
            print('You have typed {}! If this is incorrect, restart the program!'.format(city))
            if city.lower() != 'chicago' and city.lower()!='new york city' and city.lower()!='washington':
                raise CityError
                
                
        except CityError:
            print('Sorry please try again (chicago, new york city, washington)')
            
        else:
            #print('So you wanted to know about {} bikesharing.'.format(city))
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Key in one of the following months or all (all, january, february...., june): ')
            if month.lower()!='all' and month.lower()!='january' and month.lower()!='february' and month.lower()!='march' and month.lower()!='april' and month.lower()!='may' and month.lower()!='june':
                raise MonthError

        except MonthError:
            print('Sorry please try again (all, january, february...., june)')
            
        else:
            #print('So you wanted to know about {} bikesharing during this period {}.'.format(city, month))
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Key in a day of the week (all, monday, tuesday,..... sunday): ')
            if day.lower()!='all' and day.lower()!='monday' and day.lower()!='tuesday' and day.lower()!='wednesday' and day.lower()!='thursday' and day.lower()!='friday' and day.lower()!='saturday' and day.lower()!='sunday':
                raise DayError
        except DayError:
            print('Sorry please try again (all, monday, tuesday, ... sunday)')
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    city = city.lower()
    month = month.lower()
    day = day.lower()
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    
    if month!='all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] ==month]
    
    if day!='all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].value_counts().idxmax()

    # TO DO: display the most common day of week

    common_day = df['day'].value_counts().idxmax()
    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].value_counts().idxmax()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("The most frequent month of travel is {}".format(common_month))
    print("The most frequent day of travel is {}".format(common_day))
    print("The most frequent hour of travel is {}".format(common_hour))
    print('-'*40)
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].value_counts().idxmax()

    # TO DO: display most commonly used end station
    common_end = df['End Station'].value_counts().idxmax()

    # TO DO: display most frequent combination of start station and end station trip
    common_combine = df.groupby(['Start Station', 'End Station']).count().idxmax()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("The most popular Start Station is {}".format(common_start))
    print("The most popular End Station  is {}".format(common_end))
    print("The most popular Start and End Stations are {}".format(common_combine))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("The total travel time is {}".format(total_time))
    print("The mean travel time is {}".format(mean_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()

    except:
        print('There is no data on gender for this state')
        
    # TO DO: Display earliest, most recent, and most common year of birth
#    df = df.sort_values(df['Birth Year'])
    try:
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common_year = df['Birth Year'].value_counts().idxmax()
    
    except:
        print('There is no birth data for this state')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    try:
        print("The count of user types {}".format(user_types))
    except:
        print('There is no count on user types')
    try:
        print("The gender count is {}".format(gender))
    except:
        print('There is no data on gender for this state')
    try:
        print("The most common birth year is {}".format(common_year))
    except:
        print('There is no birth data for this state')
    print('-'*40)


def more_data(df):
    start = 0
    ask_data = input('Would you like to see the first 5 rows of data? Yes or no?')
    while ask_data.lower() == 'yes':
        df_data = df.iloc[start:start+5]
        print(df_data)
        start +=5
        ask_data = input('Would you like to see 5 more rows of data? Yes or no?')
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        more_data(df)      
        
        
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
