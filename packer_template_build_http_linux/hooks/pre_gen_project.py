#!/usr/bin/env python3
# Standard Library Imports
import sys

# Third Party Imports

# Local Application Imports

ERROR_PREFIX = "Error:"

build_name = "{{ cookiecutter.build_name }}"
description = "{{ cookiecutter.description }}"
builds_directory = "{{ cookiecutter.builds_directory }}"

if build_name == "":
    print(f"{ERROR_PREFIX} 'build_name' is required")
    sys.exit(1)

if description == "":
    print(f"{ERROR_PREFIX} 'description' is required")
    sys.exit(1)

if description == "":
    print(f"{ERROR_PREFIX} 'builds_directory' is required")
    sys.exit(1)

sys.exit(0)
