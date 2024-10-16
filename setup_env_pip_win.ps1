Set-ExecutionPolicy RemoteSigned

py -3 -m venv .venv
.venv\scripts\activate

pip install pipreqs
pipreqs . --force
pip install -r requirements.txt
