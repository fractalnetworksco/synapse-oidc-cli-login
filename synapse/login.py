import requests
import uuid
from urllib import parse

session_id = str(uuid.uuid4())

OIDC_PROXY_HOST = f"http://localhost:8008"
OIDC_PROXY_CALLBACK_ENDPOINT = f"{OIDC_PROXY_HOST}/callback/{session_id}"
OIDC_PROXY_SESSION_ENDPOINT = f"{OIDC_PROXY_HOST}/poll/{session_id}"
SYNAPSE_HOST = "https://access.fractalnetworks.co"
SYNAPSE_OIDC_ENDPOINT = f"{SYNAPSE_HOST}/_matrix/client/v3/login/sso/redirect/oidc-keycloak?redirectUrl={parse.quote_plus(OIDC_PROXY_CALLBACK_ENDPOINT)}&org.matrix.msc3824.action=login"
SYNAPSE_AUTH_ENDPOINT = f"{SYNAPSE_HOST}/_matrix/client/v3/login"

def do_synapse_login(token):
    response = requests.post(SYNAPSE_AUTH_ENDPOINT,
                             json={"token": token,
                                    "initial_device_display_name": "Fractal Networks",
                                    "type": "m.login.token"})
    return response.json()


# launch the browser so the user can login
sh.wslview(SYNAPSE_OIDC_ENDPOINT)

# poll oidc proxy for auth session data
session_data = requests.get(OIDC_PROXY_SESSION_ENDPOINT).json()

print(do_synapse_login(session_data['token']))
