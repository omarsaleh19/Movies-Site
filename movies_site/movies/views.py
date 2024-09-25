from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

def movie_list(request):
    # Retrieve all movies from the database
    movies = Movie.objects.all()  
    return render(request, 'movies/movie_list.html', {'movies': movies})


def movie_detail(request, slug):
    movie = Movie.objects.get(slug=slug)
    reviews = movie.reviews.all()
    
    if request.method == 'POST':
        if not request.user.is_authenticated:
            # Redirect if user is not authenticated
            return redirect('accounts:login')  

        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user  # Associate the review with the logged-in user
            review.save()
            return redirect('movie:detail', slug=movie.slug)  # Redirect to refresh the page after saving
    else:
        form = ReviewForm()

    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'reviews': reviews,
        'form': form,
    })
