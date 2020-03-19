from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    '''
    handles requests to the home page.
    '''
    # return render(request, 'core/home.html')
    return redirect('hrmsApp:login')