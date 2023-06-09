from django.shortcuts import render
from membershipform.forms import ClienteForm
from django.shortcuts import redirect

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

def horarios(request):
    print("horarios")
    return render(request, 'horarios.html')

def servicios(request):
    print("servicios")
    return render(request, 'servicios.html')


def contacto(request):
    return render(request, 'contacto.html')

def planes(request):
    return render(request, 'planes.html')


