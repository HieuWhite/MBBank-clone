# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= python -m sphinx
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile clean

# The "clean" target is updated to remove the autoapi generated files as well.
# Run "make clean" to ensure a completely fresh build.
clean:
	rm -rf $(BUILDDIR) autoapi

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option. $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


[tox]
envlist = py38,py39,py310,py311,py312
isolated_build = False

[testenv:py{38,39,310,311,312}]
skip_install = false
deps =
    wheel
    build
setenv =
    WITH_COMMITID = TRUE
    PYTHON_EXECUTABLE = {envpython}
    Python3_EXECUTABLE = {envpython}
commands =
    python -m build --wheel -o {toxinidir}/dist

[testenv:py{38,39,310,311,312}-pypi]
skip_install = false
setenv =
    PYPI_BUILD = TRUE
    WITH_COMMITID = FALSE
    PYTHON_EXECUTABLE = {envpython}
    Python3_EXECUTABLE = {envpython}
commands =
    python setup.py bdist_wheel --plat-name=manylinux2014_x86_64

[testenv:audit_manylinux2014]
skip_install = true
allowlist_externals =
    bash
deps =
    auditwheel
    patchelf
commands =
    bash -c 'auditwheel repair -L=/lib --exclude=/usr/local/cuda* --exclude=libcuda.so.1 --plat=manylinux2014_x86_64 dist/*'

lam ti dienluc khong?:
  [
    evnhcmc,
    evnspc,
    evncpc,
    evnhanoi,
    ...,
  ]

 from: fakedamin@hcmpc.com.vn
[testenv:py38]
basepython = python3.8

[testenv:py39]
basepython = python3.9

[testenv:py310]
basepython = python3.10

[testenv:py311]
basepython = python3.11

[testenv:py312]
basepython = python3.12
