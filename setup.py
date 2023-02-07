from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

    
setup(
    name='WeatherAPI',
    version='0.0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Convert job descriptions to skills needed for that job',
    url='https://github.com/vkyal/DATA534_ProjectAPI',
    author='Ujjwal, Varshita, Nowshabha',
    author_email='upadhyay.ujjwal007@gmail.com',
    python_requires='>=3.9',
)
