all:

install:
	install -m755 hello.py $(HOME)/.gimp-2.8/plug-ins

.PHONY: all install
