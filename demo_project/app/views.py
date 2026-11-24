from django.shortcuts import render
from django.views.generic import CreateView, ListView, FormView
from .models import *
from .forms import *
from django.urls import reverse_lazy
# Create your views here.

class ServicesView(ListView):
    model = Service
    template_name = "services.html"
    context_object_name = 'service'
    paginate_by = 3

class DoctorView(ListView):
    model = Doctor
    template_name = "doctors.html"
    context_object_name = 'doctor'
    paginate_by = 3

class RequestView(ListView):
    model = Request
    template_name = "request.html"
    context_object_name = 'request'
    paginate_by = 3

class NewRequestView(FormView):
    form_class = RequestFrom
    template_name = "new_request.html"
    success_url = reverse_lazy('request-form')

    def form_valid(self, form):
        request_obj = form.save(commit=False)
        request_obj.status = "new"
        request_obj.save()
        return super().form_valid(form)
    
class AddCommentView(CreateView):
    model = Comment
    form_class = CommentFrom
    template_name = "add_comment.html"
    success_url = reverse_lazy('request-list')
