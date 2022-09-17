from django.db.models import fields
from rest_framework import serializers
from .models import Action, Journal
from django.db.models import Sum



class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ['id', 'action', 'date', 'cost']
        depth = 1
    


class ActionSerializer(serializers.ModelSerializer):
    journals = JournalSerializer(many=True)
    total_journal_cost = serializers.SerializerMethodField()

        
    class Meta:
        model = Action
        fields = ['id', 'name', 'category', 'logo', 'journals', 'total_journal_cost']

    # asina get + anaranle variable ny serializer method mba reference
    # ito method ito dia mamoka ny sum an'i cost an'i Action 1 via id
    def get_total_journal_cost(self, id):
        return Journal.objects.filter(action=id).aggregate(Sum('cost'))

    

    def create(self, validated_data):
        journals_data = validated_data.pop('journals')
        action = Action.objects.create(**validated_data)
        for journal_data in journals_data:
            Journal.objects.create(action=action, **journal_data)
        return action

    def update(self, instance, validated_data):
        journals_data = validated_data.pop('journals')
        journals = list((instance.journals).all())
        
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.save()
        
        for journal_data in journals_data:
            journal = journals.pop(0) # mamafa le id
            journal.cost = journal_data.get('cost', journal.cost)
            journal.save()
        return instance
