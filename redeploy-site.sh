#!/usr/bin/env bash

cd project-h-squad-AnthonyH
git fetch && git reset origin/main --hard
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip3 install -r requirements.txt
systemctl daemon-reload
systemctl enable myportfolio
systemctl start myportfolio