from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from app_main.models import Note


def my_notes(request):
    notes = Note.objects.filter(owner=request.user)  # [ note1, note2, ... ]
    return render(request, "my_notes.html", {"notes": notes})


def my_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, "my_note.html", {"note": note})


def profile_page(request):
    if not request.user.is_authenticated:
        return redirect("/login/")

    return render(request=request, template_name="profile_page.html")


def home_page(request):
    return render(request=request, template_name="home_page.html")


def contacts_page(requests):
    return render(request=requests, template_name="contacts_page.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            login(request=request, user=user)
            return redirect("/")

    return render(request=request, template_name="login.html")


def logout_user(request):
    logout(request=request)
    return redirect("/login/")


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        users = User.objects.filter(username=username)

        if len(users) != 0:
            return redirect("/register/")

        if (password1 and password2 and username) and (password1 == password2):
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
            )
            user.set_password(raw_password=password2)
            user.save()
            return redirect("/login/")

    return render(request=request, template_name="register.html")


def profile_update(request):
    username = request.POST.get("username")
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    email = request.POST.get("email")

    user = request.user

    # If username is empty, redirect user back to profile page without changing any user's information
    if len(username.strip()) == 0:
        return redirect("/profile")

    # Saving user's information and redirecting to profile page again
    user.username = username
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.save()
    return redirect("/profile")


def new_note(request):
    return render(request, "new_note.html")


def create_note(request):
    # {'title': 'Some title', 'description': 'Some text'}
    title = request.POST.get('title')
    description = request.POST.get('description')

    note = Note.objects.create(
        owner=request.user,
        title=title,
        description=description,
    )
    note.save()

    return redirect('/my-notes/')


def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect('/my-notes/')
