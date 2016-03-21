# Type your code here
def my_final_grade_calculation(filename):
    dict_of_grade = {}
    filename = open(filename)
    filename = filename.read()
    filename = saperat_the_file_line(filename)
    for i in range(len(filename)):
        ##read the first line
        list1 = filename[i]
        
        ##check the Qgrades and remove the first
        ##lower value in the grades 
        grade_list = list1[1:7:1]
        lower_grade_list = str(lower_grade(grade_list))
        index_to_del = grade_list.index(lower_grade_list)
        del grade_list[index_to_del]

        ##check the Qgrades again and remove the
        ##first lower value in the grades
        lower_grade_list = str(lower_grade(grade_list))
        index_to_del = grade_list.index(lower_grade_list)
        del grade_list[index_to_del]
        
        ##calculat the Qgrade in percentage
        Qgrade = average_Qgrade(grade_list)
        
        ##check the Agrades JUST one time
        ##and remove the first lower value in the grades 
        grade_list = list1[7:11:1]
        lower_grade_list = str(lower_grade(grade_list))
        index_to_del = grade_list.index(lower_grade_list)
        del grade_list[index_to_del]
        
        ##calculat the Agrade in percentage
        Agrade = average_Agrade(grade_list)
        
        ##calculat the midterm in percentage       
        Mgrade = int(list1[11])/4 
    
        ##calculat the final in percentage       
        Fgrade = int(list1[12])/4 

        ##calculat if the studant pass
        final = Qgrade + Agrade + Mgrade + Fgrade
        dict_of_grade[list1[0]] = final_score(final)
    return dict_of_grade
    
    
def final_grade(list_of_grade):
    grade = 0
    for i in list_of_grade:
        grade += i
    
def Midterm_and_final(grade):
    return int(grade*0.25) 
    
def average_Qgrade(grade_list):
    grade = 0
    for i in grade_list:
        grade += int(i)
    return (grade /4) /4
    
def average_Agrade(grade_list):
    grade = 0
    for i in grade_list:
        grade += int(i)
    return grade/3/4
    
def lower_grade(grade_list):
    lower = 100
    for grade1 in grade_list:
        for grade2 in grade_list:
            if lower > int(grade2):
                lower = int(grade2)
            elif lower > int(grade1):
                lower = int(grade1)           
    return lower

def remove_sine_from_str(string):
    str1 = ''
    for i in string:
        if ',' == i:
            i = ''
        if '\n' == i:
            i = ' '
        str1 += i
    return str1
        
    
def list_of_str(my_string):    
    tuple1 = ''
    tuple2 = []
    for i in my_string:
        if i == ' ':
            tuple1 = [tuple1]
            tuple2 += tuple1
            tuple1 = ''
        else:
            tuple1 += i
    tuple1 = [tuple1]
    tuple2 += tuple1
    return tuple2
    
def number_of_lines(string):
    count = 1
    for i in string:
        print i
        if '\n' == i:
            count +=1
    return count

def saperat_the_file_line(filename):
    filename = remove_sine_from_str(filename)
    filename = list_of_str(filename)
    list1 = []
    list2 = []
    for grade in filename:
        list1.append(grade)
        if len(list1) == 13:
            list2.append(list1)
            list1 = []
    return list2
    
def final_score(final):
    if final >= 60:
        return "pass"
    else:
        return "fail"
