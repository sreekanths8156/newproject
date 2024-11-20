from django.shortcuts import render,redirect
from newapp.models import Department,User,Teacher,Student
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

def dep_add(request):
    if request.method=="POST":
        d=request.POST["dep"]
        x=Department.objects.create(DEPNAME=d)
        x.save()
        return HttpResponse("success")
    else:
        return render(request,'dep_add.html')    

def adminhome(request):
    return render(request,'adminhome.html') 

def reg_teacher(request):
    if request.method=="POST":
        d=request.POST['dep']
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        u=request.POST['uname']
        p=request.POST['password']
        a=request.POST['age']
        ad=request.POST['address']
        q=request.POST['qual']
        x=User.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=p,USERTYPE='teacher')
        x.save()
        y=Teacher.objects.create(Tid=x,Depid_id=d,age=a,Address=ad,Qualification=q)
        y.save()
        return HttpResponse("success")
    else:
        x=Department.objects.all()
        return render(request,'reg_teacher.html',{'x1':x})    


def mainhome(request):
    return render(request,'mainhome.html')

def reg_student(request):
    if request.method=="POST":
        d=request.POST['dep']
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        u=request.POST['uname']
        p=request.POST['password']
        a=request.POST['age']
        ad=request.POST['address']
        x=User.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=p,USERTYPE='student',is_active=False)
        x.save()
        y=Student.objects.create(Depid_id=d,sid=x,age=a,Address=ad)
        y.save()
        return HttpResponse("student registerd")
    else:
        x=Department.objects.all()
        return render(request,'reg_student.html',{'x1':x})    

def viewstudents(request):
    x=Student.objects.all()
    return render(request,'viewstudents.html',{'x1':x})        


def approve(request,aid):
    st=Student.objects.get(id=aid)
    st.sid.is_active=True
    st.sid.save()
    return redirect(viewstudents)

def logins(request):
    if request.method=="POST":
        print('/////////////////////   loginn')
        u=request.POST['username']
        p=request.POST['password']
        user=authenticate(request,username=u,password=p)
        if user is not None and user.is_superuser==1:
            print('////////////////////////////  admin')
            return redirect(adminhome)
        elif user is not None and user.USERTYPE=="teacher":
            login(request,user)
            request.session['teach_id']=user.id
            return redirect(teachhome)
        elif user is not None and user.USERTYPE=="student" and user.is_active==1:
            print('////////////////////////////////////////////////////////////////////////////////student')
            login(request,user)
            request.session['stud_id']=user.id
            return redirect(studhome)
        else:
            return HttpResponse("not valid")
    else:
        return render(request,'logins.html')

def teachhome(request):
    return render(request,'teachhome.html')

def studhome(request):
    return render(request,'studhome.html')                                


def approved_stview(request):
    x=User.objects.filter(is_active=1,USERTYPE="student")
    return render(request,'approved_stview.html',{'x':x})

def updatest(request):
    stud=request.session.get('stud_id')
    student=Student.objects.get(sid_id=stud)
    user=User.objects.get(id=stud)
    return render(request,'updatest.html',{'view':student,'data':user})

def updatestudent(request,uid):
    if request.method=="POST":
        stud=Student.objects.get(id=uid)
        sid=stud.sid_id
        user=User.objects.get(id=sid)
        user.first_name=request.POST['fname']    
        user.last_name=request.POST['lname']    
        user.email=request.POST['email']    
        user.username=request.POST['uname']  
        user.save()
        stud.age=request.POST['age']
        stud.Address=request.POST['address']
        stud.save()
        return HttpResponse("success")  

def updatetr(request):
    teach=request.session.get('teach_id')
    teacher=Teacher.objects.get(Tid_id=teach)
    user=User.objects.get(id=teach)
    return render(request,'updatetr.html',{'view':teacher,'data':user})   



def updateteacher(request,aid):
    if request.method=="POST":
        teach=Teacher.objects.get(id=aid)
        Tid=teach.Tid_id
        user=User.objects.get(id=Tid)
        user.first_name=request.POST['fname']    
        user.last_name=request.POST['lname']    
        user.email=request.POST['email']    
        user.username=request.POST['uname']  
        user.save()
        teach.age=request.POST['age']
        teach.Address=request.POST['address']
        teach.Qualification=request.POST['qual']
        
        teach.save()
        return HttpResponse("success")  



def viewteacher(request):
    x=Teacher.objects.all()
    return render(request,'viewteacher.html',{'x1':x})       
        


def lgout(request):
    logout(request)
    return redirect(logins)  


def deletest(request,id):
    x=User.objects.get(id=id)
    x.delete()
    return redirect(viewstudents)  

def deletetr(request,id):
    x=User.objects.get(id=id)
    x.delete()
    return redirect(viewteacher)       

def depbystudent(request):
    teacher=Teacher.objects.get(Tid=request.user)
    department_students=Student.objects.filter(Depid=teacher.Depid) 

    return render(request,'department_students.html',{'x1':department_students}) 
        
        
def depbyteacher(request):
    student=Student.objects.get(sid=request.user)
    department_teachers=Teacher.objects.filter(Depid=student.Depid)

    return render(request,'department_teachers.html',{'x1':department_teachers})



def index(request):
    return render(request,'index.html')        





    
