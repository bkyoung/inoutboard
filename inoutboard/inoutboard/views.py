import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from inoutboard.inoutboard.models import Employee
from inoutboard.inoutboard.forms import StatusUpdateForm

def main(request):
    if request.method == 'POST':
        form = StatusUpdateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            emp = Employee.objects.get(id=int(cd['full_name']))
            old_status = emp.status
            new_status = cd['status']
            if new_status:
                emp.status = cd['status']
            else:
                if old_status == "Out":
                    emp.status = "In"
                else:
                    emp.status = "Out"
            emp.comment = "%s %s" %(cd['comment1'], cd['comment2'])
            emp.estimated_return = cd['estimated_return']
            emp.save()
        return HttpResponseRedirect('/')
    else:
        employees = Employee.objects.all()
        return render_to_response('statusboard.html', {'employees': employees})
