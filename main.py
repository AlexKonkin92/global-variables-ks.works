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

def get_variables_and_projects(session, auth_token):
    # Получаем список проектов
    projects_url = 'https://dev.ks.works/api/projects/get-list'
    projects_headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {auth_token}'
    }
    projects_data = {
        "limit": 0,
        "page": 0,
        "perPage": 0,
        "term": ""
    }
    
    projects_response = session.post(projects_url, headers=projects_headers, json=projects_data, verify=False)
    projects_response.raise_for_status()
    projects_list = projects_response.json()
    projects_dict = {project['uuid']: project for project in projects_list['data']}
    
    # Получаем глобальные переменные по приоритету
    variables_url = 'https://dev.ks.works/api/users/get-global-variables-by-priority'
    variables_headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {auth_token}'
    }
    variables_response = session.post(variables_url, headers=variables_headers, verify=False)
    variables_response.raise_for_status()
    
    variables = variables_response.json()
    
    for var in variables['defaultVariables']:
        print(f"{var['value']['name']} - {var['eventType']} - {var['projectUuid']} - {var['uuid']} - {projects_dict.get(var['projectUuid'], {}).get('name', 'Н/Д')} - {projects_dict.get(var['projectUuid'], {}).get('description', 'Н/Д') if projects_dict.get(var['projectUuid'], {}).get('description') else 'Н/Д'}")


session, auth_response = get_auth_session()
auth_token = auth_response['token']
get_variables_and_projects(session, auth_token)


#print(f"{var['value']['name']} - {var['eventType']} - {var['projectUuid']} - {var['uuid']} - {projects_dict.get(var['projectUuid'], {}).get('name', 'Н/Д')} - {projects_dict.get(var['projectUuid'], {}).get('description', 'Н/Д')}")
