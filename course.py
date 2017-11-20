#!/usr/bin/env python
# coding: UTF-8

class Course(object):
	def __init__(self):
		self._name = ''
		self._thema = ''
		self._lecture_content = ''
		self._schedule = ''
		self._grade = ''
		self._textbook = ''
		self._note = ''
		self._remark = ''
		self._target = ''
		self._annual = ''
		self._semesta = ''
		self._unitnum = ''
		self._teachers = ''
		self._extra = []

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name += name
	
	@property
	def thema(self):
		return self._thema
	@thema.setter
	def thema(self, value):
		self._thema += value
	
	@property
	def lecture_content(self):
		return self._lecture_content
	@thema.setter
	def lecture_content(self, value):
		self._lecture_content += value

	@property
	def schedule(self):
		return self._schedule
	@schedule.setter
	def schedule(self, value):
		self._schedule += value

	@property
	def grade(self):
		return self._grade
	@grade.setter
	def grade(self, value):
		self._grade += value

	@property
	def textbook(self):
		return self._textbook
	@textbook.setter
	def textbook(self, value):
		self._textbook += value

	@property
	def note(self):
		return self._note
	@note.setter
	def note(self, value):
		self._note += value

	@property
	def target(self):
		return self._note
	@target.setter
	def target(self, value):
		self._note += value

	@property
	def remark(self):
		return self._remark
	@remark.setter
	def remark(self, value):
		self._remark += value

	@property
	def target(self):
		return self._target
	@target.setter
	def target(self, value):
		self._target += value

	@property
	def extra(self):
		return self._extra
	@extra.setter
	def extra(self, value):
		self._extra.append(value)

	@property
	def annual(self):
		return self._annual
	@annual.setter
	def annual(self, value):
		self._annual.append(value)

	@property
	def semesta(self):
		return self._semesta
	@semesta.setter
	def semesta(self, value):
		self._semesta.append(value)

	@property
	def unitnum(self):
		return self._semesta
	@unitnum.setter
	def unitnum(self, value):
		self._unitnum.append(value)

	@property
	def teachers(self):
		return self._teachers
	@teachers.setter
	def teachers(self, value):
		self._teachers.append(value)

	def parse_extra(self):
		for i in range(len(self._extra)):
			if i == 4:
				self._annual = self._extra[i]
			elif i== 5:
				self._semesta = self._extra[i]
			elif i == 6:
				self._unitnum = self._extra[i]
			elif i > 6 and self._extra[i].find('1．講義内容と目的') == -1:
				self._teachers += self._extra[i]

	def print_all(self):
		self.parse_extra()
		print 'name: ' + self._name
		print 'thema: ' + self._thema
		print '_lecture_content: '+ self._lecture_content
		print 'scgedule: '+ self._schedule
		print 'grade: '+ self._grade
		print 'textbook: '+ self._textbook
		print 'note: '+ self._note
		print 'remark: '+ self.remark
		print 'target: '+ self._target
		print 'thema: ' + self._thema
		print 'annual: '+ self._annual
		print 'semesta:  '+ self._semesta
		print 'unitnum: '+ self._unitnum
		print 'teacher: '+ self._teachers
