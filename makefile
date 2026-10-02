build:
	uv run python -m generate_font
	uv run python -m scripts.banner
	uv run python -m scripts.specimen_pdf
	uv run python -m scripts.samples

build-otf:
	uv run python -m generate_font --otf

install-mac:
	cp -r fonts/otf/EigerSans-*.otf ~/Library/Fonts

visualize:
	uv run python -m visualize lowercase_a --focus
