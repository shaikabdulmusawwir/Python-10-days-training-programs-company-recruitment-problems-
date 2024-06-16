'''Max is planning to take part in a Diwali contest at a Diwali Party that will begin at 8
PM and will run until midnight (12 AM) i.e., for 4 hours. He also needs to travel to the
party venue within this time which takes him P minutes. The contest comprises
of N problems that are arranged in order of difficulty, with problem 1 being the
simplest and problem N being the most difficult. Max is aware that he will require 5*i
minutes to solve the ith problem.
Your task is help Max find and return an integer value, representing the number of
problems Max can solve and reach the party venue within the given time frame of 4
hours.
Note: Max will leave his home at exactly 8 PM to reach the party venue.
Input Format:
input1: An integer value N, representing the total number of problems.
input2: An integer value P, Representing the time to travel in minutes from his home
to the party venue.'''


'''def calculate_problems_solved(N, P):
    total_time_available = 4 * 60  # 4 hours in minutes
    travel_time = P
    time_available_for_problems = total_time_available - travel_time
    problems_solved = 0
    time_taken = 0
    for i in range(1, N + 1):
        time_required = 5 * i
        if time_taken + time_required <= time_available_for_problems:
            problems_solved += 1
            time_taken += time_required
        else:
            break
    return problems_solved

N = int(input("Enter the total number of problems: "))
P = int(input("Enter the travel time in minutes: "))
problems_solved = calculate_problems_solved(N, P)
print("Max can solve", problems_solved, "problems and reach the party venue within the given time frame.") '''

inp1=int(input())
inp2=int(input())
problem_solved=0
remaining_time=240-inp2
for i in range(1,inp1+1):
     if (remaining_time>0 and remaining_time>5*i):
        remaining_time=remaining_time-5*i
        problem_solved+=1
print(problem_solved)
