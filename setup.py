from distutils.core import setup

setup(
    name='CodingKata',
    version='0.1dev',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    tests_require=['pylint', 'coverage'],
    scripts=['basic_arithmetic.py',
             'test_basic_arithmetic.py'],
)