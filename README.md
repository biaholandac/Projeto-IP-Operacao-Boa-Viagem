# Projeto-final-IP
Projeto Final da disciplina de Introdução a Programação
# Operação Boa Viagem 🦈🌊

Jogo desenvolvido em **Python e Pygame** como projeto final da disciplina de Introdução à Programação.

O jogador surfa pelo mar de Boa Viagem, recolhendo resíduos que estão espalhados pela pista enquanto tenta escapar de um tubarão. Durante a partida, é necessário desviar de obstáculos, utilizar mergulhos e aproveitar os itens encontrados para alcançar a meta antes que o tempo termine.

**Equipe:** Bia H, Bia N, Clara, João, Lucia e Luiza.

---

## Como funciona o jogo

A partida acontece em uma pista com **três faixas**, pelas quais o jogador pode se movimentar. O jogo possui duração de aproximadamente dois minutos, e o objetivo principal é recolher:

- 6 latas;
- 6 sacos plásticos.

Enquanto coleta os itens, o jogador precisa evitar obstáculos e controlar a distância em relação ao tubarão.

### Controles

| Tecla | Ação |
|---|---|
| ← / → ou A / D | Trocar de faixa |
| ↓, Espaço ou S | Mergulhar |
| Enter | Confirmar nas telas |
| R | Tentar novamente após a derrota |
| Esc | Voltar ao menu ou sair |

### Coletáveis

Os coletáveis são objetos espalhados pela pista que podem ser recolhidos pelo jogador. Cada tipo possui uma função diferente.

| Coletável | Efeito |
|---|---|
| Lata | Conta para a meta de coleta, concede pontos e afasta o tubarão |
| Saco plástico | Conta para a meta de coleta, concede pontos e afasta o tubarão |
| Garrafa de vidro | Ativa um turbo por alguns segundos, aumentando a velocidade do jogador |

### Obstáculos

Além dos coletáveis, existem objetos que atrapalham o progresso do jogador.

| Obstáculo | Efeito |
|---|---|
| Boia | Aproxima o tubarão. O jogador pode passar por baixo dela utilizando o mergulho |
| Piche | Deixa o jogador mais lento por alguns segundos |

### Condições de término

A partida pode terminar de três maneiras:

- **Vitória:** o jogador consegue cumprir a meta de coleta.
- **Captura:** o tubarão alcança o jogador.
- **Derrota por tempo:** o tempo da partida acaba antes de cumprir o objetivo.

---

## Instalação e execução

É necessário ter **Python 3.13** instalado.

### Instalar as dependências

Na pasta principal do projeto, execute:

```bash
py -3.13 -m pip install -r requirements.txt
```

### Executar o jogo

```bash
py -3.13 main.py
```

### Executar os testes

```bash
py -3.13 testes/testar.py
```

---

## Organização e divisão do projeto

O projeto foi dividido entre os seis integrantes, de acordo com as responsabilidades de cada parte do jogo.

### João — Recursos visuais, sonoros e dados da fase

**Arquivos:** `assets/`, `fase_dados.py`, `docs/capturas/`

Responsável pela parte visual e sonora do jogo, além da organização dos dados utilizados na montagem da fase.

Principais responsabilidades:

- Organizar as imagens e os sprites utilizados no jogo.
- Disponibilizar os efeitos sonoros e as músicas.
- Definir os dados e as posições dos objetos distribuídos pela fase.
- Organizar as capturas de tela utilizadas na documentação.
- Auxiliar na organização dos materiais do projeto, README e apresentação.

### Bia H — Inicialização e controle geral do jogo

**Arquivos:** `main.py`, `jogo.py`, `partida.py`

Responsável pela estrutura principal do jogo e pela integração dos diferentes sistemas.

Principais responsabilidades:

- Inicializar o Pygame e preparar a janela do jogo.
- Controlar o loop principal, responsável pela atualização e exibição contínua do jogo.
- Gerenciar a troca entre as diferentes telas.
- Controlar o início, a execução e o encerramento das partidas.
- Integrar os sistemas de jogador, tubarão, HUD, fase e demais elementos.
- Coordenar a lógica geral de funcionamento da partida.

### Bia N — Jogador, HUD e montagem da fase

**Arquivos:** `jogador.py`, `hud.py`, `fase.py`

Responsável pelo personagem controlado pelo jogador, pelas informações exibidas na tela e pela organização dos elementos da fase.

Principais responsabilidades:

- Implementar a movimentação do jogador entre as três faixas.
- Controlar o mergulho e os estados de movimento do personagem.
- Gerenciar as interações do jogador com os objetos da pista.
- Desenvolver o HUD, exibindo informações como pontuação, tempo e quantidade de itens coletados.
- Controlar a montagem e a organização da fase.
- Utilizar os dados definidos em `fase_dados.py` para posicionar os objetos no percurso.
- Integrar os coletáveis e obstáculos à fase.

### Clara — Recursos e objetos do mar

**Arquivos:** `recursos.py`, `objeto_mar.py`, `coletaveis.py`

Responsável pelo carregamento e gerenciamento dos recursos utilizados no jogo, além da estrutura dos objetos presentes no mar.

Principais responsabilidades:

- Implementar o carregamento de imagens, sons e fontes.
- Gerenciar a reprodução de efeitos sonoros e músicas.
- Criar mecanismos de armazenamento em cache para evitar carregamentos repetidos.
- Garantir que o jogo continue funcionando mesmo quando algum recurso não estiver disponível.
- Desenvolver a classe-base `ObjetoDoMar`, que reúne características comuns dos objetos presentes na pista.
- Implementar os coletáveis por meio de classes que herdam da classe-base.

Os principais coletáveis desenvolvidos são:

- `Lata`: representa as latas recolhidas pelo jogador.
- `SacoPlastico`: representa os sacos plásticos que devem ser coletados.
- `GarrafaVidro`: representa as garrafas que concedem o efeito de turbo.

A classe `ObjetoDoMar` também serve de base para os obstáculos desenvolvidos por Lucia, permitindo reutilizar características como posição, faixa, imagem e desenho com perspectiva.

### Lucia — Perspectiva, obstáculos e telas

**Arquivos:** `perspectiva.py`, `obstaculos.py`, `telas.py`

Responsável pelo funcionamento da perspectiva da pista, pelos obstáculos e pelas telas de interface do jogo.

Principais responsabilidades:

- Implementar o sistema de perspectiva, transformando a posição dos objetos na pista em coordenadas na tela.
- Controlar o posicionamento e o tamanho dos objetos de acordo com a distância em relação ao jogador.
- Desenvolver os obstáculos presentes no percurso.
- Implementar a boia e o piche, incluindo seus efeitos durante a partida.
- Utilizar a classe-base `ObjetoDoMar` para estruturar os obstáculos.
- Desenvolver o menu inicial, a introdução e a tela de derrota.
- Organizar a navegação entre as telas.

### Luiza — Tubarão e cenas especiais

**Arquivos:** `tubarao.py`, `cenas_tubarao.py`

Responsável pelo comportamento do tubarão e pelas cenas relacionadas aos momentos especiais da partida.

Principais responsabilidades:

- Implementar o comportamento e a movimentação do tubarão.
- Controlar a distância entre o tubarão e o jogador.
- Gerenciar as alterações de comportamento provocadas pelas ações do jogador e pelos objetos coletados.
- Implementar a perseguição e a captura do jogador.
- Desenvolver as cenas de captura e vitória.
- Integrar os efeitos visuais e sonoros relacionados ao tubarão.

### Trabalho coletivo

**Arquivos:** `config.py`, `testes/`, `README.md`

Algumas partes são compartilhadas entre os integrantes:

- `config.py`: reúne as constantes e configurações gerais do jogo, como dimensões da tela, velocidades, tempo de partida, metas, distâncias e cores.
- `testes/`: reúne os testes utilizados para verificar o funcionamento dos diferentes sistemas.
- `README.md`: documenta o projeto, sua execução, organização e desenvolvimento.

---

## Relação entre os arquivos

Os arquivos trabalham em conjunto para garantir o funcionamento do jogo.

- `main.py` inicia o jogo por meio de `jogo.py`.
- `jogo.py` controla o loop principal e a troca de telas.
- `partida.py` reúne os elementos necessários para executar uma partida.
- `jogador.py` controla o personagem e suas ações.
- `hud.py` exibe as informações da partida.
- `fase.py` organiza os elementos do percurso utilizando os dados de `fase_dados.py`.
- `coletaveis.py` implementa os objetos que podem ser recolhidos pelo jogador.
- `obstaculos.py` implementa os objetos que dificultam o percurso.
- `objeto_mar.py` fornece uma estrutura comum para coletáveis e obstáculos.
- `perspectiva.py` calcula a posição dos objetos na tela de acordo com sua distância.
- `recursos.py` centraliza o carregamento e a utilização de imagens, sons e fontes.
- `tubarao.py` controla o comportamento do tubarão.
- `cenas_tubarao.py` apresenta as cenas relacionadas à captura e à vitória.
- `telas.py` organiza as telas de interface do jogo.
- `config.py` centraliza os valores utilizados pelos diferentes módulos.
