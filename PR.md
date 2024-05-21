# RPCW Normal 2324

Aluno: Vitor Lelis Noronha Leite
Numero: PG54273

## Resolução

Baseado no modelo `medical.ttl`, resolvi iterar por cada linha dos CSV's para formar os arquivos `.ttl` e gerar o output desejado.

Para as queries, foi usado um container correndo localmente do `GraphDB` para testar as queries `SPARQL`

## Correr

É necessário realizar a instalação do modulo de JSON do Python e depois dentro do diretório `ex2` usa-se o comando:

    python3 main.py

## Ficheiros

+ `Disease_*.csv` e `pg54273.json` -> Ficheiros de dados fornecidos;
+ `med_*.ttl` -> Ficheiros `.ttl` criados;
+ `main.py` -> Script Pyhton para criar os `.ttl`;
+ `queries.md` -> Arquivo com as queries feitas;
+ `query-result.ttl` -> Resultado da query `CONSTRUCT`.