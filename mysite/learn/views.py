from django.shortcuts import render

# Create your views here.
def home(request):
#	return render(request, 'home.html')
	string = u"这是个test"
	TutorialList = ["HTML","CSS","JQUERY","PYTHON","DJANGO"]
	info_dict = {'site': u'啦啦啦', 'content': u'吸吸吸'}
	List = map(str, range(100))
#	return render(request, 'home.html', {'string': string})
#	return render(request, 'home.html', {'TutorialList': TutorialList})
#	return render(request, 'home.html', {'info_dict': info_dict})
	return render(request, 'home.html', {'List': List})