from rest_framework import serializers

from database.models import task

class get_all_tasks_serializer(serializers.ModelSerializer):
	class Meta(object):
		model = task
		fields = "__all__"

class create_new_task_serializer(serializers.ModelSerializer):
	class Meta(object):
		model = task
		fields = (
				"name",
				"description",
				"email"
			)