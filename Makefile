
default: help
.PHONY: default

help:
	@echo 'Usage:'
.PHONY: help

run:
	./app/usr/bin/chewup-editor
.PHONY: run

pyc-clean:
	find ./app | grep -E '(__pycache__|\.pyc|\.pyo)' | xargs rm -rf
.PHONY: pyc-clean

deb-build: pyc-clean
	debuild
.PHONY: deb-build

deb-clean:
	debclean
.PHONY: deb-clean

deb-install:
	sudo dpkg -i ../chewup_0.1.0_all.deb
.PHONY: deb-install
