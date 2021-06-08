from django.shortcuts import render
from .models import Notification
from django.views.generic import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
	context = {
		'notifications': Notification.objects.all()
	}
	return render(request, 'meduza/home.html', context)


class NotificationCreateView(CreateView):
	model = Notification
	fields = ['lek', 'godzina']

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class NotificationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Notification
	success_url = '/'

	def test_func(self):
		notification = self.get_object()
		if self.request.user == notification.user:
			return True
		return False
