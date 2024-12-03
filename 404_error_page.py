from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.exceptions import HTTPException

app = FastAPI()

@app.get("/")
def read_main():
    """
    Uses FastAPI to provide a welcome message when customers access the main HTML page.
    """
    return {"message": "Welcome to AD's Michael Kors PopUp!"}

@app.exception_handler(404)
async def custom_404(request: Request, e: HTTPException):
    """
    Uses FastAPI to create a custom page for 404 errors.
    """
    return HTMLResponse(content="<html><body><h1>Page Not Found</h1></body></html>", status_code=404)
