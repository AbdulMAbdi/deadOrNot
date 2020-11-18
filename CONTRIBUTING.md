## Getting Started

### Prerequisites
The following are needed to run DeadOrNot
* [Python/Python 3] (https://www.python.org/)
* [Git] (https://git-scm.com/)

### Installation
To install DeadOrNot locally follow the steps below
1. Clone the repo from github
```bash
git clone https://github.com/AbdulMAbdi/deadOrNot.git
```
2. Use [pip](https://pip.pypa.io/en/stable/) to install the requirements.
```bash
pip install -r requirements.txt
```
## Contributing, Formatting and Linting
Any help, ideas or issues with the program are welcome and encouraged. 

The project is configured so that [black](https://pypi.org/project/black/) code formatter and [flake8](https://flake8.pycqa.org/en/latest/) linter 
are run whenever you save if you are using vscode as your IDE/Editor

If you would like to run [black](https://pypi.org/project/black/) source formatter manually use 
```bash
black deadOrNot.py fileReader.py
```

If you would like to run [flake8](https://flake8.pycqa.org/en/latest/) linter source formatter manually use 
```bash
flake8 . --ignore W605,E501,W503
```

Before making a pull request use Black code formatter and flake8 linter on your code with the methods shown above. 
Thanks you for your contributions :) !