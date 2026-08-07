class Student : 
    def __init__ (self,id,name,department,math,physics,english) : 
        self.__ID = id
        self.__name = name 
        self.__department = department 
        self.__math = math 
        self.__physics = physics
        self.__english = english 
    
    def to_dict(self) : 
        return{
            "ID" : self.__ID , 
            "Name" : self.__name , 
            "Department" : self.__department , 
            "Math" : self.__math , 
            "Physics" : self.__physics , 
            "English" : self.__english 
        }
