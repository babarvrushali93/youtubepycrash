import sqlite3 as lite


# functionality goes here

class DatabaseManage(object):
    
    def __init__(self):
        global con
        try:
            con  = lite .connect('courses.db')
            with con:
                cur = con.coursor()
                cur.execute("CRAEATE TABLE IF NOT EXISTS course(ID INTEGER PRIMARY KEY AUTOINCREMENT , name TEXT ,description TEXT,price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print("Unable to create a DB !")
            
    # TODO: create data        
    def insert_data(self,data):
        try:
            with can:
                cur = con.cursor()
                cur.execute("INSERT INTO course(name,description,price,is_private) VALUES (?,?,?,?)",data)
            return True
        except Exception:
            return False
            
    
    #TODO: read data
    def fetch_data(self):
        try:
            with con:
                cur = con.corsor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall()
            
        except  Exception:
            return False
            
    #TODO: delete data
    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM courses WHERE id = ?"
                cur.execute(sql, [id])
                return True
        except Exception:
            return False
        
# TODO: provide interface to user

def main():
    print("*"*40)
    print("\n:: COURSE MANAGEMENT :: \n")
    print("*"*40)
    print("\n")
    
    db = DatabaseManage()
    
    print("#"*40)
    print("\n :: User Manual :: \n")
    print("#"*40)
    
    print('\nPress 1. Insert a new courses\n')
    print('Press 2. show all courses\n')
    print('Press 3. Delete a course (NEED ID OF COURSE\n)')
    print("#"*40)
    print("\n")
    
    choice = input("\n Enter a choice:")
    
    if choice == "1":
        name = input("\n Enter course name: ")
        decription = input("\n Enter course decription: ")
        price = input("\n Enter course price: ")
        private = input("\n Enter course private (0/1): ")
          
        if db.insert_data([name,decription,price,private]):
           print("Course was inserted successfully")
        else:
            print("OOPS SOMEthing is wrong")
          
    elif choice == "2":
        print("\n :: Course List ::")
        
        for index, item in enumerate(db.fetch_data()):
            print("\n Sl no : " + str(index + 1))
            print("course ID :" + str(item[0]))
            print("course Name : " + str(item[1]))
            print("course Description : " + str(item[2]))
            print("course Price : " + str(item[3]))
            private = 'yes' if item[4] else 'NO'
            print("IS Private :" + private)
            print("\n")
          
          
    elif choice == "3":
        record_id = input("Enter the course ID: ")  
        
        if  db.delete_data(record_id):
            print("Course was deleted with a success ")    
        else:
            print("OOPS SOMWTHING WANT WRONG")  
            
    else: 
        print("\n BAD CHOICE")    
        
        
if __name__  == '__main__':
   main()       
            
            