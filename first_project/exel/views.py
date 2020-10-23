from django.http import HttpResponse
from django.shortcuts import render
import random
# Create your views here.

def generate_secret():
    x = random.sample([1,2,3,4,5,6,7,8,9,0],4)
    return x

def count_bulls(answer,guess):
    bulls = 0
    i = 0
    while i < len(guess):
        i = i + 1
        if guess[i] == answer[i]:
            bulls =+1
    return bulls

def count_cows(answer,guess):
    cows = 0
    i = 0
    while i < len(guess):
        i = i + 1
        if guess in answer:
            cows =+1
    return cows

def result(request):
    answer = generate_secret()
    guess = [1,2,3,4]
    bulls = count_bulls(answer,guess)
    cows = count_cows(answer,guess)
    return render(request,'exel/home.html',{'bulls':bulls,'cows':cows})
