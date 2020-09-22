#!/usr/bin/python

import os
import sys
import pickle
import httplib2

import google.oauth2.credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class Auth:
    def __init__(self):
        pass

    def authenticate(self, api_key, scopes, service_name, service_version):
        
