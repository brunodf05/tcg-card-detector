# TCG Card Detection

## Aluno: Bruno d'Almeida Franco (github)
#### Orientador: Vitor Bento de Sousa

---

Trabalho apresentado ao curso [VC MASTER](https://ica.puc-rio.ai/vc-master) como pré-requisito para conclusão de curso e obtenção de crédito na disciplina "Projetos de Sistemas Inteligentes de Apoio à Decisão".

- [Link para o código](src\card_detector.ipynb).
- [Link para a imagem de teste](runs\detect\predict\1test_img.jpg)
---

### Resumo

Projeto de visão computacional para detecção de cartas de TCG. O objetivo do trabalho é a detecção de cartas em uma mesa de jogo de TCG (Trading Card Games) por meio de webcam em tempo real ou por video gravado.

### Abstract

Project of Computer Vision for TCG cards detection. The goal of the project is to detect TCG (Trading Card Games) cards on a table either by webcam in real time or by previously recorded videos.

### 1. Introdução

Com o aumento no numero de TCGs surgindo e comunidades que participam crescendo constantemente, seja tanto por hobby ou de forma competitiva, alem do aumento de torneios de formato online tanto para jogar com webcam quanto a transmissao via plataformas de streaming, muitas vezes é dificil para quem esta entrando no meio de se familiarizar com as mesas vendo pela primeira vez e mais dificil ainda saber o que cada carta na mesa quer dizer para o jogo. O objetivo final desse projeto é a criacao de um programa onde ao utilizar tanto para jogar ou acompanhando um video de aprendizado o usuario possa identificar cada carta que esta dentro da mesa de jogo e possa tambem identifica-la de forma mais rapida, mesmo tendo uma qualidade de video baixa.

### 2. Modelagem

Para a preparação do dataset foram tiradas 300 imagens de diferentes angulos e qualidades de diversas mesas de jogos e torneios online transmitidos, tanto por webcam quanto videos em alta qualidade. Foi utilizado a ferramenta Roboflow para a preparação desse dataset de forma manual identificando nas imagens todas as cartas nas imagens.

O treinamento do modelo foi feito utilizando Yolo8 para a primeira instancia do projeto de detecção de objetos.

### 3. Resultados

Ao analisar os resultados do treinamento feito com 150 epochs e reduzindo a resolucao das imagens para 640 , o modelo tem uma precisão de 0.941 , recall de 0.9 , map50 de 0.949.

### 4. Conclusões

 Os resultados são aceitaveis para o treinamento inicial feito para a primeira parte desse projeto com o foco da detecção de objetos, para a continuidade dele serão realizados treinamento de modelos de similaridade, OpenCV para a utilização de videos e acesso a APIs das empresas responsaveis para identificação precisa do dataset de cada carta especificamente.

---

Matrícula: 241.100.498

Pontifícia Universidade Católica do Rio de Janeiro

Curso de Pós Graduação *Visão Computacional Master*