from django.shortcuts import render
from django.http import Http404,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.


monthly_challenges={
    "january":"Do not eat meat whole month ",
    "february":"walk at least 20 minutes",
    "march":"learn django for 20 minutes",
    "april":"learn advanced python",
    "may":"learn spring and spring boot",
    "june":"learn angular",
    "july":"learn react",
    "august":"learn cloud technologies",
    "september":"learn devops",
    "october":"learn microservices",
    "november":"learn website automation",
    "december":None
}


def index(request):
    month_list=monthly_challenges.keys()
    return render(request,"challenges/index.html",{
        'months':month_list
    })

def monthly_challenges_by_number(request,month):
    months=list(monthly_challenges.keys())
    if month > len(months):
        raise Http404()
    redirect_month=months[month-1]
    redirect_path=reverse("monthly_challenge",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges_by_name(request,month):
     try:
         challenges_text=monthly_challenges[month]
        # challenges_text=render_to_string('challenges/challenge.html')
     except:
         raise Http404()
     return render(request,'challenges/challenge.html',
                   {"text":challenges_text,
                    "month_name":month,
                    })
