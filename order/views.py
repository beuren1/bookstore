from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


@login_required(login_url="/api-auth/login/")
def order_redirect(request):
    return redirect("/bookstore/v1/order/")


from django.shortcuts import render

# Create your views here.
