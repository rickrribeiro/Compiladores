# Compiladores
<br>
txts > arquivos texto relacionados ao automato. Esse diretório começa com os arquivos das wirths simplificadas e é preenchido na execução.<br>
<br>
src > Scripts em Python a serem chamados pelo programa principal.<br>
    - bota_ponto.py : Coloca os pontos na wirth simplificada para formar o automato bruto<br>
    - estados_finais.py : Busca pelos estados finais após a definição dos estados<br>
    - estados.py : verifica as regras para formações dos estados no automato bruto<br>
    - helpers.py : sub rotinas de apoio que são utilizadas em várias partes do código<br>
    - lexico.py: rotina da análise léxica que transforma as cadeias em atomos e preenche a tabela de simbolos<br>
    - matriz_trans.py : gera as matrizes de transições<br>
    - model.py: model com as classes Estado e Transição<br>
    - sintatico.py: parte da rotina da análise sintática que verifica a ordem dos atomos (incompleta, funciona apenas com o program)<br>
    - tabelas.py: tabela de palavras e simbolos, simbolos e tabela com resultado do .lex<br>
    - transs_acess.py: remove transições não acessiveis<br>
    - trans_equivalentes.py: remove as transições equivalentes<br>
    - trans_nao_det.py: remove as transições não deterministicas<br>
    - trans_vazio.py: remove as transições em vazio<br>
    - transicoes.py : lê os estados e gera as transições<br>
setup.py - arquivo para gerar o EXE<br>
testes.py - arquivo fora do projeto para fazer testes<br>
staticchecker.py - main do projeto que vai desde a formação do automato até o fim<br>
staticchecker.min.py - main do projeto que faz apenas a análise léxica<br>
observação ><br>
    Precisa ser utilizado espaço ou \n como delimitadores. ex: (TRUE) não será aceito, o correto seria ( TRUE )<br>
