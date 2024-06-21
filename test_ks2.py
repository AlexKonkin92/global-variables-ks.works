import requests

def get_auth_session():
    session = requests.Session()
    data = {
        "login": "admin",
        "password": "Werq12345"
    }
    headers = {'Content-Type': 'application/json'}
    response = session.post('https://dev.ks.works/api/auth/login', json=data, headers=headers, verify=False)
    response.raise_for_status()
    print("Статус код ответа аутентификации:", response.status_code)

    response_data = response.json()
    return session, response_data

# def get_default_variables_by_project(session, auth_token):
#     url = 'https://dev.ks.works/api/variables/get-by-id'
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {auth_token}'
#     }

#     data = {
#         'uuid': '01ee57c4-ceea-1ae5-9fa3-00b15c0c4000'
#     }
    
#     response = session.post(url, headers=headers, json=data , verify=False) 
#     response.raise_for_status() 
    
#     variables = response.json()
#     return variables

# session, auth_response = get_auth_session()
# auth_token = auth_response['token']

# variables = get_default_variables_by_project(session, auth_token)
# print(variables)

def get_default_variables_by_project(session, auth_token):
    url = 'https://dev.ks.works/api/users/get-default-variables-by-project'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {auth_token}'
        ,'X-Project-Uuid': "01ee09b7-9523-d21f-b3ed-00b15c0c4000"
    }

    data = {
  #'uuid': '01ee57c4-ceea-1ae5-9fa3-00b15c0c4000'
}
    
    response = session.post(url, headers=headers , verify=False)  # Пустой объект, как указано в документации
    response.raise_for_status()  # Генерирует исключение для статус-кодов 4XX/5XX
    
    variables = response.json()
    return variables

session, auth_response = get_auth_session()
auth_token = auth_response['token']

variables = get_default_variables_by_project(session, auth_token)
print(variables)