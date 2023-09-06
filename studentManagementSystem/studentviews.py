from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import Student_Notification,Student,Student_Feedback,Student_Leave
from django.contrib import messages

from django.contrib import messages
def home(request):
    return render(request,'student/home.html')

def studentNotification(request):
    student = Student.objects.filter(admin = request.user.id)
    for i in student:
        student_id = i.id
        notification =Student_Notification.objects.filter(student_id = student_id)
        context = {
            'notification':notification,

        }
        return render(request,'student/notification.html',context)
def studentNotificationMarkAsDone(request,status):
    notification = Student_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('studentNotification')
def studentFeedback(request):
    student_id = Student.objects.get(admin = request.user.id)
    feedback_history =Student_Feedback.objects.filter(student_id = student_id)
    context ={
        'feedback_history':feedback_history,

    }
    return render(request,'student/feedback.html',context)
def studentFeedbackSave(request):
    if request.method=="POST":
        feedback = request.POST.get('feedback')
        student = Student.objects.get(admin = request.user.id)
        feedbacks =  Student_Feedback(
            student_id = student,
            feedback = feedback,
            feedback_reply = "",

        )
        feedbacks.save()
    return redirect('studentFeedback')
def studentApplyLeave(request):
    student =Student.objects.get(admin=request.user.id)
    print(student)
    return render(request,'student/studentApplyLeave.html')
def studentLeaveSave(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')

        student_id = Student.objects.get(admin = request.user.id)

        student_leave = Student_Leave (
            student_id = student_id,
            date = leave_date,
            message = leave_message
        )
        student_leave.save()
        messages.success(request,'Leave Requested')
        return redirect('studentApplyLeave')



