from rest_framework import serializers
from ecomSyS_CNPM05_Truc.search_service.search.models import Search


class SearchSerializer(serializers.Serializer):
    class Meta:
        model = Search
        fields = ['key']

    def destroy(self,instance):
        instance.is_active = False
        instance.save()
        return instance