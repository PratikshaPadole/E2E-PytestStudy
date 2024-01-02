import pytest
import requests

class REQUEST_Method:

    def testcase_01_post(self):
        payload={
            "name":"prati_jha"  ,
            "job":"Senior_test_engineer"
        }
        resp=requests.post("https://reqres.in/api/users",data=payload)
        print(resp.json())
        code=resp.status_code
        assert code == 200 ,"Not Created"


