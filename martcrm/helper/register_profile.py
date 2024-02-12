from django.shortcuts import render , redirect,HttpResponseRedirect
from martcrm.models.AccountEmails import AccountEmails
from martcrm.models.AccountMobiles import AccountMobiles
from martcrm.models.AccountProfile import AccountProfiles
from martcrm.models.ProfileMaster import ProfileMaster
from martcrm.models.UserAccounts import UserAccounts
from martcrm.models.MobileMaster import MobileMaster
from martcrm.models.EmailMaster import EmailMaster
from django.db import transaction


def create_profile(request,**kwargs):
    client_id = request.session.get('client_id')
    try:
        with transaction.atomic() as txn:
            email_obj = EmailMaster.objects.create(email=kwargs.get('email_id'))
            print("Email obj ======",email_obj)
            mobile_obj = MobileMaster.objects.create(mobile=kwargs.get('mobile_no'))
            print("mobile_obj ======",mobile_obj)
            user_obj = UserAccounts.objects.create(username=kwargs.get('username'), password=kwargs.get('password'), fname=kwargs.get('f_name'), mname=kwargs.get('m_name'), lname=kwargs.get('l_name'), desg=kwargs.get('desg'))
            print("user_obj ======",user_obj.__dict__);
            profile_obj = ProfileMaster.objects.create(
                co_name=kwargs.get('co_name'),
                client_id = client_id,
                address=kwargs.get('address'),
                pincode=kwargs.get('pincode'),
                city=kwargs.get('city'),
                state=kwargs.get('state'),
                country_code=kwargs.get('country_code'),
                # estd=kwargs.get('estd'),
                # staff=kwargs.get('staff'),
                # prod_exp=kwargs.get('prod_exp'),
                # prod_manu=kwargs.get('prod_manu'),
                # prod_supplier=kwargs.get('prod_supplier'),
                # prod_serv=kwargs.get('prod_serv'),
                # prod_trader=kwargs.get('prod_trader'),
                # # ifexporter=kwargs.get('ifexporter'),
                # # ifservice=kwargs.get('ifservice'),
                # # ifmanu=kwargs.get('ifmanu'),
                # # iftrader=kwargs.get('iftrader'),
                # gst_no=kwargs.get('gst_no'),
                # pan_no=kwargs.get('pan_no'),
                # tan_no=kwargs.get('tan_no'),
                # export_category=kwargs.get('export_category'),
                # manu_category=kwargs.get('manu_category'),
                # trader_category=kwargs.get('trader_category'),
                # supplier_category=kwargs.get('supplier_category'),
                # serv_category=kwargs.get('serv_category'),
                # directory_listing=kwargs.get('directory_listing')
            )
            print("Profile obj == ",profile_obj)
            email_key = email_obj.email_key
            print("email_key == ",email_key)
            mobile_key = mobile_obj.mobile_key
            print("mobile_key == ",mobile_key)
            userid = user_obj.userid
            print("user_user_id ====",user_obj.userid);
            profile_id = profile_obj.profile_id
            acc_email_obj = AccountEmails.objects.create(userid=user_obj, email_key=email_obj,ifdefault=True)
            acc_mob_obj = AccountMobiles.objects.create(userid=user_obj, mobile_key=mobile_obj,ifdefault=True)
            acc_profile = AccountProfiles.objects.create(profile=profile_obj, userid=user_obj,default_account=True)

            return profile_id
    except Exception as ex:
        print(ex)
        raise


    