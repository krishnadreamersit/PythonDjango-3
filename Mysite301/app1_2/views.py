from django.shortcuts import render

# Create your views here.
def index(request):
    # Receive value form url
    tmpid = request.GET.get('id')
    tmpname = request.GET.get('name')

    # Sending value to html template
    context = {'id': tmpid, 'name': tmpname} # Packaging received value
    return render(request, 'app1_2/index.html', context)


def get_value2(request, pid):
    context = {'pid': pid}
    return render(request, 'app1_2/display2.html', context)
