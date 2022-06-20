from dataclasses import dataclass


@dataclass
class Configuration():
    api_key : str
    api_key_secret : str
    access_token : str
    access_token_secret : str
    bearer_token : str
    return_type = dict
