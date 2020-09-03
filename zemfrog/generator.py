import os
import string

from .helper import copy_template

def g_project(name):
    copy_template("project", name)

def g_api(name):
    print("Creating rest api %r... " % name, end="")
    copy_template("api", "api")
    old_filename = os.path.join("api", "name.py")
    with open(old_filename) as fp:
        old_data = fp.read()
        py_t = string.Template(old_data)
        new_data = py_t.safe_substitute(name=name)

    os.remove(old_filename)
    new_filename = os.path.join("api", name.lower() + ".py")
    with open(new_filename, "w") as fp:
        fp.write(new_data)

    print("(done)")

def g_blueprint(name):
    print("Creating blueprint %r... " % name, end="")
    copy_template("blueprint", name.lower())
    filename = os.path.join(name.lower(), "routes.py")
    with open(filename) as fp:
        old_data = fp.read()
        py_t = string.Template(old_data)
        new_data = py_t.safe_substitute(name=name)

    with open(filename.lower(), "w") as fp:
        fp.write(new_data)

    print("(done)")

def g_schema(name):
    print("Creating model schema %r... " % name, end="")
    copy_template("schema", "schema")
    old_filename = os.path.join("schema", "name.py")
    with open(old_filename) as fp:
        old_data = fp.read()
        py_t = string.Template(old_data)
        new_data = py_t.safe_substitute(name=name)

    os.remove(old_filename)
    new_filename = os.path.join("api", name.lower() + ".py")
    with open(new_filename, "w") as fp:
        fp.write(new_data)

    print("(done)")