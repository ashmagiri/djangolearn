from django.shortcuts import redirect,render
from django.contrib.auth import get_user_model, login as auth_login, authenticate

from .forms import UserLoginForm
User = get_user_model()

from django.contrib import messages



# Create your views here.
def login(request):
    """
    loginview
    """
    if request.method == "POST":
        login_form = UserLoginForm(data=request.POST)
        if login_form.is_valid():
            user = authenticate(
                request,
                username=login_form.cleaned_data.get("username"),
                password=login_form.cleaned_data.get("password"),
            )
            print(user)
            if user:
                auth_login(
                    request,
                    user,
                    backend="django.contrib.auth.backends.ModelBackend",
                )
                messages.success(request, "Logged In Successfully")
            else:
                messages.warning(request, "Invalid Credential")

        else:
            messages.warning(request, "something went wrong")
        return redirect("/login")
    else:
        form=UserLoginForm()
        return render(request,"login.html",{"form":form})
