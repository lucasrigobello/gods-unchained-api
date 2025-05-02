import pandas as pd
import yaml

# Read Features Config YAML file
with open("./src/config/conf.yaml", 'r') as stream:
    conf_features = yaml.safe_load(stream)

numerical_features = conf_features['numerical_features']
categorical_features = conf_features['categorical_features']
target = conf_features['target']

class Test_Data:
  def __init__(self, id):
    # load base de dados
    self.df_train = pd.read_csv('./data/challenge_train.csv', sep = ';')
    self.train_columns = list(self.df_train.columns)

    self.df_test = pd.read_csv('./data/challenge_test.csv', sep = ';')
    self.test_columns = list(self.df_test.columns)

    self.df = pd.concat([self.df_train, self.df_test])
    self.item = self.df[self.df['id'] == int(id)]

    self.name = self.item.name

  def X(self):
    return self.item[numerical_features + categorical_features]
  
class Train_Data:
  def __init__(self):
    # load base de dados
    self.df = pd.read_csv('./data/challenge_train.csv', sep = ';')
    self.columns = list(self.df.columns)

  def X(self):
    return self.df[numerical_features + categorical_features]
  
  def target(self):
    return self.df[target]