from .serializers import *
from rest_framework.views import APIView
from utility.api_response import *

class get_all_tasks(APIView):
	def get(self, request):
		serializer = get_all_tasks_serializer

		try:
			queryset = task.objects.all()
			return api_get_response(serializer, queryset)
		except:
			return HttpResponse(status=500, content=b'Internal Server Error')

class create_new_task(APIView):
	def post(self, request):
		serializer = create_new_task_serializer

		return api_post_response(serializer, request)
		
		try:
			return api_post_response(serializer, request)
		except:
			return HttpResponse(status=500, content=b'Internal Server Error')
