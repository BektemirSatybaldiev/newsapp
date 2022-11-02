from django.shortcuts import render
from django.views import View


class MainView(View):
    def homepage(request):
        return render(
            request,
            'home.html')

    def signup(request):
        return render(request, 'signup.html')

    def contacts(request):
        return render(request, 'contacts.html')

    def search(request):
        return render(request, 'search.html')

    def signin(request):
        return render(request, 'signin.html')
