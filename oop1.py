'''
Create a Python class to represent a University. The university should have attributes like name, location,
and a list of departments. Implement encapsulation to protect the internal data of the University class.
Create a Department class that inherits from the University class. The Department class should have attributes
like department name, head of the department, and a list of courses offered. Implement polymorphism by definin
a common method for both the University and Department classes to display their details. 
'''

import logging

logging.basicConfig(filename='log.txt')

class University:
    def __init__(self,uni_name:str, location:str, departs:list):
        if not isinstance(uni_name, str):
            raise TypeError("University name must be a string.")
        if not isinstance(location, str):
            raise TypeError("University location must be a string.")
        
        if not isinstance(departs, list):
            raise TypeError("Departs must be a list.")
        
        self._university_name = uni_name
        self._location = location
        self._departs = departs

    def get_info(self):
        print(f'Name: {self._university_name}')
        print(f'Location: {self._university_name}')
        print(f'List of departments: {self._university_name}')

class Department(University):
    def __init__(self, uni_name:str, location:str, departs:list,depart_name:str, hod:str, courses:list):
        super().__init__(uni_name, location, departs)
        
        if not isinstance(depart_name, str):
            raise TypeError("Depart name must be a string.")
        if not isinstance(hod, str):
            raise TypeError("HOD name must be a string.")
        
        if not isinstance(courses, list):
            raise TypeError("Courses must be a list.")
        
        self.depart_name = depart_name
        self.hod = hod
        self.cources = courses
    
    def get_info(self):
        print(f'University Name: {self._university_name}')
        print(f'Deartment: {self.depart_name}')
        print(f'HOD: {self.hod}')
        print(f'List of Courses: {self.cources}')

try:
    uni1 = University('TU','Kathmandu',['IOE','IOM','IOF'])
    depart1 = Department('TU','Kathmandu',['IOE','IOM','IOF'],'IOE','Mr. XYZ','BCT,BEI,BEX,BCE')

    print('Information of university.')
    uni1.get_info()

    print('\nInformation of department.')
    depart1.get_info()

except Exception as e:
    logging.error(f'Failed to create object: {e}')
