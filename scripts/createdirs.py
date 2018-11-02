#!/usr/bin/env python3

# To create the project directory structure from a given Pipfile.lock file
# Usage: ./scripts/createdirs.py ~/projects/myproject/Pipfile.lock

import os
import sys
import json
import shutil

if len(sys.argv) != 2:
    print("Missing path to the Pipfile.lock")
    sys.exit(1)


with open(sys.argv[1]) as fobj:
    data = json.load(fobj)

    defaults = data["default"]
    for name in defaults:
        pathname = os.path.join("./simple/", name)
        os.makedirs(pathname, exist_ok=True)
        print("Project {0}".format(name))
        # Now make sure that we have an index.html there.
        project_index = os.path.join(pathname, "index.html")
        if not os.path.exists(project_index):
            shutil.copyfile("./templates/project-index.html", project_index)
