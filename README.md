# Welcome to Auth0-Streamlit :forked:

**The fastest way to provide comprehensive login inside Streamlit**

_Updated to latest auth0 sdk_

This is a fork of the original [onradbez/streamlit-auth0@c5e5666](https://github.com/conradbez/streamlit-auth0#c5e5666). Thanks to the original author for the great work!

![Example of Streamlit-Auth0|635x380](demo.gif?raw=true)

## Installation

`pip install streamlit-auth0-ts`

## Setup

- Register for Auth0
- Create a Single Page Application and navigate to the "settings" tab
- Set `Allow Callback URLs` to `http://localhost:8501/component/streamlit_auth0_component.auth0_login_button/index.html`
- Set `Allowed Logout URLs` to `http://localhost:8501/component/streamlit_auth0_component.auth0_login_button/index.html`
- Set `Allowed Web Origins` to `http://localhost:8501`
- Copy `client_id` and `domain` from the Application settings, and put it into a `.env` file in the root of your project and ddd the following:

  - `AUTH0_CLIENT_ID="your_client_id"`
  - `AUTH0_DOMAIN="your_domain"`

- Follow example below

## An example

On Auth0 website start a "Single Page Web Application" and copy your client-id / domain (of form xxxx.us.auth0.com) into code below.

```
from auth0_component import login_button
import streamlit as st

clientId = "...."
domain = "...."

user_info = login_button(clientId, domain = domain)
st.write(user_info)
```

`user_info` will now contain your user's information

## Todo

- Pass all info through JWT, at the moment the `sub` field is the only field passing through verification
- Test with other providers, only Google tested

## Deploy

- `Change version in setup.py`
- `cd auth0_component/frontend/  && npm run build && cd .. && cd .. && rm -rf dist/* && python setup.py sdist bdist_wheel`
- `twine upload dist/*`
