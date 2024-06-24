To Create a virtual Environment there are two approaches-

1st approach-
python -m venv env              ...env is virtual environment name
.\env\Scripts\activate          ...to activate the virtual environment

2nd approach-
pip install virtualenv          ...install virtual environment
virtualenv env                     ...create a virtual environment named as env
.\env\Scripts\activate          ...to activate the virtual environment

sometimes while activating virtual environment you may encounter an error. so check which terminal you are
using, if you are using powershell and you get an error means that PowerShell script execution is disabled 
on your system. so open new terminal in cmd and try to activate the virtual environment by running the command.  