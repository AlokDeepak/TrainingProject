from wtforms import Form, StringField, IntegerField, validators

class DoctorsForm(Form):
    id = StringField('Doctor ID')
    name = StringField('Name', [validators.Length(min=1, max=255)])
    email = StringField('Email Address', [validators.Email(message='Enter a valid email id')])
    gender = StringField('Gender', [validators.Length(max=1)])
    recommendations = StringField('Recommendations', [validators.Length(min=1, max=4)])
    experience = StringField('Experience', [validators.Length(min=1, max=3)])

class ClinicsForm(Form):
    id = StringField('Clininc ID')
    clinicName = StringField('Clinic Name', [validators.Length(min=4, max=255)])
    location = StringField('Location', [validators.Length(min=1, max=255)])
    address = StringField('Address', [validators.Length(min=1, max=255)])

class EducationForm(Form):
	id = StringField('Education ID')
	doctorID = StringField('Doctor ID')
	degree = StringField('Degree', [validators.Length(min=1, max=255)])
	institution = StringField('Institution', [validators.Length(min=1, max=255)])
	yearOfPassing = IntegerField('Year of Passing')

class SpecialityForm(Form):
	id = StringField('Speciality ID')
	specialityName = StringField('Speciality', [validators.Length(min=1, max=255)])

class ReviewForm(Form):
	id = StringField('Review ID')
	doctorID = StringField('Doctor ID')
	description = StringField('Review', [validators.Length(min=1, max=255)])
	username = StringField('Username', [validators.Length(min=1, max=255)])

class WorksInForm(Form):
	id = StringField('Review ID')
	doctorID = StringField('Doctor ID')
	clinicID = StringField('Clininc ID')
	fees = StringField('Fees')
	mobileNumber = StringField('Contact Number', [validators.Length(min=10, max=15)])
	timings = StringField('Timings', [validators.Length(min=1, max=255)])

class HasSpecialityForm(Form):
	id = StringField('Review ID')
	doctorID = StringField('Doctor ID')
	specialityID = StringField('Speciality ID')