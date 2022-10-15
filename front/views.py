from django.shortcuts import render
from django.views.generic import TemplateView, View, CreateView, ListView, UpdateView, DeleteView
# Create your views here.

class HomeView(View):
    template_name = 'page/home.html'
    
    def get(self,request):
        return render(request, self.template_name, locals())
    

class SingleView(View):
    template_name = "page/single-post.html"
    
    def get(self,request):
        return render(request, self.template_name, locals())

class ContactView(View):
    template_name = "page/contact.html"
    
    def get(self,request):
        return render(request, self.template_name, locals())