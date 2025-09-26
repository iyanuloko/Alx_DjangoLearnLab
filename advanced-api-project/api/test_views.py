from rest_framework.test import APIRequestFactory, force_authenticate
from django.contrib.auth.models import User

from api.views import CreateView

factory = APIRequestFactory()
user = User.objects.create_user(username='testuser', password='password')
request = factory.post('/books/create/', {'title': '1984', 'publication_year': 1979, 'authors': 'James Orwelll'}, format='json')
request2 = factory.patch('/books/update/', {'authors': 'James Orwell'})
request3 = factory.delete('/books/1/')

force_authenticate(request, user=user)
force_authenticate(request2, user=user)
force_authenticate(request3, user=user)

view = CreateView.as_view({'post': 'create'})
response = view(request)
print(response.status_code)