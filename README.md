# Shapes - an example repository
[![Build Status](https://travis-ci.org/bannanc/shapes.svg?branch=master)](https://travis-ci.org/bannanc/shapes)
[![codecov](https://codecov.io/gh/bannanc/shapes/branch/master/graph/badge.svg)](https://codecov.io/gh/bannanc/shapes)
[![Documentation Status](https://readthedocs.org/projects/shapes/badge/?version=latest)](http://shapes.readthedocs.io/en/latest/?badge=latest)

This repository will provide methods for calculating the area and parimeter of certain shapes, but the main use
is to provide an example of how to setup and use the following tools:

 - [GitHub](github.com) - Version Control
 - [Travis CI](https://travis-ci.org) - Continous Integration
 - [pytest](https://docs.pytest.org/en/latest/) - Unit and Regression Testing
 - [CodeCov](https://codecov.io) - Testing Coverage Analysis
 - [Read the Docs](https://readthedocs.org) - Documentation

This README will provide instructions for how to start with a skeleton set of files and make your repository look like this one.

### Template files

It is always easier to start from example files than writing them from scratch, especially for `setup.py`, `.travis.yml`, and sphinx documentation files.
MolSSI has graciously provided such examples at [`MolSSI/python_template`](https://github.com/MolSSI/python_template) on GitHub.
I have forked this repository and updated some files to fit my typically preferences at [`bannanc/python_template`](https://github.com/bannanc/python_template).
When I say to start with a template file, these repositories are a good source of examples.

## Starting a new Reposiory

If you want to generate your own version of this repository you can start with the [skeleton of shapes](https://github.com/bannanc/shapes/releases/tag/0.0).
Unzip/Untar the directory and save it where you want your github repository.
Otherwise you can follow these steps to make any new repository.

* Got to your GitHub Home page and click on the **New Repository** button.

* Fill in the information about your repository
    - Repository Name: pick a name
    - Description: Typically 1 sentence that will appear under the repo name
    - Public/Private: If you're creating open source code it is best practice to start with a public repository. Also, Travis, CodeCov, and BuildTheDocs are only free for public repositories.
    - Initialize with a README: Always important to have a README. If you're copying from the skeleton above then you don't need one since that directory has one already.
    - Add `.gitignore`: These are useful files, the provide a list of files that you do not want tracked in your repository, such as `__pycache__` in a python directory. You do not need one of these if you're starting from the skeleton as it is included. You can always add this file later or copy a template version.
    - Add a license: If you do not have a license then technically you are not allowing anyone to use your code, so pick one. The skeleton of this repository has an MIT License.

* Copy Repository or set up remote link
    - If you include a README, .gitignore, or License file then a repository will be created. In that case you should click on the **Clone or Download** button and copy the remote link. Go to where you want to store the repository on your computer and call `git clone [paste link]`
    - If you started with an empty repository, you will be given a link for the repository, copy this link. On your computer move into the repository you want to put on GitHub. Use the following commands:
        - `git init`
        - `git remote add origin [paste url here]`
        - `git push -u origin master`

#### Update Repository

From this point forward, these instructions assume you have a working `setup.py` file that will install any python modules in your repository.

## Add Integrated Tests

Test scripts should be stored in their own repository; for more details about good practices for writing tests see [tests/README.md](tests/README.md).

* Add integration for this repository
    - Go to [travisci.org](travis-ci.org) and make an account if you don't already have one.
    - click on [your name] > profile
    - toggle the switch next to the repository you want tests for

* Make a `.travis.yml` file. (This is the file the travis integration will look for)
    - Copy a template `.travis.yml` file
    - Update as needed to have all dependencies your project needs
    - push these changes to your github branch:
        ```
        git add .travis.yml
        git commit -m "adding .travis file"
        git push origin [master or whatever branch you're on]
        ```

* Add a badge to your README
    - back on [travisci.org](travis-ci.org) click on your project, you should see your tests passing (or failing)
    - click on the "badge" **[build|passing]** chose Markdown and copy the text
    - back on your terminal, add this line to your README.md file under the title (or wherever you want it). Then push these changes to your remote repository.

## Add Code Coverage Tests

Make sure in your `script` section of `travis.yml` make sure you include the `--cov` option.

* Make a codecov account at [codecov.org](codecov.org)

* Add your repository:
    - go to your profile (click on your name)
    - Click on the **Add new repository** button
    - select your repository name

* Add the badge to your README
    - On the codecov website for this repository select settings > badge
    - copy the markdown option
    - paste the line into your README file and add the changes

## Add Documentation

For full disclosure, this is just an overview, making documentation look exactly as you like is a bit complicated, but this will help you get started.

To add documentation integration to your directory make an account on [readthedocs.org](readthedocs.org).

For more help, checkout Read the Docs website for
* [getting started](https://docs.readthedocs.io/en/latest/) and
* [Documentation](https://docs.readthedocs.io/en/latest/)

### Make Sphinx files in your terminal

* Install sphinx: `pip install sphinx sphinx-autobuild sphinx_rtd_theme`
* Make a documentation directory (`docs`) to store these files.
* Call `sphinx-quickstart`, then answer all the questions and there are a ton of questions. Here are the choices I did not use the default on:
```
> Separate source and build directories (y/n) [n]: y
> Project name: Shapes
> Author name(s): Caitlin C. Bannan
> Project version []: 0.0.1
> autodoc: automatically insert docstrings from modules (y/n) [n]: y
> mathjax: include math, rendered in the browser by MathJax (y/n) [n]: y
> viewcode: include links to the source code of documented Python objects (y/n) [n]: y
> Create Windows command file? (y/n) [y]: n
```
For all other options I use the default.

This autogenerates a `source/` and `build/` directory we will then edit files in the source directory. You only want to link the `source` directory to your remote respository.

### Edit source files

In the source directory, make the following changes

##### `index.rst`

This is a `reStructuredTest File`. Here is a [cheat sheet](https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html) for how to format these files.

In this file add a description of your package under the auto create title **Welcome to ...**

You can auto add documentation from your functions by including a line like:

`.. autofunction:: shapes.square.area.area_square`

##### `conf.py`

These are my preferred setting, to make your documentation look like [this](http://shapes.readthedocs.io/en/latest/?badge=latest).

* uncomment `import os`

* add `'sphinx.ext.napoleon'` to the extensions list (approximately line 34)

* Update the section under `# -- Options for HTML output ----------`
    - remove the line `html_theme = 'alabaster'`
    - add the lines below:
```
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

    html_context = {
        'css_files': [
            '_static/theme_overrides.css'
        ]
    }
else:
    html_context = {
        'css_files': [
            '//media.readthedocs.org/css/sphinx_rtd_theme.css',
            '//media.readthedocs.org/css/readthedocs-doc-embed.css',
            '_static/theme_overrides.css'
        ]
    }
```

* Make sure the variable `html_slidebars` has the following:
```
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
        # 'donate.html', see if I actually need this one
    ]
}
```

##### Build your files

From the `docs/` directory call `make html` you can see what your documentation will look like by opening `docs/build/html/index.html`

### Add your documentation

* Add your files in `docs/source` to GitHub
* Build your documentation
    - go back to [ReadTheDocs.org](readthedocs.org)
    - click on **Import a Project**
    - click on the **+** next to this repository name
    - fill in the information
        - Note: the name must be unique so you might have to add something more than just your repository name, this is just for the build the docs storage so it isn't too important
    - click **build**
* Add badge: click on the badge `[docs|passing]` and copy the Markdown line to your README file.

