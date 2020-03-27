# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
LANG            = en
SPHINXOPTS      =
SPHINXINTLOPTS  = $(SPHINXOPTS) -D language=$(LANG)
SPHINXBUILD     ?= sphinx-build
SPHINXINTL      ?= sphinx-intl
SOURCEDIR       = .
BUILDDIR        = build



# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

springclean:
	rm -r $(BUILDDIR)
	# all .mo files
	find $(SOURCEDIR)/locale/*/LC_MESSAGES/ -type f -name '*.mo' -delete

gettext:
	@$(SPHINXBUILD) -M gettext "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

html:
	echo "$(SPHINXOPTS) $(SPHINXINTLOPTS)"
	if [ $(LANG) != "en" ]; then \
		$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)/html/$(LANG)" $(SPHINXINTLOPTS) $(0); \
	else \
		$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)/html/$(LANG)" $(SPHINXOPTS) $(0); \
	fi
