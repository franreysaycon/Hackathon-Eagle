# EAGLE

Your personal logs sniffer built with Svelte and Python EEL.

## Requirements

Python >= v3
Node >= 12

## Instalation

Create a virtual env (in this case I auto ignored eagle-env if you want to name it that way) that is python3.

`pip install -r requirements.txt`

To make integration of Svelte and Python run
`./build.sh`

To make development mode in Svelte without the python service
`npm start:dev`

To make autobuild happen while Python is running
`npm run autobuild`
