# sveltekit-python-websocket-experiment
This is a repo to experiment websocket between sveltekit and python

## Usage

### 1. Launch sveltekit app

```
cd sveltekit-app
pnpm install
pnpm dev
```

### 2. connect to websocket server of sveltekit from Python

```
cd python-api
pipenv install
pipenv run serve
```

Python websocket client will send progress value every second.

### 3. Open sveltekit app in browser

open http://localhost:5173, click `Establish WebSocket connection` to start getting progress value from Python.
