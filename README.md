# TCG Card Detection

## Aluno: [Bruno d'Almeida Franco](https://github.com/brunodf05)
#### Orientador: Vitor Bento de Sousa

---

Trabalho apresentado ao curso [VC MASTER](https://ica.puc-rio.ai/vc-master) como pré-requisito para conclusão de curso e obtenção de crédito na disciplina "Projetos de Sistemas Inteligentes de Apoio à Decisão".

- [Link para o código](src\card_detector.ipynb).
- [Link para a imagem de teste](runs\detect\predict-2\1test_img.jpg)
---

### Resumo

Projeto de Visão Computacional para detecção de cartas de TCG. O objetivo do trabalho é detectar cartas em uma mesa de jogo de TCG (Trading Card Games) por meio de webcam em tempo real ou de vídeos gravados, utilizando as técnicas aprendidas ao longo do curso para treinamento e validação do modelo, inicialmente aplicado em imagens para, posteriormente, evoluir para vídeos e processamento em tempo real.

### Abstract

Computer Vision project for TCG card detection. The goal of this project is to detect TCG (Trading Card Games) cards on a game table using either a real-time webcam feed or previously recorded videos, applying the techniques learned throughout the course for model training and validation. The model is initially trained using images and will later be extended to process videos and real-time camera input.

### 1. Introdução

Com o aumento do número de TCGs e o crescimento constante de suas comunidades, tanto por hobby quanto de forma competitiva, além do aumento da realização de torneios em formato online, seja para partidas por webcam ou transmissões em plataformas de streaming, muitas vezes é difícil para novos jogadores se familiarizarem com o estado da mesa de jogo. Além disso, torna-se ainda mais difícil compreender rapidamente o significado de cada carta presente na mesa. O objetivo final deste projeto é criar um programa que permita ao usuário identificar automaticamente cada carta presente em uma mesa de jogo, tanto durante uma partida quanto ao assistir a vídeos educativos, possibilitando uma identificação rápida e precisa mesmo em vídeos de baixa qualidade.

### 2. Modelagem

Para a preparação do dataset, foram coletadas 300 imagens de diferentes ângulos e níveis de qualidade, provenientes de diversas mesas de jogos e torneios online, tanto por webcam quanto por vídeos em alta qualidade. Foi utilizada a ferramenta Roboflow para a anotação manual do dataset, identificando todas as cartas presentes em cada imagem.

O treinamento do modelo foi realizado utilizando o YOLOv8 como primeira etapa do projeto de detecção de objetos.

### 3. Resultados

Ao analisar os resultados do treinamento, realizado com 150 epochs e resolução de imagem reduzida para 640 × 640 pixels, o modelo obteve precisão de 0,941, recall de 0,900, e mAP@50 de 0,949. Para os conjuntos de treino, validação e teste, os resultados foram, respectivamente:

Treino: precisão de 0,9563, recall de 0,9251 e mAP@50 de 0,9679;
Validação: precisão de 0,9410, recall de 0,9003 e mAP@50 de 0,9489;
Teste: precisão de 0,9002, recall de 0,8589 e mAP@50 de 0,9030.

### 4. Conclusões

 Os resultados obtidos são satisfatórios para a primeira etapa deste projeto, cujo foco é a detecção de objetos. Como continuidade do trabalho, serão realizados treinamentos de modelos de similaridade, integração com OpenCV para processamento de vídeos em tempo real e acesso às APIs das empresas responsáveis pelos jogos, permitindo a identificação precisa da carta correspondente a cada objeto detectado.

---

Matrícula: 241.100.498

Pontifícia Universidade Católica do Rio de Janeiro

Curso de Pós Graduação *Visão Computacional Master*