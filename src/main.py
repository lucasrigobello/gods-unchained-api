import uvicorn
from fastapi import FastAPI

## =====================================================================
## Inicio do serviço Fast API
## =====================================================================

# Iniciando FastAPI
app = FastAPI()

#===========================================
# Rota Hello World
@app.get("/")
async def root():
    return {"message": "Hello World"}

#===========================================
# Iniciando web server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)