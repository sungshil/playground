from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader


from .models import Posts
# Create your views here.

def nfMenu(request):

	p_list = Posts.objects.all()

	template = loader.get_template('nfwithdb/menu.html')
	context = RequestContext(request,{
		'p_list': p_list,
	})


	return HttpResponse(template.render(context,request))

def nfRead(request):
	if ('Name' in request.POST) and ('commentsX' in request.POST):
		new_post = Posts(name=request.POST['Name'], comment=request.POST['commentsX'])
		new_post.save()

		return HttpResponse('Post succeeded')
	else:
		return HttpResponse('Not normal gateway')

def nfRevMenu(request):

	p_list = Posts.objects.order_by('-id')

	template = loader.get_template('nfwithdb/menu.html')
	context = RequestContext(request,{
		'p_list': p_list,
	})


	return HttpResponse(template.render(context,request))