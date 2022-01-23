from unicodedata import name
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

bioengineering = {
    'required_courses': ['BIOS 201', 'BIOS 341', 'CHEM 121',
                        'CHEM 122', 'CHEM 211', 'CAAM 210',
                        'ELEC 243', 'MATH 101', 'MATH 102',
                        'MATH 211', 'MATH 212', 'MECH 202',
                        'PHYS 101', 'PHYS 102', 'BIOE 252',
                        'BIOE 320', 'BIOE 322', 'BIOE 330',
                        'BIOE 332', 'BIOE 342', 'BIOE 370',
                        'BIOE 372', 'BIOE 383', 'BIOE 385',
                        'BIOE 391', 'BIOE 420', 'BIOE 440',
                        'BIOE 451', 'BIOE 452', 'BIOE 446',
                        'BIOE 447'],
    'elective_courses': ['BIOE 401', 'BIOE 380', 'BIOE 392',
                        'BIOE 400', 'BIOE 408', 'BIOE 422',
                        'BIOE 464', 'BIOE 485', 'BIOE 486',
                        'BIOE 492', 'BIOE 523', 'BIOE 543',
                        'BIOE 580', 'BIOE 587', 'BIOE 589',
                        'BIOE 615', 'BIOE 620', 'CAAM 334',
                        'CHBE 310', 'ELEC 220', 'NEUR 416',
                        'ENGI 300', 'ENGI 301', 'MECH 311',
                        'BIOE 321', 'BIOE 348', 'BIOE 431',
                        'BIOE 518', 'CAAM 335', 'CHBE 640',
                        'COMP 571', 'ELEC 305', 'ELEC 327',
                        'ELEC 432', 'BIOE 360', 'BIOE 421',
                        'BIOE 454', 'BIOE 484', 'BIOE 490',
                        'BIOE 509', 'BIOE 574', 'CHBE 390',
                        'COMP 502', 'ELEC 301', 'ELEC 326',
                        'ELEC 342', 'ELEC 422', 'ELEC 435',
                        'ENGI 355', 'MECH 371', 'MECH 400',
                        'MECH 417', 'MECH 420', 'MECH 488',
                        'MSNE 402', 'MECH 343'],
    'l300_requirement': 48,
    'course_amt_req': 37,
    'hour_requirement': 131
}

engineering_design = {
    'required_courses': ['FWIS 188', 'ENGI 200', 'ENGI 210',
                        'ENGI 350'],
    'elective_courses': ['BIOE 360', 'BUSI 221', 'BUSI 463',
                        'BIOE 365', 'CHBE 490', 'ELEC 327',
                        'ELEC 442', 'ELEC 491', 'ENGI 300',
                        'ENGI 301', 'ENGI 315', 'ENGI 355',
                        'MECH 203', 'MECH 488', 'PSYC 370'],
    'l300_requirement': 0,
    'course_amt_req': 6,
    'hour_requirement': 18
}

gpa_scale = {
    'A+': 4.0,
    'A': 4.0,
    'A-': 3.6667,
    'B+': 3.3333,
    'B': 3.0,
    'B-': 2.6667,
    'C+': 2.3333,
    'C': 2.0,
    'C-': 1.6667
}

class Course():
    all_courses = []
    quality_points = 0
    hours = 0
    course_count = 0
    gpa = 0

    def __init__(self, course_code, name, hours, distribution=0, description="", cross=[]):
        self.name = name
        self.cross = cross
        self.course_code = course_code
        self.department = course_code.split()[0]
        self.level = course_code.split()[1]
        self.hours = hours
        self.distribution = distribution
        self.description = description
        self.taken = False
        self.taking = False
        Course.all_courses.append(self)

    def tookCourse(self, grade):
        self.taken = True
        self.grade = grade
        self.quality_points = gpa_scale[grade]*self.hours
        Course.quality_points += self.quality_points
        Course.hours += self.hours
        Course.course_count += 1
        Course.gpa = Course.quality_points / Course.hours
    
    def takingCourse(self):
        self.taking = True

    def getInfo(self):
        print(f'Name: {self.name}\nDepartment: {self.department}\nHours: {self.hours}\nDistribution: {self.distribution}\nDescription: {self.description}')
        return

def getCourse(code):
    for course in Course.all_courses:
        if course.course_code == code:
            return course

#COMPLETED COURSES
Course(course_code="PHYS 101", name="MECHANICS", hours=4, distribution=3, description="A calculus-based introduction to mechanics. Includes classes and lab exercises on kinematics, Newton's Laws, work and energy, conservation laws and rotational motion. Primarily for physical science and engineering students.")
Course(course_code="MATH 211", name="ORDINARY DIFFERENTIAL EQUATIONS AND LINEAR ALGEBRA", hours=3, description="Study of ordinary differential equations (e.g., solutions to separable and linear first-order equations and to higher-order linear equations with constant coefficients, the properties of solutions to differential equations, and numerical solution methods) and linear algebra (e.g., vector spaces and solutions to algebraic linear equations, dimension, eigenvalues, and eigenvectors of a matrix), as well as the application of linear algebra to first-order systems of differential equations and the qualitative theory of nonlinear systems and phase portraits.")
Course(course_code="PSYC 101", name="INTRODUCTION TO PSYCHOLOGY", hours=3, description="Survey of topics, problems, and approaches in contemporary psychology. Includes the biological basis of behavior, sensation, perception, attention, learning and memory, thinking, language, abnormal behavior and therapies, personality, and individual differences.")
for course in Course.all_courses:
    if course.course_code != "PSYC 101":
        course.tookCourse("B+")
    else:
        course.tookCourse("A+")

#CURRENT COURSES
s22 = ["CAAM 210", "BIOS 201", "CHEM 122", "MATH 212", "PHYS 100", "PHYS 116", "FWIS 188"]
Course(course_code="CAAM 210", name="INTRODUCTION TO ENGINEERING COMPUTATION", hours=3, description="Modeling, Simulation, and Visualization via MATLAB. Numerical methods: Newton's method in one and several dimensions. Gaussian elimination and optimization. Application to problems in science and engineering.")
Course(course_code="BIOS 201", name="INTRODUCTORY BIOLOGY I", hours=3, distribution=3, description="This course examines chemistry and energetics, cell physiology, cell biology, Mendelian genetics, molecular genetics, developmental biology, and plant physiology.")
Course(course_code="CHEM 122", name="GENERAL CHEMISTRY II", hours=4, distribution=3, description="Introduction of chemical phenomena emphasizing problems and methods in Chemistry.")
Course(course_code="MATH 212", name="MULTIVARIABLE CALCULUS", hours=3, description="Calculus of multiple variables. Vectors, partial derivatives and gradients, double and triple integrals, vector fields, line and surface integrals, Green's theorem, Stokes's theorem, and Gauss's theorem.")
Course(course_code="PHYS 100", name="EXPLORING PHYSICS", hours=1, description="Introduction to concepts, methods, debates, and discoveries of physics, with a theme to be chosen from one of many fields of modern physics research.")
Course(course_code="PHYS 116", name="SEMINAR IN PHYSICS AND ASTRONOMY AT RICE AND BEYOND", hours=1, description="This half-semester seminar course will meet in the first half of the Spring semester to introduce prospective and current science and engineering majors to the exciting research in physics and astronomy at Rice and beyond. The course will provide students with the context to think about how the facts presented in physics and astronomy textbooks are applied to real-world research. Undergraduate students in a small group will meet weekly with a graduate student to explore a published research article by a local lab, learning about what was done and why it was important. Toward the end of the course, the group will tour the lab that produced the featured article.")
Course(course_code="FWIS 188", name="ENGINEERING DESIGN AND COMMUNICATION", hours=3, description="Students learn the engineering design process to solve real-world problems by evaluating design requirements and constructing innovative solutions in the OEDK. Several communication assignments will be completed by individuals rather than teams.", cross=["ENGI 120", "ENGI 220"])

for course in Course.all_courses:
    if course.course_code in s22:
        course.takingCourse()

