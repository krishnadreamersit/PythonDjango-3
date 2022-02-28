from django.shortcuts import render


def index(request):
    if request.method =='POST':
        user = request.POST.get('txt_user')
        password = request.POST.get('txt_password')
        if user =='admin' and password == 'admin': # you can take value from database table
            request.session['user'] = user
            return render(request, 'app8_1/display_result.html', {'user': user, 'flag': True})
    return render(request, 'app8_1/login.html')


def check_session(request):
    if request.session.has_key('user'):
        user = request.session['user']
        return render(request, 'app8_1/display_result.html', {'user': user, 'flag': True})
    else:
        return render(request, 'app8_1/display_result.html', {'user': 'NA', 'flag': False})


def check_session2(request):
    if request.session.has_key('user'):
        user = request.session['user']
        return render(request, 'app8_1/display_result.html', {'user': user, 'flag': True})
    else:
        return render(request, 'app8_1/display_result.html', {'user': 'NA', 'flag': False})