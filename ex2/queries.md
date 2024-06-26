# Queries

## Quantas doenças estão presentes na ontologia?

```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.example.org/disease-ontology#>

select (count(?d) as ?total) where{
    ?d rdf:type :Disease.
}
```
## Que doenças estão associadas ao sintoma "yellowish_skin"?
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.example.org/disease-ontology#>

select (count(?d) as ?total) where{
    ?d rdf:type :Disease.
    ?d :hasSymptom :_yellowish_skin .
}
```
## Que doenças estão associadas ao tratamento "exercise"?
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.example.org/disease-ontology#>

select (count(?d) as ?total) where{
    ?d rdf:type :Disease.
    ?d :hasTreatment :exercise .
}
```
## Produz uma lista ordenada alfabeticamente com o nome dos doentes.
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.example.org/disease-ontology#>

select ?name where{
    ?s rdf:type :Patient ;
       :name ?name .
}

order by ?name
```
## Cria uma query CONSTRUCT que diagnostique a doença de cada pessoa, ou seja, produza uma lista de triplos com a forma :patientX :hasDisease :diseaseY. No fim, acrescenta estes triplos à ontologia;
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.example.org/disease-ontology#>

construct{
    ?p :hasDisease ?d
}
where{
    ?p rdf:type :Patient .
    ?d rdf:type :Disease .
    ?p :exhibitsSymptom ?s.
    ?d :hasSymptom ?s .
}
```
order by ?name

## Cria um query SPARQL que poduza uma distribuição dos doentes pelas doenças, ou seja, dá como resultado uma lista de pares (doença, nº de doentes)
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.example.org/disease-ontology#>

select ?doenca (count(?d) as ?doentes) where{
    ?doenca rdf:type :Disease .
    ?d rdf:type :Patient .
    ?d :hasDisease ?doenca .
} group by ?doenca
```
## Cria um query SPARQL que poduza uma distribuição das doenças pelos sintomas, ou seja, dá como resultado uma lista de pares (sintoma, nº de doenças com o sintoma);
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.example.org/disease-ontology#>

select ?sintoma (count(?d) as ?doencas) where{
    ?sintoma rdf:type :Symptom .
    ?d rdf:type :Disease .
    ?d :hasSymptom ?sintoma .
} group by ?sintoma
```
## Cria um query SPARQL que poduza uma distribuição das doenças pelos tratamentos, ou seja, dá como resultado uma lista de pares (tratamento, nº de doenças com o tratamento)
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.example.org/disease-ontology#>

select ?tratamento (count(?d) as ?doencas) where{
    ?tratamento rdf:type :Treatment .
    ?d rdf:type :Disease .
    ?d :hasTreatment ?tratamento .
} group by ?tratamento
```