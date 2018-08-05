from django.shortcuts import render
from django.views import generic

# Create your views here.
from .models import Book, Author, BookInstance, Genre, Language

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    #num_authors = Author.objects.count()  # The 'all()' is implied by default.
    
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1


    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_genres = Genre.objects.count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    #num_books_specific = Book.objects.filter(title__icontains='harry').count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)





class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    #context_object_name = 'my_book_list'   # your own name for the list as a template variable
    #queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    #template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location
   # def get_context_data(self, **kwargs):
    #    # Call the base implementation first to get the context
     #   context = super(BookListView, self).get_context_data(**kwargs)
      #  # Create any data and add it to the context
       # context['some_data'] = 'This is just some data'
        #return context



class BookDetailView(generic.DetailView):
    model = Book
    
#    def book_detail_view(request, primary_key):
 #   	try:
  #      	book = Book.objects.get(pk=primary_key)
   # 	except Book.DoesNotExist:
    #    	raise Http404('Book does not exist')

    ## from django.shortcuts import get_object_or_404
    # #book = get_object_or_404(Book, pk=primary_key)
    
    	#return render(request, 'catalog/book_detail.html', context={'book': book})



class AuthorListView(generic.ListView):
	model = Author
	paginate_by = 10




class AuthorDetailView(generic.DetailView):
	model = Author
