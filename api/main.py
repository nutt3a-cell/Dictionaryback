# FastAPI is a Python library that 
# allows us to 
# - take in a request (from the client)
# - send back a response
from fastapi import FastAPI

# CORS (Cross-Origin Resource Sharing)
# allows us to restrict/enable 
# which client urls are allowed 
# to send requests to this backend code. 
from fastapi.middleware.cors import CORSMiddleware

# Initialize the FastAPI application
app = FastAPI(
    title="FastAPI Example",
    description="This is an example of using FastAPI"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # star means all client urls allowed 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")           #endpoint, or route, always starts with a forward slash
def default_route():    #route handler function
    """
    This is the default endpoint for this back-end.
    """
    return "You have reached the default route. Back-end server is listening..."
    
@app.get("/example")  
def get_example():    
    """
    This endpoint returns a JSON object consisting of a simple message.
    """
    return {"message": "Hello World!"}

@app.get("/example2")  
def get_example2(name):    # can also pass in parameters
    """
    This endpoint takes in a parameter called "name"
    """
    return {"message": f"Hello {name}!"}
