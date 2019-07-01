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

By default the behavior of eagle is to find all files in your server with .log, .json, .error extensions.
You may edit that on the code itself.

You will nead to create an eagle.conf in the main directory. We didn't include this here for security.

```
[eagle]
username=???
flndevdomain=???
maxlines=???
gaflogsdir=???
thriftlogsdir=???
remotetmpdir=???
```

You will also need to create a config.js on web folder to list all the log names and their corresponding view names like so.

```
export const LOG_FILES = {
    'logname': 'displayName',
}
```