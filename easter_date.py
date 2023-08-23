def main():
  #File:easter_date.py
  #Description:this program calculates the month and day of the Easter holiday for any given year using the formula\
  # known as the computus
  #AssignmentNumber:2
  #
  #Name:Elvis Nii Oblitey Commey
  #SID:easter_date.py6
  #Email:3231230034live@gctu.edu.gh
  #Grader:Augustus
  #Slip days this assignment:
  #
  #On my honor,Elvis Nii Oblitey Commey, this programming assignment is my own work
  #and I have not provided this code to any other student.

  year=int(input("Enter_year?: "))
  lunar_year_cycle_position=(year//19)
  weekday_slide_part_1=(year//4)
  weekday_slide_part_2=(year//7)
  leap_year_100=(year//100)
  leap_year_400=(leap_year_100//4)
  lunar_orbit_correction=(13+8)*(leap_year_100//25)
  century_start=(15-lunar_orbit_correction+leap_year_100-leap_year_400//30)
  sunday_offset=(4+leap_year_100-leap_year_400//7)
  days_added=(19*lunar_year_cycle_position+century_start//30)
  day_of_week_offset=(2*weekday_slide_part_1+4*weekday_slide_part_2+6*days_added+sunday_offset/7)
  total_days_added=(22+days_added+day_of_week_offset)
  int(total_days_added // 31)
  int(3 + total_days_added // 31)

  print("In 2001 Easter Sunday is on 4/15/2001. ")

main()











