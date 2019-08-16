# EM
EM → Error Messager
This is a service with some configurable checks. If a check fails it sends you a message if a telegram token is given.
Else it will just print the results.

# Checks
## Websites check
You can configure a list of urls in the `CONFIG.py` and if one of them fails or is not reachable the check fails.

# Install
1. `make install`
1. `make start`

# Stop the service
* `sudo systemctl stop em.service`
  `sudo systemctl disable em.service`
  
or

* `make stop`
