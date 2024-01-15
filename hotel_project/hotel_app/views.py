from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Room, Client, BookApplication

def index(request):
    return render(request, 'hotel_app/index.html')

def room_list(request):
    rooms = Room.objects.filter(is_reserved=False)
    return render(request, 'hotel_app/room_list.html', {'rooms': rooms})

def room_detail(request, slug_room):
    room = get_object_or_404(Room, slug=slug_room)
    return render(request, 'hotel_app/room_detail.html', {'room': room})

def book_application(request, slug_room):
    room = get_object_or_404(Room, slug=slug_room)
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        check_in_date = request.POST['check_in_date']
        check_out_date = request.POST['check_out_date']
        additional_services = request.POST['additional_services']

        client = Client.objects.create(full_name=full_name, email=email)
        BookApplication.objects.create(room=room, client=client, check_in_date=check_in_date, check_out_date=check_out_date, additional_services=additional_services)

        return redirect('index')
    return render(request, 'hotel_app/book_application.html', {'room': room})

def admin_index(request):
    return render(request, 'hotel_app/admin_index.html')

def add_room(request):
    if request.method == 'POST':
        category = request.POST['category']
        description = request.POST['description']
        image = request.FILES.get('image')

        Room.objects.create(category=category, description=description, image=image)

        messages.success(request, 'Room added successfully.')
        return redirect('admin_index')
    return render(request, 'hotel_app/add_room.html')

def admin_room_list(request):
    rooms = Room.objects.all()
    return render(request, 'hotel_app/admin_room_list.html', {'rooms': rooms})

def admin_book_applications(request):
    applications = BookApplication.objects.all()
    return render(request, 'hotel_app/admin_book_applications.html', {'applications': applications})

def admin_book_application_detail(request, slug_book_application):
    application = get_object_or_404(BookApplication, slug=slug_book_application)

    if request.method == 'POST':
        action = request.POST['action']

        if action == 'approve':
            application.is_approved = True
            application.save()
            messages.success(request, 'Application approved successfully.')
        elif action == 'reject':
            application.delete()
            messages.success(request, 'Application rejected successfully.')
        return redirect('admin_book_applications')
    return render(request, 'hotel_app/admin_book_application_detail.html', {'application': application})
