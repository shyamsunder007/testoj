from rest_framework import serializers
from problelemapi.models import Problems

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problems
        fields = ('assignment','Pid', 'name', 'score', 'is_upload_only', 'c_time_limit', 'python_time_limit','java_time_limit','memory_limit','allowed_languages','diff_cmd','diff_arg')
    def create(self, validated_data):
        problem_obj = Problems(**validated_data)
        problem_obj.save()
        return problem_obj

    def update(self, instance, validated_data):
        instance.name = validated_data["name"]
        instance.save()
        return instance