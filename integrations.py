import requests
from config import Config


def global_variables_view():
    try:
        session, auth_response = get_auth_session()
        auth_token = auth_response['token']
        projects_dict = get_integrations_list(session, auth_token)
        
        projects_dict2 = get_integrations_list2(session, auth_token)
        
        print(projects_dict)
        print(projects_dict2)
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

def get_integrations_list(session: requests.Session, auth_token: str) -> dict:
    
    headers = {
        'Content-Type': Config.CONTENT_TYPE,
        'Authorization': f'Bearer {auth_token}',
        'Referer': Config.REFERER_URL,
            'X-Project-Uuid': "01ef32d0-b624-dada-96aa-00b15c0c4000"
    }
    data = {
  "UUIDs": [
    "01ef32db-a668-9cdd-8e0e-00b15c0c4000"#integrationUuid
  ]
}
    response = session.post(Config.TEST_URL, headers=headers, json=data, verify=Config.VERIFY_SSL)
    response.raise_for_status()
    projects_list = response.json()
    print(projects_list)

def get_integrations_list2(session: requests.Session, auth_token: str) -> dict:
    
    headers = {
        'Content-Type': Config.CONTENT_TYPE,
        'Authorization': f'Bearer {auth_token}',
        'Referer': Config.REFERER_URL,
            'X-Project-Uuid': "01ef32d0-b624-dada-96aa-00b15c0c4000"
    }
    data = {'onlyGlobal': False, 'byProject': '01ef32d0-b624-dada-96aa-00b15c0c4000'}
    response = session.post(Config.TEST_URL2, headers=headers, json=data, verify=Config.VERIFY_SSL)
    response.raise_for_status()
    projects_list = response.json()
    print(projects_list)

if __name__ == "__main__":
    global_variables_view()
