from django.shortcuts import render
def home(request):
	return render(request,'cfront/index.html')
def selectone(request):
	return render(request,'cfront/showone.html')
def delete(request):
	return render(request,'cfront/delete.html')
def insert(request):
	return render(request,'cfront/insert.html')
def update(request):
	return render(request,'cfront/update.html')
def restfn(request):
	return render(request,'cfront/functions.html')



# Create your views here.
