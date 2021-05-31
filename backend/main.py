import uvicorn

inside = os.environ.get('IN_DOCKER', False)

print("Launching Dungeons And Dungeons API")
h = "127.0.0.1"
if inside:
    print('I am running in a Docker container')
	h = "0.0.0.0"
if __name__ == '__main__':
    uvicorn.run("app:app", host=h, port=8000)