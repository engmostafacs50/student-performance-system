import pandas as pd 
from student import Student
class StudentManager : 
    def __init__(self) :
        self.df = None
        
        
    def load_data(self):
        self.df = pd.read_csv("students.csv")

    def save_data(self) : 
        self.df.to_csv("students.csv")
        
    def view_students(self) :
        return self.df.to_string()
    
    def view_student(self , id) : 
        return self.df.loc[str(id)] 
    


def add_student(self, student: Student):
    student_dict = student.to_dict()

    if student_dict["ID"] in self.df["ID"].values:
        print("Student already exists.")
        return

    new_row = pd.DataFrame([student_dict])

    self.df = pd.concat([self.df, new_row], ignore_index=True)

    print("Student added successfully.")
        