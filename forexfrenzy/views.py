import matplotlib.pyplot as plt
from io import BytesIO
from django.http import HttpResponse
from forexfrenzy.models import Rates

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def features(request):
    return render(request, 'forexfrenzy/features.html')

def contact(request):
    return render(request, 'forexfrenzy/contact.html')

def rates(request):
    return render(request, 'forexfrenzy/rates.html')

def terms(request):
    return render(request, 'forexfrenzy/terms.html')
def privacy(request):
    return render(request, 'forexfrenzy/privacy.html')

def static_chart_view(request):
    # Generování grafu
    queryset = Rates.objects.all()

    currency = list()
    values = list()

    for obj in queryset:
        currency.append(obj.currency)
        values.append(obj.cnb)

    fig, ax = plt.subplots()

    ax.bar(currency, values)
    ax.set_title("Simple Static Bar Chart")
    ax.set_ylabel("Values")

    # Uložení grafu do paměti
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Odeslání grafu jako HTTP odpověď
    return HttpResponse(buffer, content_type='image/png')