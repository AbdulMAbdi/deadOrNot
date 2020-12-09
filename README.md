# DeadOrNot

DeadOrNot is a Python program that parses a file for URLs and returns information about the HTTP status of those links to the command line

![DeadOrNot](https://i.imgur.com/zw850Cd.png)

### Installation

To install DeadOrNot locally follow the steps below

1. Install Python 3.6+

2. Use [pip](https://pip.pypa.io/en/stable/) to install the deadOrNot.

```bash
pip install deadOrNot
```

## Usage

Use the -h option to see information and other options

```bash
deadOrNot -h
```

![DeadOrNot](https://i.imgur.com/pbr75wt.png)
Check and output URL status

```bash
deadOrNot *fileName*
```

![DeadOrNot](https://i.imgur.com/zw850Cd.png)
Use the -g/-good option to check and output live URL statuses

```bash
deadOrNot  *fileName* -g
```

![DeadOrNot](https://i.imgur.com/Cr4lMpn.png)
Use the -d/-dead option to check and output dead or unknown URL statuses

```bash
deadOrNot *fileName* -d
```

![DeadOrNot](https://i.imgur.com/WcqMzVM.png)
Use the -in option to check URL statuses and output overall status information for all links in file

```bash
deadOrNot *fileName* -in
```

![DeadOrNot](https://i.imgur.com/u3Ve1RD.png)
Use the -i option to compare links with links provided in a separate text file
If the links partially match, the corresponding link will be excluded from being checked

```bash
deadOrNot *fileName* -i *ignoreFileName*
```

## License

Distributed under the [MIT](https://choosealicense.com/licenses/mit/) License. See LICENSE for more information.
