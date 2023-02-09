#Basic School Administration tool
#The main objective of the School administration program is to enable the user to enter the student data,
# pre-process the data and write it into a file. (pre-processing is done with funcs and methods.)
import csv

def write_into_csv(info_list):
    with open('student.csv', 'a', newline= '') as csv_file:
        writer = csv.writer(csv_file)
     #i have wrote the if function here bcz i want the row to be executed only once or when the file is initially empty
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","contact number","Email -Id"," College Roll No :"])
     #writer.writerow(and the list up here)  
        writer.writerow(info_list)
       
if __name__ =='__main__':  
    condition = True
    student_num = 1 #increment function to increase the student values by +1 everytime we initialize the new student
    while (condition):
        student = input("Enter the details of the student #{}, in the format ( Name age Phone_number Email-ID USN) : "
                        .format(student_num))#we can use  student#{student_num} directly rather than using .format method
      #  print("The entered student details are : " + student)
    # This print statement is no longer needed, you know 
      #split ' '
        student_details_split = student.split(' ')#split(,.'') we can use these elements to split up things in a list
        print("Split Student information is as follows : " ,student_details_split)
      # This statement is no longer needed, since this makes our code look more garbage
        print("\nEntered information is :\nName :{}, \nage : {}, \nPhone :{}, \nEmail-ID : {}, \nUSN :{}".
        format(student_details_split[0],student_details_split[1],student_details_split[2],
               student_details_split[3],student_details_split[4]))
       #we can use Name, age , phone_number,Email_ID, USN_Number + student_details_split
        choice_check = input("Is the entered information true to your knowledge? Give your ans in (yes/no) : ")
        if choice_check == "yes":
            write_into_csv(student_details_split)#when the choice_check comes
            #true then we aren't printing but saving it to our csv_file directly.
            condition_check = input("Do you wish to enter another student details? type yes if you wish to else no : ")
            if condition_check == "yes":
                condition = True#when this condition = True then the loop starts again from the beginning.
                student_num = student_num+1#if the condition is true then the student value gets incremented and 
                #shows #student2
                print("Please enter the next student details in the below mentioned format, Thank you ")
#if the choice is satisfied then the loop enters the inner loop and checks for the condition inside.
            elif condition_check == "no":
                condition = False
                print("Application exited, thanks for using the services")
        elif choice_check == "no":
            print("\n Please re-enter the values ")
#first the outer loop is executed then the inner loop is executed only if the outer loop is satisfied
#outer loop here is choice_check and the inner loop is condition_check