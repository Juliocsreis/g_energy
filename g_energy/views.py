from django.shortcuts import render


def homeView(request):
    return render(request, template_name='home.html')

def privacyPolicy(request):
    return render(request, 'privacy_policy.html')


def termsOfUse(request):
    return render(request, 'terms_of_use.html')


def baseApp(request):
    return render(request, 'base.html')
