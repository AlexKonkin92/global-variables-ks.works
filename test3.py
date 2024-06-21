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


# def get_vars_list(session, auth_token):
#     url = 'https://dev.ks.works/api/variables/get-by-id'
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {auth_token}'
#     }
#     data = {
#   "UUID": "01edc23d-a7b3-4026-ac67-00b15c0c4000"
# }
    
#     response = session.post(url, headers=headers, json=data, verify=False)
#     response.raise_for_status()
    
#     print("Статус код получения списка проектов:", response.status_code)
#     projects_data = response.json()
    
#     return projects_data

# session, auth_response = get_auth_session()
# auth_token = auth_response['token']
# projects_list = get_vars_list(session, auth_token)
# print(projects_list)

def get_projects_list(session, auth_token):
    url = 'https://dev.ks.works/api/projects/get-list'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {auth_token}'
    }
    data = {
        "limit": 0,
        "page": 0,
        "perPage": 0,
        "term": ""
    }
    
    response = session.post(url, headers=headers, json=data, verify=False)
    response.raise_for_status()
    projects_data = response.json()
    return projects_data

session, auth_response = get_auth_session()
auth_token = auth_response['token']
projects_list = get_projects_list(session, auth_token)
filtered_project_uuid = '01eec0fa-c2cb-5321-a282-00b15c0c4000'
filtered_projects = [project for project in projects_list['data'] if project['uuid'] == filtered_project_uuid]
print(filtered_projects)