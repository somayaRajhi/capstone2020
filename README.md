# capstone2020
# Developer Setup

1. Create a virtual environment

    `python3 -m venv .venv`

2. Activate the virtual environment

    Linux/mac: `source .venv/bin/activate`
    
    Windows: `.venv\Scripts\activate`

3. Install required libraries

    `pip install -r requirements.txt`

4. Install source as an editable package

    `pip install -e .`

5. Create the file `.env` containing our sensitive data (that should never go in the repo)

	 `API_KEY=<your api key>`
	 
Once you have completed these steps you should be able to:

* Run `pytest` from the root of the project
* Run `pytest` from `tests/`
* Run `main.py` from anywhere (e.g. `python src/python_structure/main.py`)
* Run `pylint` from the root directory of the project


## Files and Directories

* `requirements.txt` - The list of required libraries.  
* `setup.py` - The script the `pip` runs to install the package.  The current version is bare-bones.  Many
   other options should be set for a production system.
* `src/python_structure/__init__.py` - Establishes the `python_structure` directory as a package. This file is empty
   by default.


## Pylint

* When running Pylint, run the command while in the root directory of the project
* Command to run pylint: `pylint tests/*.py src`
* Pylint config file name is `.pylintrc`
* Pylint can only run recursively through directories if they are included in the Python package
* Pylint uses the config file in the folder from where it is called
* If there is no generated config file in folder, Pylint will use a default built-in config file
* Pylint can be run on packages such as the demo folder with `pylint <name_of_package>`
