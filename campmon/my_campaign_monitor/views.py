from django.shortcuts import render
from .models import subscriber
from rest_framework import viewsets
from .serializers import SubscriberSerializer
import requests
from requests.auth import HTTPBasicAuth
from rest_framework.response import Response
from rest_framework import status
import json
# Create your views here.
api_key='DdSHrCNVmqQgTqZi+o9kIKU4H1uuS+Lhl9SWYt4AJCN9Q6GweRK5S2aXWgusWkSy9Pqu3VI5UUVbp8vk3dy1SwPPwU6asvYGEexoFd8/fWh4p3xR5jHBETF+ROR8bt/1mm03Nz9mVwcTq1bGxOEEig=='
list_id='3a59257cf2e4fe77d92863a0b7309f7f'

"""def subscriber_list_view(request):


    subscriber_object=subscriber.objects.all()
    context= {'subscriber_objects':subscriber_object}
    return render(request,"subscriber/index.html",context)"""

class SubscriberView(viewsets.ModelViewSet):

   #This loads the API data everytime an operation is performed. Its bad practice actually this part should happen once when the server loads.
   #But it also keeps the data concurrent 
    if subscriber.objects.all():
        subscriber.objects.all().delete()
    url='https://api.createsend.com/api/v3.2/lists/'+list_id+'/active.json'
    auth = (api_key,'x')
    response= requests.get(url,auth=auth)
    data=response.json()
    subscribers=data['Results']
    for i in subscribers:
        sub_data=subscriber(email=i['EmailAddress'],name=i['Name'])
        sub_data.save()
    serializer_class = SubscriberSerializer
    queryset=subscriber.objects.all()

    #Custom CRUD in order to update the campaign API

    def create(self, request):
        url='https://api.createsend.com/api/v3.2/subscribers/'+list_id+'.json'
        auth = (api_key,'x')
        serializer = SubscriberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        body= {"EmailAddress":serializer.data["email"],"Name":serializer.data["name"],"ConsentToTrack":"Yes"}
        response= requests.post(url,auth=auth, data=json.dumps(body))
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):

        

        instance = self.get_object()
        serializer = SubscriberSerializer(
            instance=instance,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        url='https://api.createsend.com/api/v3.2/subscribers/'+list_id+'.json?email='+serializer.data["email"]
        auth = (api_key,'x')
        body= {"EmailAddress":serializer.data["email"],"Name":serializer.data["name"],"ConsentToTrack":"Yes"}
        response= requests.post(url,auth=auth, data=json.dumps(body))


        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        field_value = getattr(instance, 'email')
        url='https://api.createsend.com/api/v3.2/subscribers/'+list_id+'.json?email='+field_value
        auth = (api_key,'x')
        response= requests.delete(url,auth=auth)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
    