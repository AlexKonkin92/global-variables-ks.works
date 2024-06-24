import requests
from config import Config


def global_variables_view():
    try:
        session, auth_response = get_auth_session()
        auth_token = auth_response['token']
        projects_dict = get_projects_dict(session, auth_token)
        print(projects_dict)
    # except HTTPError as e:
    #     print(f"HTTP error during authentication or user validation: {str(e)}", 400)
    except KeyError as e:
        print(f"Key error: {str(e)}", 400)
    except Exception as e:
        print(f"Unknown error: {str(e)}", 400)


def get_auth_session() -> dict:
    session = requests.Session()
    data = {
        "login": Config.LOGIN,
        "password": Config.PASSWORD
    }
    headers = {'Content-Type': Config.CONTENT_TYPE,
        'Referer': Config.REFERER_URL
        }
    response = session.post(Config.AUTH_URL, json=data, headers=headers, verify=Config.VERIFY_SSL)
    response.raise_for_status()
    response_data = response.json()
    return session, response_data

def get_projects_dict(session: requests.Session, auth_token: str) -> dict:
    
    headers = {
        'Content-Type': Config.CONTENT_TYPE,
        'Authorization': f'Bearer {auth_token}',
        'Referer': Config.REFERER_URL
    }
    print(headers)
    data = {
        "limit": 0,
        "page": 0,
        "perPage": 0,
        "term": ""
    }
    # response = session.post(Config.PROJECTS_URL, headers=headers, json=data, verify=Config.VERIFY_SSL)
    # response.raise_for_status()
    # projects_list = response.json()
    # print(projects_list)
    # projects_data = projects_list.get('data', [])
    # print(projects_data)
    # for project in projects_data:
    #     project_uuid = project.get('uuid')
    #     project_name = project.get('name')
    #     print(f'UUID: {project_uuid}, Name: {project_name}')
    #projects_dict = {project['uuid']: project for project in projects_list['data']}
    #return projects_dict
    response = session.post(Config.INTEGRATION_URL, headers=headers, json=data, verify=Config.VERIFY_SSL)
    response.raise_for_status()
    projects_list = response.json()
    print(projects_list)

if __name__ == "__main__":
    global_variables_view()
