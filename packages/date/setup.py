from setuptools import setup

setup(
    name='lektor-date',
    version='0.1',
    author=u'Martin Häcker',
    author_email='spamfaenger@gmx.de',
    license='MIT',
    py_modules=['lektor_date'],
    url='https://github.com/dwt/lektor-date',
    entry_points={
        'lektor.plugins': [
            'date = lektor_date:DatePlugin',
        ]
    }
)
