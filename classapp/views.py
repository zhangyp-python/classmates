from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import render, redirect

# Create your views here.
from classapp.models import ClassMates, Mates_node


def classmates(request):
    num = request.GET.get('num')
    num1 = request.session.get('num')
    pagtor = Paginator(ClassMates.objects.all(), per_page=30)
    if num:
        page=pagtor.page(num)
        return render(request,'classmates.html',{'page':page})
    # elif num1=='ok':
    #     page = pagtor.page(pagtor.page_range[-1])
    #     return render(request, 'classmates.html', {'page': page})
    elif num1:
        page = pagtor.page(num1)
        return render(request, 'classmates.html', {'page': page})
    else:
        page = pagtor.page(1)
        return render(request, 'classmates.html', {'page': page})
def addMate(request):



    return render(request, 'addMate.html')


def add(request):

    with transaction.atomic():

        name = request.POST.get('name')
        t_n1 = request.POST.get('telephone')

        t_n2=request.POST.get('gender')

        ClassMates.objects.create( name=name, t_n1=t_n1, t_n2=t_n2)
        return redirect('classapp:classmates')
def delMate(request):
    add = request.GET.get('id')
    print(add)
    num = request.GET.get('num')
    num2 = request.GET.get('num2')
    num3 = request.GET.get('num3')


    if add:

        if int(num2) > int(num3):
            request.session['num'] = num
        elif num2 == num3:
            request.session['num'] = int(num) - 1
        with transaction.atomic():
            ClassMates.objects.filter(id=add).delete()
            return redirect('classapp:classmates')
    else:
        return redirect('classapp:classmates')

def update_mate_node(request):
    add = request.GET.get('id')


    if add:

        cm=ClassMates.objects.filter(id=add)[0]

        return render(request,'update_mate_node.html',{'cm':cm})
    else:
        add=request.session.get('id')
        cm = ClassMates.objects.filter(id=add)[0]

        return render(request, 'update_mate_node.html', {'cm': cm})


def update(request):
    id = request.GET.get('id')
    request.session['id']=id
    if id:


        user=ClassMates.objects.filter(id=id)
        if user:

            with transaction.atomic():
                node=request.POST.get('node')
                mate_node=user[0]
                Mates_node.objects.create(node=node,mate_node=mate_node)


                return redirect('classapp:class_mate_node')
        else:
            return redirect('classapp:update_mate_node')
def class_mate_node(request):
    num = request.GET.get('num')
    id=request.GET.get('id')

    if id:
        request.session['id']=id
        pagtor = Paginator(Mates_node.objects.filter(mate_node__id=id), per_page=4)
        if num:
            page = pagtor.page(num)
            return render(request, 'class_mate_node.html', {'page': page})

        else:
            page = pagtor.page(1)
            return render(request, 'class_mate_node.html', {'page': page})
    else:
        id=request.session.get('id')
        pagtor = Paginator(Mates_node.objects.filter(mate_node__id=id), per_page=4)
        if num:
            page = pagtor.page(num)
            return render(request, 'class_mate_node.html', {'page': page})

        else:
            page = pagtor.page(1)
            return render(request, 'class_mate_node.html', {'page': page})