#!/usr/bin/env python3
# Standard Library Imports
import sys
from distutils.spawn import find_executable

# Third Party Imports

# Local Application Imports
from classes.preset import Preset

PACKER_BIN_PATH = find_executable("packer")  # searchs PATH by default
if PACKER_BIN_PATH is None:
    print("Error: Packer could not be found in the PATH")
    sys.exit(1)

presets = list()

# Example preset
##
# hostname = "foo"
# httpdir = "http"
# domain = "bar"
# template_file_name = "foobar.json"

# presets.append(
#     Preset
#     (
#         desc="to build the best foo",
#         template_name=template_file_name,
#         subprocess_args=[
#             PACKER_BIN_PATH,
#             "build",
#             "-var",
#             f"http_directory={httpdir}",
#             "-var",
#             f"hostname={hostname}",
#             "-var",
#             f"domain={domain}",
#             template_file_name,
#         ]
#     )
# )

##

##
template_file_name = "build.json"
hostname = "{{ cookiecutter.build_name }}-default"
presets.append(
    Preset(
        desc="default run of the build file",
        template_name=template_file_name,
        subprocess_args=[
            PACKER_BIN_PATH,
            "build",
            "-var",
            f"hostname={hostname}",
            template_file_name,
        ],
    )
)

##
