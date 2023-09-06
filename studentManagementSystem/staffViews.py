from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import Staff,Staff_Notification,Staff_Leave,Staff_Feedback,Subject,Session_Year
from django.contrib import messages
@login_required(login_url="/")
def home(request):
    return render(request,'staff/home.html')
@login_required(login_url="/")
def staffNotifications(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id

        notifications = Staff_Notification.objects.filter(staff_id = staff_id)

        context = {
            'notification':notifications,
        }
        return render(request,'staff/staffNotifications.html',context)
@login_required(login_url="/")
def staffNotificationsMarkAsDone(request,status):
    notification =Staff_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('staffNotification')
@login_required(login_url="/")
def staffApplyLeave(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id

        staff_leave_history =Staff_Leave.objects.filter(staff_id = staff_id)

        context ={
            'staff_leave_history':staff_leave_history,
        }
        return render(request,'staff/staffApplyLeave.html',context)
@login_required(login_url="/")
def staffApplyLeaveSave(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')
        staff = Staff.objects.get(admin = request.user.id)
        leave = Staff_Leave(
            staff_id = staff,
            date = leave_date,
            message = leave_message,
        )
        leave.save()
        messages.success(request,'Leave Applied, Wait for Approval')
        return redirect('staffApplyLeave')

@login_required(login_url="/")
def staffFeedback(request):
    staff_id = Staff.objects.get(admin = request.user.id)
    feedback_history =  Staff_Feedback.objects.filter(staff_id = staff_id)
    context ={
        'feedback_history':feedback_history,
    }
    return render(request,'staff/feedback.html',context)
@login_required(login_url="/")
def staffFeedbackSave(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')
        staff = Staff.objects.get(admin = request.user.id)

        feedback = Staff_Feedback(
            staff_id = staff,
            feedback = feedback,
            feedback_reply = '',

        )
        feedback.save()
        return redirect('staffFeedback')
def staffTakeAttendance(request):
    staff_id =Staff.objects.get(admin = request.user.id)

    subject = Subject.objects.filter(staff = staff_id)
    session_year = Session_Year.objects.all()

    return render(request,'staff/takeAttendance.html')
