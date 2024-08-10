from django.shortcuts import render
from accounts.models import User

def about_us(request):
    users = User.objects.all()
    users_chunked = [users[i:i + 2] for i in range(0, len(users), 2)]
    return render(request, 'about_us.html', {'users_chunked': users_chunked})
