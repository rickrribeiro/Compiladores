# Compiladores

txts > arquivos texto relacionados ao automato. Esse diretório começa com os arquivos das wirths simplificadas e é preenchido na execução.

src > Scripts em Python a serem chamados pelo programa principal.
    - bota_ponto.py : Coloca os pontos na wirth simplificada para formar o automato bruto
    - estados_finais.py : Busca pelos estados finais após a definição dos estados
    - estados.py : verifica as regras para formações dos estados no automato bruto
    - helpers.py : sub rotinas de apoio que são utilizadas em várias partes do código
    - lexico.py: rotina da análise léxica que transforma as cadeias em atomos e preenche a tabela de simbolos
    - matriz_trans.py : gera as matrizes de transições
    - model.py: model com as classes Estado e Transição
    - sintatico.py: parte da rotina da análise sintática que verifica a ordem dos atomos (incompleta, funciona apenas com o program)
    - tabelas.py: tabela de palavras e simbolos, simbolos e tabela com resultado do .lex
    - transs_acess.py: remove transições não acessiveis
    - trans_equivalentes.py: remove as transições equivalentes
    - trans_nao_det.py: remove as transições não deterministicas
    - trans_vazio.py: remove as transições em vazio
    - transicoes.py : lê os estados e gera as transições
setup.py - arquivo para gerar o EXE
testes.py - arquivo fora do projeto para fazer testes
staticchecker.py - main do projeto que vai desde a formação do automato até o fim
staticchecker.min.py - main do projeto que faz apenas a análise léxica
observação >
    Precisa ser utilizado espaço ou \n como delimitadores. ex: (TRUE) não será aceito, o correto seria ( TRUE )