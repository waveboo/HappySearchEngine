# -*- coding:utf-8 -*-

import os
import yaml

_project_filename = os.path.join(os.path.dirname(__file__), 'config.yml')

with open(_project_filename) as ymlfile:
    project_config = yaml.load(ymlfile)

