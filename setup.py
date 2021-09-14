import os
import sys
from setuptools import setup, find_packages

setup(
    name = "TYStravaDiscordBot",
    version = "0.0.1",
    author = "Joseph Hung",
    author_email = "joseph.hung@mail.utoronto.ca",
    description = ("Something something"),
    packages=find_packages(include=[
    	'generated', 'strava'
    	])
)

print(sys.path)
