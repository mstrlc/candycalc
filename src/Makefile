ARCHIVE = xstrel03_xkurci00_xseidl06_xnovym00

all:
	@echo "No need to compile."

pack:
	mkdir -p ../../$(ARCHIVE)/doc
	mkdir -p ../../$(ARCHIVE)/install
	mkdir -p ../../$(ARCHIVE)/repo
	cp -a ../doc/* ../../$(ARCHIVE)/doc
	cp -a ../installer/* ../../$(ARCHIVE)/install
	cp -a ../* ../../$(ARCHIVE)/repo
	rm -rf ../../$(ARCHIVE)/repo/doc
	rm -rf ../../$(ARCHIVE)/repo/installer
	cd ../.. && zip -r $(ARCHIVE).zip $(ARCHIVE)

clean:
	rm -rf ../profiling/__pycache__
	rm -rf ../src/__pycache__
	rm -rf ../src/.pytest_cache
	rm -rf ../src/dest
	rm -rf ../src/build

test: mathlib_test.py
	pytest mathlib_test.py

doc:
	doxygen Doxyfile

run: main.py
	python3 main.py

profile: profiler.py
	python3 profiler.py 

build:
	python3 -m pyinstaller pyinstaller.spec
