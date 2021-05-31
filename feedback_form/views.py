from django.shortcuts import render
from .forms import InputForm
from feedback_form.models import feedback_response

# Create your views here.
def response_page(request):
    responses = feedback_response.objects.all().order_by('-created_on') 
    context = {
        "responses" : responses,
    }
    return render(request, "response_page.html", context)

def response_form(request):
    form = InputForm()
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            Response = feedback_response(
                name = form.cleaned_data["name"],
                email_id = form.cleaned_data["email_id"],
                rating = form.cleaned_data["rating"],
                comment = form.cleaned_data["comment"],
            )
            Response.save()
    context = {
        "form" : form
    }
    return render(request, "response_form.html", context)
