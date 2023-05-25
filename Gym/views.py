from django.shortcuts import render
from membershipform.forms import ClienteForm

def home(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('membershipform:solicitud_exitosa')
    else:
        form = ClienteForm()
    context = {'form': form}  # Pass the form to the context dictionary
    return render(request, 'home.html', context)

def about(request):
    print("about")
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

