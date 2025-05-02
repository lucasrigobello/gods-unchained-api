from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.svm import SVC

import joblib
import yaml
import pandas as pd

import datetime

def preparar_dado_predict(id):

    # load base de dados
    df_train = pd.read_csv('./dataset/challenge_train.csv', sep = ';')
    df_test = pd.read_csv('./dataset/challenge_test.csv', sep = ';')
    df = pd.concat([df_train,df_test])
    item = df[df['id'] == int(id)]
       
    # Read Features Conf YAML file
    with open("./app/conf/conf.yaml", 'r') as stream:
        conf_features = yaml.safe_load(stream)

    numerical_features = conf_features['numerical_features']
    categorical_features = conf_features['categorical_features']

    numerical_data = item[numerical_features]
    categorical_data = item[categorical_features]

    # load OneHotEncoder
    enc = joblib.load("./models/OneHotEncoder_model.pkl") 

    # preparando dado para predição
    X = pd.concat([numerical_data.reset_index(drop=True), 
                   pd.DataFrame(enc.transform(categorical_data).toarray(), 
                                columns=enc.get_feature_names_out(categorical_features)
                                )
                    ],
              axis = 1)
    return X

def preparar_dado_trainamento():
    
    X, y = get_dataset()
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    return X_train, X_test, y_train, y_test


def validation(y_true, y_pred):

    return pd.DataFrame(data=classification_report(y_true, y_pred, output_dict=True)).to_html()


def treinar_modelo(X_train, y_train):

    # treinar novo modelo
    clf = SVC(gamma='auto')
    clf.fit(X_train, y_train)

    # salvar o Classification Model
    joblib.dump(clf, "./models/Classification_model.pkl")

    return clf

def get_dataset():

    # load base de dados
    df_train = pd.read_csv('./dataset/challenge_train.csv', sep = ';')

    # Read Features Conf YAML file
    with open("./app/conf/conf.yaml", 'r') as stream:
        conf_features = yaml.safe_load(stream)

    numerical_features = conf_features['numerical_features']
    categorical_features = conf_features['categorical_features']
    target = conf_features['target']

    numerical_data = df_train[numerical_features]
    categorical_data = df_train[categorical_features]
    y = df_train[target[0]]

    # load OneHotEncoder
    enc = joblib.load("./models/OneHotEncoder_model.pkl") 

    # preparando dado para predição
    X = pd.concat([numerical_data, pd.DataFrame(enc.transform(categorical_data).toarray(), columns=enc.get_feature_names_out(categorical_features))],
              axis = 1)
    
    return X, y

def primeiro_test(name):

    return name

def get_age(yyyy:int, mm:int, dd:int) -> int:
    dob = datetime.date(yyyy, mm, dd)
    today = datetime.date.today()
    age = round((today - dob).days / 365.25)
    return age