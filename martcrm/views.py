from django.shortcuts import render , redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from martcrm.models import ClientMaster
from martcrm.models.WebCategoryMaster import WebCategoryMaster
from martcrm.models.CountryMaster import CountryMaster
from martcrm.models.CountryStates import CountryStates
from martcrm.models.CityMaster import CityMaster
from martcrm.models.ProfileMaster import ProfileMaster
from martcrm.models.UserAccounts import UserAccounts
from martcrm.models.EmailMaster import EmailMaster
from martcrm.models.MobileMaster import MobileMaster
from martcrm.models.AccountProfile import AccountProfiles
from martcrm.helper.category import build_category_tree
from martcrm.helper.register_profile import create_profile
from django.db import transaction
from django.urls import reverse
from django.http import JsonResponse


# Create your views here.

@csrf_exempt
def index(request):
    context = dict()

    client_id = request.session.get('client_id')
    user_id = request.session.get('user_id')
    print("Session",client_id)
    print("Session",user_id)
    if client_id or user_id:
        user_obj = ClientMaster.objects.get(client_id = client_id)

        context.update({'client_id':user_obj.client_id,'contact_person':user_obj.contact_person,'co_name':user_obj.co_name})

        return render(request,'mart-trade/index.html',context)
    else:
        # return redirect('mart-trade/login.html')
        return render(request,'mart-trade/login.html')

@csrf_exempt
def login(request):
    context = dict()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:

            login_check = ClientMaster.objects.filter(username = username,password=password).exists()

            if login_check:
                user_obj = ClientMaster.objects.filter(username = username).first()
                request.session['client_id'] = user_obj.client_id
                request.session['contact_person'] = user_obj.contact_person
                request.session['co_name'] =  user_obj.co_name

                context.update({'client_id':user_obj.client_id,'contact_person':user_obj.contact_person,'co_name':user_obj.co_name})

                return redirect ('index')            

    return render(request,'mart-trade/login.html')

@csrf_exempt
def logout(request):
    context = dict()
    if request.method == 'POST':
        logout = request.POST.get('logout')
        try:
            if logout:
                request.session.clear()
                return HttpResponseRedirect(reverse('login')) 
        except Exception as ex:
            error = f"There is some error in execution {ex}"
            context.update({'error': error, 'status': 400})
            return render(request, 'mart-trade/error.html', context)

def success(request):
    return render(request,'mart-trade/success.html')

def error(request):
    context = {}
    country_obj = CountryMaster.objects.all()
    print("Country Obj ==",country_obj)
    context.update({'country':country_obj})
    return render(request,'mart-trade/error.html',context)



@csrf_exempt
def register(request):
    context = dict()
    if request.method == 'POST':
        co_name = request.POST.get('company_name')
        contact_person = request.POST.get('name')
        emailid = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if emailid:
            cl_obj = ClientMaster.objects.filter(emailid = emailid).exists()

            if not cl_obj:
                if co_name and contact_person and emailid and username and password:
                    try:
                        with transaction.atomic() as txn:
                            client_obj = ClientMaster(co_name=co_name, contact_person = contact_person, emailid = emailid, username=username, password=password)
                            client_obj.save()
                            if client_obj:
                                success = "Your profile has been created successfully. Try to login via login Page."
                                context.update({'success':success})
                    except Exception as ex:
                            message = f"There is some technical Issue : {ex}"
                            context.update({'error':message})
            else:
                error = "Email Id already register user another email id"
                context.update({'error':error})

    return render(request,'mart-trade/register.html',context)


@csrf_exempt
def search(request):
    return render(request,'mart-trade/search.html')
    
@csrf_exempt
def add_category(request):
    context = {}

    category_obj = WebCategoryMaster.objects.all()
    context['categories'] = category_obj  # Updated this line to properly update the context dictionary

    if request.method == 'POST':
        parrent_id = request.POST.get('parrent_id')
        category_name = request.POST.get('category_name')
        category_description = request.POST.get('category_description')
        cat_type = request.POST.get('cat_type')

        if category_name:
            webcat_obj = WebCategoryMaster(
                category_name=category_name,
                parrent_id=parrent_id,
                category_description=category_description,
                type = cat_type,
                multilingual_catalogs =0
            )
            webcat_obj.save()
            if webcat_obj:
                context.update({'success':"Category Added Successfully."})
                return render(request,'mart-trade/success.html',context)

    return render(request, 'mart-trade/add_category.html', context)


def category_list(request):
    context = {}
    categories = WebCategoryMaster.objects.all()

    if categories:
        formatted_category_list = format_category_list(categories)
        return render(request, 'mart-trade/category_list.html', {'formatted_category_list': formatted_category_list})
    else:
        return render(request, 'mart-trade/category_list.html', context)


def format_category_list(categories):
    formatted_category_list = []

    # Create a dictionary to quickly look up categories by ID
    category_dict = {category.category_id: category for category in categories}

    # Format the category list
    for category in categories:
        formatted_category_list.append(format_category(category, category_dict))

    return formatted_category_list

def format_category(category, category_dict):
    category_path = [category.category_name]

    # Traverse the hierarchy upward
    parent_id = category.parrent_id
    while parent_id is not None:
        parent_category = category_dict.get(parent_id)
        if parent_category:
            category_path.insert(0, parent_category.category_name)
            parent_id = parent_category.parrent_id
        else:
            break

    # Join the category path with " > "
    formatted_category = f"{category.category_id} : {' : '.join(category_path)}"

    return formatted_category

@csrf_exempt
def select_state(request):
    context = {}
    if request.method == 'POST':
        country_code = request.POST.get('country_code')
        state_objs = CountryStates.objects.filter(country_code=country_code).values('state_id', 'state')

        # Serialize the data to send as JSON response
        serialized_data = list(state_objs)  # Convert queryset to a list

        # Return a JsonResponse with the serialized data
        return JsonResponse(serialized_data, safe=False)

    # Handle other HTTP methods if needed
    return JsonResponse({'error': 'Invalid request method'}, status=400)



@csrf_exempt
def select_city(request):
    context = {}
    if request.method == 'POST':
        state = request.POST.get('state')
        city_objs = CityMaster.objects.filter(state=state).values('city_id', 'city')

        # Serialize the data to send as JSON response
        serialized_data = list(city_objs)  # Convert queryset to a list

        # Return a JsonResponse with the serialized data
        return JsonResponse(serialized_data, safe=False)

    # Handle other HTTP methods if needed
    return JsonResponse({'error': 'Invalid request method'}, status=400)


def create_company(request):
    context = {}
    country_obj = CountryMaster.objects.all()
    context['country'] = country_obj
    if request.method == 'POST':
        kwargs = {}
        kwargs['co_name'] = request.POST.get('company_name')
        kwargs['address'] = request.POST.get('address')
        kwargs['pincode'] = request.POST.get('pincode')
        kwargs['city'] = request.POST.get('city')
        kwargs['state'] = request.POST.get('state')
        kwargs['country_code'] = request.POST.get('country_code')
        kwargs['estd'] = request.POST.get('estd')
        kwargs['staff'] = request.POST.get('staff')
        kwargs['prod_exp'] = request.POST.get('prod_exp')
        kwargs['prod_manu'] = request.POST.get('prod_manu')
        kwargs['prod_trader'] = request.POST.get('prod_trader')
        kwargs['prod_serv'] = request.POST.get('prod_serv')
        kwargs['prod_supplier'] = request.POST.get('prod_supplier')
        kwargs['ifexporter'] = 'if_export' in request.POST
        kwargs['ifservice'] = 'if_service' in request.POST
        kwargs['ifmanu'] = 'if_manufacturer' in request.POST
        kwargs['ifsupplier'] = 'if_supplier' in request.POST
        kwargs['iftrader'] = 'if_trader' in request.POST
        kwargs['export_category'] = request.POST.get('export_category')
        kwargs['manu_category'] = request.POST.get('manu_category')
        kwargs['serv_category'] = request.POST.get('serv_category')
        kwargs['trader_category'] = request.POST.get('trader_category')
        kwargs['supplier_category'] = request.POST.get('supplier_category')
        kwargs['directory_listing'] = request.POST.get('directory_listing')
        kwargs['tan_no'] = request.POST.get('tan_no')
        kwargs['gst_no'] = request.POST.get('gst_no')
        kwargs['pan_no'] = request.POST.get('pan_no')
        kwargs['f_name'] = request.POST.get('f_name')
        kwargs['m_name'] = request.POST.get('m_name')
        kwargs['l_name'] = request.POST.get('l_name')
        kwargs['username'] = request.POST.get('username')
        kwargs['password'] = request.POST.get('password')
        kwargs['email_id'] = request.POST.get('email_id')
        kwargs['mobile_no'] = request.POST.get('mobile_no')
        kwargs['desg'] = request.POST.get('designation')
        try:
            profile_obj = create_profile(request,**kwargs)
            print("Profile====Obj ==",profile_obj);
        except Exception as ex:
            print(f"There is some error in company registration {ex}")
            raise

        message = "Profile Created Successfully!"
        context.update({'success': kwargs.get('company_name')})
        return render(request, 'mart-trade/success.html', context)
    return render(request, 'mart-trade/add_company.html', context)


def upload_bulk_profiles(request):
    context= {}
    return render(request,'mart-trade/upload_bulk_profiles.html',context)


def check_email(request):
    if request.method == 'POST':
        email_id = request.POST.get('email_id')
        email_obj = EmailMaster.objects.filter(email=email_id).exists()
        if email_obj:
            return JsonResponse({'message': "Email id already registered", 'status': 409})
        else:
            return JsonResponse({'message': "Email id not registered.", 'status': 200})
        

def select_categories(request):
    if request.method == 'GET':
        webcat_obj = WebCategoryMaster.objects.exclude(parrent_id=0).values('category_id', 'category_name')
        if webcat_obj:
            serialized_data = list(webcat_obj)
            return JsonResponse({'categories': serialized_data}, safe=False)
        else:
            return JsonResponse({'error': 'No categories found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)