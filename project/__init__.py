from flask import Flask, render_template, request, session, redirect, url_for
from database import init_db, db_session
from models import Doctors, Clinics, WorksIn, Education, Speciality, HasSpeciality, Reviews, Experiences
from forms import DoctorsForm, ClinicsForm, EducationForm, SpecialityForm, ReviewForm, WorksInForm, HasSpecialityForm

init_db()

project = Flask('project')
@project.route('/', methods=['GET', 'POST'])
def home():
    
    return render_template('index.html')

@project.route('/search', methods=['POST','GET'])
def searchDoctors():
    location=request.form['location'] # for POST form method
    speciality=request.form['speciality'] # for POST form method
    
    kwargs = {'location': location}
    clinicList=Clinics.query.filter_by(**kwargs)

    clinicIDList = {}
    for clinic in clinicList:
        clinicIDList['clinicID']=clinic.id

    workList = WorksIn.query.filter_by(**clinicIDList)

    vargs = {}
    for work in workList:
      vargs['id'] = work.doctorID
    print "heret"
    doctors = Doctors.query.filter_by(**vargs)
    return render_template('result.html', doctors=doctors)


@project.route('/admin', methods=['POST','GET'])
def admin():
    if request.method == 'GET':    
        return render_template('admin.html')
    

@project.route('/doctors', methods=['GET', 'POST'])
def doctorDetails():
    doctors = Doctors.query.all()
    form = DoctorsForm(request.form)
    if request.method == 'POST':
        if form.validate():
           if form.id.data == '':
               print 
               d = Doctors(form.name.data, form.email.data, form.gender.data, form.recommendations.data, form.experience.data)
               db_session.add(d)
               db_session.commit()
           else:
               doctor = Doctors.query.get(int(form.id.data))
               doctor.name = form.name.data
               doctor.email = form.email.data
               doctor.gender = form.gender.data
               doctor.recommendations = form.recommendations.data
               db_session.commit()
           doctors = Doctors.query.all()
    return render_template('doctor.html', doctors=doctors)

@project.route('/doctors/delete/<int:doctorID>')
def deleteDoctor(doctorID):
    doctorObj = Doctors.query.get(doctorID)
    db_session.delete(doctorObj)
    db_session.commit()
    return redirect(url_for('doctorDetails'))

@project.route('/doctors/add/<doctorID>')
def addDoctor(doctorID):
    if doctorID == 'new':
        form = DoctorsForm(request.form)
    else:
        doctorObj = Doctors.query.get(int(doctorID))
        form = DoctorsForm(obj=doctorObj)
    return render_template('doctorForm.html', form=form)

@project.route('/clinics', methods=['GET', 'POST'])
def clinicDetails():
    clinics = Clinics.query.all()
    form = ClinicsForm(request.form)
    if request.method == 'POST':
        if form.validate():
           if form.id.data == '':
               c = Clinics(form.clinicName.data, form.location.data, form.address.data)
               db_session.add(c)
               db_session.commit()
           else:
               clinic = Clinics.query.get(int(form.id.data))
               clinic.clinicName = form.clinicName.data
               clinic.location = form.location.data
               clinic.address = form.address.data
               db_session.commit()
           clinics = Clinics.query.all()
    return render_template('clinic.html', clinics=clinics)

@project.route('/clinics/delete/<int:clinicID>')
def deleteClinic(clinicID):
    clinicObj = Clinics.query.get(clinicID)
    db_session.delete(clinicObj)
    db_session.commit()
    return redirect(url_for('clinicDetails'))

@project.route('/clinics/add/<clinicID>')
def addClinic(clinicID):
    if clinicID == 'new':
        form = ClinicsForm(request.form)
    else:
        clinicObj = Clinics.query.get(int(clinicID))
        form = ClinicsForm(obj=clinicObj)
    return render_template('clinicForm.html', form=form)

@project.route('/worksIn', methods=['GET', 'POST'])
def worksInDetails():
    worksIn = WorksIn.query.all()
    form = WorksInForm(request.form)
    if request.method == 'POST':
        if form.validate():
           if form.id.data == '':
               w = WorksIn(form.doctorID.data, form.clinicID.data, form.timings.data, form.fees.data, form.mobileNumber.data)
               db_session.add(w)
               db_session.commit()
           else:
               worksIn = WorksIn.query.get(int(form.id.data))
               worksIn.doctorID = form.doctorID.data
               worksIn.clinicID = form.clinicID.data
               worksIn.fees = int(form.fees.data)
               worksIn.mobileNumber = form.mobileNumber.data
               db_session.commit()
           worksIn = WorksIn.query.all()
    return render_template('worksIn.html', worksIn=worksIn)

@project.route('/worksIn/delete/<int:worksInID>')
def deleteWorksIn(worksInID):
    worksInObj = WorksIn.query.get(worksInID)
    db_session.delete(worksInObj)
    db_session.commit()
    return redirect(url_for('worksInDetails'))

@project.route('/worksIn/add/<worksIn>')
def addWorksIn(worksIn):
    if worksIn == 'new':
        form = WorksInForm(request.form)
    else:
        worksInObj = WorksIn.query.get(int(worksIn))
        form = WorksInForm(obj=worksInObj)
    return render_template('worksInForm.html', form=form)

@project.route('/education', methods=['GET', 'POST'])
def educationDetails():
    education = Education.query.all()
    form = EducationForm(request.form)
    if request.method == 'POST':
        if form.validate():
           if form.id.data == '':
               e = Education(form.doctorID.data, form.degree.data, form.institution.data, form.yearOfPassing.data)
               db_session.add(e)
               db_session.commit()
           else:
               education = Education.query.get(int(form.id.data))
               education.doctorID = form.doctorID.data
               education.degree = form.degree.data
               education.institution = form.institution.data
               education.yearOfPassing = form.yearOfPassing.data
               db_session.commit()
           education = Education.query.all()
    return render_template('education.html', education=education)

@project.route('/education/delete/<int:educationID>')
def deleteEducation(educationID):
    educationObj = Education.query.get(educationID)
    db_session.delete(educationObj)
    db_session.commit()
    return redirect(url_for('educationDetails'))

@project.route('/education/add/<educationID>')
def addEducation(educationID):
    if educationID == 'new':
        form = EducationForm(request.form)
    else:
        educationObj = Education.query.get(int(educationID))
        form = EducationForm(obj=educationObj)
    return render_template('educationForm.html', form=form)

@project.route('/speciality', methods=['GET', 'POST'])
def specialityDetails():
    speciality = Speciality.query.all()
    form = SpecialityForm(request.form)
    if request.method == 'POST':
        if form.validate():
           if form.id.data == '':
               s = Speciality(form.specialityName.data)
               db_session.add(s)
               db_session.commit()
           else:
               s = Speciality.query.get(int(form.id.data))
               s.speciality = form.specialityName.data
               db_session.commit()
           speciality = Speciality.query.all()
    return render_template('speciality.html', speciality=speciality)

@project.route('/speciality/delete/<int:specialityID>')
def deleteSpeciality(specialityID):
    specialityObj = Speciality.query.get(specialityID)
    db_session.delete(specialityObj)
    db_session.commit()
    return redirect(url_for('specialityDetails'))

@project.route('/speciality/add/<specialityID>')
def addSpeciality(specialityID):
    if specialityID == 'new':
        form = SpecialityForm(request.form)
    else:
        specialityObj = Speciality.query.get(int(specialityID))
        form = SpecialityForm(obj=specialityObj)
    return render_template('specialityForm.html', form=form)

@project.route('/review', methods=['GET', 'POST'])
def reviewDetails():
    reviews = Reviews.query.all()
    form = ReviewForm(request.form)
    if request.method == 'POST':
        if form.validate():
           if form.id.data == '':
               r = Reviews(form.doctorID.data, form.description.data, form.username.data)
               db_session.add(r)
               db_session.commit()
           else:
               r = Reviews.query.get(int(form.id.data))
               r.doctorID = form.doctorID.data
               r.description = form.description.data
               r.username = form.username.data
               db_session.commit()
           reviews = Reviews.query.all()
    return render_template('review.html', reviews=reviews)

@project.route('/review/delete/<int:reviewID>')
def deleteReview(reviewID):
    reviewObj = Reviews.query.get(reviewID)
    db_session.delete(reviewObj)
    db_session.commit()
    return redirect(url_for('reviewDetails'))

@project.route('/review/add/<reviewID>')
def addReview(reviewID):
    if reviewID == 'new':
        form = ReviewForm(request.form)
    else:
        reviewObj = Reviews.query.get(int(reviewID))
        form = ReviewForm(obj=reviewObj)
    return render_template('reviewForm.html', form=form)

@project.route('/hasSpeciality', methods=['GET', 'POST'])
def hasSpecialityDetails():
    hasSpeciality = HasSpeciality.query.all()
    form = HasSpecialityForm(request.form)
    if request.method == 'POST':
        if form.validate():
           if form.id.data == '':
               hs = HasSpeciality(form.doctorID.data, form.specialityID.data)
               db_session.add(hs)
               db_session.commit()
           else:
               hs = HasSpeciality.query.get(int(form.id.data))
               hs.doctorID = form.doctorID.data
               hs.specialityID = form.specialityID.data
               db_session.commit()
           hasSpeciality = HasSpeciality.query.all()
    return render_template('hasSpeciality.html', hasSpeciality=hasSpeciality)

@project.route('/hasSpeciality/delete/<int:hasSpecialityID>')
def deleteHasSpeciality(hasSpecialityID):
    hasSPecialityObj = HasSpeciality.query.get(hasSpecialityID)
    db_session.delete(hasSPecialityObj)
    db_session.commit()
    return redirect(url_for('hasSpecialityDetails'))

@project.route('/hasSpeciality/add/<hasSpecialityID>')
def addHasSpeciality(hasSpecialityID):
    if hasSpecialityID == 'new':
        form = HasSpecialityForm(request.form)
    else:
        hasSpecialityObj = HasSpeciality.query.get(int(hasSpecialityID))
        form = HasSpecialityForm(obj=hasSpecialityObj)
    return render_template('hasSpecialityForm.html', form=form)    