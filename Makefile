SHELL := /bin/sh

PAPER_DIR := paper
BUILD_DIR := build
LATEXMK := latexmk -pdf -interaction=nonstopmode -halt-on-error

.PHONY: all paper clean

all: paper

paper:
	cd $(PAPER_DIR) && $(LATEXMK) main.tex
	mkdir -p $(BUILD_DIR)
	cp $(PAPER_DIR)/main.pdf $(BUILD_DIR)/GenCoord_preprint.pdf

clean:
	cd $(PAPER_DIR) && rm -f *.aux *.blg *.fdb_latexmk *.fls *.log *.out *.pdf *.synctex.gz
	rm -rf $(BUILD_DIR)
