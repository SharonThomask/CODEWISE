from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from Repository.models import QuestionsDb
from Repository.serializers import QuestionsSerializer


class QuestionListCreate(APIView):

    def get(self, request):
        qs = QuestionsDb.objects.all()
        serializer_instance = QuestionsSerializer(qs, many=True)
        return Response(data=serializer_instance.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = QuestionsSerializer(data=form_data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(
                data={"Message": "Question added successfully"},
                status=201
            )

        return Response(
            data={"errors": serializer_instance.errors},
            status=400
        )


class QuestionRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk):
        question = get_object_or_404(QuestionsDb, id=pk)
        serializer_instance = QuestionsSerializer(question)
        return Response(data=serializer_instance.data)

    def put(self,request,pk):
        question = get_object_or_404(QuestionsDb, id=pk)
        form_data=request.data
        serializer_instance=QuestionsSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self, request, pk):
        QuestionsDb.objects.filter(id=pk).delete()
        return Response({"Message": "Question deleted successfully"})


