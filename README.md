# DeadOrNot

DeadOrNot is a Python program that parses a file for URLs and returns information about the HTTP status of those links to the command line 

![DeadOrNot](https://i.imgur.com/zw850Cd.png)

## Getting Started

### Prerequisites
The following are needed to run DeadOrNot
* [Python/Python 3] (https://www.python.org/)
* [Git] (https://git-scm.com/)

### Installation
To install DeadOrNot to locally follow the steps below
1. Clone the repo from github
```bash
git clone https://github.com/AbdulMAbdi/deadOrNot.git
```
2. Use [pip](https://pip.pypa.io/en/stable/) to install the requirements.
```bash
pip install -r requirements.txt
```

## Usage

Use the -h option to see information and other options
```bash
python deadOrNot.py -h
```
![DeadOrNot](https://i.imgur.com/pbr75wt.png)
Check and output URL status  
```bash
python deadOrNot.py *fileName*
```
![DeadOrNot](https://i.imgur.com/zw850Cd.png)
Use the -g/-good option to check and output live URL statuses
```bash
python deadOrNot.py  *fileName* -g
```
![DeadOrNot](https://i.imgur.com/Cr4lMpn.png)
Use the -d/-dead option to check and output dead or unknown URL statuses
```bash
python deadOrNot.py  *fileName* -d
```
![DeadOrNot](https://i.imgur.com/WcqMzVM.png)
Use the -i option to check URL statuses and output overall status information for all links in file
```bash
python deadOrNot.py *fileName* -i
```
![DeadOrNot](https://i.imgur.com/u3Ve1RD.png)
## Contributing
Any help, ideas or issues with the program are welcome and encouraged. 

## License
Distributed under the [MIT](https://choosealicense.com/licenses/mit/) License. See LICENSE for more information.
