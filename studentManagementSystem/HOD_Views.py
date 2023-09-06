from django.shortcuts import redirect,render,HttpResponse
from django.contrib.auth.decorators import login_required
from app.models import  Course,Session_Year,CustomUser,Student,Staff,Subject,Staff_Notification,Staff_Leave,Staff_Feedback,Student_Notification,Student_Feedback,Student_Leave
from django.contrib import messages

@login_required(login_url="/")
def home(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subject.objects.all().count()
    student_gender_male= Student.objects.filter(gender= 'Male').count()
    student_gender_female = Student.objects.filter(gender='Female').count()

    context = {
        'student_count':student_count,
        'staff_count':staff_count,
        'course_count':course_count,
        'subject_count':subject_count,
        'student_gender_male': student_gender_male,
        'student_gender_female': student_gender_female,

    }

    return render(request,'Hod/home.html',context)
@login_required(login_url='/')
def addStudent(request):
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('addStudent')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('addStudent')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=2
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id = course_id)
            session_year = Session_Year.objects.get(id=session_year_id)

            student = Student(
                admin = user,
                address = address,
                session_year_id = session_year,
                course_id = course,
                gender = gender,
            )
            student.save()
            messages.success(request, user.first_name + "  " + user.last_name + " Are Successfully Added !")
            return redirect('addStudent')

    context = {
        'course': course,
        'session_year': session_year,
    }

    return render(request, 'Hod/add-student.html', context)
@login_required(login_url='/')
def viewStudent(request):
    student = Student.objects.all()

    context ={
        'student':student,

    }

    return render(request,'hod/viewStudent.html',context)
@login_required(login_url='/')
def editStudent(request,id):
    student = Student.objects.filter(id=id)
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    context = {
        'student': student,
        'course': course,
        'session_year': session_year,
    }
    return render(request, 'Hod/editStudent.html',context)

@login_required(login_url='/')
def updateStudent(request):
        if request.method == "POST":
            student_id = request.POST.get('student_id')
            print(student_id)
            profile_pic = request.FILES.get('profile_pic')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            address = request.POST.get('address')
            gender = request.POST.get('gender')
            course_id = request.POST.get('course_id')
            session_year_id = request.POST.get('session_year_id')

            user = CustomUser.objects.get(id=student_id)

            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username

            if password != None and password != "":
                user.set_password(password)
            if profile_pic != None and profile_pic != "":
                user.profile_pic = profile_pic
            user.save()

            student = Student.objects.get(admin=student_id)
            student.address = address
            student.gender = gender

            course = Course.objects.get(id=course_id)
            student.course_id = course

            session_year = Session_Year.objects.get(id=session_year_id)
            student.session_year_id = session_year

            student.save()
            messages.success(request, 'Record Are Successfully Updated !')
            return redirect('viewStudent')

        return render(request, 'Hod/editStudent.html')
@login_required(login_url='/')
def deleteStudent(request,admin):
    student = CustomUser.objects.get(id = admin)
    student.delete()
    messages.success(request,'Record is Successfully Deleted')
    return redirect('viewStudent')



@login_required(login_url='/')
def addCourse(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        course = Course(
        name = course_name,
        )
        course.save()
        messages.success(request,'Course Created Successfully')
        return redirect('addCourse')

    return render(request,'Hod/addCourse.html')
@login_required(login_url='/')
def viewCourse(request):
    course = Course.objects.all()
    context = {
        'course': course,
    }
    return render(request, 'Hod/viewCourse.html', context)
@login_required(login_url='/')
def editCourse(request,id):
    course = Course.objects.get(id = id)
    context ={
        'course':course,
    }
    return render(request,'Hod/editCourse.html',context)
@login_required(login_url='/')
def updateCourse(request):
    if request.method =="POST":
        name = request.POST.get('name')
        course_id = request.POST.get('course_id')

        course = Course.objects.get(id = course_id)
        course.name = name
        course.save()
        messages.success(request,'Course Updated Successfully')
        return redirect('viewCourse')
    return render(request,'Hod/editCourse.html')
@login_required(login_url='/')
def deleteCourse(request,id):
    course =  Course.objects.get(id = id)
    course.delete()
    messages.success(request,'Course Deleted Successfully')
    return redirect('viewCourse')
@login_required(login_url='/')
def addStaff(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('addStudent')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('addStaff')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=3
            )
            user.set_password(password)
            user.save()

            staff = Staff(
                admin = user,
                address = address,
                gender = gender,

            )
            staff.save()
            messages.success(request,"Staff added Successfully")
            return redirect('addStaff')

    return render(request,'Hod/addStaff.html')
@login_required(login_url='/')
def viewStaff(request):
    staff = Staff.objects.all()
    context ={
        'staff':staff,
    }
    return render(request,'hod/viewStaff.html',context)
@login_required(login_url='/')
def editStaff(request,id):
    staff = Staff.objects.get(id = id)
    context ={
        'staff':staff,
    }
    return render(request,'hod/editStaff.html',context)
@login_required(login_url='/')
def updateStaff(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        #print(student_id)
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        #course_id = request.POST.get('course_id')
        #session_year_id = request.POST.get('session_year_id')

        user = CustomUser.objects.get(id=staff_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        staff = Staff.objects.get(admin = staff_id)
        staff.gender = gender
        staff.address =address
        staff.save()
        messages.success(request,'Staff Data Updated Successfully')
        return render(request,'viewStaff')
    return render(request,'Hod/edit_staff.html')
@login_required(login_url='/')
def deleteStaff(request,admin):
    staff = CustomUser.objects.get(id=admin)
    staff.delete()
    messages.success(request,'Record deleted Successfully')
    return redirect('viewStaff')
@login_required(login_url='/')
def addSubject(request):
    course = Course.objects.all()
    staff = Staff.objects.all()
    context ={
        'course':course,
        'staff':staff,
    }
    if request.method =="POST":
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course = Course.objects.get(id = course_id)
        staff = Staff.objects.get(id = staff_id)
        subject = Subject(
            name= subject_name,
            course = course,
            staff = staff,
        )
        subject.save()
        messages.success(request,'Subjects Added Successfully')
        return redirect('addSubject')



    return render(request,'Hod/addSubject.html',context)
@login_required(login_url='/')
def viewSubject(request):
    subject = Subject.objects.all()

    context ={
        'subject':subject,

    }
    return render(request,'hod/viewSubject.html',context)
@login_required(login_url='/')
def editSubject(request,id):
    subject = Subject.objects.get(id=id)
    course = Course.objects.all()
    staff = Staff.objects.all()
    context = {
        'subject' : subject,
        'course' : course,
        'staff' : staff,
    }
    return render(request,'hod/editSubject.html',context)
@login_required(login_url='/')
def updateSubject(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')


        course = Course.objects.get(id = course_id)
        staff = Staff.objects.get(id = staff_id)

        subject = Subject(
            id = subject_id,
            name = subject_name,
            course = course,
            staff = staff,
        )
        subject.save()
        messages.success(request,'Subject Updated Successfully')
        return redirect('viewSubject')

@login_required(login_url='/')
def deleteSubject(request,id):
    subject = Subject.objects.filter(id=id)
    subject.delete()
    messages.success(request,'Subject Deleted Successfully')
    return redirect('viewSubject')

@login_required(login_url='/')
def addSession(request):
    if request.method =="POST":
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')
        session = Session_Year(
            session_start = session_year_start,
            session_end = session_year_end
        )
        session.save()
        messages.success(request,'Session Created Successfully')
        return redirect('addSession')

    return render(request,'hod/addSession.html')

@login_required(login_url='/')
def viewSession(request):
    session = Session_Year.objects.all()
    context ={
        'session':session,
    }
    return render(request,'Hod/viewSession.html',context)

@login_required(login_url='/')
def editSession(request,id):
    session = Session_Year.objects.filter(id = id)
    context = {
        'session':session,
    }
    return render(request, 'hod/editSession.html',context)
@login_required(login_url='/')
def updateSession(request):
    if request.method =="POST":
        session_id = request.POST.get('session_id')
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')

        session =Session_Year(
            id = session_id,
            session_start=session_year_start,
            session_end=session_year_end,
        )
        session.save()
        messages.success(request,'SEssion updated Successfully')
        return redirect('viewSession')
@login_required(login_url="/")
def deleteSession(request,id):
    session = Session_Year.objects.get(id = id)
    session.delete()
    messages.success(request,'Session Deleted Successfully')
    return redirect('viewSession')
@login_required(login_url="/")
def staffSendNotification(request):
    staff = Staff.objects.all()
    see_notification = Staff_Notification.objects.all().order_by('-id')[0:10]
    context ={
        'staff':staff,
        'see_notification':see_notification,

    }
    return render(request,'hod/staffNotifications.html',context)
@login_required(login_url="/")
def saveStaffNotification(request):
    if request.method =='POST':
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')

        staff=Staff.objects.get(admin = staff_id)
        notification =Staff_Notification(
            staff_id = staff,
            message = message,
        )
        notification.save()
        messages.success(request,'Notified Successfully')
        return redirect('staffSendNotification')
@login_required(login_url="/")
def staffLeaveViews(request):
    staff_leave =Staff_Leave.objects.all()
    context ={
        'staff_leave':staff_leave,

    }
    return render(request,'hod/staffLeave.html',context)
@login_required(login_url="/")
def staffApproveLeave(request,id):
    leave =Staff_Leave.objects.get(id = id)
    leave.status = 1
    leave.save()
    return redirect('staffLeaveViews')
@login_required(login_url="/")
def staffRejectLeave(request,id):
    leave =Staff_Leave.objects.get(id = id)
    leave.status = 2
    leave.save()
    return redirect('staffLeaveViews')

def staffFeedback(request):
    feedback = Staff_Feedback.objects.all()
    context ={
        'feedback':feedback,
    }
    return render(request,'hod/staffFeedback.html',context)
def staffFeedbackSave(request):
    if request.method =="POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = Staff_Feedback.objects.get(id = feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.save()
        return redirect('staffFeedbackReply')
def getStudentFeedback(request):
    feedback = Student_Feedback.objects.all()
    feedback_history = Student_Feedback.objects.all().order_by('-id')[0:5]
    context = {
        'feedback': feedback,
        'feedback_history':feedback_history,
    }
    #return render(request, 'hod/getStudentFeedback.html', context)
    return render(request,'Hod/studentfeedback.html',context)

def studentFeedbackReplySave(request):
    if request.method =="POST":
        feedback_id =request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')
        feedback = Student_Feedback.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status =1
        feedback.save()
        return redirect('getStudentFeedback')


def studentSendNotification(request):
    student = Student.objects.all()
    notification = Student_Notification.objects.all()
    context = {
        'student':student,
        'notification':notification
    }
    return render(request,'hod/studentNotifications.html',context)
def saveStudentNotification(request):
    if request.method == "POST":
        message =request.POST.get('message')
        student_id = request.POST.get('student_id')

        student =Student.objects.get(admin = student_id)
        #print(student)
        #print(message,student_id)
        stud_notifications = Student_Notification(
            student_id = student,
            message = message,

        )
        stud_notifications.save()
        messages.success(request,'Sent Course Successfully')
        return redirect('studentSendNotification')
def studentLeaveView(request):
    student_leave = Student_Leave.objects.all()
    context = {
        'student_leave':student_leave,

    }
    return render(request,'hod/studentLeave.html',context)
def studentApproveLeave(request,id):
    student_leave = Student_Leave.objects.get(id = id)
    student_leave.status = 1
    student_leave.save()
    return redirect('studentLeaveView')
def studentRejectLeave(request,id):
    student_leave = Student_Leave.objects.get(id=id)
    student_leave.status = 2
    student_leave.save()
    return redirect('studentLeaveView')

