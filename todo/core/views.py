from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Todo, User

# Create your views here.


def create_todo(request):

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        username = request.POST.get("username")

        user = User.objects.get(username=username)

        Todo.objects.create(title=title, description=description, user=user)

        return redirect("core:get_todos")

    return render(request, "create.html")
    #


def get_todos(request):
    todos = Todo.objects.all()
    newtodos = []
    for todo in todos:
        newtodos.append(
            {
                "id": todo.id,
                "title": todo.title,
                "description": todo.description,
                "user": todo.user.username,
            }
        )
    print(newtodos)
    return render(request, "index.html", {"todo_lists": newtodos})


def get_todo_by_id(request, todo_id):
    find_todo = Todo.objects.get(pk=todo_id)
    if not find_todo:
        return HttpResponse("Todo not found", status=404)
    return render(request, "detail.html", {"todo": find_todo})


#


def update_todo(request, todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id)
    except Todo.DoesNotExist:
        return HttpResponse("Todo not found", status=404)

    if request.method == "POST":
        todo.title = request.POST.get("title")
        todo.description = request.POST.get("description")
        todo.save()
        return redirect("core:get_todos")

    # 👇 THIS WAS MISSING (GET request handling)
    return render(request, "edit.html", {"todo": todo})


def delete_todo(request, todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id)
    except Todo.DoesNotExist:
        return HttpResponse("Todo not found", status=404)

    todo.delete()
    return redirect("core:get_todos")
