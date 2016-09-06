import json
from django.core import serializers
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse

from usermessages.models import Messages

def rest_view(request, id=None):
	message = {"fail": "data not found"}
	if request.method == 'GET':
		data = Messages.objects.all()
		if data:
			messages = [model_to_dict(message) for message in data]
			message = {"messages": messages}
		return JsonResponse(message)
	elif request.method == 'POST':
		json_data = json.loads(request.body)
		message = {"fail": "Missing data for message_text"}
		if 'message_text' in json_data:
			message = Messages(message_text = json_data['message_text'])
			message.save()
			message = {"message": model_to_dict(message)}
		return JsonResponse(message)
	elif request.method == 'DELETE':
		data = Messages.objects.filter(id=id)
		if data:
			data.delete()
			message = {"success": "true"}
		return JsonResponse(message)

