from rest_framework import serializers
from .models import Branch,Organisarion


class BranchFormSerializer(serializers.ModelSerializer):
    org = serializers.StringRelatedField(read_only=True)

    def get_org(self, obj):
        if obj.org:
            return obj.org.org_name
        else:
            return "No Org."

    class Meta:
        model = Branch
        fields = '__all__'


class OrgFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organisarion
        fields = '__all__'
