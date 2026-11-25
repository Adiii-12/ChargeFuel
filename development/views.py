import datetime
import sqlite3
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"index.html")


def about(request):
    return render(request,"about.html")


def service(request):
    return render(request,"service.html")


def contact(request):
    return render(request,"contact.html")

def signup(request):
    return render(request,"signup.html")


def login(request):
    return render(request,"login.html")

def signupcode(request):
    userid = request.POST['uid']
    password = request.POST['password']
    name = request.POST['fnm']
    contact = request.POST['contact']
    mail = request.POST['mail']
    dOB = request.POST['dob']
    gender = request.POST['gender']
    address = request.POST['address']
    city = request.POST['city']
    con = sqlite3.connect("db.sqlite3");
    operation = con.cursor()
    sql = "insert into customertab values(?,?,?,?,?,?,?,?,?)"
    values = (userid,password,name,contact,mail,dOB,gender,address,city)
    operation.execute(sql, values)
    con.commit()
    con.close()
    return render(request, "signup.html",{'signup_msg':"Account Created Succesfully"})


def logincode(request):
    userid = request.POST['uid']
    password = request.POST['password']
    con = sqlite3.connect("db.sqlite3");
    operation = con.cursor()
    sql = "select * from customertab where id=? and password=?"
    values = (userid,password)
    result = operation.execute(sql, values)
    if(result.fetchone()):
        return render(request, "cust_dashboard.html")
    else:
        return render(request, "login.html", {'error_msg': "Invalid Id/Password"})



def custdashboard(request):
    return render(request,"cust_dashboard.html")


def passwordsetting(request):
    return render(request,"pwd_setting.html")


def passwordchangecode(request):
    userid = request.POST['uid']
    oldpass = request.POST['opwd']
    newpass = request.POST['npwd']
    cnewpass = request.POST['cnpwd']
    con = sqlite3.connect("db.sqlite3");
    operation = con.cursor()
    sql = "select * from customertab where id=? and password=?"
    values = (userid,oldpass)
    result = operation.execute(sql, values)
    if(result.fetchone()):
        if(newpass==cnewpass):
            sql1 = "update customertab set password=? where id=?"
            values1 = (newpass,userid)
            operation.execute(sql1,values1)
            con.commit()
            return render(request, "login.html")
        else:
            return render(request, "pwd_setting.html",{'error_msgg':"Password Doesn't Match"})

    else:
        return render(request, "pwd_setting.html", {'error_msg': "Invalid Id/Password"})



def deleteacc(request):
    return render(request,"deleteacc.html")



def deleteaccountcode(request):
    userid = request.POST['uid']
    password = request.POST['pwd']
    con = sqlite3.connect("db.sqlite3");
    operation = con.cursor()
    sql = "select * from customertab where id=? and password=?"
    values = (userid,password)
    result = operation.execute(sql, values)
    if(result.fetchone()):
        sql1 = "delete from customertab where id=? and password=?"
        values1 = (userid,password)
        operation.execute(sql1,values1)
        con.commit()
        return render(request, "index.html")
    else:
        return render(request, "deleteacc.html",{'error_msg':"Invalid ID/Password"})



def authlogin(request):
    return render(request,"authlogin.html")



def authlogincode(request):
    authid = request.POST['aid']
    password = request.POST['password']
    con = sqlite3.connect("db.sqlite3");
    operation = con.cursor()
    sql = "select * from authlogin where authid=? and password=?"
    values = (authid,password)
    result = operation.execute(sql, values)
    if(result.fetchone()):
        return render(request, "auth_dashboard.html")
    else:
        return render(request, "authlogin.html", {'error_msg': "Invalid Id/Password"})



def feedback(request):
    return render(request,"feedback.html")



def feedbackcode(request):
    userid = request.POST['uid']
    feed = request.POST['feedback']
    con = sqlite3.connect("db.sqlite3");
    operation = con.cursor()
    sql = "insert into feedbacktab values(?,?)"
    values = (userid,feed)
    operation.execute(sql, values)
    con.commit()
    con.close()
    return render(request, "feedback.html",{'feedback_msg':"Feedback Sent Succesfully"})



def order(request):
    return render(request,"order.html")

def orderfuel(request):
    return render(request,"orderfuel.html")

def orderev(request):
    return render(request,"orderev.html")



def orderfuelcode(request):
    userid = request.POST['uid']
    fuelcategory= request.POST['fuelcat']
    fueltype= request.POST['fueltype']
    quantity = request.POST['quant']
    droplocation = request.POST['drop']
    contact = request.POST['contact']
    con = sqlite3.connect("db.sqlite3");
    operation = con.cursor()
    sql = "insert into orderfueltab(id,fuelcategory,fueltype,quantity,droplocation,contact) values(?,?,?,?,?,?)"
    values = (userid,fuelcategory,fueltype,quantity,droplocation,contact)
    operation.execute(sql, values)
    con.commit()
    con.close()
    return render(request, "orderfuel.html")



def orderevcode(request):
    userid = request.POST['uid']
    droplocation = request.POST['drop']
    contact = request.POST['contact']
    con = sqlite3.connect("db.sqlite3");
    operation = con.cursor()
    sql = "insert into orderevchargetab(id,droplocation,contact) values(?,?,?)"
    values = (userid,droplocation,contact)
    operation.execute(sql, values)
    con.commit()
    con.close()
    return render(request, "orderev.html")



def complain(request):
    return render(request,"complain.html")


def complaincode(request):
    userid = request.POST['uid']
    complain = request.POST['complain']
    orderid = request.POST['orderid']
    con = sqlite3.connect("db.sqlite3");
    operation = con.cursor()
    sql = "insert into complaintab(id,complain,orderid,dateofcomplain,status) values(?,?,?,?,?)"
    values = (userid,complain,orderid,datetime.datetime.now(),"Under Process")
    operation.execute(sql, values)
    con.commit()
    con.close()
    return render(request, "complain.html",{'feedback_msg':"Complain Sent Succesfully"})



def authdashboard(request):
    return render(request,"auth_dashboard.html")


# def showaccount(request):
#     return render(request,"showaccount.html")

def  loadaccount(request):
    con = sqlite3.connect("db.sqlite3")
    operation = con.cursor()
    sql = "select *  from customertab"
    result = operation.execute(sql)
    list = result.fetchall()
    return render(request, "showaccount.html",{'data':list})



def  loadevorder(request):
    con = sqlite3.connect("db.sqlite3")
    operation = con.cursor()
    sql = "select *  from orderevchargetab"
    result = operation.execute(sql)
    list = result.fetchall()
    return render(request, "showorder.html",{'ev':list})


def  loadfuelorder(request):
    con = sqlite3.connect("db.sqlite3")
    operation = con.cursor()
    sql2 = "select *  from orderfueltab"
    result2 = operation.execute(sql2)
    list2 = result2.fetchall()
    return render(request, "showorder.html",{'fuel':list2})


def  loadcomplain(request):
    con = sqlite3.connect("db.sqlite3")
    operation = con.cursor()
    sql = "select *  from complaintab"
    result = operation.execute(sql)
    list = result.fetchall()
    return render(request, "showcomplain.html",{'comp':list})



def  loadfeedback(request):
    con = sqlite3.connect("db.sqlite3")
    operation = con.cursor()
    sql = "select *  from feedbacktab"
    result = operation.execute(sql)
    list = result.fetchall()
    return render(request, "showfeedback.html",{'feed':list})



def contactcode(request):
    name = request.POST['fnm']
    city = request.POST['city']
    contact = request.POST['contact']
    query = request.POST['query']
    con = sqlite3.connect("db.sqlite3");
    operation = con.cursor()
    sql = "insert into contacttab values(?,?,?,?)"
    values = (name,city,contact,query)
    operation.execute(sql, values)
    con.commit()
    con.close()
    return render(request, "contact.html")

