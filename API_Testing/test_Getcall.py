import pytest
import requests
class Test_case:

    def test_case_001(self):
        Resp=requests.get("https://reqres.in/api/users?page=2")
        Code=Resp.status_code
        assert  Code==200 ,"status code doesn't match"
       #print(Resp.cookies)
       #print(Resp.headers)
       #print(Resp.content)
       #print(Resp.status_code)
       #print(Resp.text)
        Json_Resp=Resp.json()
        print(Json_Resp['total'])
        assert Json_Resp["total"]==12,"does not match json response"
        print(Json_Resp['data'])
        print(Json_Resp['data'][0]["email"])
        assert  (Json_Resp['data'][0]['email']).endswith("@reqres.in"),"Email does not Match"
        print(Json_Resp['data'][1]['first_name'])
        assert Json_Resp['data'][1]['first_name']=="Lindsay",'Please Enter valide name '


    def test_case_002(self):

        payload ={
        "name": "morpheus",
        "job": "automation"
          }
        response=requests.post("https://reqres.in/api/users",data=payload)
        print(response.json())
        assert response.json()["job"]=="automation","Job details are not correct"

    def test_case003(self):
        delet_res= requests.delete("https://reqres.in/api/users/2")
        code=delet_res.status_code
        print(code)
        assert code==204 ," record not deleted "
