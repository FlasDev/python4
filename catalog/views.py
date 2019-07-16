from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Book, Author, BookInstance, NameForm


# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    return render(
        request,
        'index.html',
        context={'num_books': num_books,
                 'num_instance': num_instances,
                 'num_instances_available': num_instances_available,
                 'num_authors': num_authors},
    )



def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'index.html', {'form': form})

