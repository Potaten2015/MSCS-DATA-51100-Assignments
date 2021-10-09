"""
Taten H. Knight
2021.09.25
Statistical Programming
Fall 2021
Programming Assignment 5 – Data Preparations and Statistics
"""
import pandas as pd
import re


pd.set_option('display.max_columns', None)

grade_scale = {
    'PE': 0,
    'PK': 1,
    'K': 2,
    '1': 3,
    '2': 4,
    '3': 5,
    '4': 6,
    '5': 7,
    '6': 8,
    '7': 9,
    '8': 10,
    '9': 11,
    '10': 12,
    '11': 13,
    '12': 14,
}

reg_exp = re.compile('[1-9]{1,2}:[0-9]{1,2}')


def get_smallest_grade(grades):
    split_grades = grades.split(',')
    ascending_grades = sorted(split_grades, key=lambda x: grade_scale[x])
    return ascending_grades[0]


def get_largest_grade(grades):
    split_grades = grades.split(',')
    ascending_grades = sorted(split_grades, key=lambda x: grade_scale[x])
    return ascending_grades[-1]


def get_start_time(time):
    try:
        time_match = reg_exp.search(time)
        return time_match.group()[0]
    except:
        return 'None'



def main():
    cps = pd.read_csv('cps.csv')
    filtered = pd.DataFrame({'School_ID': cps['School_ID'],
                             'Short_Name': cps['Short_Name'],
                             'Is_High_School': cps['Is_High_School'],
                             'Zip': cps['Zip'],
                             'Student_Count_Total': cps['Student_Count_Total'],
                             'College_Enrollment_Rate_School': cps['College_Enrollment_Rate_School'].fillna(cps['College_Enrollment_Rate_School'].mean()),
                             'Lowest Grade Offered': cps['Grades_Offered_All'].apply(get_smallest_grade),
                             'Highest Grade Offered': cps['Grades_Offered_All'].apply(get_largest_grade),
                             'Starting Hour': cps['School_Hours'].apply(get_start_time)})

    high_school_rows = filtered['College_Enrollment_Rate_School'][filtered['Is_High_School'] == True]
    hs_enrollment_rate = high_school_rows.mean()
    enrollment_rate_sd = high_school_rows.std()
    student_count_non_hs = filtered['Student_Count_Total'][filtered['Is_High_School'] == False]
    student_count_non_hs_mean = student_count_non_hs.mean()
    student_count_non_hs_sd = student_count_non_hs.std()
    all_starting_hours = filtered['Starting Hour'][filtered['Starting Hour'] != 'None']
    starting_hours_unique = all_starting_hours.unique()
    starting_hour_counts = all_starting_hours.value_counts()
    loop_zips = [60601, 60602, 60603, 60604, 60605, 60606, 60607,  60616]
    outside_schools = filtered['Zip'][~filtered['Zip'].isin(loop_zips)]
    outside_school_number = outside_schools.size

    print('DATA 51100 - Fall 2021')
    print('Name: Taten H. Knight')
    print('PROGRAMMING ASSIGNMENT #5')
    print(filtered.head(10))
    print()
    print(f'College Enrollment Rate for High Schools = {"%.2f" % hs_enrollment_rate} (sd={"%.2f" % enrollment_rate_sd})')
    print()
    print(f'Total Student Count for non-High Schools = {"%.2f" % student_count_non_hs_mean} (sd={"%.2f" % student_count_non_hs_sd})')
    print()
    print('Distribution of Starting Hours:')
    for i, val in enumerate(starting_hours_unique):
        print(f'{val}am: {starting_hour_counts[i]}')
    print()
    print(f'Number of schools outside Loop: {outside_school_number}')

main()
