cd ./src

piccolo migrations new jokes --auto

piccolo migrations forwards all

uvicorn main:app --host 0.0.0.0 --port 80