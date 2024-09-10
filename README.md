# Cam-Cap
A project for the shop camera to take captures at times using OpenCV


## Relevant documentation

- Python venv: https://docs.python.org/3/library/venv.html
- OpenCV(cv2): https://docs.opencv.org/4.x/index.html



## Run Locally

Have an active camera and clone the project

```bash
  git clone https://github.com/Stony-Brook-Solar-Racing/Cam-Cap.git
```

### Creating and activating an venv (virtual environment)

In the project directory, create an venv named "env"

```bash
  python -m venv env
```

Then activate the newly created venv by typing one of the commands below:

| Shell  | Command |
| ------------- | ------------- |
| cmd  | `env\Scripts\activate.bat` |
| PowerShell  | `env\Scripts\activate.ps1`  |
| bash/zsh  | `source env/Scripts/activate`  |
| csh/tcsh  | `source <venv>/bin/activate.csh`  |


Once virutal environment is active, install dependencies

```bash
  pip install -r requirements.txt
```

Then start running!

### Deactivate venv
Once you've wrapped up what your doing, the venv must be deactivated. 
- To deactivate the virtual environment, type `deactivate` in the shell
