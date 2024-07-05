# Django SAML2 Service Provider (SP) integrating with JWT

This project implements a Django REST Framework project configured as a SAML2 Service Provider (SP) that integrates SAML2 and Django REST Framework JWT, using `https://stubidp.sustainsys.com/` as the Identity Provider (IdP).

## Installation

### Prerequisites

- Python 3.6 or higher
- Virtualenv
- pip

### Steps

1. **Clone the repository:**

   ```sh
   git clone https://github.com/sinachaichi/django-rest-jwt-saml2
   cd django-saml2-sp
   ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```
4. **Apply migrations and run server:**

    ```sh
    python manage.py migrate
    python manage.py runserver 8000
    ```
### Configuration
Django Settings
Update your settings.py with the necessary configurations for SAML2 and JWT integration.

### Certificates
You need to generate a private key and public certificate:

```sh
openssl req -new -x509 -key private.key -out public.cert -days 365
```

Place the generated private.key and public.cert in the certificates directory.


### Access the SAML login endpoint:

```sh
http://localhost:8000/api/saml/login/
```
The login will redirect to the Sustainsys Stub IdP for authentication. After successful authentication, it will redirect back to your SP and process the SAML response.

### Documentation
For more details on configuration and usage, refer to the djangosaml2 documentation:
https://djangosaml2.readthedocs.io/index.html
