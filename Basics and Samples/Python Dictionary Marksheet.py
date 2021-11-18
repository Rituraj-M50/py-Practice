# 1. Rituraj's dictionary 
Rituraj = { "name":"Rituraj Mahato", 
		"assignment" : [80, 70, 76, 71], 
		"test" : [85, 92], 
		"lab" : [78.20, 87.20] 
	} 
		
# 2. Prayag's dictionary 
Prayag = { "name":"Prayag C", 
		"assignment" : [82, 56, 68, 70], 
		"test" : [80, 80], 
		"lab" : [80.90, 78.72] 
		} 

# 3. Prachi's dictionary 
Prachi = { "name" : "Prachi Patel", 
		"assignment" : [77, 82, 68, 70], 
		"test" : [78, 77], 
		"lab" : [73, 71] 
		} 
		
# 4. Rajesh's dictionary 
Rajesh = { "name" : "Rajesh Kumar", 
		"assignment" : [67, 80, 77, 73], 
		"test" : [70, 75], 
		"lab" : [69, 94.56] 
	} 
		
# 5. Soumya's dictionary 
Soumya = { "name" : "Soumya Shah", 
		"assignment" : [73, 72, 73, 76], 
		"test" : [75, 72], 
		"lab" : [75.02, 60.6] 
	} 

def get_average(marks): 
	total_sum = sum(marks) 
	total_sum = float(total_sum) 
	return total_sum / len(marks) 

def calculate_total_average(students): 
	assignment = get_average(students["assignment"]) 
	test = get_average(students["test"]) 
	lab = get_average(students["lab"]) 

	return (0.1 * assignment +
			0.7 * test + 0.2 * lab) 

def assign_grade(score): 
	if score >= 90: return "A"
	elif score >= 80: return "B"
	elif score >= 70: return "C"
	elif score >= 60: return "D"
	else : return "E"

def class_average_is(student_list): 
	result_list = [] 

	for student in student_list: 
		stud_avg = calculate_total_average(student) 
		result_list.append(stud_avg) 
		return get_average(result_list) 

students = [Rituraj, Prayag, Prachi, Rajesh, Soumya] 


for i in students : 
	print(i["name"]) 
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*") 
	print("Average marks of %s is : %s " %(i["name"], 
						calculate_total_average(i))) 
						
	print("Grade's of %s is : %s" %(i["name"], 
	assign_grade(calculate_total_average(i)))) 
	
	print() 


class_av = class_average_is(students) 
print( "Class Average is %s" %(class_av)) 
print("Grade's of the Class is %s "
		%(assign_grade(class_av)))
print("################################################")
