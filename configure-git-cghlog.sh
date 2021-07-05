#!/usr/bin/env bash
set -x

echo Downloading git-chglog....

go get -u github.com/git-chglog/git-chglog/cmd/git-chglog

cd ${PROJECT_LOCATION}

git fetch --tags

./../go/bin/git-chglog ${TAG_ORIGIN}.. >> changelog_generated
