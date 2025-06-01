# setup.py
from setuptools import setup, find_packages

setup(
    name="aiclub_auth_lib",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "google-auth",
        "google-auth-oauthlib",
        "requests",
    ],
    author="AIClub",
    description="Reusable Google OAuth login library for Streamlit",
    python_requires=">=3.7",
)
