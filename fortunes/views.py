from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from djortunes.fortunes.models import Comment, Fortune
from djortunes.fortunes.forms import PublicCommentForm, PublicFortuneForm

def detail(request, fortune_id):
    "Display one fortune, and provides a comment form wich will be handled and persisted if request is POST"
    fortune = get_object_or_404(Fortune, id = fortune_id)
    comments = fortune.comment_set.all().order_by('pub_date')
    comment = Comment(fortune = fortune)
    if request.method == "POST":
        commentForm = PublicCommentForm(request.POST, instance = comment)
        if commentForm.is_valid():
            comment = commentForm.save()
            return redirect(reverse('fortune-detail', args=[fortune.id]) + '#c_' + str(comment.id))
    else:
        commentForm = PublicCommentForm(instance = comment)
    return render_to_response('detail.html', RequestContext(request, {
        'fortune':     fortune, 
        'comments':    comments, 
        'commentForm': commentForm,
    }))

def index(request):
    "Lists Fortunes"
    fortunes = Fortune.objects.all().order_by('-pub_date')[:10]
    return render_to_response('index.html', {'fortunes': fortunes})

def new(request):
    "Provides a Fortune creation form, validates the form and saves a new Fortune in the database"
    if request.method == "POST":
        form = PublicFortuneForm(request.POST)
        if form.is_valid():
            fortune = form.save()
            return redirect(reverse('fortune-detail', args=[fortune.id]))        
    else:
        form = PublicFortuneForm()
    return render_to_response('new.html', RequestContext(request, {
        'form': form,
    }))

def vote(request, fortune_id, direction):
    "Votes for a fortune"
    fortune = get_object_or_404(Fortune, id = fortune_id)
    fortune.votes += 1 if direction == 'up' else -1
    fortune.save()
    return redirect(reverse('fortune-detail', args=[fortune.id]))
