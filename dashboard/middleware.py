from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings

class InactiveUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if not request.user.is_active:
                # Log out the user if their account is inactive
                from django.contrib.auth import logout
                logout(request)
                messages.error(request, "Your account has been deactivated. Please contact admin for reactivation.")
                return redirect('account_login')  # Redirect to login page
        response = self.get_response(request)
        return response
