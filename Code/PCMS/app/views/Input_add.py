from django.shortcuts import render, redirect
from Code.PCMS.app import models


def input_add(request):
    return render(request, "create_hand.html")
