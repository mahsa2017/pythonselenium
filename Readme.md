# Python Selenium Web Automation

## Features
- Support for browser:
    - Chrome (default)
    - Edge
    - Firefox
    - Safari
- Support headless test runs
- Selenium 4.7.0
- Logging info for each action
- HTML Report and HTML dashboard
For more features, see [SeleniumBase Features](https://seleniumbase.io/help_docs/features_list/#seleniumbase-features).

## Installation
IDE used: PyCharm

Python Selenium Web Automation Framework requires [Python](https://www.python.org/) v3+ and [SeleniumBase](https://seleniumbase.io/) to run.
Once you install Python from their official website now it's time to Install SeleniumBase:
```sh
pip3 install seleniumbase
```
Note: If your python is version 3 above you will need to run pip3 otherwise pip will work

Next you need to install browser drive for instance chromeDrive through seleniumBase:

```commandline
sbase get chromedriver latest 
```
Create a virtual environment on your local machine.  See [Pipenv & Virtual Environments](https://docs.python-guide.org/dev/virtualenvs/#virtualenvironments-ref) for details.

Install the dependencies:
```sh
python3 -m pip install -r requirements.txt
```

## Structure:
Folders:
- **assets**: This folder will contain all the files like images, css files or json files or test data.
- **custom_Screenshot**: This folder will save any screenshots that you make
- **latest_logs**: This folder will be generated when a test fails to save any log and screenshots.
- **tests**:  All the test cases python files will be kept here.
- **requirements.txt**: This file stores information about all the libraries, modules, and packages which are specific to project.

Test report files:
- dashboard.html
- report.html

## Run tests
To run each individual test, right-click on the test name on pyCharm IDE and select "run <test name>".
To run a test file, go to the terminal and type:
```sh
pytest tests/<file name> --dashboard --rs --headless --html=report.html
```
Or if you need to run tests for an specific file which has some print commands in it
```commandline
pytest -k ${test_file_name} -s
```

To see a full list of `pytest` options, go to the terminal and type:
```sh
sbase options
```

## Integrate with Azure pipelines
Read [here](https://seleniumbase.io/integrations/azure/azure_pipelines/ReadMe/#give-your-new-project-a-name-and-set-visibility-to-public-for-your-seleniumbase-fork).

## Coming Up:
- Page object model pattern (see [5. Page Object Model with BaseCase](https://seleniumbase.io/help_docs/syntax_formats/#sb_sf_05) and [Page Object Model with the "sb" fixture](https://seleniumbase.io/help_docs/syntax_formats/#sb_sf_06))
- Test suite file at project root folder