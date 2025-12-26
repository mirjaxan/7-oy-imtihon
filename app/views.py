from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Course, Student, Enrollment
from .serializers import CourseSerializer, StudentSerializer, EnrollmentSerializer
from .filters import CourseFilter

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('-id')
    serializer_class = CourseSerializer
    filterset_class = CourseFilter

    @action(detail=True, methods=['get'])
    def students(self, request, pk=None):
        course = self.get_object()
        enrollments = Enrollment.objects.filter(course=course)
        students = [e.student for e in enrollments]
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('-id')
    serializer_class = StudentSerializer

    @action(detail=True, methods=['get'])
    def courses(self, request, pk=None):
        student = self.get_object()
        enrollments = Enrollment.objects.filter(student=student)
        courses = [e.course for e in enrollments]
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)



class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all().order_by('-id')
    serializer_class = EnrollmentSerializer
