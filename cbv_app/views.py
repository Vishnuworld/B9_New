from django.shortcuts import render
from http import HTTPStatus
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View  


class NewView(View):  
    def get(self, request):  
        print("in get method")
        return HttpResponse('get response') # 200 - OK
     
    def post(self, request):  
        data = request.POST
        nm = data.get("name")
        age = data.get("age")
        print("in post method")
        return HttpResponse('post response', status=HTTPStatus.CREATED)  # 201 - Resource Created
    
    # put, patch, delete - 204


from django.views.generic.edit import CreateView  
from .models import Employee

class EmployeeCreate(CreateView):  
    model = Employee  
    fields = '__all__'  # form
    success_url = "http://127.0.0.1:8000/cbv/emp-create/"

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        print("saving the data in database")
        self.object = form.save()  # save 
        return super().form_valid(form)


from django.views.generic.list import ListView

class EmployeeList(ListView):  # object_list
    model = Employee
    context_object_name = "all_employees"
    ordering = "-email"  # field name -- id, first_name
    # queryset = Employee.objects.filter(is_active=1)


from django.views.generic.detail import DetailView

class EmployeeDetailView(DetailView):
    model = Employee  # Employee.objects.get(id=1)
    context_object_name = "single_employee"

    def get_object(self, queryset=None):
        """
        Return the object the view is displaying.

        Require `self.queryset` and a `pk` or `slug` argument in the URLconf.
        Subclasses can override this to return any object.
        """
        # Use a custom queryset if provided; this is required for subclasses
        # like DateDetailView
        if queryset is None:
            queryset = self.get_queryset()

        # Next, try looking up by primary key.
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)

        # Next, try looking up by slug.
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})

        # If none of those are defined, it's an error.
        if pk is None and slug is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )

        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            return "No Data"
        return obj

    def get(self, request, *args, **kwargs):  # overridden method
        self.object = self.get_object()  # "No Data"   str and Employee
        print(type(self.object))
        if type(self.object) ==  str:
            return HttpResponse("No Data Found")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)



from django.views.generic.edit import DeleteView


class EmployeeDetailView(DeleteView):
    model = Employee 
    # success_url = 

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        # self.object.is_active = 0  # soft delete
        # self.object.save()
        return HttpResponseRedirect(success_url)
    

class MohiniView(DeleteView):
    pass