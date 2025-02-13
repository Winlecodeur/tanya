from django.shortcuts import render, get_object_or_404, redirect
from .forms import SpaceForm, AppointForm, MembreForm, ProprieteForm, ReceiptForm
from .models import Space, Appointment, Membre, Propriete, Receipt
from django.core.mail import send_mail
from django.db.models import Q 

#here's a home, it allow to see a lot of information from the firm
def home(request):
    return render(request, 'home.html')

#here's a form for rendez-vous
def form(request):
    if request.method == 'POST':
        form  = AppointForm(request.POST)
        if form.is_valid() :
            appoint = form.save()
            recipient_list=["therryconsu@gmail.com"]
            #To send an email
            whatsapp_number = "243859087408"
            message =f"Un Nouveau  rendez-vous a été soumis \n\n"
            message += f"Nom : {appoint.name}\n"
            message += f"Post-nom : {appoint.last_name}\n"
            message +=    f"Prénom : {appoint.given_name}\n"
            message +=    f"Date : {appoint.date}\n"
            message +=    f"Num.Tél : {appoint.number}\n"
            message +=f"Date de crétion : {appoint.created_at}\n" 
            import urllib.parse
            message_encoded = urllib.parse.quote(message)
            whatsapp_url = f"https://wa.me/{whatsapp_number}?text={message_encoded}"

            return redirect(whatsapp_url)
    else :
        form = AppointForm()
    return render (request, 'form.html', {'form':form})

#here's a way to get every information, this one is only for superuser 
def profile(request):
    if request.user.is_superuser :
        appoint = Appointment.objects.all().order_by('-created_at')[:4]
        members = Membre.objects.all().order_by('-date_acquired')[:4]
        return render (request, 'profile.html', {'appoint':appoint,'members':members})
    else :
        return redirect ('home')
    
#here's a way to add a new member
def add_member(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = MembreForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('profile')
        else :
            form = MembreForm()
        return render (request, 'add_member.html', {'form':form})
    else : 
        return redirect ('home')
    
#here's a way to see every member in the system
def member(request):
    if request.user.is_superuser:
        members = Membre.objects.all()
        return render(request, 'member.html',{'members':members})
    else :
        return redirect('home')
    

#here's  a way to get more information of such member
def detail_member(request, member_id):
    if request.user.is_superuser:
        member = get_object_or_404(Membre, id=member_id)
        return render (request, 'detail_member.html', {'member':member})
    else :
        return redirect ('home')
#here's  a way to get more information of such member
def delete_member(request, member_id):
    if request.user.is_superuser:
        member = get_object_or_404(Membre, id=member_id)
        member.delete()
        return redirect('member')
    else :
        return redirect ('home')
#here's a way to edit or modifie a way item (member) info in the list 
def edit_member(request, member_id):
    if request.user.is_superuser:
        member = get_object_or_404(Membre, id=member_id)
        form = MembreForm(request.POST, instance=member)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect ('detail_member',member_id=member.id)
        else:
            form = MembreForm(instance=member)
        return render (request, 'edit_member.html', {'member':member, 'form':form})
    else :
        return redirect ('home')
    
#here's a way to research a member 
def search_member(request):
    query = request.GET.get('q')
    resultats = []
    if query :
        resultats = Membre.objects.filter(Q(name__icontains=query)|Q(given_name__icontains=query))
    return render (request, 'search_member.html', {'query':query,'resultats':resultats})

#here's a way to watch and consulte a space infos
def space(request):
    if request.user.is_superuser : 
        spaces = Space.objects.all()
        return render (request, 'space.html', {'spaces':spaces})
    else :
        return redirect ('home')
    
#here's a way to add a new space item
def space_form(request):
    if request.method == 'POST':
        form = SpaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('space')
    else :
        form = SpaceForm()
    return render(request, 'space_form.html', {'form':form})

def space_detail(request, space_id):
    space = get_object_or_404(Space, id=space_id)
    return render (request, 'space_detail.html', {'space':space})

def space_delete(request, space_id):
    space = get_object_or_404(SpaceForm, id=space_id)
    space.delete()
    return redirect('space')

def space_modif(request, space_id):
    space = get_object_or_404(Space, id=space_id)
    if request.method == 'POST':
        form = SpaceForm(request.POST, instance=space)
        if form.is_valid():
            form.save()
            return redirect('space')
    else :
        form = SpaceForm(instance=space)
    return render(request, 'space_modif.html', {'form':form, 'space':space})

def appoint_all(request):
    appoints = Appointment.objects.all().order_by('-created_at')
    return render (request, 'appoint.html', {'appoints':appoints})

def appoint_detail(request, appoint_id):
    appoint = get_object_or_404(Appointment, id=appoint_id)
    return render (request, 'appoint_detail.html', {'appoint':appoint})

def appoint_edit(request, appoint_id):
    appoint = get_object_or_404(Appointment, id=appoint_id)
    if request.method == 'POST':
        form = AppointForm(request.POST, instance=appoint)
        if form.is_valid():
            form.save()
            return redirect('appoint_detail', appoint=appoint.id)
    else :
        form = AppointForm(instance=appoint)
    return render (request, 'appoint_edit.html', {'appoint':appoint, 'form':form})

def property(request):
    propertys = Propriete.objects.all()
    return render(request, 'property.html', {'propertys':propertys})

def property_form(request):
    if request.method == 'POST' :
        form = ProprieteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property')
    else:
        form = ProprieteForm()
    return render (request, 'property_form.html',{'form':form})

def property_modif(request, property_id):
    property = get_object_or_404(Propriete, id=property_id)
    if request.method == 'POST' :
        form = ProprieteForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property')
    else:
        form = ProprieteForm(instance=property)
    return render (request, 'property_modif.html',{'form':form, 'property':property})

def property_detail(request, property_id):
    property = get_object_or_404(Propriete, id=property_id)
    return render (request, 'property_detail.html',{'property':property})

def property_delete(request, property_id):
    property = get_object_or_404(Propriete, id=property_id)
    property.delete()
    return redirect ('property')

def receipt(request):
    receipts = Receipt.objects.all()
    return render(request, 'receipt.html', {'receipts':receipts})

def receipt_form(request):
    if request.method == 'POST' :
        form = ReceiptForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('receipt')
    else:
        form = ReceiptForm()
    return render (request, 'receipt_form.html',{'form':form})

def receipt_modif(request, receipt_id):
    receipt = get_object_or_404(Receipt, id=receipt_id)
    if request.method == 'POST' :
        form = ReceiptForm(request.POST, instance=receipt_delete)
        if form.is_valid():
            form.save()
            return redirect('receipt_detail')
    else:
        form = ReceiptForm(instance=receipt)
    return render (request, 'receipt_modif.html',{'form':form, 'receipt':receipt})

def receipt_detail(request, receipt_id):
    receipt = get_object_or_404(Receipt, id=receipt_id)
    return render (request, 'receipt_detail.html',{'receipt':receipt})

def receipt_delete(request, receipt_id):
    receipt = get_object_or_404(Receipt, id=receipt_id)
    receipt.delete()
    return redirect ('property')

def search_receipt(request):
    query = request.GET.get('q')
    resultats = []
    if query :
        resultats = Receipt.objects.filter(Q(user__name__icontains=query)|Q(user__name__icontains=query)|Q(user__given_name__icontains=query))
    return render (request, 'search_receipt.html', {'query':query,'resultats':resultats})