install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build -o /home/charaeva/python-project-49/dist

package-install:
	uv tool install /home/charaeva/python-project-49/dist/*.whl

make lint:
	uv run ruff check brain_games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

brain-gcd:
	uv run brain-gcd