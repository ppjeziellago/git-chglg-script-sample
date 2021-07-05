#!/usr/bin/env python
# coding: utf-8

from os import system, environ
import json

GIST_ID=environ['GIST_ID']
GITHUB_TOKEN=environ['GITHUB_USER_TOKEN']
PROJECT_DIR=environ['PROJECT_LOCATION']

CHANGELOG_JSON_FILE="changelog.json"
CHANGELOG_FILE=PROJECT_DIR + "/changelog_generated"
 
# -------------------------------------------------------------------------------------- #
def read_changelog():
    with open(CHANGELOG_FILE, 'r') as changelog_file:
        return changelog_file.read()
# -------------------------------------------------------------------------------------- #
def send_changelog_to_gist(changelog):
    gist_content = {
        "description": "Changelog",
        "files": {
            "CHANGELOG.md": {
                "content": str(changelog)
            }
        }
    }

    open(CHANGELOG_JSON_FILE, "w").write(json.dumps(gist_content))

    CURL_COMMAND = "curl --verbose \'https://api.github.com/gists/{0}\' \
        -X PATCH  -H \'Authorization: Token {1}\' \
        -H \'Content-Type: text/json; charset=utf-8\' \
        --data @{2}".format(GIST_ID, GITHUB_TOKEN, CHANGELOG_JSON_FILE)

    system(CURL_COMMAND)
# -------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    send_changelog_to_gist(read_changelog())
    print('Changelog was generated successfully.')
    