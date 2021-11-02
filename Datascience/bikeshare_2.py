import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'newyork': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'newyork', 'washington']
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'All']
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    # Get the input city from User
    while True:
        city=input('Please specifiy your desired city by inserting one of the following (chicago ,newyork ,washington)\n').lower()
        #user will input the city name in either upper or lower case and code will make it lower case
        if city in CITIES:
            break
        else:
            print('Please insert the correct city name from on of the following (chicago ,newyork ,washington)\n')

    # Get the Month city from User
    while True:
        month=input('Please choose on of the following months (January, February,March,April,May,June,July,August,September,October,November,December) \n or (All) for no month filter\n take care it is case sensitive').title()
        #user will input the month and if don't want month filter type all
        if month in MONTHS:
            break
        else:
            print('Please insert the correct month or all for no filter \n ')

     # Get the day city from User
    while True:
        day = input('Please choose on of the following days (Saturday, Sunday,Monday,Tuesday,Wednesday,Thursday,Friday)  \n or (All) for no day filter\n take care it is case sensitive').title()
        # user will input the month and if don't want month filter type all
        if day in DAYS:
            break
        else:
                print('Please insert the correct day or all for no filter \n ')
    print('-' * 40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from the Start Time column to create month and day columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by day of week if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        month = MONTHS.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df,month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month == 'All':
        popular_month = df['month'].mode()[0]
        popular_month = MONTHS[popular_month - 1]
        print('The Popular month is', popular_month)

    # display the most common day of week
    if day == 'All':
        popular_day= df['day_of_week'].mode()[0]
        print('The Popular day is', popular_day)

    try:
    # display the most common start hour
        df['Start Hour'] = df['Start Time'].dt.hour
        popular_hour = df['Start Hour'].mode()[0]
        print('The popular Start Hour is', popular_hour,'.00')
    except:
        print('There is no popular starting hour for this month and day')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    try:
        popular_start_station = df['Start Station'].mode()[0]
        print('The most commonly used Start Station is',popular_start_station)
    except:
        print('There is no popular starting station for this month and day')
        # display most commonly used end station
    try:
        popular_end_station = df['End Station'].mode()[0]
        print('The most commonly used End Station is', popular_end_station)
    except:
        print('There is no popular end station for this month and day')
    # display most frequent combination of start station and end station trip
    try:
        df['combination'] = df['Start Station'] + df['End Station']
        popular_combination = df['combination'].mode()[0]
        print('The most commonly used combination of start and end Station', popular_combination)
    except:
        print('There is no combination of start end station for this month and day')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    try:
        total_travel_duration = df['Trip Duration'].sum()
        hours=total_travel_duration//60//60
        minutes=int(60*(total_travel_duration/60/60- hours))
        seconds=round(60*(60*(total_travel_duration/60/60- hours)-minutes))
        print('the total travel duration is {} Hours , {} Minutes , {} Seconds'.format(hours,minutes,seconds))

        # display mean travel time
        mean_travel_duration = (df['Trip Duration'].mean())
        hours = mean_travel_duration  // 60 // 60
        minutes = int(60 * (mean_travel_duration  / 60 / 60 - hours))
        seconds = round(60 * (60 * (mean_travel_duration  / 60 / 60 - hours) - minutes))
        print('the mean travel duration is {} Hours , {} Minutes , {} Seconds'.format(hours, minutes, seconds))
    except:
        print('There is trips for this month and day')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print('The user types are \n', user_type)

    # Display counts of gender
    # take care ,  washington does not include gender count
    if city != 'washington':
        gender_count = df['Gender'].value_counts()
        print('The counts of each gender are \n', gender_count)

    # Display earliest, most recent, and most common year of birth
        earliest = int(df['Birth Year'].min())
        print('\nThe earliest year of birth \n', earliest)
        most_recent = int(df['Birth Year'].max())
        print('The most recent year of birth\n', most_recent)
        most_common = int(df['Birth Year'].mode()[0])
        print('The most common year of birth \n', most_common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df,month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        r = 0
        while True:
            Raw_Data = input('\nDo you want to see some raw data?   yes or no.\n')
            if Raw_Data.lower() == 'yes':
                print(df[r:r + 5])
                r = r + 5
            else:
                break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
