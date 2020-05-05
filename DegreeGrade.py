#                     MB,PP,--,--,--,--,--,--
level6_grade_array = [0,0,0,0,0,0,0,0] #GRADES FROM LEVEL 6 - PROJECT MARK TWICE(double credit weight)
level6_grade_array.sort()
level6_grade_array.reverse()
#print(level6_grade_array)

#LEVEL 5 GRADES BELOW ARE CORRECT
level5_grade_array = [0,0,0,0,0,0,0,0] #GRADES FROM LEVEL 5 - CSDE MARK TWICE(double credit weight)
level5_grade_array = level5_grade_array + level6_grade_array[6:]
level5_grade_array.sort()
level5_grade_array.reverse()
#print(level5_grade_array)

def year_average(grades):
        total = sum(grades[0:6])
        total = total/6
        return total;

higher_grade = year_average(level6_grade_array)*75
lower_grade = year_average(level5_grade_array)*25
total_grade = (higher_grade + lower_grade)/100

print(total_grade)

#print((year_average(level6_grade_array)+ year_average(level5_grade_array))/2)
#print(sum(level5_grade_array))
#print(sum(level5_grade_array[0:6])/6)

