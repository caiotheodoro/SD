#  Dependencias
```
python

```
# Como Compilar/Executar
```

python3 ./client.py <topicos para assinar>
python3 ./funnel.py 
python3 ./collector.py

```

# Bibliotecas usadas
```
- tweepy: biblioteca da api do twitter  - https://pypi.org/project/tweepy/
- pika: biblioteca de comunicação com rabbitmq - https://pypi.org/project/pika/
- sys: biblioteca de sistema - https://docs.python.org/3/library/sys.html

```

# Exemplo de uso
```bash
python3 ./client.py chess
python3 ./funnel.py 
python3 ./collector.py
```


# Será retornado no cliente o tópico e a mensagem.

```
Tópico: 'magnus'
Mensagem: 'Vivek Ranjan Agnihotri - Congratulations GRANDMASTER R Praggnanandhaa for defeating World Champion Magnus Carlsen for the second time in jus… https://t.co/3riYwQCQaZ\n' 

Tópico: 'chess'
Mensagem: 'Anshul Saxena - 16-year-old Indian grandmaster Praggnanandhaa Rameshbabu defeated world chess champion Magnus Carlsen for the 2nd t… https://t.co/kylDtxZT0q\n' 

Tópico: 'magnus'
Mensagem: 'Anshul Saxena - 16-year-old Indian grandmaster Praggnanandhaa Rameshbabu defeated world chess champion Magnus Carlsen for the 2nd t… https://t.co/kylDtxZT0q\n' 

Tópico: 'chess'
Mensagem: 'Mark Erlenwein - @SITech_HS Chess Club President: Chang Zhe Zeng, with the 2022 Knight Tour Chess Tournament winners: 1st Place: Dan… https://t.co/cnLE4yrcXu\n'         

Tópico: 'chess'
Mensagem: '. - @Eng_alharbi_mm @mkt_chess هذا انا 🤦🏻\u200d♀️\n' 
```