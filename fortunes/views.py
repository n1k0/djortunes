from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from djortunes.fortunes.models import Fortune
from djortunes.fortunes.forms import PublicFortuneForm

def detail(request, fortune_id):
    "Display one Fortune details"
    fortune = get_object_or_404(Fortune, id = fortune_id)
    comments = fortune.comment_set.all()
    return render_to_response('detail.html', {'fortune': fortune, 'comments': comments})

def index(request):
    "Lists Fortunes"
    fortunes = Fortune.objects.all().order_by('-pub_date')[:10]
    return render_to_response('index.html', {'fortunes': fortunes})

def new(request):
    "provides a Fortune cration form, validates the form and creates a new Fortune"
    if request.method == "POST":
        form = PublicFortuneForm(request.POST)
        if form.is_valid():
            fortune = form.save()
            return redirect(reverse('fortune-detail', args=[fortune.id]))        
    else:
        form = PublicFortuneForm()
    return render_to_response('new.html', RequestContext(request, {'form': form}))

def vote(request, fortune_id, direction):
    "Votes for a fortune"
    fortune = get_object_or_404(Fortune, id = fortune_id)
    fortune.votes += 1 if direction == 'up' else -1
    fortune.save()
    return redirect(reverse('fortune-detail', args=[fortune.id]))
