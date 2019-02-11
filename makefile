test: init_env
	@echo "=================================================="
	@echo "Running with sample words not the acctualy Aylien API."
	@echo "For using this on real data please make sure you update the Aylien api credentials in the python file in the line:"
	@echo "client = textapi.Client( CREDENTIALS GOES HERE )"
	@echo "You can make a free account here: https://aylien.com/"
	@echo "=================================================="

	python src/main_with_sample_words.py res/sample.txt

	@echo "=================================================="
	@echo "Checkout out/ directory"

run: init_env
	@echo "=================================================="
	@echo "Running with Aylien API."
	@echo "Please make sure you updated the Aylien api credentials in the python file in the line:"
	@echo "client = textapi.Client( CREDENTIALS GOES HERE )"
	@echo "You can make a free account here: https://aylien.com/"
	@echo "=================================================="

	python src/main.py res/sample.txt

	@echo "=================================================="
	@echo "Checkout out/ directory"

init_env:
	mkdir -p out
