from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import os

app = FastAPI()

# Configure OpenAI API key (ensure you set this securely)
# OPENAI_API_KEY = "your_openai_api_key"
# openai.api_key = OPENAI_API_KEY

#class TaskRequest(BaseModel):
 #   task: str

# @app.post("/run")
#async def run_task(task: str = Query(..., description="Task description in plain English")):
 #   try:
        # Query OpenAI LLM to interpret and execute the task
  #      response = openai.ChatCompletion.create(
   #         model="gpt-4",  # Ensure you're using an appropriate model
    #        messages=[
     #           {"role": "system", "content": "You are a helpful assistant capable of executing tasks."},
      #          {"role": "user", "content": task}
       #     ]
        #)
     
   #     result = response["choices"][0]["message"]["content"].strip()
    #    return {"status": "success", "result": result}
    
    #except openai.error.OpenAIError as e:
     #   raise HTTPException(status_code=500, detail=f"LLM processing error: {str(e)}")
    #except Exception as e:
     #   raise HTTPException(status_code=400, detail=f"Invalid task: {str(e)}")

@app.get("/read")
async def read_file(path: str = Query(..., description="Path to the file")):
    return ("We are in get function now")
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found")
    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
        return {"status": "success", "content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading file: {str(e)}")
