from rest_framework.response import Response
from django.http import HttpResponse

def api_get_response(serializer, queryset=[], many=True):
	serializer = serializer(queryset, many=many)
	return Response(serializer.data)

def api_post_response(serializer, request):
	serializer = serializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)