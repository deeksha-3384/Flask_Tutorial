- First create a folder and open
- Open terminal and check the python version using: python --version
- Create a virtual envirnment file using: python -m venv venv
- Activate the virtual envirnment using: venv\Scripts\Activate.ps1
- Intsall flask: pip instal flask
- Check packages: pip list

## requirements.txt
- It contains the Python packages your project depends on.
- Created using the command: pip freeze > requirements.txt
  - pip : Python's package manager
  - pip freeze : Show me all Python packages currently installed in this environment, along with their versions
  - > : sends to the requirments.txt file

## templates
- In Flask, templates is a folder where you keep your HTML files.

## jinja2
- Jinja2 is a template engine for Python. In Flask, it lets you put Python data/logic into your HTML.