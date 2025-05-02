import uvicorn
from fastapi import FastAPI, UploadFile
from fastapi.responses import HTMLResponse

import pandas as pd
from io import BytesIO
import joblib
import yaml

from utils.functions import preparar_dado_predict, preparar_dado_trainamento, validation, treinar_modelo, get_dataset

## =====================================================================
## Inicio do serviço Fast API
## =====================================================================

# Read Features Confing YAML file
with open("./src/config/swagger_documentation.yaml", 'r', encoding='utf-8') as stream:
    conf_swagger = yaml.safe_load(stream)

# Iniciando FastAPI
app = FastAPI(**conf_swagger)

#===========================================
# Rota da Prediçao da Classificação do Card
@app.get("/classificar/{id}", tags=["Classificar"])
async def classificar(id):

    try:
        # carregar o dado para o predict    
        X = preparar_dado_predict(id)
        
        # carregar o modelo e fazer predição
        modelo = joblib.load("./src/models/pipeline_model.pkl") 
        pred = modelo.predict(X)

    except:
        # se id não estiver na base de dados, retornar vazio
        return {'strategy': ''}
    
    return {'strategy': pred[0]}

#===========================================
# Rota para upload de dataset de treinmaento
@app.post("/atualizar_base_treinamento", tags=["Base de Dados"])
async def upload_train_data(file: UploadFile):
 
    contents = file.file.read()
    buffer = BytesIO(contents)

    if ';' in str(contents[:35]):
        df_train = pd.read_csv(buffer, sep = ';')
    elif ',' in str(contents[:35]):
        df_train = pd.read_csv(buffer)
    
    df_train.to_csv('./data/challenge_train.csv', sep = ';', index=False)
    
    return {"filename": file.filename}

#===========================================
# Rota para upload de dataset de Test
@app.post("/atualizar_base_test", tags=["Base de Dados"])
async def upload_test_data(file: UploadFile):
    
    contents = file.file.read()
    buffer = BytesIO(contents)
    
    if ';' in str(contents[:35]):
        df_test = pd.read_csv(buffer, sep = ';')
    elif ',' in str(contents[:35]):
        df_test = pd.read_csv(buffer)
    
    df_test.to_csv('./data/challenge_test.csv', sep = ';', index=False)
    
    return {"filename": file.filename}

#===========================================
# Rota para realizar Evaluation do Modelo
@app.get("/evaluation", tags=["Avaliar Modelo"], response_class=HTMLResponse)
async def evaluation():

    # carregar o dado para o treinamento
    X, y = get_dataset()

    # carregar o modelo e fazer predição
    modelo = joblib.load("./src/models/pipeline_model.pkl") 

    return """
        <html>
            <h1>Avalição do Modelo Atual Executada com Sucesso</h1>
            <h3>Avaliação do Score</h3>
            {}
        </html>""".format(validation(y, modelo.predict(X)))

#===========================================
# Rota para realizar o Treinamneto do Modelo
@app.get("/treinar", tags=["Treinar Novo Modelo"], response_class=HTMLResponse)
async def treinar():

    # carregar o dado para o treinamento
    X_train, X_test, y_train, y_test = preparar_dado_trainamento()

    # treinamento do modelo
    clf = treinar_modelo(X_train, y_train)

    return """
        <html>
            <h1>Treinamento Executado com Sucesso</h1>
            <h3>Score treinamento</h3>
            {}
            <h3>Score validação</h3>
            {}
        </html>""".format(validation(y_train, clf.predict(X_train)),
                          validation(y_test, clf.predict(X_test)))

#===========================================
# Iniciando web server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)