"""
URL configuration for ChargeFuel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from development import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="index.html"),
    path("homelink",views.home),
    path("aboutlink",views.about),
    path("servicelink",views.service),
    path("contactlink",views.contact),
    path("signuplink",views.signup),
    path("loginlink",views.login),
    path("custdashboardlink",views.custdashboard),
    path("settinglink",views.passwordsetting),
    path("deletelink",views.deleteacc),
    path("authlogin",views.authlogin),
    path("feedbacklink", views.feedback),
    path("orderlink", views.order),
    path("orderfuellink", views.orderfuel),
    path("orderevlink", views.orderev),
    path("complainlink", views.complain),
    path("authlink", views.authdashboard),

    path("load_account", views.loadaccount),

    path("load_order", views.loadevorder),

    path("load_order", views.loadfuelorder),

    path("load_complain", views.loadcomplain),

    path("load_feedback", views.loadfeedback),


    # Database Connectivity Codes

    path("signupcodedb",views.signupcode),
    path("logincodedb",views.logincode),
    path("ps", views.passwordchangecode),
    path("da", views.deleteaccountcode),
    path("al", views.authlogincode),
    path("feed", views.feedbackcode),
    path("contactcodedb", views.contactcode),
    path("orderf", views.orderfuelcode),
    path("orderev", views.orderevcode),
    path("comp", views.complaincode),

]
