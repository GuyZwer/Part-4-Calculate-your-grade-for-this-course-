# Part-4-Calculate-your-grade-for-this-course-
Write a function named my_final_grade_calculation that receives a file
name and returns a dictionary that tells whether a student in this course 
passed or failed based on the following criteria.  Each line of the file 
will have the format:  name, q1, q2, q3, q4, q5, q6, a1, a2, a3, a4, midterm, final  
where      name is a string     q1 through q6 are quiz scores (integers)     a1 through a4 are assignment 
scores (integers values)     midterm is midterm score (integer)     final is final exam score (integer)  
For example, if the content of the file looks like this:  
tom, 10, 20, 0, 100, 0, 100, 70, 80, 90, 0, 80, 85 
mary, 0, 50, 66, 40, 10, 60, 70, 80, 90, 100, 80, 85 
joan, 0, 80, 40, 10, 50, 60, 7, 80, 90, 0, 80, 5  
Note that there may be additional spaces between the entries in each line.  
Your function should return a dictionary such as: 
{"tom":"pass", "mary":"pass", "joan":"fail"}   
Notes:      
Two of the lowest quizzes should be dropped and the average of the 
remaining four quizzes is worth 25% of the total grade.     
The lowest assignment score should be dropped and the average of the 
remaining three assignments is worth 25% of the total grade.     
Midterm and final exams are each 25% of the total grade.  
Calculate the total score of the student and if the total score is greater than 
or equal to 60 (totalscore >= 60) then the student has passed. 
Notice that the keys (names) and the values (pass or fail) of the dictionary 
should be all lower cased with no spaces in any of them.
