## This file is where the the configuration is defined. The keys are taken from the .env file.
## In order to change the api_key for example, you would to change it from the .env file.

import refactor.configuration
import refactor.client
import os
from dotenv import load_dotenv
load_dotenv()

## This is where the configuration is set up
con = refactor.configuration.Configuration(
    api_key=os.environ.get('api_key'),
    api_key_secret=os.environ.get('api_key_secret'),
    access_token=os.environ.get('access_token'),
    access_token_secret=os.environ.get('access_token_secret'),
    bearer_token=os.environ.get('bearer_token'),
)

## We are creating a Twitter client using the defined configuration.
## The twitter client is what will allow us to make API requests.
twitter_client = refactor.client.Client(con)

