from rest_framework import serializers
from .models import Notes

class NotesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    link = serializers.SerializerMethodField("link_detail")
    class Meta:
        model = Notes
        fields = ['name','discriptions','owner','create_at','link']

    def link_detail(self,obj):
        return "http://127.0.0.1:8000/notes/%d/" %obj.id