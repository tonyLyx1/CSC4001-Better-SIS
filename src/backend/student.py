import course
from course import Course, Instructor, Session
from typing import List, Set


class Preference:
    def __init__(self,
                 course_wishlist: List[Course] = None,
                 no_morning=False,
                 no_noon=False,
                 no_friday=False):

        self.course_wishlist = list()
        if course_wishlist is not None:
            self.course_wishlist = course_wishlist
        self.no_morning = no_morning
        self.no_noon = no_noon
        self.no_friday = no_friday

    def __str__(self):
        wishlist = 'Wish list - ' + '[' + \
                   ', '.join(c.full_code for c in self.course_wishlist) + ']'
        no_class = f'No morning classes - {self.no_morning}\n'  \
                   f'No noon classes - {self.no_noon}\n'        \
                   f'No Friday classes - {self.no_friday}\n'
        return wishlist + '\n' + no_class

    # def add_to_wishlist(self, courses: List[Course]):
    #     """
    #     Check-free method for adding courses to wish list. NOTE: Most of the time
    #     this function should not be called directly as it does not check student's
    #     prerequisites status. Instead, use Schedule.add_course_to_wishlist()
    #     """
    #     self.course_wishlist.extend(
    #         c for c in courses if c not in self.course_wishlist
    #     )


class Student:
    """
    Class of student, contains the basic info of a student
    """
    def __init__(self, 
                 stuid: str, 
                 name: str, 
                 school: str, 
                 major: str, 
                 year: int, 
                 tot_credit: int,                # Maybe add major_tot_credit, GE_tot_credit ...
                 studied_courses: Set[str],      # Use (full) course code for reducing complexity and memory
                 preference: Preference = None
                 ):
        """
        Class Student:
        :param stuid str: student id
        :param name str: student name
        :param school str: school name
        :param major str: major abbr
        :param year int: year of study
        :param tot_credit int: current total credit units
        :param studied_courses List[str]: list of studied courses, use course code
        :param preference: Preference config
        # :param schedule Schedule: schedule of the student this semester
        """
        self.__stuid = stuid
        self.__name = name
        self.__school = school
        self.__major = major
        self.__year = year
        # self.__GPA = 4.0
        self.__tot_credit = tot_credit
        self.__studied_courses = studied_courses
        self.__preference = Preference() if preference is None else preference


# properties and setters # no setter for stuid and name
    @property 
    def stuid(self):
        return self.__stuid

    @property 
    def name(self):
        return self.__name

    @property 
    def school(self):
        return self.__school

    @property 
    def major(self):
        return self.__major

    @property 
    def year(self):
        return self.__year

    @property 
    def tot_credit(self):
        return self.__tot_credit

    @property
    def studied_courses(self):
        return self.__studied_courses

    @property
    def preference(self):
        return self.__preference

    @school.setter
    def school(self, school: str):
        self.__school = school

    @major.setter
    def major(self, major: str):
        self.__major = major

    @tot_credit.setter
    def tot_credit(self, tot_credit: str):
        self.__tot_credit = tot_credit

    @studied_courses.setter
    def studied_courses(self, studied_courses: str):
        self.__studied_courses = studied_courses

    # @schedule.setter
    # def schedule(self, schedule: str):
    #     self.__schedule = schedule

# Methods
    def has_taken(self, course_code: str):
        return course_code in self.studied_courses

    def add_studied_courses(self, course_code: str):
        if self.has_taken(course_code):
            print('[WARN] The course is in the studied list already!')
            return
        self.studied_courses.add(course_code)
        # self.tot_credit += course.credit_units
    
    def list_studied_courses(self):
        print(', '. join(c for c in self.studied_courses))

    def lookInto_studied_courses(self, course: str):
        idx = self.studied_courses.find(course)
        # db query and return info
        # initialize the course and show




