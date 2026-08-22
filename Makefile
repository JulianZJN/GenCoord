SHELL := /bin/sh

PAPER_DIR := paper
LATEX := pdflatex -interaction=nonstopmode -halt-on-error
BIBTEX := bibtex

.PHONY: all main supplement combined evidence verify-evidence

all: main supplement

main:
	cd $(PAPER_DIR) && $(LATEX) main.tex
	cd $(PAPER_DIR) && $(BIBTEX) main
	cd $(PAPER_DIR) && $(LATEX) main.tex
	cd $(PAPER_DIR) && $(LATEX) main.tex

supplement:
	cd $(PAPER_DIR) && $(LATEX) supplement.tex
	cd $(PAPER_DIR) && $(BIBTEX) supplement
	cd $(PAPER_DIR) && $(LATEX) supplement.tex
	cd $(PAPER_DIR) && $(LATEX) supplement.tex

combined: all
	mkdir -p build
	pdfunite $(PAPER_DIR)/main.pdf $(PAPER_DIR)/supplement.pdf build/GenCoord_preprint.pdf

evidence:
	python3 $(PAPER_DIR)/anc/scripts/build_e1e2_tables.py \
		--analysis $(PAPER_DIR)/anc/source_data/e1e2_analysis.json \
		--training $(PAPER_DIR)/anc/source_data/e1e2_training_budget.json \
		--tables-dir $(PAPER_DIR)/tables \
		--data-dir $(PAPER_DIR)/anc/source_data

verify-evidence: evidence
	git diff --exit-code -- $(PAPER_DIR)/tables $(PAPER_DIR)/anc/source_data
