from rest_framework import serializers
from Repository.models import QuestionsDb


class QuestionsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    language = serializers.ChoiceField(
        choices=QuestionsDb.LANGUAGE_CHOICES,
        default='Python'
    )
    difficulty = serializers.ChoiceField(
        choices=QuestionsDb.DIFFICULTY_CHOICES,
        default='Easy'
    )
    topic = serializers.CharField(max_length=200)
    notes = serializers.CharField()
    sample_input = serializers.CharField()
    sample_output = serializers.CharField()
    published_date = serializers.DateTimeField(read_only=True)
    is_active = serializers.BooleanField(default=True)
    score = serializers.IntegerField()

    def create(self, validated_data):
        return QuestionsDb.objects.create(**validated_data)
        