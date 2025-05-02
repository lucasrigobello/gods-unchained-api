from src.classes.dataset import Test_Data, Train_Data

# Estrutura de teste do objeto dataset que busca e prepara os dados de treino e teste/predict

#===========================================
# Teste da base de teste/predict
def test_base_dados_teste():

    # Teste de alguns registros em banco de teste
    # 1245;Crystal Rain;5;0;0;spell;magic
    registro = Test_Data(1245)

    # Teste de valores do registro
    assert registro.name.values[0] == 'Crystal Rain'
    assert registro.item.id.values[0] == 1245
    assert registro.item.mana.values[0] == 5
    assert registro.item.attack.values[0] == 0
    assert registro.item.health.values[0] == 0
    assert registro.item.type.values[0] == 'spell'
    assert registro.item.god.values[0] == 'magic'
    assert registro.item.strategy.isna().all()

    # Teste das features para treinmaneto
    assert 'id' not in registro.X().columns 
    assert 'name' not in registro.X().columns
    assert 'mana' in registro.X().columns
    assert 'attack' in registro.X().columns
    assert 'health' in registro.X().columns
    assert 'type' in registro.X().columns
    assert 'god' in registro.X().columns
    assert 'strategy' not in registro.X().columns

    # Teste de alguns registros em banco de treinamento
    # 846;Dionysus, the Bountiful;9;8;8;creature;nature;late
    registro = Test_Data(846)

    # Teste de valores do registro
    assert registro.name.values[0] == 'Dionysus, the Bountiful'
    assert registro.item.id.values[0] == 846
    assert registro.item.mana.values[0] == 9
    assert registro.item.attack.values[0] == 8
    assert registro.item.health.values[0] == 8
    assert registro.item.type.values[0] == 'creature'
    assert registro.item.god.values[0] == 'nature'
    assert not registro.item.strategy.isna().all()
    assert registro.item.strategy.values[0] == 'late'

    # Teste das features para treinmaneto
    assert 'id' not in registro.X().columns 
    assert 'name' not in registro.X().columns
    assert 'mana' in registro.X().columns
    assert 'attack' in registro.X().columns
    assert 'health' in registro.X().columns
    assert 'type' in registro.X().columns
    assert 'god' in registro.X().columns
    assert 'strategy' not in registro.X().columns


#===========================================
# Teste da base de treinamneto
def test_base_dados_treinamento():

    # teste de objeto de base de dados de treinmaento.
    df_train = Train_Data()

    # Teste da base original para treinmaneto
    assert 'id' in df_train.columns 
    assert 'name' in df_train.columns
    assert 'mana' in df_train.columns
    assert 'attack' in df_train.columns
    assert 'health' in df_train.columns
    assert 'type' in df_train.columns
    assert 'god' in df_train.columns
    assert 'strategy' in df_train.columns

    # Teste das features para treinmaneto
    assert 'id' not in df_train.X().columns 
    assert 'name' not in df_train.X().columns
    assert 'mana' in df_train.X().columns
    assert 'attack' in df_train.X().columns
    assert 'health' in df_train.X().columns
    assert 'type' in df_train.X().columns
    assert 'god' in df_train.X().columns
    assert 'strategy' not in df_train.X().columns

    # Teste do Target para treinmaneto
    assert 'id' not in df_train.target().columns 
    assert 'name' not in df_train.target().columns
    assert 'mana' not in df_train.target().columns
    assert 'attack' not in df_train.target().columns
    assert 'health' not in df_train.target().columns
    assert 'type' not in df_train.target().columns
    assert 'god' not in df_train.target().columns
    assert 'strategy' in df_train.target().columns



