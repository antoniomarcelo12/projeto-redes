

 # - [](#) Instructions: 
 #### (1) Run the DNS server with python3 dns_server.py
 #### (2) Run the UDP/TCP server with python3 [tcp/udp]-server.py
 #### (3) Run the UDP/TCP client with python3 [tcp/udp]-client.py



 # - [](#) Project: 


- [X] (1) O serviço final é livre, mas a arquitetura cliente-servidor é obrigatória e devem
ser desenvolvidas duas versões da aplicação: uma com suporte do TCP e outra
utilizando UDP;
-   (a) Como o serviço a ser proposto é livre, recomenda-se elaborar uma
    aplicação cliente-servidor simples, como:
- - [X] (i) Calculadora Remota;
- -   (ii) Sistema de busca (restaurantes, pontos turísticos, jogos digitais)
- -    (iii) Cálculo de notas (Cadastro de alunos, retorno de notas,
- -    armazenamento de condição {Reprovado, Aprovado});
- -    (iv) Sistema de tarefas a serem realizadas;
- -    (v) Entre outros.

- [X] (2) Utilize primeiro um dos protocolos (TCP ou UDP) para construir toda a
aplicação. Uma vez que funcione com o primeiro protocolo, adapte a sua
aplicação para funcionar corretamente com o segundo protocolo.

- [ ] (3) Ambas as versões (TCP e UDP) devem estar funcionando simultaneamente: os
quatro processos (um par TCP e outro par UDP) devem estar ativos ao mesmo
tempo.
- - [X] (a) Executar os processos em terminais distintos;
- - [X] (b) Ambas as aplicações, ao serem inicializadas, devem ser registradas no
    servidor de nomes e disponíveis para os clientes;
- - [X] (c) Não há a necessidade de implementar um sistema DNS completo.
    Desenvolva o mínimo para que o cliente obtenha as informações
    necessárias sobre o processo servidor da aplicação em questão.
- - [X] (d) Uma vez que ambas as versões (TCP e UDP) estejam disponíveis, os
    clientes podem iniciar suas requisições;
- - [ ] (e) Quando as aplicações forem encerradas, suas informações devem ser
    removidas do servidor de nomes;

- [X] (4) Tente criar um diagrama de Fluxo ou UML para melhor visualização do
funcionamento do projeto.

- [X] (5) Obtenha todos os pacotes (entre o servidor de nomes e os servidores, entre o
cliente e o servidor, entre o servidor de nomes e o cliente) em uma única captura
Wireshark.

- [X] (6) Note que, a captura do tempo de envio e recebimento está atrelada à análise de
desempenho da camada de transporte, então só deve ser capturado o tempo dos
pacotes da aplicação cliente-servidor;
- - [X] (a) Utilize o código-fonte para cronometrar o tempo entre a solicitação do
    cliente e o recebimento da resposta:
- - - [X] (i) Quando o cliente enviar o pacote, deve-se armazenar o tempo
    inicial (utilize uma variável para isso, por meio de bibliotecas que
    capturam o tempo de execução do código);
- - - [X] (ii) Quando o cliente receber a resposta final, o tempo será armazenado
    (repita o processo da etapa anterior por meio de variáveis).
- - - [X] (iii) Vale ressaltar que o tempo a ser salvo deve ser a diferença entre o
    tempo final (ii) e o tempo inicial (i):
    - - - [X] (1) Utilize arquivos de texto para armazenar os tempos e poder
        plotá-los, facilitando as análises comparativas;
- - - [X] (iv) Para evitar interferências nos resultados, sua aplicação não pode
    receber valores via input da linha de comando. Portanto, deixe as
    solicitações pré-determinadas via código (utilização de listas,
    mapas ou variáveis);

## Entregas

- [X] (1) Deve ser elaborado um relatório explicando o serviço desenvolvido, a captura do
Wireshark e a análise comparativa entre os tempos capturados utilizando cada
protocolo da camada de transporte (UDP e TCP);
- [X] (a) Para se ter uma análise comparativa válida, faça com que o cliente solicite
    5 requisições ao servidor;
    - [X] (i) Vale ressaltar que o tempo a ser utilizado é aquele desde a
        solicitação até o recebimento da resposta, ou seja, existirão 5
        tempos totais, um para cada requisição.

- [X] (2) Os códigos devem ser armazenados no Github, assim como as capturas feitas via
Wireshark, e o link deve constar no relatório:
- [X] (a) Criar um README contendo as informações de como executar os
    códigos;
- [X] (b) Lembre-se de criar um repositório público.

- [X] (3) O Relatório com os prints das capturas do Wireshark deve ser anexado nesta
atividade do Classroom, com identificação da dupla e enviado apenas por um
membro da equipe que realizou a atividade.