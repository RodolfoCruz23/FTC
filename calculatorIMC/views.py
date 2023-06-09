from django.shortcuts import render

def calculate_bmi_view(request):
    if request.method == 'POST':
        weight = float(request.POST['weight'])
        height = float(request.POST['height'])

        # Realiza el cálculo del IMC
        bmi = weight / (height ** 2)

        context = {'bmi': bmi}
        return render(request, 'calculatorIMC/result.html', context)

    return render(request, 'calculatorIMC/form.html')