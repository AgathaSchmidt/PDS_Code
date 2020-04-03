## Python software packages
This directory shows an example of a python package (called pds). 
Once you are (with your terminal/conda prompt/...) in the same directory as `setup.py`, 
you can install it to your machine via `pip install -e .`. 
This way, it's installed in _editable_ mode and your
changes in the python files will directly be available without reinstallation.
Kernel restart might be necessary.
When changes in `setup.py` are made, reinstallation is needed.

You can also use notebooks along with the package, I provided a sample notebook in `notebooks/`.
There, you have to run `!pip install -e ..`, as it is a sub-directody.

The command line interface is created with click (https://click.palletsprojects.com/en/7.x/). 
There are other packages available for this and we don't force you to work with
a specific one. Also, you don't have to use Pycharm (as I did). If you don't
have a preference, feel free to do exactly the same as in the video for your
python packages!
