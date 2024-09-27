from django.shortcuts import redirect
from django.contrib import messages

class InactiveUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and not request.user.is_active:
            messages.error(request, 'Your account has been deactivated. Please contact support for assistance.')
            return redirect('account_logout')  # Log out inactive users
        return self.get_response(request)
