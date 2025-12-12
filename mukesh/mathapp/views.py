from django.shortcuts import render

def lamp_power(request):
    print("Request :", request)
    context = {}
    context['power'] = "0"
    context['I'] = "0"
    context['R'] = "0"

    if request.method == "POST":
        print("POST method is used")

        I = request.POST.get('current', '0')
        R = request.POST.get('resistance', '0')

        print("Current :", I)
        print("Resistance :", R)

        try:
            power = (float(I) * float(I)) * float(R)
        except:
            power = "Invalid"

        context['power'] = power
        context['I'] = I
        context['R'] = R

        print("Power :", power)

    return render(request, 'mathapp/math.html', context)