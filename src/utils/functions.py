from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

import joblib
import pandas as pd
import yaml

from classes.dataset import Train_Data, Test_Data

#===========================================
# Read Features Confif YAML file
with open("./src/config/conf.yaml", 'r') as stream:
    conf_features = yaml.safe_load(stream)

numerical_features = conf_features['numerical_features']
categorical_features = conf_features['categorical_features']
target = conf_features['target']


#===========================================
# Prepara o dado para realizar predict
def preparar_dado_predict(id):
    
    # load base de dados
    X = Test_Data(id).X()
    return X

#===========================================
# Prepara o dado para treinamento - Train e Test Split
def preparar_dado_trainamento():
    
    X, y = get_dataset()
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    return X_train, X_test, y_train, y_test

#===========================================
# Gerar relatorio de avaliação do modelo - Retorno em uma tabela HTML
def validation(y_true, y_pred):

    return pd.DataFrame(data=classification_report(y_true, y_pred, output_dict=True)).to_html()

#===========================================
# Realizar o treinmento de novo Modelo SVC em Pipeline com pré processamento
def treinar_modelo(X_train, y_train):
    
    # Pré processamento das colunas de categorical features
    preprocessor = ColumnTransformer([("cat", 
                                       OneHotEncoder(handle_unknown='ignore'), 
                                       categorical_features)], 
                                       remainder="passthrough")

    # Criar novo modelo
    clf = SVC(gamma='auto')

    # create a pipeline with preprocessor and classifier
    pipeline = Pipeline([('preprocessor', preprocessor),
                         ('classifier', clf)
                         ])

    modelo = pipeline.fit(X_train, y_train.values.ravel())

    # salvar o Classification Model
    joblib.dump(modelo, "./src/models/pipeline_model.pkl") 

    return modelo

#===========================================
# Preparar o dado para realizar treinamento
def get_dataset():

    # load base de dados
    X = Train_Data().X()
    y = Train_Data().target()
    
    return X, y