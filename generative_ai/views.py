from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from django.conf import settings
from rest_framework.response import Response
from .models import BusinessAI, About, ScrollCard
from .serializers import BusinessAISerializer, AboutSerializer, ScrollCardSerializer
from .forms import BusinessForm
from .permissions import AllowAnyPermission
import openai


class GenerateIdeasViewset(viewsets.ViewSet):

    def create(self, request):
        form = BusinessForm(request.data)

        if form.is_valid():
            industry = form.cleaned_data['industry']
            audience = form.cleaned_data['audience']
            budget = form.cleaned_data['budget']
            generate_txt = f'Business ideas about {industry} targeting {audience} with the budget of {budget}.'
            openai.api_key = settings.OPENAI_DATA['OPENAI_API_KEY']
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                      "role": "system",
                      "content": "Generate"
                    },
                    {
                        "role": "user",
                        "content": generate_txt
                    }
                ],
                temperature=0,
                max_tokens=1024,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0

            )

            ideas = response['choices'][0]['message']['content']
            print(ideas)

            business_data = BusinessAI(
                industry=industry,
                audience=audience,
                budget=budget,
                title=generate_txt,
                idea=ideas

            )

            business_data.save()
            response_data = {
                'ideas': ideas
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


class AboutViewset(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class ScrollCardViewset(viewsets.ModelViewSet):
    queryset = ScrollCard.objects.all()
    serializer_class = ScrollCardSerializer
    permission_classes = [AllowAnyPermission]


class IdeaListViewset(viewsets.ModelViewSet):
    queryset = BusinessAI.objects.all()
    serializer_class = BusinessAISerializer
    permission_classes = [AllowAnyPermission]
