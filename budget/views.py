from django.db.models import query
from django.shortcuts import render
from django_filters.filters import OrderingFilter
from rest_framework.response import Response


from .serializers import ActionSerializer, JournalSerializer

from .models import Action, Journal

from .filters import ActionFilterSet, JournalFilterSet

from rest_framework import viewsets

from django_filters.rest_framework.backends import DjangoFilterBackend

from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


# Create your views here.



class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = ActionFilterSet
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    # ordering_fields = ['journals_date']
    





class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = JournalFilterSet


    def create(self, request, *args, **kwargs):
        journal = request.data
        new_journal = Journal.objects.create(
            action = Action.objects.get(id=journal["action"]),
            cost = journal["cost"]
        )

        new_journal.save()

        serializer = JournalSerializer(new_journal)
        
        return Response(serializer.data)

    # def update(self, request, *args, **kwargs):
    #     journal = request.data
    #     get_journal = Journal.objects.get(id=journal["id"])
    #     get_action = Action.objects.get(id=journal["action"])
    #     get_journal.action = get_action
    #     get_journal.cost = journal["cost"]

    #     get_journal.save()

    #     serializer = JournalSerializer(get_journal)

    #     return Response(serializer.data)

    


