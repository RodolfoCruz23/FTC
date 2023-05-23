from django.shortcuts import render, redirect
from .forms import ClienteForm

def solicitud_membresia(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('membershipform:solicitud_exitosa')
    else:
        form = ClienteForm()
    return render(request, 'membershipform/solicitud_membresia.html', {'form': form})

def solicitud_exitosa(request):
    return render(request, 'membershipform/solicitud_exitosa.html')


