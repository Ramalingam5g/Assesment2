import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Ramkaja@16",
  database="assesment2"
)
mycursor=mydb.cursor(buffered=True)

class School:               #Create a class as School
  
  def __init__(self, student_count):
      self.student_count = student_count
      

  def get_school_details(self):   #Create a method school details
        sqlinsertcmd='CREATE TABLE student_details[IF NOT EXIST](roll_no int AUTO_INCREMENT PRIMARY KEY,STUDENT_NAME VARCHAR(30))'
        sqlinsertcmd='INSERT student_details VALUES(101,"ram"),(102,"sam"),(103,"velu"),(104,"kannan")'
        query = "SELECT * from student_details"
        mycursor.execute(query)
        result_set = mycursor.fetchall()      
        for row in result_set:          
          print("STUDENT DETAILS :",row)
        
  def get_attenance_details(self):         #Create a method attenance details
        sqlinsertcmd="CREATE TABLE student_attenance[IF NOT EXIST](roll_no int,presenting_days int,amount int,FOREIGN KEY(roll_no) REFERENCES student_details(roll_no))"
        i=1
        while i <= self.student_count:      #using while loop to collect a value from users
          sqlinsertcmd="insert student_attenance values(%s,%s,%s)"#insert a values to get it from a users
          roll_no=int(input("Enter Student Roll_No:")) #get a roll no from users
          present_days=int(input("Enter Presenting Days:")) #Get a presenting days from users
          Amount=present_days*50                            #calculate the amount
          values=(roll_no,present_days,Amount)              #values are assingned to a variable
          mycursor.execute(sqlinsertcmd,values)             
          mydb.commit()                                     
          i+=1                                              #increment the variable
        query = "SELECT DISTINCT roll_no ,presenting_days,amount from student_attenance"
        mycursor.execute(query)
        result_set = mycursor.fetchall() #Fetch the values from student attenance
        for row in result_set:
          print("STUDENT ATTENANCE DETAIL:",row) #Print the values using for loop
        School.total_amount=Amount*self.student_count   #Here calculate the total amount
        print(School.total_amount)
        return School.total_amount                      #Here return the  total amount
          
  def get_account_details(self, student_fees):    #Create a another method called account details
    sqlinsertcmd ="CREATE TABLE IF NOT EXISTS account_details ( TOTAL_STUDENTS int,STUDENT_FEES int,TOTAL_AMOUNT int)"
    #Create a table account details
    sqlinsertcmd="INSERT INTO account_details(TOTAL_STUDENTS,STUDENT_FEES,TOTAL_AMOUNT) VALUES(%s,%s,%s)"
    #Insert the values in account details
    values=(self.student_count,student_fees,School.total_amount)
    mycursor.execute(sqlinsertcmd,values)
    mydb.commit()
    query="SELECT DISTINCT TOTAL_AMOUNT FROM account_details"
    mycursor.execute(query)
    result_set=mycursor.fetchone()
    for row in result_set:
      print(".......TOTAL AMOUNT.......:",School.total_amount)

class Teacher(School):        #create a class teacher

  def __init__(self, teacher_count=2):
    self.amount=School.total_amount
    self.teacher_count=teacher_count
    
  
  def get_teachers_details(self):  #Create a method teachers details
    #sqlinsertcmd='CREATE TABLE teachers_detail[IF NOT EXIST](teachers_id int AUTO_INCREMENT PRIMARY KEY,teachers_name VARCHAR(30))'
    # mycursor.execute(sqlinsertcmd)
    # mydb.commit()
    query = "SELECT * from teachers_details"
    mycursor.execute(query)
    result_set = mycursor.fetchall()
    for row in result_set:
        print("TEACHERS  DETAIL:",row)
  def get_salary_details(self):   #Create a another method salary details
    sqlinsertcmd="CREATE TABLE salary_details[IF NOT EXIST](teachers_id int,Salary_amount int,FOREIGN KEY(teachers_id) REFERENCES teachers_details(teachers_id))"
    #Create a table salary details
    sqlinsertcmd="INSERT INTO salary_details(teachers_id,Salary_amount) VALUES(%s,%s)"
    #Insert the values get it from users
    i=1
    while i<=self.teacher_count:    #Using While loop get the value from user
      teacher_id=int(input("ENTER TEACHER ID:"))
      calculation=self.amount/2
      values=(teacher_id,calculation)
      mycursor.execute(sqlinsertcmd,values)
      mydb.commit()
      print("SALARY AMOUNT OF TEACHERS:",calculation)
      i+=1
      if calculation>=1000:
        return School.get_attenance_details()
      else:
        print("Salary credited")
      
      
class LossOfPay:               #Create a another class lossof pay

  student_fine=10               #Here declare a student fine and lossof pay as glopal variable
  teachers_lossofpay=100

  def __init__(self,student_count,teacher_count):
    self.amount=School.total_amount
    self.student_count=student_count
    self.teacher_count=teacher_count
    print(self.amount)

  def update_salary_details(self):     #Create a another method salary details
    sql_select_query="select *from salary_details where teachers_id=111"
    mycursor.execute(sql_select_query)
    fine_amount=self.amount+LossOfPay.student_fine*self.student_count    #Here calculate the fine amount
    calc_result=fine_amount/self.student_count
    mycursor.executemany('UPDATE salary_details SET salary_amount= %s WHERE teachers_id=%s',  #Update the values in a table
    [(calc_result,111),(calc_result,222)])
    mydb.commit()
    print("TEACHERS SALARY AMOUNT WITH STUDENTFINE MONEY:",calc_result)
    print("RECORD UPDATE SUCCESSFULLY") 

  def get_teachers_lossofpay(self):      #Create a another method of lossofpay
    sqlinsertcmd="CREATE TABLE lossofpay[IF NOT EXIST](teachers_id int,loss_of_pay int,salary_amount int,FOREIGN KEY(teachers_id) REFERENCES teachers_details(teachers_id))"
    #Create a table as lossofpay
    calc=self.amount/2
    lossofpay=calc-LossOfPay.teachers_lossofpay        #calculate the lossofpay
    sql_query=[(111,100,lossofpay),(222,0,calc)]       #Here execute the query
    mycursor.executemany("INSERT INTO lossofpay(teachers_id,loss_of_pay,salary_amount) VALUES (%s,%s,%s)",sql_query)
    mydb.commit()
    print("TEACHERS SALARY AMOUNT AFTER LOSSOFPAY:",lossofpay)
    print("....LOSS OF PAY UPDATED SUCEESFULLY....")



object=School(1) 
object.get_school_details()
object.get_attenance_details()
object.get_account_details(500)
objectA=Teacher(2)
objectA.get_teachers_details()
objectA.get_salary_details()
objectB=LossOfPay(2,1)
objectB.update_salary_details()
objectB.get_teachers_lossofpay()



