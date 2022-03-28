from django.shortcuts import render

def cart(request):
    return render(request, "cart.html")

def thankyoupage(request):
    return render(request, "typ.html")