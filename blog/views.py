from django.shortcuts import render


def allblogs(request):
    return render(request,'blog/allblogs.html')


def hey(request):
    return render(request, 'blog/hey.html')
