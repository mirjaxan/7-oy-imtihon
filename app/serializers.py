from rest_framework import serializers
from .models import Course, Student, Enrollment


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("narx 0 dan katta bolishi kerak")
        return value


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

    def validate(self, data):
        if Enrollment.objects.filter(
            student=data['student'],
            course=data['course']
        ).exists():
            raise serializers.ValidationError("Bu student bu kursga allaqachon yozilgan")
        return data
