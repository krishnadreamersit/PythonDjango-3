from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def index(request):
    # values - source (static, url, web form, file, database, network, api)
    """
    id=1
    name="Bikki Goit"
    address ="KTM"
    office = "Broadway InfoSys"
    context = {'id':id, 'name':name, 'address':address, 'office': office}
    return render(request, 'app6_1/index.html', context)
    """
    # Tags

    # autoescape
    """
    context = {'var1': '<strong>Welcome to Broadway</strong>'}
    return render(request, 'app6_1/index.html', context)
    """
    # comment
    # csrf_token # web form
    # debug # settings.py -> DEBUG = True

    # cycle
    # for loop
    """
    persons = [
        {'id':1, 'name':'Bikki Goit', 'address':'KTM'},
        {'id':2, 'name':'Sanjaya Sharma', 'address':'LAT'},
        {'id':3, 'name':'Tript Gurung', 'address':'BHK'},
        {'id':4, 'name':'Krishna Aryal', 'address':'KTM'},
    ]
    context = {'persons':persons}
    return render(request, 'app6_1/index2.html', context)
    """

    # firstof
    """
    var1 = None
    var2 = None
    var3 = None
    return render(request, 'app6_1/index.html', {'var1':var1, 'var2':var2, 'var3':var3})
    """

    # for … empty
    """
    persons = [
        {'id': 1, 'name': 'Bikki Goit', 'address': 'KTM'},
        {'id': 2, 'name': 'Sanjaya Sharma', 'address': 'LAT'},
        {'id': 3, 'name': 'Tript Gurung', 'address': 'BHK'},
        {'id': 4, 'name': 'Krishna Aryal', 'address': 'KTM'},
    ]
    return render(request, 'app6_1/index.html', {'persons': persons})
    """

    # if
    """
    values={'n1':34, 'n2':43}
    return render(request, 'app6_1/index.html', {'values': values})
    """

    # ifchanged
    # ?

    # extends
    # block
    """
    return render(request, 'app6_1/child.html')
    """

    # include
    return render(request, 'app6_1/body.html')

    # load ?
    # regroup ? # Record Grouping


def filter_test(request):
    # add
    # return render(request, 'app6_1/index2.html',{'n1':'2', 'n2':'4'})
    dt1 = datetime.now()
    persons = [
        {'name': 'zed', 'age': 19},
        {'name': 'amy', 'age': 22},
        {'name': 'joe', 'age': 31},
    ]
    return render(request, 'app6_1/index2.html',{'n1':'2', 'n2':'4', 'dt1':dt1, 'persons': persons, 'str1':"person"})
