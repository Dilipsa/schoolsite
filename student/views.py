from django.shortcuts import render, redirect
from student.models import Student, Course

def create_student_view(request):
    courses = Course.objects.all()
    if request.method=="POST":
        rol = request.POST.get("roll_no")
        name = request.POST.get("name")
        course_ids = request.POST.getlist("course")
        st = Student(name=name, roll_no=rol)
        st.save()
        st.course.set(course_ids)
    return render(request, 'student/create_student.html', {"courses": courses})

def update_student_view(request, id):
    courses = Course.objects.all()
    student = Student.objects.get(pk=id)
    if request.method=="POST":
        rol = request.POST.get("roll")
        name = request.POST.get("nm")
        student.name=name
        student.roll_no=rol
        student.save()
        return redirect("/student_list/")
    return render(request, 'student/update_student.html', {'student': student, 'courses': courses})

def student_list_view(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})

def student_detail_view(request, id):
    student = Student.objects.get(pk=id)
    return render(request, 'student/student_detail.html', {'student': student})

def student_delete_view(request, id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect("/student_list/")
