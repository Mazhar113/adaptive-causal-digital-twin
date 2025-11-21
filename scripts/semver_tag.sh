#!/usr/bin/env bash
set -e
BUMP=${1:-patch}
MSG=${2:-"release"}
if ! git diff --quiet; then
  echo "Uncommitted changes present. Commit before tagging."
  exit 1
fi
CURRENT=$(git describe --tags --abbrev=0 2>/dev/null || echo "v0.0.0")
VER=${CURRENT#v}
IFS='.' read -r MA MI PA <<< "$VER"
case "$BUMP" in
  major) MA=$((MA+1)); MI=0; PA=0;;
  minor) MI=$((MI+1)); PA=0;;
  patch) PA=$((PA+1));;
  *) echo "Unknown bump: $BUMP"; exit 1;;
esac
NEW="v${MA}.${MI}.${PA}"
git tag -a "$NEW" -m "$MSG"
git push origin "$NEW"
echo "Tagged $NEW"
