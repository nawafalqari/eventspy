from setuptools import setup, find_packages

# README.md
with open('README.md', 'r', encoding='utf-8') as readme_file:
    readme = readme_file.read()

setup(
    name='eventspy',
    packages=find_packages(),
    version="1.0.0",
    description='Events in Python',
    author='Nawaf Alqari',
    author_email='nawafalqari13@gmail.com',
    keywords=['events', 'event', 'pyevent', 'eventpy', 'eventspy'],
    long_description=readme,
    long_description_content_type='text/markdown',
    project_urls={
        'Documentation': 'https://github.com/nawafalqari/eventspy#readme',
        'Bug Tracker': 'https://github.com/nawafalqari/eventspy/issues',
        'Source Code': 'https://github.com/nawafalqari/eventspy/',
        'Discord': 'https://discord.gg/cpvynqk4XT'
    },
    license='MIT',
    url='https://github.com/nawafalqari/eventspy/',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)