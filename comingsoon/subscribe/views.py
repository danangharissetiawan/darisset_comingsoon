from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import Subscriber
from .forms import SubscriberForm


def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Thank you, we made sure you would get a notification'
            )
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = SubscriberForm()
    return render(request, 'index.html', {'form':form})