from os.path import join, isdir, dirname
from os import listdir
from setuptools import setup

# import the package, auto-discover it
root = join(dirname(__file__), 'kivy', 'garden')
dirs = [f for f in listdir(root) if isdir(join(root, f))]
assert len(dirs) == 1
name = dirs[0]

_import_args = 'kivy.garden.{}'.format(name), join(root, name, '__init__.py')
try:
    from imp import load_source
except ImportError:
    from importlib.machinery import SourceFileLoader
    garden_package = SourceFileLoader(*_import_args).load_module()
else:
    garden_package = load_source(*_import_args)

setup(
    name='kivy.garden.{}'.format(name),
    version=garden_package.__version__,
    author='',
    author_email='',
    description='',
    url='http://kivy.org/docs/api-kivy.garden.html',
    license='MIT',
    namespace_packages=['kivy', 'kivy.garden'],
    packages=['kivy', 'kivy.garden', 'kivy.garden.{}'.format(name)]
)