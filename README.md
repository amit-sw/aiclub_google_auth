# AIClub Google Auth

A lightweight Python library for implementing Google OAuth authentication in AIClub applications.

## Overview

This library provides a simple interface for implementing Google OAuth 2.0 authentication flow in Python applications. It's specifically designed for AIClub applications but can be used in any Python project requiring Google authentication.

## Features

- Easy-to-use Google OAuth 2.0 authentication flow
- User information retrieval from Google ID tokens
- Configurable scopes for different access levels
- Support for both secure and development environments
- Streamlit integration example included

## Installation

```bash
pip install -r requirements.txt
```

## Dependencies

- `google-auth-oauthlib`: For handling the OAuth 2.0 flow
- `google-auth`: For ID token verification
- `streamlit`: For the sample application (optional)

## Configuration

Create a `.env` file with the following variables:

```
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_client_secret
GOOGLE_REDIRECT_URI=your_redirect_uri
```

You'll need to create OAuth 2.0 credentials in the [Google Cloud Console](https://console.cloud.google.com/).

## Usage

### Basic Usage

```python
from oauth import AIClubGoogleAuth

auth_config = {
    "client_id": "your_client_id",
    "client_secret": "your_client_secret",
    "redirect_uri": "your_redirect_uri",
    "allow_insecure_http": True  # Set to False in production
}

auth = AIClubGoogleAuth(auth_config)

# Get the authorization URL to redirect the user to
auth_url, state = auth.get_authorization_url()

# After the user is redirected back to your application
user_info = auth.get_user_info(query_params, state)
```

### Streamlit Integration

See `sample_test.py` for a complete example of integrating with Streamlit:

```python
import streamlit as st
import uuid
import os
from dotenv import load_dotenv
from oauth import AIClubGoogleAuth

load_dotenv()

auth_config = {
    "client_id": os.getenv("GOOGLE_CLIENT_ID"),
    "client_secret": os.getenv("GOOGLE_CLIENT_SECRET"),
    "redirect_uri": os.getenv("GOOGLE_REDIRECT_URI"),
    "allow_insecure_http": True
}

auth = AIClubGoogleAuth(auth_config)

# Streamlit UI and authentication logic
# ...
```

## Security Considerations

- Always set `allow_insecure_http` to `False` in production environments
- Store your client secrets securely
- Validate the state parameter to prevent CSRF attacks
- Use HTTPS for all production deployments

## License

This project is proprietary and confidential to AIClub.

## Contributing

Contributions are welcome. Please ensure you follow the coding standards and include appropriate tests for new features.