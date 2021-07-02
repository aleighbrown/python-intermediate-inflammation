# Inflam

Inflam is a data management system written in Python that manages trial data used in clinical inflammation studies.

## Main features

Here are some key features of Inflam:

- Provide basic statistical analyses over clinical trial data
- Ability to work on trial data in Comma-Separated Value (CSV) format
- Generate plots of trial data
- Analytical functions and views can be easily extended based on its Model-View-Controller architecture

## Prerequisites

Inflam requires the following Python packages:

- [NumPy](https://www.numpy.org/) - makes use of NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) - uses Matplotlib to generate statistical plots

The following optional packages are required to run Inflam's unit tests:

- [pytest](https://docs.pytest.org/en/stable/) - Inflam's unit tests are written using pytest
- [pytest-cov](https://pypi.org/project/pytest-cov/) - Adds test coverage stats to unit testing


# Installation/deployment
clone the repo, cd into it, and the interaction through CLI

```
git clone https://github.com/aleighbrown/python-intermediate-inflammation.git

cd python-intermediate-inflammation

python patientdb.py --help 
```

Will display usage as below:

```
usage: patientdb.py [-h] [--view {visualize,record}] [--patient PATIENT] infiles [infiles ...]

A basic patient data management system

positional arguments:
  infiles               Input CSV(s) containing inflammation series for each patient

optional arguments:
  -h, --help            show this help message and exit
  --view {visualize,record}
                        Which view should be used?
  --patient PATIENT     Which patient should be displayed?
```

# Contributing
Make a pull request, and we're happy to take any sensible contributions. 
We have yet to integrate patient name linking and the plotting capability is limited as of now. 

# Contact information/getting help

The team is best reached via smoke signals sent on the autumn equinox every year. Otherwise you can reach out via twitter. 

# Credits/Acknowledgements
I would like to thank Taylor Swift as the guiding light in my research and her constant inspiration. 
# Licence
We're using [GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/) - the details of which you can see in the [LICENSE.TXT](LICENSE.txt)
# Inflam
![build](https://github.com/aleighbrown/python-intermediate-inflammation/workflows/CI/badge.svg?branch=main)

