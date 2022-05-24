from typing import List, Union
from aiohttp import streamer
from fastapi import APIRouter, Query
from stream import Streamer
import os
from dotenv import load_dotenv
load_dotenv()

bearer_token = os.getenv('bearer_token')

the_stream = Streamer(bearer_token)

router = APIRouter(
    prefix = '/stream_tweets',
    tags=['Streaming Tweets']
)

@router.get('/show_all_rules')
def get_all_rules():
    return the_stream.show_all_rules()

@router.get('/get_rule/{r_tag}')
def get_rule_by_tag(r_tag):
    return the_stream.get_rule(r_tag)

@router.get('/get_tag_query/{r_tag}')
def get_tag_query_by_tag(r_tag):
    return the_stream.get_tag_query(r_tag)

@router.delete('/delete_all_rules')
def delete_rules_all():
    return the_stream.delete_all_rules()

@router.delete('/delete_by_id/{r_id}')
def delete_rule_by_id(r_id):
    return the_stream.delete_rule(r_id)

@router.delete('/delete_rule_by_tag/{r_tag}')
def delete_rule_by_tag(r_tag):
    return the_stream.delete_rule_by_tag(r_tag)

@router.post('/create_rule/{r_value}/{r_tag}')
def create_new_rule(r_value,r_tag):
    return the_stream.create_rule(r_value,r_tag)
