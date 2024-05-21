import json
import csv
import re

regex = re.compile(' |\(|\)')

f = open('pg54273.json','r')
doentes = json.load(f)
f.close()

base = """@prefix : <http://www.example.org/disease-ontology#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix swrl: <http://www.w3.org/2003/11/swrl#> .
@prefix swrlb: <http://www.w3.org/2003/11/swrlb#> .

:Ontology a owl:Ontology .

# Classes
:Disease a owl:Class .
:Symptom a owl:Class .
:Treatment a owl:Class .
:Patient a owl:Class .

# Properties
:hasSymptom a owl:ObjectProperty ;
    rdfs:domain :Disease ;
    rdfs:range :Symptom .

:hasTreatment a owl:ObjectProperty ;
    rdfs:domain :Disease ;
    rdfs:range :Treatment .

:exhibitsSymptom a owl:ObjectProperty ;
    rdfs:domain :Patient ;
    rdfs:range :Symptom .

:hasDisease a owl:ObjectProperty ;
    rdfs:domain :Patient ;
    rdfs:range :Disease .

:receivesTreatment a owl:ObjectProperty ;
    rdfs:domain :Patient ;
    rdfs:range :Treatment .
"""

base += """\n:hasDesc a owl:ObjectProperty ;
    rdfs:domain :Disease ;
    rdfs:range xsd:string .
\n"""

dis_set = set()
synt_set = set()

reader = csv.DictReader(open('Disease_Syntoms.csv'))
for row in reader:
    string = ""
    synts = list(row.values())[1:]
    dis = regex.sub('_',row['Disease'])

    if not dis in dis_set:
        string += f":{dis} a :Disease .\n"
        dis_set.add(dis)

    for s in synts:
        if not s == '':
            ns = regex.sub('_',s)
            if not ns in synt_set:
                string += f":{ns} a :Symptom .\n"
                synt_set.add(ns)
            
            phrase = f":{dis} :hasSymptom :{ns} .\n"
            
            if not phrase in base:
                string += phrase

    base += string


reader = csv.DictReader(open('Disease_Description.csv'))
for row in reader:
    string = ""
    desc = row['Description'].replace("\"",'\'')
    dis = regex.sub('_',row['Disease'])

    if not dis in dis_set:
        string += f":{dis} a :Disease .\n"
        dis_set.add(dis)

    string += f":{dis} :hasDesc \"{desc}\" .\n"

    base += string

file1 = open("med_doencas.ttl","w")
file1.write(base)
file1.close()

prec_set = set()
reader = csv.DictReader(open('Disease_Treatment.csv'))
for row in reader:
    string = ""
    prec = list(row.values())[1:]
    dis = regex.sub('_',row['Disease'])

    if not dis in dis_set:
        string += f":{dis} a :Disease .\n"
        dis_set.add(dis)

    for p in prec:
        if not p == '':
            np = regex.sub('_',p)
            if not np in prec_set:
                string += f":{np} a :Treatment .\n"
                prec_set.add(np)
            
            phrase = f":{dis} :hasTreatment :{np} .\n"
            
            if not phrase in base:
                string += phrase

    base += string

file2 = open("med_tratamentos.ttl","w")
file2.write(base)
file2.close()

id = 0
for d in doentes:
    string = ""
    string += f":P{id} a :Patient .\n"
    string += f":P{id} :name \"{d['nome']}\" .\n"
    for ds in d["sintomas"]:
        string += f":P{id} :exhibitsSymptom \"{ds}\" .\n"
    
    base += string

    id +=1
    
file3 = open("med_doentes.ttl","w")
file3.write(base)
file3.close()