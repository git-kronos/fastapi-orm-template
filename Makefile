ifeq ($(OS), Windows_NT)
remove_git:
	if exist rmdir /S /Q .git
else
remove_git:
	rm -rf .\.git
endif

init: remove_git
	pipenv install

init_req: requirements.txt remove_git
	@pip install requirements.txt

migrate:
	@alembic revision --autogenerate
	@alembic upgrade head

run:
	@uvicorn main:app --reload