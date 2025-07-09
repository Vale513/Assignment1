from django.shortcuts import render

def analog_clock(request):
   return render(request, 'clock/clock.html')


