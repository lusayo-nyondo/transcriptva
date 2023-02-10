from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader

from transcriptva_clienthub.models import (
    Notification,
    DashboardPost
)

def index(request):
    if not request.user.is_authenticated:
        return redirect('sign_in')

    template = loader.get_template('transcriptva_clienthub/home/index.dtl.html')
    
    context = {
        'user': request.user,
        'notifications': [],
        'dashboard_posts': []
    }

    notifications = Notification.objects.all()
    dashboard_posts = DashboardPost.objects.all()

    context['notifications'] = notifications
    context['dashboard_posts'] = dashboard_posts

    return HttpResponse(template.render(
        context,
        request
    ))

def notifications(request):
    if not request.user.is_authenticated:
        return redirect('sign_in')
    
    template = loader.get_template('transcriptva_clienthub/home/notifications.dtl.html')
    context = {
        'notifications': []
    }

    notifications = Notification.objects.all()

    context['notifications'] = notifications

    return HttpResponse(template.render(
        context,
        request
    ))