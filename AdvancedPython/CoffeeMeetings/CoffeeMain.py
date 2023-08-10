# Raj Shah CIST005B Coffee Meetings
# Write code to let an even number of 'n' employees meet unique times for n-1 weeks

from Employee import Employee
from Meeting import Meeting
from Schedule import Schedule

import random as r

'''
# Import the necessary libraries
from itertools import permutations

n = 6
employees = ["Employee 1", "Employee 2", "Employee 3", "Employee 4", "Employee 5", "Employee 6"]
meetings = list(permutations(employees, 2))

# Initialize a dictionary to store the schedule
schedule = {}

for week in range(n - 1):
    current_meetings = []
    for meeting in meetings:
        if meeting not in current_meetings:
            current_meetings.append(meeting)
    schedule[week + 1] = current_meetings

for week, meetings in schedule.items():
    print("Week {}:".format(week))
    for meeting in meetings:
        print("{} and {}".format(meeting[0], meeting[1]))
    print()



def main():
    employees = [Employee("employee_1"), Employee("employee_2"), Employee("employee_3"), Employee("employee_4"),
                 Employee("employee_5"), Employee("employee_6")]

    meetings = []
    for i in range(5):
        for employee in employees:
            meet = r.randint(0, 5)
            while (["Week" + str(i + 1), employee, employees[meet]] in meetings
                   or ["Week" + str(i + 1), employees[meet], employee] in meetings
                   or employee == employees[meet]):
                meet = r.randint(0, 5)
            meetings.append(["Week " + str(i + 1), employee, employees[meet]])

    for meeting in meetings:
        print(f"{meeting[1]._name} and {meeting[2]._name} will have a coffee meeting in {meeting[0]}.")


if __name__ == "__main__":
    main()
'''


def main():
    employees = [Employee("Employee 1"), Employee("Employee 2"), Employee("Employee 3"),
                 Employee("Employee 4"), Employee("Employee 5"), Employee("Employee 6")]

    schedule = Schedule(employees)
    schedule.schedule_meetings()

    schedule.print_schedule()


if __name__ == "__main__":
    main()

