from setuptools import setup

setup(name='Markdown to Anki',
    version='1.0',
    description='Converts markdown file to anki deck',
    author='Ryan Vanden Bos',
    install_requires=['genanki'],
    packages=['mdtoanki'],
    entry_points={
        'console_scripts': ['md-to-anki=mdtoanki.command_line:main']
    }
)
