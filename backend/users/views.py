from django.http import JsonResponse
from .models import profile, customer
import json

# Login Method to authenticate user
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

# Sign up method to add user to db
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

# Helper method to check passwords
def test_password(password, hashedPassword):
    return password == hashedPassword

# Method to add a new customer
def addCustomer(request, profile_id):
    if request.method == 'POST':
        # Extract customer data from the POST request
        payload = json.loads(request.body)
        name = payload.get('name')
        address = payload.get('address')
        city = payload.get('city')
        country = payload.get('country')

        # Get the profile associated with the given profile_id
        try:
            profile_obj = profile.objects.get(unique_id=profile_id)
        except:
            # Handle case where profile with given profile_id doesn't exist
            return JsonResponse({'error':'User with that profile_id does not exist.'}, status=400)

        # Create a new customer associated with the profile
        new_customer = customer.objects.create(
            profile_id=profile_obj.unique_id,
            name=name,
            address=address,
            city=city,
            country=country
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