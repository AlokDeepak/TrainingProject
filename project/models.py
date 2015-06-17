from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Doctors(Base):
  __tablename__ = 'Doctors'
  id = Column(Integer, primary_key=True)
  name = Column(String(255))
  email = Column(String(255))
  gender = Column(String(1))
  recommendations = Column(Integer)
  experience = Column(Integer)
  
  def __init__(self, name=None, email=None, gender=None, recommendations=None, experience=None, timings=None):
    self.name = name
    self.email = email
    self.gender = gender
    self.recommendations = recommendations
    self.experience = experience
    self.timings = timings

  def __repr__(self):
    return '<User name: %s, email: %s, gender: %s, recommendations: %s, experience: %d>' % (self.name, self.email, self.gender, self.recommendations, self.experience)

class Clinics(Base):
  __tablename__ = 'Clinics'
  id = Column(Integer, primary_key=True)
  clinicName = Column(String(255))
  location = Column(String(255))
  address = Column(String(255))
  
  def __init__(self, clinicName=None, location=None, address=None):
    self.clinicName = clinicName
    self.location = location
    self.address = address
    

  def __repr__(self):
    return '<Clinic name: %s, Location: %s, Address: %s, Fees: %d, Mobile Number: %s>' % (self.clinicName, self.location, self.address, self.fees, self.mobileNumber)

class WorksIn(Base):
  __tablename__ = 'WorksIn'
  id = Column(Integer, primary_key=True)
  doctorID = Column(Integer,ForeignKey('Doctors.id'))
  clinicID = Column(Integer,ForeignKey('Clinics.id'))
  timings = Column(String(255))
  fees = Column(Integer)
  mobileNumber = Column(String(15))
  
  def __init__(self, doctorID=None, clinicID=None, timings=None, fees=None, mobileNumber=None):
    self.doctorID = doctorID
    self.clinicID = clinicID
    self.timings = timings
    self.fees = fees
    self.mobileNumber = mobileNumber

  def __repr__(self):
    return '<Doctor ID: %d, Clinic ID: %d, Timings: %s>' % (self.doctorID, self.clinicID, self.timings)

class Education(Base):
  __tablename__ = 'Education'
  id = Column(Integer, primary_key=True)
  doctorID = Column(Integer,ForeignKey('Doctors.id'))
  degree = Column(String(255))
  institution = Column(String(255))
  yearOfPassing = Column(Integer)
  
  def __init__(self, doctorID=None, degree=None, institution=None, yearOfPassing=None):
    self.doctorID = doctorID
    self.degree = degree
    self.institution = institution
    self.yearOfPassing = yearOfPassing

  def __repr__(self):
    return '<Degree: %s, Institution: %s, Year Of Passing: %d>' % (self.degree, self.institution, self.yearOfPassing)

class Speciality(Base):
  __tablename__ = 'Speciality'
  id = Column(Integer, primary_key=True)
  speciality = Column(String(255))
  
  def __init__(self, speciality=None):
    self.speciality = speciality

  def __repr__(self):
    return '<Speciality: %s>' % (self.speciality)

class HasSpeciality(Base):
  __tablename__ = 'HasSpeciality'
  id = Column(Integer, primary_key=True)
  doctorID = Column(Integer, ForeignKey('Doctors.id'))
  specialityID = Column(Integer, ForeignKey('Speciality.id'))
  
  def __init__(self, doctorID=None, specialityID=None):
    self.doctorID = doctorID
    self.specialityID = specialityID

  def __repr__(self):
    return '<Doctor ID: %d, Speciality ID: %d>' % (self.doctorID, self.specialityID)

class Reviews(Base):
  __tablename__ = 'Reviews'
  id = Column(Integer, primary_key=True)
  doctorID = Column(Integer,ForeignKey('Doctors.id'))
  description = Column(String(255))
  username = Column(String(255))
  
  def __init__(self, doctorID=None, description=None, username=None):
    self.doctorID = doctorID
    self.description = description
    self.username = username

  def __repr__(self):
    return '<Description: %s, Username: %s>' % (self.description, self.username)

class Experiences(Base):
  __tablename__ = 'Experiences'
  id = Column(Integer, primary_key=True)
  doctorID = Column(Integer,ForeignKey('Doctors.id'))
  startYear = Column(Integer)
  endYear = Column(Integer)
  description = Column(String(255))
  
  def __init__(self, doctorID=None, startYear=None, endYear=None, description=None):
    self.doctorID = doctorID
    self.startYear = startYear
    self.endYear = endYear
    self.description = description

  def __repr__(self):
    return '<Description: %s, Start year: %d, End year: %d>' % (self.description, self.startYear, self.endYear)

