.PHONY: dependencies dist pypi test rst edxml

all: dependencies dist pypi test

dependencies:
	@echo "Installing dependencies:"
	python3 -m pip install --upgrade pip setuptools wheel
	pip3 install flake8 pytest
	pip3 install 'edxml>=3.0.0.dev0'

dist:
	cd generic/python ; $(MAKE) dist .
	cd computing/python ; $(MAKE) dist .
	cd finance/python ; $(MAKE) dist .
	cd forensics/python ; $(MAKE) dist .
	cd geography/python ; $(MAKE) dist .
	cd networking/python ; $(MAKE) dist .
	cd security/python ; $(MAKE) dist .

pypi:
	cd generic/python ; $(MAKE) pypi .
	cd computing/python ; $(MAKE) pypi .
	cd finance/python ; $(MAKE) pypi .
	cd forensics/python ; $(MAKE) pypi .
	cd geography/python ; $(MAKE) pypi .
	cd networking/python ; $(MAKE) pypi .
	cd security/python ; $(MAKE) pypi .

test:
	cd generic/python ; $(MAKE) test .
	cd computing/python ; $(MAKE) test .
	cd finance/python ; $(MAKE) test .
	cd forensics/python ; $(MAKE) test .
	cd geography/python ; $(MAKE) test .
	cd networking/python ; $(MAKE) test .
	cd security/python ; $(MAKE) test .
	# Below fails when regenerating the rst documents that describe
	# the bricks results in changes in the Git repo. That happens when
	# the rst documents are not up to date.
	$(MAKE) rst && git diff --exit-code '*.rst'
	# Below fails when regenerating the EDXML serializations of the bricks
	# results in changes in the Git repo. That happens when
	# the EDXML serializations are not up to date.
	$(MAKE) edxml && git diff --exit-code '*.edxml'

rst:
	python3 dump_rst.py

edxml:
	python3 dump_edxml.py
