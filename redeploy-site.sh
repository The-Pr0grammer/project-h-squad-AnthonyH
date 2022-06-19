#!/usr/bin/env bash

pkill -f tmux
cd project-h-squad-AnthonyH
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip3 install -r requirements.txt
tmux new -d -s "portfolio-project" flask run --host=0.0.0.0  