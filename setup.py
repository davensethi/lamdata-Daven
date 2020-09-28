'lambdata a collection of Data Science Functions'

import setuptools

REQUIRED = [
    'numpy',
    'pandas'
]

with  open ('READ.md', 'r') as fh:
    LONG_DESCRIPTION  = fh.read()

setuptools.setup (
    name ='lambdata_daven',
    version = '0.01',
    author ='davensethi',
    description = 'example of the what we are doing in class'
    Long_description = LONG_DESCRIPTION
    Long_description_content = 'text/markdown'
    url= ''
    packages= setuptools.find_packages(),
    install_requires =REQUIRED
    classifiers =[
        'Programming Language :: Python :: 3'
        'License :: OSI Approved :: MIT License'
        'Operating System:: OS Independent'
    ]
)