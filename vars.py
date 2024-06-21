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
#         #,        'X-Project-UUID': '01edc7f1-603c-9d7b-8f10-00b15c0c4000'
#     }

#     data = {
#         'uuid': '01ee57c4-ceea-1ae5-9fa3-00b15c0c4000'
#     }
    
#     response = session.post(url, headers=headers, json=data , verify=False)  # Пустой объект, как указано в документации
#     response.raise_for_status()  # Генерирует исключение для статус-кодов 4XX/5XX
    
#     variables = response.json()
#     return variables

# session, auth_response = get_auth_session()
# auth_token = auth_response['token']

# variables = get_default_variables_by_project(session, auth_token)
# print(variables)

#get_default_variables_by_project - не работает
# def get_default_variables_by_project(session, auth_token):
#     url = 'https://dev.ks.works/api/variables/get-list'
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {auth_token}'
#         #,        'X-Project-UUID': '01edc7f1-603c-9d7b-8f10-00b15c0c4000'
#     }

#     data = {'processUuid': "01ee57c4-b5c6-18e9-9fa3-00b15c0c4000"}
    
#     response = session.post(url, headers=headers, json=data , verify=False)  # Пустой объект, как указано в документации
#     response.raise_for_status()  # Генерирует исключение для статус-кодов 4XX/5XX
    
#     variables = response.json()
#     return variables

# session, auth_response = get_auth_session()
# auth_token = auth_response['token']

# variables = get_default_variables_by_project(session, auth_token)
# print(variables)

# def get_default_variables_by_project(session, auth_token):
#     url = 'https://dev.ks.works/api/users/get-default-variables-by-projects-roles'
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {auth_token}'
#         #,'processUuid': "01ee57c4-b5c6-18e9-9fa3-00b15c0c4000"
#     }

#     data = {
#   "rolesUUIDs": [
#     "3bbb1ab8-0eef-11eb-a911-0242ac171102"
#   ]
# }
    
#     response = session.post(url, headers=headers, json=data , verify=False)  # Пустой объект, как указано в документации
#     response.raise_for_status()  # Генерирует исключение для статус-кодов 4XX/5XX
    
#     variables = response.json()
#     return variables

# session, auth_response = get_auth_session()
# auth_token = auth_response['token']

# variables = get_default_variables_by_project(session, auth_token)
# print(variables)

# role+user
def get_default_variables_by_project(session, auth_token):
    url = 'https://dev.ks.works/api/users/get-global-variables-by-priority'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {auth_token}'
    }
    data = {
  "rolesUUIDs": [
    "3bbb1ab8-0eef-11eb-a911-0242ac171102"
  ],
  "userUUIDs": [
    "3bbb1ab8-0eef-11eb-a911-0242ac171102"
  ]
} 
    response = session.post(url, headers=headers, json=data , verify=False)  # Пустой объект, как указано в документации
    response.raise_for_status()  # Генерирует исключение для статус-кодов 4XX/5XX
    
    variables = response.json()
    return variables

session, auth_response = get_auth_session()
auth_token = auth_response['token']

variables = get_default_variables_by_project(session, auth_token)
print(variables)

# def format_and_print_variables(variables):
#     for var in variables['defaultVariables']:
#         # Получаем имя переменной из словаря 'value'
#         name = var.get('value', {}).get('name', 'Н/Д')
#         eventType = var.get('eventType', 'Н/Д')
#         project_uuid = var.get('projectUuid', 'Н/Д')
#         uuid = var.get('uuid', 'Н/Д')
        
#         print(f'{name} - {eventType} - {project_uuid} - {uuid}')

# # Продолжение остается без изменений
# session, auth_response = get_auth_session()
# auth_token = auth_response['token']
# variables = get_default_variables_by_project(session, auth_token)
# format_and_print_variables(variables)
