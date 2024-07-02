import requests
from config import Config
import urllib3
from requests.exceptions import HTTPError

# предупреждения о ненадежных https запросах
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def global_variables_view():
    try:
        session, auth_response = get_auth_session()
        auth_token = auth_response['token']
        projects_dict = get_projects_dict(session, auth_token)
        integrations_list = get_integrations_list(session, auth_token,projects_dict)
        print(integrations_list)
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
    data = {
        "limit": 0,
        "page": 0,
        "perPage": 0,
        "term": ""
    }
    response = session.post(Config.PROJECTS_URL, headers=headers, json=data, verify=Config.VERIFY_SSL)
    response.raise_for_status()
    projects_list = response.json()
    projects_dict = {project['uuid']: project for project in projects_list['data']}
    #filtered_projects = {uuid: project for uuid, project in projects_dict.items() if not project.get('encrypted', True) and uuid == '01ef32d0-b624-dada-96aa-00b15c0c4000' } # '01ed1955-7613-8448-08af-00b15c0c4000' ??
    filtered_projects = {uuid: project for uuid, project in projects_dict.items() if not project.get('encrypted', True)}
    return filtered_projects

def get_integrations_list(session: requests.Session, auth_token: str, projects_dict: dict) -> dict:
    results = []
    for project_uuid, project_info in projects_dict.items():
        headers = {
            'Content-Type': Config.CONTENT_TYPE,
            'Authorization': f'Bearer {auth_token}',
            'Referer': Config.REFERER_URL,
            'X-Project-Uuid': project_uuid
        }
        try:
            response = session.post(Config.TEST_TEST, headers=headers, verify=Config.VERIFY_SSL)
            response.raise_for_status()
            projects_list = response.json()
            if 'data' in projects_list:
                for project in projects_list['data']:
                    if project.get('type') == 'integration' and project.get('name'):
                        results.append({'uuid': project['uuid'], 'name': project['name'], 'projectUuid': project_uuid})
        except HTTPError:
            pass
    return results

if __name__ == "__main__":
    global_variables_view()