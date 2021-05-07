from DB.dbModels import db
import DB.dbModels as dbMdl
from course import Course, Instructor, Session
from student import Student, Preference

# Global variables
courses = dict()
instructors = dict()

def get_course(full_code: str):
    for i, c in enumerate(full_code):
        if c.isdigit():
            break
    dept, code = full_code[:i], int(full_code[i:])

    # Fetch course and session info from local
    if full_code in courses:
        return courses[full_code]

    # Fetch course and session info from db
    c = dbMdl.Course.query.filter_by(code=full_code).first()
    ss = dbMdl.Session.query.filter_by(course=full_code).all()
    if not c:
        print("not found")
        return None
    # create Course instance
    prereqs = {p for p in c.prereqs.split(' ')}
    comment = None  # TODO: Fetch and create Comment instance
    course = Course(dept, code, c.name, c.units, prereqs, comment)
    courses[full_code] = course

    for s in ss:
        ins_id = [int(i) for i in s.instr.split(' ')]
        ss_ins = set()
        for id in ins_id:
            if id in instructors:
                ss_ins.add(instructors[i-1])            # idx in db begins from 1, but list starts from 0
            else:
                # Fetch info from db
                ins = dbMdl.Instructor.query.filter_by(id=id).first()
                # create Instructor instance
                # TODO: add website
                instr = Instructor(ins.name, ins.school, ins.isLecturer)
                instructors[id] = instr
                ss_ins.add(instr)

        class1 = tuple(t for t in s.class1.split('-'))
        class2 = tuple(t for t in s.class1.split('-')) if s.class2 else None
        course.add_session(s.sno, ss_ins, s.venue, s.type, class1, class2)

    return course
    # print()
    # print(s.course)

def get_student(stuid: str) -> Student:
    s = dbMdl.Student.query.filter_by(id=stuid).first()
    courses = s.studied_courses.split(' ')
    pref = Preference(course_wishlist=None, no_morning=False, no_noon=False, no_friday=False)
    return Student(s.id, s.name, s.school, s.major, s.year, s.tot_credit, courses, pref)

# def create_new_student(stuid, name, pwd, school, major, year, tot_credit, courses):
#     s = dbMdl.Student(stuid, name, pwd, school, major, year, tot_credit, studied_courses=courses)
#     db.session.add(s)
#     pref = Preference(course_wishlist=None, no_morning=False, no_noon=False, no_friday=False)
#     return Student(s.id, s.name, s.school, s.major, s.year, s.tot_credit, courses, pref)