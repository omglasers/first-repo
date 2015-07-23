from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Card

# Create your views here.
from django.http import HttpResponse


def index(request):
	return HttpResponse("Hello, world. You're at the cards index.")

class IndexView(generic.ListView):
	template_name = 'cards/index.html'
	context_object_name = 'latest_card_list'
	def get_queryset(self):
		"""Return the last five published cards."""
		return Card.objects.order_by('name')[:5]


class DetailView(generic.DetailView):
	model = Card
	template_name = 'cards/detail.html'
