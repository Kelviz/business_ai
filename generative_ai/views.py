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
        userId = request.data.get("userId")

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
                idea=ideas,
                user_id=userId

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
    permission_classes = [AllowAnyPermission]


class ScrollCardViewset(viewsets.ModelViewSet):
    queryset = ScrollCard.objects.all()
    serializer_class = ScrollCardSerializer
    permission_classes = [AllowAnyPermission]


class IdeaListViewset(viewsets.ModelViewSet):
    queryset = BusinessAI.objects.all()
    serializer_class = BusinessAISerializer

    def get_queryset(self):

        user_id = self.request.META.get('HTTP_X_USER_ID')
        print(user_id)
        queryset = super().get_queryset().filter(user_id=user_id)

        return queryset

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()

        # Use `pk` parameter to filter by primary key
        print(f'this pk {pk}')
        idea = queryset.filter(pk=pk).first()
        print(idea)
        if idea is not None:
            serializer = self.get_serializer(idea)
            return Response(serializer.data)
        else:
            return Response(status=404)


class IdeaDetailViewset(viewsets.ModelViewSet):
    queryset = BusinessAI.objects.all()
    serializer_class = BusinessAISerializer
