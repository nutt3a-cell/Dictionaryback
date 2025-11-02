from PyDictionary import PyDictionary
  dictionary = PyDictionary()

from fastapi import FastAPI 

from fastapi.middleware.cors import CORSMiddleware

# Initialize the FastAPI application
app = FastAPI(
    title="The ULTIMATE Dictionary",
    description="A Dictionary with many features!!!"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # star means all client urls allowed 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def default_route():
    """This is the default endpoint for this back-end."""
    return "You have reached the default route. Back-end server is listening..."
    
@app.get("/example")  
def get_example():    
    """
    This endpoint returns a JSON object consisting of a simple message.
    """
    return {"message": "Hello World!"}


@app.get("/example2")
def get_example2(name: str):
    """Takes in a 'name' parameter and returns a message."""
    return {"message": f"Hello {name}!"}

@app.get("/define")  
def define_word(word: str = Query(..., description="The word to define")):
    """
    Takes a word as a query parameter and returns its meanings.
    Example: /define?word=apple
    """
    meaning = dictionary.meaning(word)

    if not meaning:
        return {"error": f"Definition for '{word}' not found."}

    # Convert meaning dict to a cleaner format
    return {"word": word, "meanings": meaning}

