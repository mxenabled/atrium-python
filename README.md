# Atrium-Python

A Python wrapper for the [MX Atrium API](https://atrium.mx.com). In order to make requests, you will need to [sign up for the MX Atrium API](https://atrium.mx.com/developers/sign_up) and get a `MX-API-KEY` and a  `MX-CLIENT-ID`.

### Usage

Add the `atriumclient.py` file to your source code's directory and import into your source code file with the following
```python
from atriumclient import AtriumClient
```

Then configure your instance with the following. (The `ENVIRONMENT` will be either `vestibule.mx.com` for the development environment or `atrium.mx.com` for the production environment.)
```python
atriumClient = AtriumClient(ENVIRONMENT, YOUR_MX_API_KEY, YOUR_MX_CLIENT_ID);
```


Then start using class methods to make calls to the Atrium API for data. See the full [Atrium documentation](https://atrium.mx.com/documentation) for more details.

```python
# import AtriumClient wrapper class
from atriumclient import AtriumClient

# Configure AtriumClient
atriumClient = AtriumClient(ENVIRONMENT, YOUR_MX_API_KEY, YOUR_MX_CLIENT_ID);

# Now begin making Atrium calls
atriumClient.createUser("UniqueID", "", ""); # Create a user, etc...
```


### Suggested Atrium Workflow

In the `/examples` directory is a suggested Atrium workflow in a simple command line program.

Navigate to the `/examples` directory. This directory contains the following files:

* exampleworkflow.py - An example showing a suggested workflow for Atrium
* atriumclient.py - Wrapper class for Atrium

##### Run example workflow program with the following command

`$ python exampleworkflow.py ENVIRONMENT YOUR_MX_API_KEY YOUR_MX_CLIENT_ID`
