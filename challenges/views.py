from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.


# def january(request):
#    return HttpResponse("Do not eat oily food for a month")
#
#
# def february(request):
#    return HttpResponse("Walk for 20 mins every day")
#
#
# def march(request):
#    return HttpResponse("Learn something for 30min everyday")

# so on we can do for 12 months but its time consuming for


# def monthly_challenge(request, month):
#    challenge_text = None
#    if month == "january":
#        challenge_text = "Eat no Sugar"
#    elif month == "february":
#        challenge_text = "Walk for 20 min daily!"
#    elif month == "march":
#        challenge_text = "Learn Programming for 30 mins atleast!"
#    else:
#        return HttpResponseNotFound("This month is not supported")
#    return HttpResponse(challenge_text)
#
#
# def monthly_challenge_by_number(request, month):
#    return HttpResponse(month)


# More Dynamic Way of doing the above things
monthly_challenges = {
    "january": "Eat No Sugar for a Month",
    "february": "Walk for 30mins daily!",
    "march": "Go for a toor!",
    "april": "Solve coading questions daily atleast 2",
    "may": "join in coading contests",
    "June": "Make your own blog",
    "july": "Take rest and enjoy",
    "August": "Learn about machine learning concepts",
    "september": "Sleep",
    "october": "Go to gym",
    "november": "prepare for interview",
    "december": "Time for some django education"

}


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Error not a valid nmonth")
    forward_month = months[month-1]
    return HttpResponseRedirect("/challenges/"+forward_month)
