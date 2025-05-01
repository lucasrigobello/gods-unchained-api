# Classificação de Cards de Gods Unchained - API com FastAPI

## 📌 Sobre o projeto
Esta API foi desenvolvida para classificar os cards do jogo **Gods Unchained** como **"early game"** ou **"late game"** com base em atributos como **mana, attack, health, type e god**. O modelo treinado utiliza técnicas de machine learning para realizar essa predição e é exposto publicamente através de uma API criada com **FastAPI**.

<p align="center">
<img src="https://github.com/lucasrigobello/gods-unchained-api/blob/d92aec61a2f2ce76d7b79ab5821cc5812751865b/images/gods-unchained-cover.jpg?raw=true" width="450"></p>

## 🚀 Tecnologias utilizadas
- **Python** (para implementação do modelo e da API)
- **FastAPI** (para exposição do modelo via API REST)
- **Scikit-learn** ( para framework para machine learning)
- **Docker** (para conteinerização da aplicação)
- **Kubernetes** (para orquestração e deploy)
- **Swagger** (para documentação da API)
- **Pytest** (para testes unitários)

## 📜 Licença
Este projeto está sob a licença MIT.
________________________________________

## 📊 Análise Exploratória de Dados - EDA
### Análise de features numéricas
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>mana</th>
      <td>788.0</td>
      <td>3.572335</td>
      <td>2.190100</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>16.0</td>
    </tr>
    <tr>
      <th>attack</th>
      <td>788.0</td>
      <td>2.140863</td>
      <td>2.215047</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>13.0</td>
    </tr>
    <tr>
      <th>health</th>
      <td>788.0</td>
      <td>2.583756</td>
      <td>2.455053</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>17.0</td>
    </tr>
  </tbody>
</table>

- Gráfico em Boxplot
<div style="display: flex; flex-wrap: wrap">
<img src="https://github.com/lucasrigobello/gods-unchained-api/blob/c4a9cfa1b7ab49832bb6a95a1e9ac5cdc6f4cfa0/notebook/EDA%20Results/numerical_features_boxplot.png?raw=true" width="450">
</div>

- Gráfico de Histograma
<div style="display: flex; flex-wrap: wrap">
<img src="https://github.com/lucasrigobello/gods-unchained-api/blob/c4a9cfa1b7ab49832bb6a95a1e9ac5cdc6f4cfa0/notebook/EDA%20Results/numerical_features_histogram_mana.png?raw=true" width="450"/>
<img src="https://github.com/lucasrigobello/gods-unchained-api/blob/c4a9cfa1b7ab49832bb6a95a1e9ac5cdc6f4cfa0/notebook/EDA%20Results/numerical_features_histogram_attack.png?raw=true" width="450"/>
<img src="https://github.com/lucasrigobello/gods-unchained-api/blob/c4a9cfa1b7ab49832bb6a95a1e9ac5cdc6f4cfa0/notebook/EDA%20Results/numerical_features_histogram_health.png?raw=true" width="450"/>
</div>

- Correlação entre features
<div style="display: flex; flex-wrap: wrap">
<img src="https://github.com/lucasrigobello/gods-unchained-api/blob/c4a9cfa1b7ab49832bb6a95a1e9ac5cdc6f4cfa0/notebook/EDA%20Results/numerical_feature_correlation.png?raw=true" width="450"/>
</div>

- Vizualização de disperção entre features e segmentação pelo target
<div style="display: flex; flex-wrap: wrap">
<img src="https://github.com/lucasrigobello/gods-unchained-api/blob/c4a9cfa1b7ab49832bb6a95a1e9ac5cdc6f4cfa0/notebook/EDA%20Results/numerical_features_scatter_mana_attack.png?raw=true" width="450"/>
<img src="https://github.com/lucasrigobello/gods-unchained-api/blob/c4a9cfa1b7ab49832bb6a95a1e9ac5cdc6f4cfa0/notebook/EDA%20Results/numerical_features_scatter_mana_health.png?raw=true" width="450"/>
<img src="https://github.com/lucasrigobello/gods-unchained-api/blob/c4a9cfa1b7ab49832bb6a95a1e9ac5cdc6f4cfa0/notebook/EDA%20Results/numerical_features_scatter_attack_health.png?raw=true" width="450"/>
</div>

### Análise de features de categorias/qualitativas
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>unique</th>
      <th>top</th>
      <th>freq</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>type</th>
      <td>788</td>
      <td>4</td>
      <td>creature</td>
      <td>526</td>
    </tr>
    <tr>
      <th>god</th>
      <td>788</td>
      <td>7</td>
      <td>neutral</td>
      <td>276</td>
    </tr>
    <tr>
      <th>strategy</th>
      <td>788</td>
      <td>2</td>
      <td>early</td>
      <td>432</td>
    </tr>
  </tbody>
</table>

- Vizualiação de frequência de categórias em cada feature categórica
<div style="display: flex; flex-wrap: wrap">
<img src="https://github.com/lucasrigobello/gods-unchained-api/blob/c4a9cfa1b7ab49832bb6a95a1e9ac5cdc6f4cfa0/notebook/EDA%20Results/categorical_features_frequency_type.png?raw=true" width="450"/>
<img src="https://github.com/lucasrigobello/gods-unchained-api/blob/c4a9cfa1b7ab49832bb6a95a1e9ac5cdc6f4cfa0/notebook/EDA%20Results/categorical_features_frequency_god.png?raw=true" width="450"/>
<img src="https://github.com/lucasrigobello/gods-unchained-api/blob/c4a9cfa1b7ab49832bb6a95a1e9ac5cdc6f4cfa0/notebook/EDA%20Results/categorical_features_frequency_strategy.png?raw=true" width="450"/>
</div>

# 🔍 Resultados e Avaliação do Treinamento
- Report de avalição com dados de treinamento
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>early</th>
      <th>late</th>
      <th>accuracy</th>
      <th>macro avg</th>
      <th>weighted avg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>precision</th>
      <td>0.982993</td>
      <td>1.000000</td>
      <td>0.990512</td>
      <td>0.991497</td>
      <td>0.990674</td>
    </tr>
    <tr>
      <th>recall</th>
      <td>1.000000</td>
      <td>0.978992</td>
      <td>0.990512</td>
      <td>0.989496</td>
      <td>0.990512</td>
    </tr>
    <tr>
      <th>f1-score</th>
      <td>0.991424</td>
      <td>0.989384</td>
      <td>0.990512</td>
      <td>0.990404</td>
      <td>0.990503</td>
    </tr>
    <tr>
      <th>support</th>
      <td>289.000000</td>
      <td>238.000000</td>
      <td>0.990512</td>
      <td>527.000000</td>
      <td>527.000000</td>
    </tr>
  </tbody>
</table>

- Report de avalição com dados de teste
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>early</th>
      <th>late</th>
      <th>accuracy</th>
      <th>macro avg</th>
      <th>weighted avg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>precision</th>
      <td>0.972603</td>
      <td>0.991304</td>
      <td>0.980843</td>
      <td>0.981954</td>
      <td>0.981058</td>
    </tr>
    <tr>
      <th>recall</th>
      <td>0.993007</td>
      <td>0.966102</td>
      <td>0.980843</td>
      <td>0.979554</td>
      <td>0.980843</td>
    </tr>
    <tr>
      <th>f1-score</th>
      <td>0.982699</td>
      <td>0.978541</td>
      <td>0.980843</td>
      <td>0.980620</td>
      <td>0.980819</td>
    </tr>
    <tr>
      <th>support</th>
      <td>143.000000</td>
      <td>118.000000</td>
      <td>0.980843</td>
      <td>261.000000</td>
      <td>261.000000</td>
    </tr>
  </tbody>
</table>