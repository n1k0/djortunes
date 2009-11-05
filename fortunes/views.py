from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from djortunes.fortunes.models import Comment, Fortune
from djortunes.fortunes.forms import PublicCommentForm, PublicFortuneForm

def detail(request, fortune_id):
    """
    Display one fortune, and provides a comment form wich will be handled and persisted if 
    request is POST
    """
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

def index(request, ftype):
    "Lists Fortunes"
    if ftype == 'top':
        order_by = '-votes'
    elif ftype == 'worst':
        order_by = 'votes'
    else:
        order_by = '-pub_date'

    fortune_list = Fortune.objects.all().order_by(order_by)#[:10]
    paginator = Paginator(fortune_list, 2)
    
    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    
    # If page request (9999) is out of range, deliver last page of results.
    try:
        fortunes = paginator.page(page)
    except (EmptyPage, InvalidPage):
        fortunes = paginator.page(paginator.num_pages)

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
