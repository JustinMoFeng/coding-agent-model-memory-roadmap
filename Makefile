PIP ?= .venv/bin/pip
PYTHON ?= .venv/bin/python
MKDOCS ?= .venv/bin/mkdocs
PIP_INDEX_URL ?= https://pypi.tuna.tsinghua.edu.cn/simple
PIP_TRUSTED_HOST ?= pypi.tuna.tsinghua.edu.cn

.PHONY: venv install serve build clean

venv:
	python3 -m venv .venv

install: venv
	$(PIP) install -i $(PIP_INDEX_URL) --trusted-host $(PIP_TRUSTED_HOST) --upgrade pip
	$(PIP) install -i $(PIP_INDEX_URL) --trusted-host $(PIP_TRUSTED_HOST) -r requirements.txt

serve:
	$(MKDOCS) serve

build:
	$(MKDOCS) build --strict

clean:
	rm -rf site

