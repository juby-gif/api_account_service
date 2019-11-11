from rest_framework import status, response, views
from foundation.models import UserMemoryDB

class LoginAPIView(views.APIView):
    def post(self, request):
        username_datum = request.data.get('username', None)
        password_datum = request.data.get('password', None)
        #print(username_datum,password_datum)
        try:
            if username_datum == None or password_datum == None:
                return response.Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                  'message': 'Missing Field.',
                    })
            else:
                user_credentials = UserMemoryDB.objects.all().order_by('id').values('username','password')
                for user in user_credentials:
                    if username_datum == user['username'] and password_datum == user['password']:
                        return response.Response(
                        status=status.HTTP_200_OK,
                        data={
                          'message': 'Successfully Logged-in!',
                            })
        except Exception as e:
            return response.Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={
              'message': 'Login Failed.',
                })

class RegisterAPIView(views.APIView):
    def post(self,request):

        first_name = request.data.get('fname', None)
        last_name = request.data.get('lname', None)
        username = request.data.get('username', None)
        email_id = request.data.get('email', None)
        password_datum = request.data.get('password', None)

        print(first_name, last_name, username, email_id, password_datum)
        if first_name == None and last_name == None and username == None and email_id == None and password_datum == None:
            return response.Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={
                  'message': 'Missing Credentials!',
                 })
        else:
            print(first_name, last_name, username, email_id, password_datum)
            try:
                memory =  UserMemoryDB.objects.create(fname = first_name, lname = last_name, username = username, email = email_id, password = password_datum)
                memory.save()
                return response.Response(
                status=status.HTTP_200_OK,
                data={
                  'message': 'Successfully Registered!',
                     })

            except Exception as e:
                return response.Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                  'message': 'Please Confirm your Credentials and try again!' + str(e),
                     })

class ProfileAPIView(views.APIView):
    def get(self, request):
        user_credentials = UserMemoryDB.objects.all().order_by('id').values('username','password','fname','lname','email')
        for user in user_credentials:
            username = user['username']
            first_name = user['fname']
            last_name = user['lname']
            email = user['email']
            return response.Response(
            status=status.HTTP_200_OK,
            data={
              'Profile': 'Welcome ' + first_name + " " + last_name + ",",
              'email' : email,
              'username':username,
                })

class ChangePasswordAPIView(views.APIView):
    def post(self, request):
        new_password = request.data.get('npassword')
        user_credentials = UserMemoryDB.objects.all().order_by('id').values('username','password','fname','lname','email')
        for user in user_credentials:
            username = user['username']
            first_name = user['fname']
            last_name = user['lname']
            email = user['email']
            user['password'] = new_password
            print(user['password'])
            password = user['password']
            return response.Response(
            status=status.HTTP_200_OK,
            data={
              'Password Status': "Password Changed Successfully!",
               'username':username,
              'new_password' : password,
                })
