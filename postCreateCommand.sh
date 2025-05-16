#!/bin/bash

cd /workspaces/ADS-dev-env-template/backend/python39
export PIPENV_VENV_IN_PROJECT=true
pipenv sync --dev

cd /workspaces/ADS-dev-env-template/frontend/react
npm ci
