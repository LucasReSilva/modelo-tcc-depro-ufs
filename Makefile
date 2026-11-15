MAIN = tcc-depro-ufs

.PHONY: all manual clean distclean

all:
	latexmk -pdf $(MAIN).tex

manual:
	pdflatex -interaction=nonstopmode $(MAIN).tex
	bibtex $(MAIN)
	pdflatex -interaction=nonstopmode $(MAIN).tex
	pdflatex -interaction=nonstopmode $(MAIN).tex

clean:
	latexmk -c $(MAIN).tex
	rm -f *.loq *.lol *.bbl *.blg *.run.xml

distclean:
	latexmk -C $(MAIN).tex
	rm -f *.loq *.lol *.bbl *.blg *.run.xml $(MAIN).pdf
