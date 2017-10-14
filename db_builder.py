import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="database.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops
#c.execute('.open database.db')
#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
coursesfile = open('courses.csv','rU')
studentsfile = open('peeps.csv','rU')
coursedict = csv.DictReader(coursesfile)
studentdict = csv.DictReader(studentsfile)
c.execute('CREATE TABLE courses (code TEXT, mark NUMERIC, id NUMERIC);')
c.execute('CREATE TABLE students (name TEXT, age NUMERIC, id NUMERIC PRIMARY KEY);')
for row in coursedict:
    code = row['code']
    #print code
    mark = row['mark']
    #print mark
    idnum = row['id']
    #print idnum
    filler = repr(code) + ',' +str(mark) + ',' + str(idnum)
    #print filler
    c.execute('INSERT INTO courses VALUES ('+ filler +');')

for row in studentdict:
    name = row['name']
    age = row['age']
    idnum = row['id']
    filler = repr(name) + ',' +str(age) + ',' + str(idnum)
    c.execute('INSERT INTO students VALUES ('+ filler +');')

#c.execute('.headers on')
#c.execute('.mode column')
#c.execute('SELECT * FROM courses;')
#print('\n')
#c.execute('SELECT * FROM students;')







#==========================================================
db.commit() #save changes
db.close()  #close database


