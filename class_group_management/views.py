from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from rest_framework.views import APIView
from openai import OpenAI, OpenAIError

from .models import Homework, ClassGroup
from .serializers import HomeworkSerializer, ClassGroupSerializer

client = OpenAI(
    api_key="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",
)


class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer


class ClassGroupViewSet(viewsets.ModelViewSet):
    queryset = ClassGroup.objects.all()
    serializer_class = ClassGroupSerializer


class HomeworkOpenAIView(APIView):
    prompt_template = """
    Act as a teacher. Your input is a description of a homework task.
    Take the string in double quotes and remix this description to create a new, unique task based on the same topic.
    Return this in JSON format with the field 'new_description'.
    Task description is: "{description}"
    """

    def get(self, request, pk):
        homework = get_object_or_404(Homework, pk=pk)
        serializer = HomeworkSerializer(homework)
        sample_description = serializer.data['description']

        prompt_full = self.prompt_template.format(description=sample_description)

        try:
            response = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt_full,
                    }
                ],
                model="gpt-3.5-turbo",
            )

            if response.choices and 'message' in response.choices[0]:
                openai_response = response.choices[0].message['content'].strip()
            else:
                openai_response = "API response was incomplete or invalid."

        except OpenAIError as e:
            return JsonResponse({'error': f"OpenAI API error: {str(e)}"}, status=500)

        return JsonResponse({
            'homework': serializer.data,
            'openai_response': openai_response
        })


