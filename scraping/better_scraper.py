from linkedin_api import Linkedin
import os

# Load credentials from environment variables
linkedin_email = os.getenv('LINKEDIN_EMAIL')
linkedin_password = os.getenv('LINKEDIN_PASSWORD')

if not linkedin_email or not linkedin_password:
    raise ValueError("LinkedIn credentials not found in environment variables.")

api = Linkedin(linkedin_email, linkedin_password)


# GET a profile
#profile = api.get_profile('kylejohnmorris')
#print(api.get_profile_network_info("stevekfrey"))

#print(profile)
# GET 1st degree connections of a given profile

connections = api.get_profile_connections('ACoAAAqywH0BTWzI6ZJYNYP4udit6Dx_9Jlc1f4')
print(connections)