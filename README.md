# Sistema de Gestão de Inventário

Desenvolver um sistema de gestão de inventário utilizando listas, dicionários, algoritmos de busca e ordenação, com  ênfase em segurança da informação. O sistema será implementado em Python, sem o uso de banco de dados externo, e  todas as operações serão realizadas em memória.

# Sumário

1. [Como Contribuir](#como-contribuir)

## Como Contribuir:

* A branch principal é a ***main***;
* Toda ***feature*** (nova-funcionalidade) deve ser criada uma ***branch*** à partir da ***main***;
* Ao concluir a ***feature***, deve ser criado um ***pull requeast*** para ***main***, para que uma implementação seja avaliada pelos demais integrantes do grupo;
* As ***features*** devem estar compatíveis com a ***main*** para que não haja conflito de ***merge***. Para isso, é necessário realizar um ***git pull*** na sua ***branch*** ***main*** local, em seguida um ***git merge***;
* A seguir, o passo a passo de como realizar:

### Criar _Feature_

* `git checkout main` 
* `git pull`
* `git checkout -b feature/<nome-da-sua-funcionalidade>`

### Atualizar _Branch_

* `git checkout main` 
* `git pull`
* `git checkout feature/<nome-da-sua-funcionalidade>`
* `git merge main`

**OBSERVAÇÃO**

Caso haja um **conflito** de _merge_ ao realizar o `git merge main`, corrija antes de realizar o _pull request_. Isso irá poupar tempo dos outros integrantes ao realizar o _**code review**_ do seu _pull request_.

###  Versionar Suas Alterações (Atualizar _branch_ remota em relação a local)

* `git add .`
* `git commit -m"sua mensagem"`
* `git push`


