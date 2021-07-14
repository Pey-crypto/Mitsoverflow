from django.shortcuts import render,redirect
from forum.models import * 
from django.contrib.auth.models import User
from datetime import date
import secrets
from django.http import HttpResponseRedirect

def home(request):
    try:
        item = forum.objects.all()
    except:
        item = None
    return render(request,"index.html",{'item':item})

def new_forum(request):
    if request.method == 'POST':
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        current_user = request.user
        name = request.POST.get("name")
        pri  = request.POST.get("privacy")
        email = current_user.email
        topic = request.POST.get("topic")
        description = request.POST.get("description")


        new_entry = forum(
            name = name,
            email = email,
            topic = topic,
            description = description,
            date_created = d1,
            privacy = pri,
            link = "forum/"+secrets.token_urlsafe(11),
        )

        new_entry.save()
        f = forum.objects.get(email = email, name = name, topic = topic,description = description,privacy = pri)
        f_id = f.fid
        new_entry1 = memeber_info(
                name = name,
                forum_id = f_id,
                email = email,)
        new_entry1.save()
        try:
            item = forum.objects.all()
        except:
            item = None


    return redirect('home')


def forum_view(request,base64string):
    return render(request,"dyna.html")

def profile(request):
    current_user = request.user
    count = 0
    try:
            item = forum.objects.filter(email = current_user.email )
            for i in item:
                count=count+1
    except:
            item = None
    try:
            memb = memeber_info.objects.filter(email = current_user.email )
            dic = []
            for i in memb:
                f = memeber_info.objects.get(fid = i.forum_id)
                print(f.topic)
                dic.append(f.topic)


    except:
            memb = None
    print(memb)

    return render(request,"profile.html",{'user':current_user,'count':count,'dic':dic})


def open_thread(request,t_id):
    current_user = request.user
    email = current_user.email
    t_id = int(t_id)
    try:
        thread = Thread.objects.get(tid = t_id)
    except:
        thread = None
    try:
        r1 = Reply_thread.objects.filter(thread_id = t_id,email = email)
    except:
        r1 = None
    try:
        r2 = Reply_thread.objects.filter(thread_id = t_id).exclude(email = email)
    except:
        r2 = None
    return render(request,"open_thread.html",{'thread':thread,'r1':r1,'r2':r2})

def reply(request):
    if request.method == 'POST':
        current_user = request.user
        email = current_user.email
        thread_id = request.POST.get("thread_id")
        reply = request.POST.get("reply")
        obj1 = Thread.objects.get(tid = thread_id)
        f_id = obj1.forum_id
        print(thread_id)
        print(f_id)
        
        try:
            obj = memeber_info.objects.get(email = email, forum_id = f_id)
            
            name = obj.name

            new_entry = Reply_thread(
                name = name,
                email = email,
                thread_id = thread_id,
                reply = reply,
            )

            new_entry.save()
        except:
            obj = None

    return open_thread(request,thread_id)

def join_forum(request):
    if request.method == 'POST':
        name = request.POST.get("name1")
        f_id = request.POST.get("forum_id1")
        current_user = request.user
        email = current_user.email
        try:
            obj = memeber_info.objects.get(email = email, forum_id = f_id)
        except memeber_info.DoesNotExist:
            new_entry = memeber_info(
                name = name,
                forum_id = f_id,
                email = email,)
            new_entry.save()
        try:
            f = forum.objects.get(fid = f_id)
        except:
            f = None
        try:
            t = Thread.objects.filter(forum_id = f_id)
        except:
            t = None
        try:
            m = memeber_info.objects.filter(forum_id = f_id)
        except:
            m = None
    return render(request,"forum.html",{'forum':f,'thread':t,'member':m})

def new_thread(request):
    if request.method == 'POST':
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        current_user = request.user
        email = current_user.email
        topic = request.POST.get("topic")
        forum_id = request.POST.get("forum_id")
        description = request.POST.get("description")
        try:
            obj = memeber_info.objects.get(email = email, forum_id = forum_id)
            name = obj.name
            new_entry = Thread(
                name = name,
                email = email,
                topic = topic,
                description = description,
                date_created = d1,
                forum_id = forum_id,
            )

            new_entry.save()
        except:
            obj = None


    return open_forum(request,forum_id)

def open_forum(request,f_id):
    current_user = request.user
    email = current_user.email
    try:
        checker = memeber_info.objects.get(forum_id = f_id,email=email)
    except:
        checker = None
    try:
        f = forum.objects.get(fid = f_id)
    except:
        f = None
    try:
        t1 = Thread.objects.filter(forum_id = f_id,email = email)
    except:
        t1 = None
    try:
        t2 = Thread.objects.filter(forum_id = f_id).exclude(email = email)
    except:
        t2 = None
    try:
        m = memeber_info.objects.filter(forum_id = f_id)
    except:
        m = None
    return render(request,"forum.html",{'forum':f,'thread1':t1,'thread2':t2,'member':m,'checker':checker})

def exit_forum(request):
    current_user = request.user
    email = current_user.email
    if request.method == 'POST':
        f_id = request.POST.get("forum_id2")
        try:
            f = memeber_info.objects.get(forum_id = f_id, email = email)
            f.delete()
        except:
            f = None
    return redirect('home')

def delete_thread(request,t_id):
    current_user = request.user
    email = current_user.email
    try:
        f = Thread.objects.get(tid = t_id)
        f_id = f.forum_id
        f.delete()
    except:
        f = None
    print(f)
    return open_forum(request,f_id)

def delete_reply(request,r_id):
    current_user = request.user
    email = current_user.email
    try:
        f = Reply_thread.objects.get(repid = r_id)
        t_id = f.thread_id
        f.delete()
    except:
        f = None
    return open_thread(request,t_id)





