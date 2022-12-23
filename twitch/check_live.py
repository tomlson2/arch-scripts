#!/usr/bin/python3
import sys
import requests


def checkLive(channel):
    url = "https://gql.twitch.tv/gql"
    query = "query {\n  user(login: \""+channel+"\") {\n    stream {\n      id\n    }\n  }\n}"
    return True if requests.request("POST", url, json={"query": query, "variables": {}}, headers={"client-id": "kimne78kx3ncx6brgo4mv6wki5h1ko"}).json()["data"]["user"]["stream"] else False


for channel in sys.stdin:
    channel = channel.strip()
    if checkLive(channel):
        sys.stdout.write(f"{channel}\n")
