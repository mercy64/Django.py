# from django.shortcuts import render
# from django.http import HttpResponse
#
# # Create your views here.
# # reques
# # -> response
# #request handler
# #action
# def say_hello(request):
#     x = 2
#     y = 3
#     return render(request, 'polls/hello.html')
#

from django.shortcuts import render
from .models import Author

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'playground/author_list.html', {'authors': authors})


# playground/views.py
from .forms import AuthorForm
from django.shortcuts import render, redirect

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'playground/author_form.html', {'form': form})

# playground/views.py
def author_edit(request, id):
    author = Author.objects.get(id=id)  # Get the existing author
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()  # Save the updated author
            return redirect('author_list')  # Redirect to the author list page
    else:
        form = AuthorForm(instance=author)
    return render(request, 'playground/author_form.html', {'form': form})



# playground/views.py
def author_delete(request, id):
    author = Author.objects.get(id=id)  # Get the author to delete
    author.delete()  # Delete the author from the database
    return redirect('author_list')  # Redirect to the author list page


