from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import profile, customer, business
import json

# Login Method to authenticate user.
def authenticate(request):
    if request.method == 'POST':
        try:
            payload = json.loads(request.body)
            email = payload.get('email')
            password = payload.get('password')

            # If email and password are provided
            if email and password:
                # Check if an account with the email exists
                user_object = profile.objects.filter(email=email).first()

                #Check if the password with that email is correct
                if user_object:
                    password_matches = test_password(password, user_object.password)
                    if (password_matches):
                        return JsonResponse({'authenticated': True, 'profileId': user_object.unique_id}, status=200)
                    else:
                        return JsonResponse({'authenticated': False, 'errorDescription': 'Incorrect password entered. Please try again.'}, status=400) 
                else:
                    return JsonResponse ({'authenticated': False, 'errorDescription': 'Incorrect email or password entered. Please try again.'}, status=400)
            else:
                return JsonResponse({'errorDescription': 'Email and password are required fields'}, status=400)
        except Exception as e:
            # Return error if an exception occurs
            return JsonResponse({'errorDescription': str(e)}, status=500)
    else:
        # Return error for unsupported request method
        return JsonResponse({'errorDescription': 'Only POST requests are supported'}, status=405)

# Sign up method to add user to db.
def addUser(request):
    if request.method == 'POST':
        try:
            # Parse JSON payload
            payload = json.loads(request.body)
            name = payload.get('name')
            email = payload.get('email')
            password = payload.get('password')

            # Check that all 3 fields are provided
            if name and email and password:
                # Check if a user with the same email exists
                if profile.objects.filter(email=email).exists():
                    return JsonResponse({'error':'User with the same email already exists. Please try again.'}, status=400)
                else:
                    # Create a new user object
                    new_user = profile(
                        name = name,
                        email = email,
                        password = password
                    )
                    new_user.save()
                    # Return success response
                    return JsonResponse({'success': True, 'message': 'User added successfully'}, status=200)
            else:
                # Return error if any field is missing
                return JsonResponse({'error': 'Name, email, and password are required fields'}, status=400)
        except Exception as e:
            # Return error if an exception occurs
            return JsonResponse({'error': str(e)}, status=500)
    else:
        # Return error for unsupported request method
        return JsonResponse({'error': 'Only POST requests are supported'}, status=405)

# Helper method to check passwords.
def test_password(password, hashedPassword):
    return password == hashedPassword

# Method to add a new customer.
def addCustomer(request, profile_id):
    if request.method == 'POST':
        # Extract customer data from the POST request
        payload = json.loads(request.body)
        name = payload.get('name')
        address = payload.get('address')
        city = payload.get('city')
        country = payload.get('country')
        phone_number = payload.get('phone_number')

        # Get the profile associated with the given profile_id
        try:
            profile_obj = profile.objects.get(unique_id=profile_id)
        except:
            # Handle case where profile with given profile_id doesn't exist
            return JsonResponse({'error':'User with that profile_id does not exist.'}, status=400)

        # Create a new customer associated with the profile
        customer.objects.create(
            profile_id=profile_obj,
            name=name,
            address=address,
            city=city,
            country=country,
            phone_number = phone_number
        )
        return JsonResponse({'success': 'Customer added successfully'}, status=200)
    else:
        return JsonResponse({'error':'Only POST methods are supported.'}, status=400)
    
# Method that returns all customers a user has (filtered by profile_id).
def getCustomers(request, profile_id):
    try:
        customers = list(customer.objects.filter(profile_id=profile_id).values('profile_id', 'name', 'address', 'city', 'country', 'phone_number'))
    except customer.DoesNotExist:
        customers = None

    return JsonResponse({'customers': customers})

# Method that updates a given customer.
def updateCustomer(request, profile_id):
    if request.method == 'POST':
        
        # Get all customers associated with the profile_id
        response = getCustomers(request, profile_id)
        
        customers_json = json.loads(response.content)
        customers = customers_json.get('customers', [])  # Extract customers list
        json_data = (json.loads(request.body)) # The request that is being sent, old and new info

        if customers:
            # Get the specific customer to update (can customize this filter based on the requirements)
            specific_customer = [c for c in customers if c['name'] == json_data.get('name') and c['address'] == json_data.get('address')]
            if specific_customer:
                specific_customer = specific_customer[0]  # Extract the first matching customer

                customer_instance = get_object_or_404(customer, profile_id=profile_id, name=specific_customer['name'], address=specific_customer['address'])
                customer_instance.name = json_data.get('new_name')
                customer_instance.address = json_data.get('new_address')
                customer_instance.city = json_data.get('new_city')
                customer_instance.country = json_data.get('new_country')
                customer_instance.phone_number = json_data.get('new_phone_number')
                customer_instance.save()

                return JsonResponse({'message': 'Customer updated successfully'})
            else:
                return JsonResponse({'error': 'Customer not found'}, status=404)
        else:
            return JsonResponse({'error': 'No customers found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

# Get all customers associated with the profile_id.
# Parse json of the request being sent.
# Match customer with the customer in the request.
# Select customer and delete it from db.
def deleteCustomer(request, profile_id):
    if request.method == 'POST':
        response = getCustomers(request, profile_id)
        
        customers_json = json.loads(response.content)  # Convert JSON response to Python dictionary
        customers = customers_json.get('customers', [])  # Extract customers list
        json_data = (json.loads(request.body)) # The request that is being sent, customer info

        if customers:
            # Get the specific customer to delete.
            specific_customer = [c for c in customers if c['name'] == json_data.get('name') and c['address'] == json_data.get('address')]
            if specific_customer:
                specific_customer = specific_customer[0]  # Extract the first matching customer
                customer_instance = get_object_or_404(customer, profile_id=profile_id, name=specific_customer['name'], address=specific_customer['address'])
                customer_instance.delete()

                return JsonResponse({"message": "Customer deleted successfully"}, status=200)
            else:
                return JsonResponse({"error": "Customer not found"}, status=404)
        else:
            return JsonResponse({"error": "No customers found"}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
def addBusiness(request, profile_id):
    if request.method == 'POST':
        try:
            # Parse JSON payload
            payload = json.loads(request.body)
            name = payload.get('name')
            phoneNumber = payload.get('phone_number')
            address = payload.get('address')
            city = payload.get('city')
            country = payload.get('country')
            organization = payload.get('organization')
            currency = payload.get('currency')

            # Check if all required fields are provided
            if name and phoneNumber and address and city and country and organization and currency:
                # Check if the profile already has a business associated with it
                if business.objects.filter(profile_id_id=profile_id).exists():
                    return JsonResponse({'error':'User already has a business associated with it'}, status=400)
                else:
                    # Create a new business object
                    new_business = business(
                        profile_id_id=profile_id,
                        business_name=name,
                        business_phone_number=phoneNumber,
                        business_address=address,
                        business_city=city,
                        business_country=country,
                        organization_type=organization,
                        currency=currency
                    )
                    new_business.save()
                    # Return success response
                    return JsonResponse({'success': True, 'message': 'Business added successfully'}, status=200)
            else:
                # Return error if any required field is missing
                return JsonResponse({'error': 'All fields are required'}, status=400)
        except Exception as e:
            # Return error if an exception occurs
            return JsonResponse({'error': str(e)}, status=500)
    else:
        # Return error for unsupported request method
        return JsonResponse({'error': 'Only POST requests are supported'}, status=405)
    
def get_business_data(profile_id):
    try:
        # Retrieve the current business associated with the profile_id
        current_business = list(business.objects.filter(profile_id=profile_id).values('business_name', 'business_phone_number', 'business_address', 'business_city', 'business_country', 'organization_type', 'currency'))
    except business.DoesNotExist:
        # If no business is found, return None
        current_business = None
    return current_business

def getBusiness(request, profile_id):
    if request.method == 'GET':
        current_business = get_business_data(profile_id)
        return JsonResponse({'business': current_business})

def updateBusiness(request, profile_id):
    if request.method == 'POST':
        # Retrieve business data associated with the profile_id
        current_business = get_business_data(profile_id)
        current_business_name = current_business[0].get('business_name')

        #Retrieve data from the request body
        request_data = (json.loads(request.body)) # The request that is being sent, old and new info
        business_instance = get_object_or_404(business, profile_id=profile_id, business_name=current_business_name)

        if(business_instance):
            # Get the business instance
            business_instance.business_name = request_data.get('businessName')
            business_instance.business_address = request_data.get('streetAddress')
            business_instance.business_city = request_data.get('city')
            business_instance.business_country = request_data.get('country')
            business_instance.business_phone_number = request_data.get('phoneNumber')
            business_instance.organization_type = request_data.get('organization')
            business_instance.currency = request_data.get('currency')
            business_instance.save()

            return JsonResponse({'message': 'Business updated successfully.'})
        else:
            return JsonResponse({'error': 'Business not found.'})
    else:
        return JsonResponse({'error': 'Method not allowed.'})