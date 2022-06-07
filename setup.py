import os
import re
import codecs

from setuptools import find_packages, setup


def abs_path(*relative_path_parts):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)),
                        *relative_path_parts)


name = 'huelog'

with codecs.open(abs_path(name, '__init__.py'), 'r', 'utf-8') as fp:
    try:
        version = re.findall(r"^__version__ = '([^']+)'.*?$",
                             fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')

setup(
    name=name,
    version=version,
    url='https://github.com/Corruptware/Huelog',
    download_url='https://github.com/Corruptware/Huelog',
    author='Corruptware',
    author_email='corruptware@gmail.com',
    description='Print rainbow in terminals and logs.',
    keywords='hue, color, terminal color, colorama, log color',
    packages=find_packages(),
    py_modules=['huelog'],
    data_files=[('', ['LICENSE'])],
    include_package_data=True,
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ])