def student_count(student_list):

   male_count = 0
   female_count = 0
   for gender in student_list:
       if gender.lower() == "male":
           male_count = male_count +1
           if gender.upper == "Male":
               male_count = male_count + 1
           elif gender.lower() == "female":
               female_count = female_count +1
               return male_count,female_count


student_list = ['Male','Female','female','male','male','male','female','male','Female','Male','Female','Male','female']
result = student_count(student_list)
print(result)
print(result)



