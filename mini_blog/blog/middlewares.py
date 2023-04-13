from django.shortcuts import render

class UderConstructionMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        respnse = render(request, 'blog/siteuc.html')
        return respnse
