# oidc-cli-proxy
Enable OIDC authentication for your command-line utilities. Only support Matrix's Synapse for now.

# Setup
```
$ python -m venv venv
$ pip install -r requirements.txt
```

# Start the proxy
```
$ python synapse/proxy.py
```

# Authenticate with access.fractalnetworks.co via CLI
```
$ python synapse/login.py
```