# Visual-R-MAT: Representação Visual de Trajetórias de Múltiplos Aspectos
==========================================================================

Visão Geral
Visual R-MAT é uma ferramenta para representação de múltiplas trajetórias de aspecto (MAT) em gráficos 2D com foco principal na comparação de um conjunto T = <t1, t2, ..., tn> de MATs a uma trajetória representativa do conjunto. Oferece as seguintes opções para a criação de gráficos:
- (i) representação do conjunto de dados: representa o conjunto de dados usando linhas e pontos que podem ser personalizados. O arquivo de entrada segue o formato proposto pelo método MAT-SG.
- (ii) trajetória representativa: desenha as trajetórias representativas com pontos e/ou linhas. O arquivo de entrada segue o formato proposto pelo método MAT-SG.
- (iii) representação de texto: uma opção para exibir informações semânticas relacionadas a cada ponto das trajetórias do conjunto T e/ou da trajetória representativa.

# Recursos não implementados
- Filtro: opção para filtrar e exibir apenas pontos que atendem a uma condição semântica.
- Opções de tipo de arquivo e qualidade de imagem não implementadas.
- ...

# Instalação
Baixe o repositório e instale as seguintes bibliotecas Python (se ainda não estiverem instaladas):
- PySimpleGui
- tkinter
- adjustText

# Como executar
Execute o programa através do arquivo app.py. Clique em "Load" e selecione o caminho do arquivo e seu formato (opção de filtro não implementada). Clique em "Trajectories" para ver as trajetórias carregadas e excluí-las manualmente. Selecione as opções de visualização de conjunto de dados e trajetória representativa e gere o gráfico clicando em "Plot". Outras funções incluem:
- O carregamento do arquivo de trajetória representativa define o tamanho da grade automaticamente. A grade também pode ser definida manualmente e ativada/desativada.
- A opção "Auto reset" redefine o gráfico toda vez que é gerado. Se desativado, adiciona linhas, pontos e textos sobre o gráfico existente (mesmo que seja a mesma informação no gráfico).
- A opção "Save" permite salvar o gráfico como imagens PNG (outros tipos de arquivo não implementados).
