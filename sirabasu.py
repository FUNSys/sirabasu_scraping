#!/usr/bin/env python
# coding: UTF-8
import re
import linecache
import sys
from enum import Enum
from course import *

class Linetype(Enum):
	NAME = 0
	THEMA = 1
        LECTURE_CONTENT = 2
        SCHEDULE = 3
        GRADE = 4 
        TEXTBOOK = 5
        NOTE = 6
        REMARK = 7
        TARGET = 8
        EXTRA = 9
	PAGE_END = 10
		
def check_partern(partern, line):
	if re.search('— ', line):
		return Linetype.PAGE_END
	elif re.search('（[ a-zA-Z]*）$', line):
		return Linetype.NAME
	elif line.find('【テーマ・目標】') > -1:
		return Linetype.THEMA
	elif line.find('【講義内容】') > -1:
		return Linetype.LECTURE_CONTENT
	elif line.find('2．講義計画') > -1:
		return Linetype.SCHEDULE
	elif line.find('3．成績の評価方法') > -1:
		return Linetype.GRADE
	elif line.find('4．教科書・参考書') > -1:
		return Linetype.TEXTBOOK
	elif line.find('5．履修にあたっての注意事項') > -1:
		return Linetype.NOTE
	elif line.find('６．備考') > -1:
		return Linetype.REMARK
	elif line.find('対象コース') > -1:
		return  Linetype.TARGET
	elif line.find('配当年次') == 0:
		return Linetype.EXTRA
	else:
		return partern

partern = -1
courses = []
course = Course()

# ファイル名の決定
argvs  = sys.argv
argc = len(argvs)
if(argc > 1):
	filename = argvs[1]
else:
	filename = 'H29_syllabus.txt'

for line in open(filename, 'r'):
	# output course
	partern = check_partern(partern, line)

	if partern == Linetype.NAME:
		course.name = line
	elif partern == Linetype.THEMA:
		course.thema = line
	elif partern == Linetype.LECTURE_CONTENT:
		course.lecture_content = line
	elif partern == Linetype.SCHEDULE:
		course.schedule = line
	elif partern == Linetype.GRADE:
		course.grade = line
	elif partern == Linetype.TEXTBOOK:
		course.textbook = line
	elif partern == Linetype.NOTE:
		course.note = line
	elif partern == Linetype.REMARK:
		course.remark = line
	elif partern == Linetype.TARGET:
		course.target = line
	elif partern == Linetype.EXTRA:
		course.extra = line
	elif partern == Linetype.PAGE_END:
		if(course.name != ''):
			courses.append(course)
		course = Course()

for course in courses:
	print course.print_all()
