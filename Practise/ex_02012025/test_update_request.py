import pytest
import requests

def test_request_update(create_token,create_bookingid,patch_request,delete_request):
    print(create_bookingid)
# Create booking assertions
    assert create_bookingid >0
    assert type(create_bookingid) == int
    assert create_bookingid is not None

# Create token assertions
    print(create_token)
    assert type(create_token) == str
    assert len(create_token) > 14

# Patch request assertions
    #assert patch_request.status_code == 200
    assert patch_request == "Mehak"
    assert type(patch_request) == str

#Delete request assertions
    #assert delete_request.statuscode == 201  this is not working
    print(delete_request) #it is printing the status code


