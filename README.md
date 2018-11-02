This is simple PyPI equivalent index. This can be served using s3 or any webserver and static
files. For now, I have filled it up with some information.


### Usage:

We can use any project's `Pipfile.lock` file to create/add new python projects in our index.

```
./scripts/createdirs.py ~/Projects/myproject/Pipfile.lock
```

This will add a new directory under `./simple/` and will also add an `index.html` to that.

Then fill up the `./simple/project/index.html` (the project name should be any new package) with
links to the sources and binary wheel files as required. In my example, I am hosting files
from `/localwheels/` directory (actually s3 bucket).


After you have any new project, you can recreate the main `./simple/index.html` by executing

```
./scripts/updateindex.py
```

Now server the `simple` directory. 

For a local usage:

```
python3 -m http.server
```

You can then use the server using `--index-url http://127.0.0.1:8000/simple` argument to `pip`.


```
pip3 install --index-url http://127.0.0.1:8000/simple requests --no-cache-dir
```