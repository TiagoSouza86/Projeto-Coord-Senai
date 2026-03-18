<div align="center">

# 📊 Quadro Kanban

</div>
🔴 **To Do** (A Fazer)
  
  -  Criar lógica de Top Student
  -  Desenvolver funções de média para as notas dos alunos 

 🟡 **Doing** (Fazendo)
  -   Criar Requisitos Funcionais (RF) 
  -   Criar Requisitos não Funcionais (RNF)  
  -   Criar Regras de Negocios  

 🟢 **Done** (Concluído)
 -   Criar mapa de Empatia <br>

**Requisitos Funcionais(RF)**
      
- RF01 O sistema deve processar uma lista de tuplas contendo o nome do aluno e as notas

- RF02  O sistema deve calcular a média aritmética das notas de cada aluno.

- RF03 O sistema deve validar se a lista de notas está vazia ou corrompida antes do processamento.

- RF04 O sistema deve identificar quais alunos estão em situação de recuperação.
- RF05 O Sistema deverá retornar os alunos aprovados e Top Student (Maior média).



 **Requisitos Não-Funcionais (RNF)**

- RNF01 O sistema deve tratar erros de dados incompletos para evitar interrupções na execução.

- RNF02   O projeto deve seguir uma estrutura lógica que facilite a manutenção futura.



**Regras de Negocios**

- Atividades: 
 
 1 - O aluno só passa se tiver média 7.0.

 2 - Identificar o aluno Top Student (A maior média)
 
 3 - A estrutura dos nomes e notas deverá esta escrita da seguinte maneira, Lista de Tuplas [("Nome", [notas])].

4 - Verificar se as notas dos alunos estao vazias ou corrompidas.
 