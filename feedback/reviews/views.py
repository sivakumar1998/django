from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import  TemplateView
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView,CreateView
# Create your views here.
class ReviewView(CreateView):
  model=Review
  form_class=ReviewForm
  template_name='reviews/review.html'
  success_url='/thank-you'
     
#   def form_valid(self, form):
#          form.save()
#          return super().form_valid(form)
     
    # def get(self,request):
    #     form=ReviewForm()
    #     return render(request,'reviews/review.html',{
    #         'form':form
    #     })
    # def post(self,request):
    #     form=ReviewForm(request.POST)
    #     if form.is_valid():
    #         print(form)
    #         form.save()
    #         return HttpResponseRedirect("/thank-you")
    #     return render(request,'reviews/review.html')

class Thankyou(TemplateView):
    # def get(self,request):
    #     return render(request,"reviews/thank_you.html")

    template_name="reviews/thank_you.html"

    def get_context_data(self, **kwargs: Any) :
        context= super().get_context_data(**kwargs)
        context['message']='This works!'
        return context


class ReviewsListView(ListView):
    template_name="reviews/review_list.html"
    model=Review
    context_object_name="reviews"
    def get_queryset(self):
        base_query= super().get_queryset()
        # data= base_query.filter(rating__gt=4)
        return base_query

class SingleReviewView(DetailView):
    template_name="reviews/single_review.html"
    model=Review
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        loaded_review=self.object
        request=self.request
        favorite_id=request.session.get("favorite_review")
        context['is_favorite']= str(favorite_id) == str(loaded_review.id)
        print(context['is_favorite'])
        return context
class AddFavoriteView(View):
    
    def post(self,request):
        review_id=request.POST["review_id"]
        request.session["favorite_review"]=review_id
        return HttpResponseRedirect("/reviews/"+review_id)



def review(request):
    if request.method=="POST":
        form=ReviewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            review=Review(user_name=form.cleaned_data['user_name'],
                          review_text=form.cleaned_data['review_text']
                          ,rating=form.cleaned_data['rating'])
            review.save() 
            return HttpResponseRedirect("/thank-you")
    else:
        form=ReviewForm()
    return render(request,"reviews/review.html",{
        "form":form
        })

def thankyou(request):
   return render(request,"reviews/thank_you.html")