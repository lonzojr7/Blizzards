#TOdo 1 test user_profile.py creationCreate 
# TODO 2 5 Profile objects
#and call every one of the Profile methods in the driver.
from user_profile import Profile
def test_profile_creation_and_methods():
    #test profile creation
    Sam = Profile("Sam", "CIS", "Physics", "Unknown")
    assert Sam.name == "Sam"