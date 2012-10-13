all: py.js programs

py.js:
	mkdir -p js
	cat library/py-core.js > js/py.js
	python js.py library/py-runtime.py >> js/py.js
	python js.py library/py-builtins.py >> js/py.js
	cp library/tests.js js/tests.js

programs:
	python js.py py/classes.py > js/classes.js
	python js.py py/decorators.py > js/decorators.js
	python js.py py/factorial.py > js/factorial.js
	python js.py py/in_1.py > js/in_1.js
	python js.py py/in_2.py > js/in_2.js

clean:
	rm js/*.js
