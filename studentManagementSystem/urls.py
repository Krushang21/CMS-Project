"""
URL configuration for studentManagementSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, HOD_Views, studentviews, tpoviews, parentviews, staffViews

urlpatterns = [
    path("admin/", admin.site.urls),
    path("base/",views.BASE, name='BASE'),
    path("",views.loginn, name='login'),
    path("doLogin",views.doLogin,name='doLogin'),
    path("doLogout",views.doLogout,name='logout'),

#profileupdate
    path('profile',views.profile,name='profile'),
    path('profile/update',views.profile_update,name='profile_update'),
#hodurls
    path('hod/home',HOD_Views.home, name='hod_home'),
    path('hod/Student/Add',HOD_Views.addStudent, name='addStudent'),
    path('hod/Student/View',HOD_Views.viewStudent, name='viewStudent'),
    path('hod/Student/Edit/<str:id>',HOD_Views.editStudent, name='editStudent'),
    path('hod/student/update',HOD_Views.updateStudent,name='updateStudent'),
    path('hod/student/delete/<str:admin>',HOD_Views.deleteStudent,name='deleteStudent'),
    path('hod/course/addCourse',HOD_Views.addCourse,name='addCourse'),
    path('hod/course/viewCourse',HOD_Views.viewCourse,name='viewCourse'),
    path('hod/course/editCourse/<str:id>',HOD_Views.editCourse,name='editCourse'),
    path('hod/course/updateCourse',HOD_Views.updateCourse,name='updateCourse'),
    path('hod/course/deleteCourse/<str:id>',HOD_Views.deleteCourse,name='deleteCourse'),
    path('hod/Staff/add',HOD_Views.addStaff,name="addStaff"),
    path('hod/Staff/view',HOD_Views.viewStaff,name="viewStaff"),
    path('hod/Staff/edit/<str:id>',HOD_Views.editStaff,name="editStaff"),
    path('hod/Staff/view',HOD_Views.updateStaff,name="updateStaff"),
    path('hod/course/deleteStaff/<str:admin>',HOD_Views.deleteStaff,name='deleteStaff'),
    path('hod/subject/add',HOD_Views.addSubject,name='addSubject'),
    path('hod/subject/view',HOD_Views.viewSubject,name='viewSubject'),
    path('hod/subject/edit/<str:id>',HOD_Views.editSubject,name='editSubject'),
    path('hod/subject/update',HOD_Views.updateSubject,name='updateSubject'),
    path('hod/subject/delete/<str:id>',HOD_Views.deleteSubject,name='deleteSubject'),
    path('hod/session/add',HOD_Views.addSession,name='addSession'),
    path('hod/session/view',HOD_Views.viewSession,name='viewSession'),
    path('hod/session/edit/<str:id>',HOD_Views.editSession,name='editSession'),
    path('hod/session/update',HOD_Views.updateSession,name='updateSession'),
    path('hod/session/delete/<str:id>',HOD_Views.deleteSession,name='deleteSession'),
    path('hod/staff/sendNotifications', HOD_Views.staffSendNotification, name='staffSendNotification'),
    path('hod/Staff/saveNotification',HOD_Views.saveStaffNotification,name='saveStaffNotification'),
    path('hod/student/sendNotifications', HOD_Views.studentSendNotification, name='studentSendNotification'),
    path('hod/student/saveNotification',HOD_Views.saveStudentNotification,name='saveStudentNotification'),


    path('hod/Staff/Leave_View',HOD_Views.staffLeaveViews,name='staffLeaveViews'),
    path('hod/Staff/approveLeave/<str:id>',HOD_Views.staffApproveLeave,name='staffApproveLeave'),
    path('hod/Staff/rejectLeave/<str:id>',HOD_Views.staffRejectLeave,name='staffRejectLeave'),
    path('hod/Staff/feedback',HOD_Views.staffFeedback,name='staffFeedbackReply'),
    path('hod/Staff/feedback/save',HOD_Views.staffFeedbackSave,name='staffFeedbackReplySave'),

    path('hod/Student/feedback',HOD_Views.getStudentFeedback,name='getStudentFeedback'),
    path('hod/Student/feedback/save',HOD_Views.studentFeedbackReplySave,name='studentFeedbackReplySave'),


    path('hod/student/studentLeaveView',HOD_Views.studentLeaveView,name='studentLeaveView'),
    path('hod/Student/approveLeave/<str:id>',HOD_Views.studentApproveLeave,name='studentApproveLeave'),
    path('hod/Staff/rejectLeave/<str:id>',HOD_Views.studentRejectLeave,name='studentRejectLeave'),
#staffUrls
    path('staff/home',staffViews.home, name='staff_home'),
    path('staff/Notifications',staffViews.staffNotifications, name='staffNotification'),
    path('staff/markAsDone/<str:status>',staffViews.staffNotificationsMarkAsDone, name='staffNotificationsMarkAsDone'),
    path('staff/ApplyLeave/',staffViews.staffApplyLeave, name='staffApplyLeave'),
    path('staff/ApplyLeaveSave/',staffViews.staffApplyLeaveSave, name='staffApplyLeaveSave'),
    path('staff/sendFeedback/',staffViews.staffFeedback, name='staffFeedback'),
    path('staff/Feedback/Save', staffViews.staffFeedbackSave, name='staffFeedbackSave'),
    path('staff/Take Attendance/Save', staffViews.staffTakeAttendance, name='staffTakeAttendance'),

#studentUrls
    path('student/home',studentviews.home, name='studentHome'),
    path('student/Courses',studentviews.studentNotification, name='studentNotification'), #notifications
    path('student/mark_as_done/<str:status>',studentviews.studentNotificationMarkAsDone, name='studentNotificationMarkAsDone'),
    path('student/feedback',studentviews.studentFeedback,name='studentFeedback'),
    path('student/Feedback/Save', studentviews.studentFeedbackSave, name='studentFeedbackSave'),
    path('student/ApplyLeave',studentviews.studentApplyLeave,name='studentApplyLeave'),
    path('student/LeaveSave',studentviews.studentLeaveSave,name='studentLeaveSave'),







]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

