from rest_framework import generics
from api.models import Person
from django.db.models import Q
from api.serializers import PersonSerializer

class PersonListCreateView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name_filter = self.request.query_params.get('name')

        if name_filter:
            queryset = queryset.filter(Q(name__icontains=name_filter))

        return queryset

class PersonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
