install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build -o /home/charaeva/python-project-49/dist

package-install:
	uv tool install dist/*.whl