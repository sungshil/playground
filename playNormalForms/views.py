from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
# Create your views here.


def playNormalForms(request):
	template = loader.get_template('playNormalForms/NormalForms.html')
	#try:
	#	poyo=request.POST['PoYo']
	#except(KeyError, Poyo.DoesNotExist)
	
	if 'PoYo' in request.POST :
		poyo = request.POST['PoYo']
	else :
		poyo = '~emptyness~'

	if 'GetYo' in request.GET :
		getyo = request.GET['GetYo']
	else :
		getyo = 'empty QQ'

#	return HttpResponse("hohoho %s" %poyo)

	context = RequestContext(request, { 
					'poyo': poyo,
					'getyo':getyo,  
				})
	return HttpResponse(template.render(context, request))
	
	#else:
	#	context = RequestContext(request, {'poyo',poyo})
	#	return HttpResponse(template.render(context))


