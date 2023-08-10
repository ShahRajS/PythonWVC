from Employee import Employee
from Meeting import Meeting


class Schedule:

    def __init__(self, employees):
        self.employees = employees
        self.meetings = []

    def schedule_meetings(self):
        for i in range(len(self.employees)):
            for j in range(i + 1, len(self.employees)):
                self.meetings.append(Meeting(self.employees[i], self.employees[j]))

    def print_schedule(self):
        for i, meeting in enumerate(self.meetings):
            print(f"Week {i + 1}: {meeting.employee1} & {meeting.employee2} will have a coffee meeting.")