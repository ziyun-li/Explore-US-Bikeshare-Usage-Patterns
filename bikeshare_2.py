import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
cities = ['chicago','new york city','washington']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze via a series of questions that allows filtering for only month, only day, both, or none.
    Code checks existing 'months' and 'days' lists to ensure input is within range, and throws out an error otherwise.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    month = 'test'
    day = 'test'
    def month():
        while True:
            try:
                month_raw = input('Which month? january,febuary,march,april,may or june?  ').lower()
                if month_raw in months:
                    print('{} successfully being input.'.format(month_raw))
                    break
                else:
                    print('That\'s not a valid month! Please enter a month from january to june.  ')
            except:
                print('Invalid! Please try again.')
        return month_raw

    def day():
        while True:
            try:
                # get user input for day of week (all, monday, tuesday, ... sunday)
                day = input('Which day? monday, tuesday, ... sunday?  ').lower()
                if day in days:
                    print('{} successfully being input.'.format(day))
                    break
                else:
                    print('That\'s not a valid day! Please enter a monday to sunday(non-integer).  ')
            except:
                print('Invalid! Please try again.')
        return day

    # HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            # get user input for city (chicago, new york city, washington).
            city = input('Which city would you like to see data from, chicago, new york city or washington?').lower()
            if city in cities:
                print('City successfully being input.')
                break
            else:
                print('That\'s not a valid city! Please enter chicago, new york city or washington.')
        except:
            print('Invalid! Please try again.')

    while True:
        try:
            # get user input for month (all, january, february, ... , june)
            time_filter = input('Would you like to filter the data by month, day, both, or not at all? Type "none" for no time filter.').lower()
            if time_filter == 'none':
                month = 'all'
                day = 'all'
                break
            elif time_filter == 'month':
                month = month()
                day = 'all'
                break
            elif time_filter == 'day':
                day = day()
                month = 'all'
                print(day)
                break
            elif time_filter == 'both':
                month = month()
                print('Great, let\'s select the day now!')
                day = day()
                break
            else:
                print('That\'s not a valid selection. Please enter month, day, both or none.')
        except:
            print('Invalid! Please try again.')
    print('-'*40)
    return city, month, day

def check():
    while True:
        try:
            # get user input for month (all, january, february, ... , june)
            check = input('Is this the right selection? y or n?').lower()
            if check == 'y':
                break
            elif check == 'n':
                city, month, day = get_filters()
            else:
                print('Please enter y for yes and n for no')
        except:
            print('Invalid! Please try again.')





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
    print('Generating Data..')
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month']=df['Start Time'].dt.month
    df['dayofweek']=df['Start Time'].dt.weekday_name
    df['hour']=df['Start Time'].dt.hour
    df['Travel Time']=df['End Time']-df['Start Time']

    if month != 'all':
        month = months.index(month) +1
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df =df[df['dayofweek']==day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # display the most common month

    print('Most common month: {}'.format(months[df['month'].mode()[0]-1]))
    # display the most common day of week
    print('Most common day of week: {}'.format(df['dayofweek'].mode()[0]))

    # display the most common start hour

    print('Most common start hour: {}'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    print('Most common start station: {}'.format(df['Start Station'].mode()[0]))
    # display most commonly used end station
    print('Most common end station: {}'.format(df['End Station'].mode()[0]))
    # display most frequent combination of start station and end station trip
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    print('Total Travel Time: {}'.format(df['Travel Time'].sum()))

    # display mean travel time
    print('Average Travel Time: {}'.format(df['Travel Time'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())

    # Display counts of gender
    print(df['Gender'].value_counts())


    # Display earliest, most recent, and most common year of birth
    print('Most Common Year of Birth: {}'.format(int(df['Birth Year'].mode()[0])))
    print('Earliest Year of Birth: {}'.format(int(df['Birth Year'].min())))


    print('Most recent Year of Birth: {}'.format(int(df['Birth Year'].max())))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        check()
        df = load_data(city, month, day)
        raw_data=input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
        while True:
            try:
                if raw_data.lower() =='yes':
                    print(df.head())
                    break
                else:
                    break
            except:
                print('Please enter yes or no')
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
