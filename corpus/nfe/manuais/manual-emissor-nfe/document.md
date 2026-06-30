---
title: "Emissor de Nota Fiscal Eletrônica"
slug: "manual-emissor-nfe"
category: "manual"
source_family: "portal_nacional_nfe"
original_sha256: "12b707c1c8b2de2a70699a64186f2709b2253e87f986242b571b1547cf534762"
converted_at_utc: "2026-06-25T15:08:56.120829+00:00"
status: "published"
type: "manual"
---
![Image](assets/image_000000_02abc7e384e65d1e7abe2ca0411d762b80b701462c2846d54f4d2d004c597ad7.png)

## Emissor de Nota Fiscal Eletrônica

Novembro de 2007

Equipe Nota Fiscal Eletrônica Secretaria da Fazenda do Estado de São Paulo

## Índice

| I - Instalação do Software Emissor NF-e...........................................................................................................         |   3 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| II - Software Emissor NF-e - primeiros passos ................................................................................................             |   3 |
| III - Cadastrando um Emitente..........................................................................................................................    |   5 |
| IV - NF-e: Situações, tipos e seqüência de emissão........................................................................................                 |   7 |
| IV.1 - Situações da NF-e...........................................................................................................................        |   7 |
| IV.2 - Outras situações para a NF-e.........................................................................................................               |   8 |
| IV.3 - Tipos de NF-e..................................................................................................................................     |   8 |
| IV.4 - Seqüência para a emissão de uma NF-e - fluxo normal.................................................................                                |   9 |
| IV.5 - Seqüência para a emissão de uma NF-e - contingência ...............................................................                                 |   9 |
| V - Gerenciamento das Notas Fiscais eletrônicas (NF-e).................................................................................                    |   9 |
| V.1 - Gerando uma Nova NF-e...............................................................................................................                 |  10 |
| V.3 - Validando uma NF-e ......................................................................................................................            |  11 |
| V.4 - Assinando uma NF-e......................................................................................................................             |  11 |
| V.5 - Transmitindo uma Nova NF-e........................................................................................................                   |  12 |
| V.6 - Busca pelos retornos na SEFAZ....................................................................................................                    |  13 |
| V.7 - Imprimindo o DANF-e.....................................................................................................................             |  14 |
| V.8 - Cancelando uma NF-e ...................................................................................................................              |  14 |
| V.9 - Excluindo uma NF-e.......................................................................................................................            |  15 |
| V.10 - Outras Funções............................................................................................................................          |  16 |
| VI - Cadastro de Clientes................................................................................................................................. |  18 |
| VI.1 - Pesquisa de clientes cadastrados.................................................................................................                   |  18 |
| VI.2 - Inclusão de novo cliente................................................................................................................            |  18 |
| VI.3 - Exclusão de cliente cadastrado ....................................................................................................                 |  19 |
| VII - Importação e exportação de dados.........................................................................................................            |  19 |
| VII.1 - Importação de Dados...................................................................................................................             |  19 |
| VII.2 - Exportação de Dados...................................................................................................................             |  20 |
| VIII - Funções de sistema................................................................................................................................  |  23 |
| VIII.1 - Avisos..........................................................................................................................................  |  23 |
| VIII.2 - Parâmetros do sistema ...............................................................................................................             |  23 |
| VIII.3 - Relatório Gerencial......................................................................................................................         |  24 |
| VIII.4 - Backup e Restauração dos dados ..............................................................................................                     |  25 |
| IX - Atualizações automáticas .........................................................................................................................    |  25 |

## I - Instalação do Software Emissor NF-e

## Instalação

2. Caso não tenha a versão Java adequada, a página retornará uma mensagem informativa:
1. Ao entrar na página para instalação do Software Emissor de NF-e, será verificado se o computador está com a versão Java adequada para a instalação.

Para executar o NF-e corretamente você precisa da versão 1,6,0 ou mais recente do Java JRE. Clique aqui para atualizar o Java JRE.

3. Caso a versão do Java esteja adequada ao Software, pular para o passo 8

## Caso seja necessário instalar o Java:

4. Clicar no link indicado (aqui)
6. Caso a página não apareça ou for informado que não é possível realizar o download , clicar no link abaixo para a realização do download Manual do Java: http://www.java.com/pt\_BR/download/manual.jsp. Verifique qual o Sistema Operacional da máquina (Windows, Linux, etc) e realize o download, seguindo as instruções apresentadas. Seguir  as  instruções  de  instalação  contidas  na  página.  Após  a  instalação  do  Java  (ou  a  sua atualização), voltar para a página inicial de instalação e ir ao passo 8.
5. O usuário será redirecionado para a página de download da versão Java necessária.

## Caso a versão Java esteja adequada ou após a instalação/atualização do Java:

7. Caso a versão Java instalada seja a correta, a página retornará uma mensagem informativa: Java 1,6,0,2 instalado. Clique aqui para instalar/executar o NF-e. Clique aqui para atualizar o Java JRE.
9. O aplicativo  iniciará  o  download  e  ao  final  do  download,  instalará  e  executará  o  Software.  Se  a mensagem  de Warning-Secutiry for  apresentada  ( The  application's  digital  signature  cannot  be verified. Do you want to run the application? ), clicar em Run Após o final do download, o software será instalado e executado. Na instalação, será criado o ícone do Software Emissor NF-e na área de trabalho , e o usuário já estará apto a utilizar o aplicativo.
8. Clicar no link indicado (aqui)

## Requisitos de Sistema

Memória RAM: 256 Megabytes ou superior (512 Megabytes recomendado)

Espaço em disco: 98 Megabytes (Java - JRE 6) + 30 Megabytes (Software Emissor NF-e).

Processador: Pentium III ou AMD K6 450

## Observações Importantes

Megahertz ou superior;

Após  a  instalação,  o  aplicativo  irá  criar  o  diretório database na  raiz  do  disco  (Caso  do  Windows  com configuração padrão, C:\database .  Caso do Linux, na raiz, \database\ ). Este diretório conterá os dados do Software e NÃO poderá ser apagado ou modificado. Caso apagado, o Software gerará um novo diretório database , mas os dados anteriores serão perdidos.

## II - Software Emissor NF-e - primeiros passos

O Software Emissor NF-e é um programa que, depois de instalado na máquina do contribuinte, permite a emissão  de  Notas  Fiscais  eletrônicas  (NF-e)  para  a  correspondente  Secretaria  de  Fazenda  Estadual (SEFAZ).

O Software compreende a geração do arquivo da Nota Fiscal eletrônica, meios para realizar a assinatura com  o  Certificado  Digital  que  o  contribuinte  possuir  e  a  sua  transmissão para  a  SEFAZ  relacionada. Também permite o gerenciamento das NF-e's e o cancelamento das mesmas, a impressão do Documento Auxiliar  da  Nota  Fiscal  eletrônica  (DANF-e)  para  a  circulação  das  mercadorias  e  outras  funcionalidades acessórias para facilitar a criação da NF-e, tais como os cadastros de clientes, produtos e transportadoras.

## Premissas

-  O  usuário  do  Software  Emissor  NF-e  deve  ser  um  emitente  de  Notas  Fiscais  modelos  1  ou  1A  e devidamente  cadastrado  e  autorizado  na  SEFAZ  correspondente  a  realizar  a  emissão  de  NF-e's.  Para maiores informações, entrar em contato com a SEFAZ de seu Estado.

-  Ser  compatível  com  a  maioria  dos  Sistemas  Operacionais  existentes  no  mercado,  com  preferência  ao Sistema Operacional Windows e Linux.

- distribuição gratuita deste Software para a emissão de Notas Fiscais Eletrônicas em substituição às notas fiscais modelos 1 e 1A.

## Iniciando o Software

Para iniciar o programa, clique duas vezes no ícone do Software Emissor NF-e.

Observação: O aplicativo não pode ser executado mais de uma vez (ou seja, não é permitida a execução simultânea de várias instâncias do programa)

## Primeiro Acesso

Caso seja o primeiro acesso ao Software, ou caso ainda não existam Emitentes cadastrados, o programa, ao ser aberto, exibirá a mensagem de boas-vindas e solicitará o cadastramento do(s) emitente(s) emissores de NF-e e exibirá a tela de seleção e cadastramento de Emitentes.

## Próximos Passos

Após  o  cadastramento  de  um  emitente  e  a  seleção  do mesmo,  o  Software  liberará  as  demais funcionalidades da NF-e: geração, gerenciamento, inutilização, entre outros.

No próximo acesso, o programa exibirá todos os emitentes cadastrados na tela de Início do Software para a seleção do emitente que realizará a emissão das NF-e's.

## Menus

## 1. Notas Fiscais

Emitir Nova Nota (Disponível apenas após a seleção de um emitente)

Abre a tela para criação e emissão de uma Nova Nota Fiscal eletrônica.

Gerenciar Notas (Disponível apenas após a seleção de um emitente)

Abre a tela de gerenciamento de Notas Fiscais eletrônicas.

Consultar pendências na SEFAZ (Disponível apenas após a seleção de um emitente)

Abre  a  tela  de  aviso  de  pendências  do  emitente  relacionado  à  Secretaria  da  Fazenda  ao  qual  está vinculado.

Inutilizar Faixa de Numeração (Disponível apenas após a seleção de um emitente)

Abre a tela de gerenciamento das inutilizações de faixa de numeração  de NF-e do emitente.

Consultar NF-e não cadastrada no Software (Disponível apenas após a seleção de um emitente)

Abre a tela para a consulta de uma NF-e na Secretaria da Fazenda vinculada ao emitente mas não presente no Software.

Cancelar NF-e não cadastrada no Software (Disponível apenas após a seleção de um emitente)

Abre a tela para o cancelamento de uma NF-e somente pela Chave de Acesso e o número de protocolo de autorização da NF-e. Operação permitida somente para as NF-e's que não estão cadastradas no Software;

## Sair

Encerra o programa.

## 2. Emitente

Dados do Emitente Atual (Disponível apenas após a seleção de um emitente)

Abre a tela de cadastro de dados do emitente atual.

## Selecionar Emitente

Abre a tela para a seleção de outro emitente.

## Sair do Emitente Atual

Opção para sair do emitente atual, mas o Software continua ativo.

## 3. Cadastros

Cliente (Disponível apenas após a seleção de um emitente)

Abre a tela de cadastro e listagem de dados dos clientes do emitente.

Produto (Disponível apenas após a seleção de um emitente)

Abre a tela de cadastro e listagem de dados dos produtos do emitente.

Transportadora (Disponível apenas após a seleção de um emitente)

Abre a tela de cadastro e listagem de dados das transportadoras do emitente.

## 4. Sistema

## Avisos

Abre a tela de avisos

## Parâmetros

Abre a tela de parâmetros do sistema, válido para todo o Software Emissor.

## Importar

Abre a tela de importação de dados para o Software Emissor NF-e.

## Backup

Abre a tela para a realização do backup de todos os dados do sistema.

## Restore

Abre  a  tela  para  a  realização  da  restauração  de  todos  os  dados  do  sistema  do  arquivo  de backup feito previamente.

## Relatório Gerencial

Abre a tela de geração do relatório gerencial do emitente.

## 5. Ajuda

## Conteúdo da Ajuda

Exibe os conteúdos da ajuda do Software Emissor.

## Sobre

Exibe uma janela com informações sobre o Software Emissor, incluindo a versão atual.

## III - Cadastrando um Emitente

A opção de Emitente é o primeiro passo para a utilização do aplicativo, pois  é nele que é cadastrado  o emitente da Nota Fiscal eletrônica.

Os  dados  cadastrados  do  emitente  são  utilizados  na  geração  da  Nota  Fiscal  eletrônica  e  identificam  o estabelecimento.

Para  habilitar  as  funcionalidades  da  Nota  Fiscal  eletrônica,  um  emitente  deverá  ser  cadastrado  e devidamente iniciado.

O cadastro de emitentes permite a inserção, alteração e exclusão e pesquisa dos emitentes cadastrados.

Acesso pelo Menu: Emitente -&gt; Selecionar Emitente

## Opções:

## 1 - Iniciando um Emitente

1. Ir para a tela de Cadastro de Emitente

Opção para iniciar um Emitente para habilitar as demais funcionalidades da NF-e.

2. Selecionar o emitente que deseja iniciar
4. Os dados do Emitente (Razão Social, CNPJ e IE) serão carregados e exibidos na barra superior do Software, confirmando que o Emitente foi iniciado com sucesso.
3. Clicar em Iniciar

## Opção para seleção de outro emitente, se necessário

2. Para a seleção de outro emitente, acessar no menu Emitente -&gt; Selecionar Emitente .  Esta opção irá sair do emitente iniciado, caso haja algum iniciado.
1. Apenas para sair do emitente iniciado, acessar no menu Emitente -&gt; Sair do Emitente Atual . Os dados do emitente (Razão social, CNPJ e IE) não serão mais exibidos na barra superior de informações, indicando que não há emitente selecionado.
3. Na tela de pesquisa e seleção de emitente, buscar e selecionar o emitente a ser iniciado.
4. Após a seleção do emitente a ser iniciado, clicar em Iniciar.

Quando o emitente não está iniciado, a barra superior não apresentará nenhum dado.

## Filtro de Pesquisa de Emitente

| CNPJ/CPF           | Preenchimento de até 14 dígitos; A pesquisa retornará todos os emitentes cujo CNPJ ou CPF inicie com o número digitado              |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Inscrição Estadual | Preenchimento de até 14 dígitos; A pesquisa retornará todos os emitentes cuja IE inicie com o número digitado                       |
| Nome/Razão Social  | Preenchimento de até 60 caracteres; A pesquisa retornará todos os emitentes cujo Nome ou Razão Social contenha a expressão digitada |

## Observações:

1. Os campos do filtro de pesquisa somam-se na busca: caso seja preenchido o campo CNPJ/CPF e o campo Inscrição Estadual ,  a  busca utilizará  os  dois  campos  para  realizar  a  pesquisa; caso  seja preenchido o campo CNPJ/CPF ,  o  campo Inscrição Estadual e o campo Nome/Razão Social ,  a busca utilizará os três campos para realizar a pesquisa
2. Caso  não  sejam preenchidos dados  nos campos  do  filtro, a pesquisa  retornará  TODOS os emitentes cadastrados

## Resultados da pesquisa

Após a pesquisa, os emitentes encontrados são apresentados em uma lista.

Caso  seja  clicado  o  título  da  coluna,  a  listagem  será  ordenada  em  ordem  crescente  de  acordo  com  a coluna. Caso seja clicada novamente, será ordenada em ordem inversa.

## 2 - Inclusão de novo emitente

2. Na tela de cadastro de emitente, acessar a opção Incluir
1. Acessar  a  tela  de  cadastro  de  emitente  através  do  menu Emitente  -&gt;  Selecionar  Emitente ou através da tela inicial na abertura do aplicativo
3. Na tela de Inclusão de emitente, preencher corretamente os campos do emitente
4. Após o preenchimento dos campos corretamente, selecionar a opção Incluir

## 3 - Detalhamento/Edição de cliente cadastrado

Existem duas formas para o detalhamento/edição de emitente:

## a) Caso o emitente já foi iniciado

1. Acessar o menu: Emitente -&gt; Dados do Emitente Atual

2. Serão exibidos os dados do emitente atual, com a opção de realizar a Edição Selecionar a opção Editar para a edição dos campos do emitente
3. Após finalizar a edição dos campos, clicar em Alterar para salvar as modificações

## b) Pela tela de cadastro de emitente

2. Realizar a pesquisa pelo emitente cadastrado que será editado
1. Acessar  a  tela  de  cadastro  de  emitente  através  do  menu Emitente  -&gt;  Selecionar  Emitente ou através da tela inicial na abertura do aplicativo
3. Selecionar o emitente a ser editado;
4. Após a seleção do emitente, a opção de Detalhar ficará disponível. Selecionar a opção Detalhar
5. A  tela  de  detalhamento  com  os  dados  do  emitente  selecionado  será  apresentada.  Selecionar  a opção Editar para a edição dos campos do emitente
6. Após finalizar a edição dos campos, clicar em Alterar para salvar as modificações

## 4 - Exclusão de emitente cadastrado

IMPORTANTE :  A  exclusão  do  emitente  acarreta  na  exclusão  de  TODOS  os  dados  vinculados  àquele emitente (NF-e's, cadastros, etc).

2. Realizar a pesquisa pelo(s) emitente(s) cadastrado(s) que será(ão) excluído(s);
1. Acessar  a  tela  de  cadastro  de  emitente  através  do  menu Emitente  -&gt;  Selecionar  Emitente ou através da tela inicial na abertura do aplicativo
3. Selecionar o(s) emitente(s) a ser(em) excluído(s);
4. Selecionar a opção Excluir
5. Confirmar a exclusão

Ao excluir, deve-se confirmar a remoção do emitente.

## IV - NF-e: Situações, tipos e seqüência de emissão

## IV.1 - Situações da NF-e

Durante a emissão de uma Nota Fiscal eletrônica, esta passa por diversas situações até ser autorizada pela Secretaria de Fazenda Estadual. Em resumo a NF-e assume as seguintes situações até a sua autorização:

## 1. Em Digitação

A NF-e que acaba de ser criada e ainda não completamente finalizada com os dados. Pode ser editada a qualquer hora.

## 2. Validada

Caso a NF-e seja editada, esta deverá passar novamente pelo processo de validação.

Apenas  após  a  inserção  de  todas  as  informações  necessárias  da  NF-e  e  a  realização  da  operação  de Validação  a  NF-e  ficará  com  a  situação  'Validada'.  Nesta  situação,  a  NF-e  encontra-se  corretamente preenchida com relação à estrutura de dados.

IMPORTANTE: O processo de validação da estrutura das informações NÃO garante a consistência tributária dos dados.

## 3. Assinada

É a situação ao qual a NF-e está após ser assinada digitalmente com o Certificado Digital do contribuinte emissor. Ainda é possível a edição desta NF-e, mas esta voltará para a situação "Em Digitação", perdendo a assinatura e sendo necessário realizar novamente os processos de Validação e Assinatura.

## 4. Em Processamento na SEFAZ

Após a transmissão da NF-e para a SEFAZ correspondente, a NF-e ganhará a situação "Em processamento na  SEFAZ".  Neste  estágio,  a  NF-e  estará  na  fila   para  ser  processada  na  SEFAZ,  tendo  o  usuário  que aguardar até que a SEFAZ recepcione e autorize a respectiva NF-e. Durante este momento, o Software fará a busca das autorizações das NF-e's enviadas, informando quando a NF-e for autorizada.

## 5. Autorizada

É o estágio na qual a NF-e foi recepcionada e autorizada pela SEFAZ, podendo o contribuinte realizar a impressão do DANF-e e a circulação da mercadoria. A NF-e já apresenta validade jurídica, e os dados nela contidos são de responsabilidade do contribuinte emissor.

## IV.2 - Outras situações para a NF-e

Além das situações da NF-e até ser autorizada pela SEFAZ, a NF-e poderá encontrar-se em outros estágios diferentes do ciclo básico da autorização. São eles:

## 1. Cancelada

Após  ser  autorizada  pela  SEFAZ,  o  contribuinte  poderá  solicitar  o cancelamento  da  NF-e,  caso  haja necessidade. Neste caso, o contribuinte deverá também justificar o pedido de cancelamento.

Depois de enviada a solicitação de cancelamento, e esta sendo homologada pela SEFAZ, a NF-e mudará de  situação  para  Cancelada,  não  sendo  possível  mais  a  sua  utilização  ou  a  impressão  do  respectivo DANFE.

## IMPORTANTE: A exclusão da NF-e pelo sistema (opção Excluir NF-e) não implica no cancelamento da NF-e na SEFAZ.

## 2. Denegada

Condição que  ocorre  quando  a  NF-e  é  enviada  para  a  SEFAZ  e  durante  o  processamento  da  nota  no sistema  da Fazenda  verifica-se que o  emitente está  em  situação  de  pendência  perante  o  Fisco. Neste caso, não será permitida a impressão do DANF-e e nem tão pouco o seu cancelamento.

## 3. Rejeitada

Após  o  envio  e  processamento da  NF-e  na  SEFAZ,  o  arquivo  poderá  ser  rejeitado  caso  haja  alguma pendência  ou  problema  com  a  NF-e.  Neste  caso,  o  sistema  da  SEFAZ  não  autorizará  a  NF-e, disponibilizando o motivo da rejeição.

Neste caso, após verificar a pendência ocorrida, o usuário poderá novamente editar a NF-e (a voltará para a situação 'Em Digitação') para realizar a  correção e,  após a  validação  e a assinatura, retransmitir  para  a SEFAZ.

## 4. Com problemas na transmissão / Em pendência de retorno

Caso especial de NF-e. Ocorre quando houve algum problema com a transmissão da NF-e para a SEFAZ (ou  seja,  não  é  conhecido  se  a  NF-e  foi  enviada  com  sucesso  para  a  SEFAZ)  ou  quando  houve  algum problema com a busca pelo retorno de autorizações da SEFAZ.

Nestes  casos,  o  Software  irá  realizar  a  busca  das  autorizações  destas  NF-e's  na  SEFAZ.  Caso  a  NF-e encontre-se  autorizada  na  SEFAZ,  o  Software  irá  automaticamente  mudar  a  situação  da  NF-e  para Autorizada.

## IV.3 - Tipos de NF-e

Existem dois tipos de NF-e:

1. Normal :  é  o  tipo  padrão  de  NF-e,  enviado  quando  não  existem  problemas  com  a  conexão  entre  o Software contribuinte e a SEFAZ.

2. Em contingência : tipo que deve ser emitida apenas  em casos de problemas de comunicação entre o Software  contribuinte  e  a  SEFAZ.  Recomenda-se  a  utilização  somente  em  último  caso.  A  NF-e  em contingência implica na impressão do DANF-e em formulário de segurança.

## IV.4 - Seqüência para a emissão de uma NF-e - fluxo normal

Seguindo os conceitos do Software sobre a NF-e, o usuário deverá, para emitir uma NF-e:

1. Criar uma nova NF-e ou importar uma NF-e.
3. Assinar a NF-e
2. Validar a estrutura do documento
4. Transmitir a NF-e para a SEFAZ utilizando o certificado digital
5. Aguardar o processamento da NF-e na SEFAZ. O Software irá informar quando concluir a busca pelos retornos da SEFAZ.
6. Após a autorização da NF-e, imprimir o DANFE para permitir a circulação da mercadoria.

## IV.5 - Seqüência para a emissão de uma NF-e - contingência

Seguindo os conceitos do Software sobre a NF-e, o usuário deverá, para emitir uma NF-e em contingência:

2. Validar a estrutura do documento
1. Criar uma nova NF-e, editar uma NF-e ou importar uma NF-e, colocando a forma de emissão como Contingência
3. Assinar a NF-e
5. Posteriormente, transmitir a NF-e para a SEFAZ utilizando o certificado digital
4. Imprimir o DANFE em formulário de segurança para permitir a circulação da mercadoria.
6. Aguardar o processamento da NF-e na SEFAZ. O Software irá informar quando concluir a busca pelos retornos da SEFAZ.

## V - Gerenciamento das Notas Fiscais eletrônicas (NF-e)

Esta opção permite ao usuário a pesquisa e a realização de operações sobre suas NF-e's. Através do filtro de pesquisa, é possível a seleção das NF-e's desejadas.

Pré-condição : Um emitente deverá estar previamente iniciado.

1. Acessar o menu: Notas Fiscais -&gt; Gerenciar Notas
2. Na tela de pesquisa de NF-e's, preencher com o filtro de pesquisa de NF-e desejado.
4. Para realizar uma nova pesquisa, clicar em Nova Pesquisa
3. Clicar em Pesquisar

| Período                  | Preenchimento com uma data inicial e final; A pesquisa retornará todas as NF-e's cuja data de emissão esteja compreendida no intervalo de tempo informado                                                                                                                                                                                                                                          |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tipo de NF-e             | Seleção de qual o tipo de NF-e:"Normal", "Contingência" ou "Todos" A pesquisa retornará todas as NF-e's cujo tipo é igual ao selecionado. Caso informe "Todos", a pesquisa retornará incluirá "Normal" e em "Contingência"                                                                                                                                                                         |
| Situação da NF-e         | Seleção entre uma das 9 situações da NF-e no Software Emissor NF-e ou "Todas": "Em Digitação", "Validada", "Assinada", "Em processamento na SEFAZ", "Autorizada", "Denegada", "Cancelada", "Rejeitada", "Com problemas na transmissão/com pendência". A pesquisa retornará todas as NF-e's cuja situação é igual a informada no filtro. Caso deseje retornar todas as situações, informar "Todas". |
| Série                    | Preenchimento com a série de até 3 dígitos. A pesquisa retornará todas as NF-e's da série informada.                                                                                                                                                                                                                                                                                               |
| Número                   | Preenchimento com os números inicial e final de até 9 dígitos. A pesquisa retornará todas as NF-e's compreendidas entre os números informados.                                                                                                                                                                                                                                                     |
| CNPJ/CPF do Destinatário | Preenchimento de até 14 dígitos. A pesquisa retornará todas as NF-e's cujo CPF ou CNPJ do destinatário inicie com o número digitado.                                                                                                                                                                                                                                                               |
| UF Destinatário          | Seleção da UF do destinatário.                                                                                                                                                                                                                                                                                                                                                                     |

|                         | A pesquisa retornará todas as NF-e's cuja UF destinatário seja igual ao informado. Selecionar a opção "Todos" para considerar todas as UFs.   |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Chave de Acesso da NF-e | Preenchimento de 44 dígitos da Chave de Acesso da NF-e. A pesquisa retornará a NF-e cuja Chave de Acesso seja igual ao informado.             |
| Com DANFE impresso      | Caso selecionado, a pesquisa retornará apenas as NF-e's cujo DANFE foi impresso.                                                              |

## Observações:

2. Caso não sejam preenchidos dados nos campos do filtro, a pesquisa retornará TODAS as NF-e's cadastradas do emitente atual
1. Os campos do filtro de pesquisa somam-se na busca: caso seja preenchido o campo Período e o campo Série,  a  busca utilizará  os  dois  campos  para  realizar  a  pesquisa; caso  seja  preenchido  o campo Período , o campo Série e o campo Número , a busca utilizará os três campos para realizar a pesquisa e assim por diante com TODOS os campos do filtro.

## Resultados da pesquisa

Após  a  pesquisa,  as  NF-e's  encontradas  são  apresentadas  em  uma  lista,  conforme  imagem  abaixo. Caso  seja  clicado  o  título  da  coluna,  a  listagem  será  ordenada  em  ordem  crescente  de  acordo  com  a coluna. Caso seja clicada novamente, será ordenada em ordem inversa.

## Operações pelo Gerenciamento

Com a listagem das NF-e's apresentadas, as seguintes operações são possíveis:

- Detalhar e Editar: Apresenta o detalhamento das informações da NF-e selecionada. Apenas UMA NF-e deve ser selecionada para que esta opção torne-se disponível
- Validar:  Realiza  o  processo  de  validação  das  NF-e's  EM  DIGITAÇÃO  selecionadas.  Caso  não  seja possível a validação, uma mensagem será gerada.
- Assinar:  Realiza  o  processo  de  assinatura  das  NF-e's  VALIDADAS  selecionadas.  Caso  não  seja possível a assinatura, uma mensagem será gerada.
- Transmitir: Realiza o processo de transmissão das NF-e's ASSINADAS selecionadas. Caso não seja possível a transmissão, uma mensagem será gerada.
- Imprimir DANFE: Gera o DANFE das NF-e's AUTORIZADAS ou das NF-e's ASSINADAS do tipo EM CONTINGÊNCIA. Apenas para as NF-e's citadas anteriormente esta opção fica disponível.
- Consulta Situação na SEFAZ:Realizar a consulta da situação da NF-e ASSINADA ou AUTORIZADA na SEFAZ correspondente, atualizando para a nova situação caso necessário.
- Exportar...: Exportação das NF-e's selecionadas.
- Cancelar NF-e: Realiza o cancelamento das NF-e's AUTORIZADAS selecionadas.
- Excluir: Remove a NF-e da base local do Software. NÃO EXCLUI A NF-E AUTORIZADA, CANCELADA OU DENEGADA DA BASE DA SEFAZ.

## V.1 - Gerando uma Nova NF-e

Opção de gerar uma nova Nota Fiscal eletrônica do Emitente atual.

Pré-condição : Um emitente deverá estar previamente iniciado.

1. Acessar o menu: Notais Fiscais -&gt; Emitir Nova Nota
2. Na tela de Inclusão de uma nova Nota Fiscal eletrônica, preencher corretamente os campos da NFe
3. A qualquer momento, o usuário poderá selecionar a opção Salvar para armazenar as informações da NF-e, sem precisar realizar o preenchimento de todos os campos obrigatórios. (*)
4. (*)  Observação: Os campos mínimos a serem preenchidos  para selecionar a opção Salvar são: a Série, o Número da NF-e e a Data de Emissão da nota.

Ao clicar em Salvar, a NF-e será armazenada no Software Emissor para posterior edição.

## V.2 - Detalhes/Editando uma NF-e

Opção para apresentar os detalhes da Nota Fiscal eletrônica e também permitir a sua edição.

Pré-condição : Um emitente deverá estar previamente iniciado.

2. Realizar a pesquisa pela Nota a ser editada.
1. Acessar o menu: Notas Fiscais -&gt; Gerenciar Notas
3. Selecionar a nota clicar em Detalhar para apresentar os dados da NF-e
4. Para  a  edição,  clicar  em Editar .  Após  realizar  as  alterações  necessárias,  clicar  em Alterar para salvar as alterações.

Observação 1: somente notas de situação em digitação, validada, assinada (sendo o tipo normal ou sendo  do  tipo  assinada  sem  o  DANFE  impresso)  ou  rejeitada  poderão  ser  editadas.  Nas  demais situações, não é permitida a edição, somente o detalhamento.

Observação  2:  caso  a  NF-e  a  ser  editada  está  em  situação  diferente  de  em  digitação,  o  software emissor irá requerer a confirmação para que a nota volte para a situação em digitação. Notas em digitação deverão passar novamente pelo processo normal de validação, assinatura e transmissão.

Caso a NF-e estiver em situação diferente de "Em Digitação", o Software solicitará a confirmação.

## V.3 - Validando uma NF-e

Esta validação verificará se a NF-e tem todos os seus campos obrigatórios preenchidos e se o formato dos mesmos estão em acordo com a estrutura definida no Manual de Integração do Contribuinte.

No  processo  de  validação,  caso  a  verificação  ocorra  com  sucesso,  o  Software  irá  salvar  a  nota automaticamente.

IMPORTANTE: A VALIDAÇÃO DA NF-e NÃO ABRANGE A CONSISTÊNCIA DOS DADOS INFORMADOS, SENDO ESTES DE EXCLUSIVA RESPONSABILIDADE DO EMITENTE.

## Pré-condição :

-  Deve(m)  ser  selecionado(s)   NF-e('s)  em  situação  igual  a  "Em  Digitação"  ou  uma  NF-e  em  criação que ainda não foi salva.
- Um emitente deverá estar previamente iniciado;

Existem duas formas para a realização da validação:

## 1ª) Pela tela de Inclusão/Edição da NF-e:

2. Caso não haja pendências no preenchimento da nota, esta passará para a situação "Validada". O Software gerará a Chave de Acesso da NF-e, que será  o identificador da NF-e nas consultas no site da SEFAZ. Caso haja pendências, o Software informará quais foram os problemas encontrados.
1. Na tela de inclusão ou edição de NF-e, acessar a opção Validar

Caso haja pendências, o Software irá informar os dados faltantes.

## 2ª) Pela tela de Gerenciamento de NF-e's:

2. Realizar a pesquisa pela(s) nota(s) com situação "Em Digitação" que será(ão) validada(s)
1. Acessar o menu: Notas Fiscais -&gt; Gerenciar Notas
3. Selecionar a(s) nota(s) a ser(em) validadas e clicar em Validar
4. Caso  não  haja  pendências  no  preenchimento  da(s)  nota(s),  esta(s)  passará(ão)  para  a  situação "Validada". O Software gerará a Chave de Acesso da NF-e de cada uma, que será  o identificador da NF-e nas consultas no site da SEFAZ. Caso haja pendências, o Software alertará quais NF-e's não  foram  possíveis  de  validação.  Para  maiores  detalhes,  realizar  o  detalhamento  da  NF-e  com pendência e verificá-la.

## V.4 - Assinando uma NF-e

A assinatura é parte integrante do processo de emissão, garantindo a integridade e autoria da Nota Fiscal eletrônica. Para realizar a assinatura é necessário possuir um Certificado Digital ICP-Brasil válido, contendo o CNPJ do emissor.

## Pré-condição :

- Um emitente deverá estar previamente iniciado.
- Deve(m) ser selecionado(s) NF-e('s) em situação igual a "Validada"
- Deve-se possuir um Certificado Digital ICP-Brasil válido para o Projeto Nota Fiscal eletrônica

Existem duas formas para a realização da assinatura:

## 1ª) Pela tela de Detalhamento/Edição da NF-e:

2. Na  janela de  seleção  de  Certificado  Digital, escolher  o Arquivo (para  Certificado tipo A1), informando a senha, ou Repositório (para Certificado tipo A3)
1. Na tela de detalhamento/edição de NF-e, acessar a opção Assinar
3. Após a seleção, clicar em Selecionar.
4. Caso não haja problemas com o certificado, a nota será assinada, ficando com a situação igual a "Assinada" e pronta para ser transmitida para a SEFAZ correspondente.

## 2ª) Pela tela de Gerenciamento de NF-e's:

2. Realizar a pesquisa pela(s) nota(s) com situação "Validada" que será(ão) assinada(s)
1. Acessar o menu: Notas Fiscais -&gt; Gerenciar Notas
3. Selecionar a(s) nota(s) a ser(em) assinada(s) e clicar em Assinar
5. Após a seleção, clicar em Selecionar.
4. Na  janela de  seleção  de  Certificado  Digital, escolher  o Arquivo (para  Certificado tipo A1), informando a senha, ou Repositório (para Certificado tipo A3)
6. Caso não haja problemas com o certificado, a nota será assinada, ficando com a situação igual a "Assinada" e pronta para ser transmitida para a SEFAZ correspondente.

## V.5 - Transmitindo uma Nova NF-e

A  transmissão  da  NF-e  é  o  processo  de  envio  do  documento  eletrônico  para  a  SEFAZ  correspondente. Após esta transmissão da NF-e entrará em uma fila de processamento na SEFAZ, e esta enviará para o Software  Emissor  um  recibo,  sendo  parte  integrante  do  processo  de  emissão  de  notas, garantindo  a integridade e autoria da Nota Fiscal eletrônica.

Para realizar a assinatura é necessário possuir um Certificado Digital ICP-Brasil válido, contendo o CNPJ do emissor.

## Pré-condição :

- Um emitente deverá estar previamente iniciado.
- Deve(m) ser selecionado(s) NF-e('s) em situação igual a "Assinada"

Existem duas formas para a realização da transmissão:

- 1ª) Pela tela de Detalhamento/Edição da NF-e: Na tela de detalhamento/edição de NF-e, acessar a opção Transmitir
2. Na  janela de  seleção  de  Certificado  Digital, escolher  o Arquivo (para  Certificado tipo A1), informando a senha, ou Repositório (para Certificado tipo A3)
3. Após a seleção, clicar em Selecionar.
4. O software Emissor NF-e irá realizar a transmissão, exibindo ao final se a NF-e foi enviada para a SEFAZ com sucesso. Caso a NF-e foi recepcionada com sucesso pela SEFAZ, a situação da nota passará a "Em processamento na SEFAZ" e o processo de busca pelo retorno será executado.

## 2ª) Pela tela de Gerenciamento de NF-e's:

2. Realizar a pesquisa pela(s) nota(s) com situação "Assinada" que será(ão) assinada(s)
1. Acessar o menu: Notas Fiscais -&gt; Gerenciar Notas
3. Selecionar a(s) nota(s) a ser(em) assinada(s) e clicar em Transmitir
5. Após a seleção, clicar em Selecionar.
4. Na  janela de  seleção  de  Certificado  Digital, escolher  o Arquivo (para  Certificado tipo A1), informando a senha, ou Repositório (para Certificado tipo A3)
6. O software Emissor NF-e irá realizar a transmissão, exibindo ao final se a NF-e foi enviada para a SEFAZ com sucesso. Caso a NF-e foi recepcionada com sucesso pela SEFAZ, a situação da nota passará a "Em processamento na SEFAZ" e o processo de busca pelo retorno será executado.

## V.6 - Busca pelos retornos na SEFAZ

A busca pelos retornos na SEFAZ é o processo que o Software Emissor executa para pesquisar o resultado do processamento das NF-e's enviadas, verificando se a nota foi autorizada, denegada ou rejeitada pela SEFAZ. A busca pelos retornos é disparada de forma automática pelo Software após qualquer transmissão de NF-e com sucesso para a SEFAZ.

Após o término da busca, um balão informativo aparecerá no system tray para avisar o usuário que a busca foi  concluída.  Também ficará disponível um pequeno ícone na barra de status do  aplicativo.  Clicando  no ícone, o Software irá apresentar o resultado da busca de cada uma das NF-e's.

O software  também  irá  atualizar  a  situação  de  cada  uma  das  NF-e's  buscadas  na  SEFAZ.  Tais  NF-e's poderão ser consultadas pela função de gerenciamento de notas.

Após o término da Busca, o Software informará através de Aviso pelo System Tray (em  caso de uso do Sistema Operacional Windows ) e apresentará o ícone de informações da Busca na barra de status (barra inferior do Software).

## Iniciando a busca de retornos manualmente

Caso existam NF-e's com situação "Em processamento na SEFAZ" ou "Com problemas na transmissão/pendente"  e  a  busca  não  estiver  em  execução  ou  agendada,  o  usuário  poderá  iniciá-la manualmente.

## Pré-condição :

-  Pelo  menos  uma  NF-e  deve  estar  "Em  processamento  na  SEFAZ"  ou  "Com  problemas  na transmissão/pendente";

- Um emitente deverá estar previamente iniciado;
1. Acesso ao menu Notas Fiscais -&gt; Consultar Pendências na SEFAZ
3. Na  janela  de seleção  de  Certificado  Digital, escolher  o Arquivo (para  Certificado tipo A1), informando a senha, ou Repositório (para Certificado tipo A3)
2. Na tela  de pendências  de buscas,  caso existam NF-e's a  em  processamento  na SEFAZ ou  com problemas  na  transmissão,  o  botão  de Iniciar  Busca estará  habilitado.  Para  iniciar  a  busca  na SEFAZ, clicar no botão.
4. Após a seleção, clicar em Selecionar.
5. O Software irá iniciar a busca pelas pendências na SEFAZ (ou seja, os respectivos protocolos das NF-e's em Processamento na SEFAZ e a situação das NF-e's com problemas na transmissão) e informará quando esta busca for concluída.

Importante: Em toda a busca de retorno, TODAS as NF-e's em processamento na SEFAZ pendentes ou com problemas na transmissão serão pesquisadas na SEFAZ.

## Agendamento de buscas

O  agendamento  das  buscas  de  retorno  da  SEFAZ  ocorre  quando,  após  uma  primeira  busca  pelos protocolos,  as  NF-e's  ainda  encontram-se Em  processamento  na  SEFAZ ,  ou  seja,  as  Notas  enviadas ainda não terminaram de ser processadas pela SEFAZ e necessita-se de mais um período de tempo para a conclusão e disponibilização da resposta.

Caso ocorra esta situação, o Software Emissor NF-e realizará automaticamente um Agendamento de uma nova  busca  na  SEFAZ  após  o  período  de  tempo  definido  no  parâmetro  de  sistema Intervalo  entre consultas  de  processamentos  pendentes .  Caso  após  esta  nova  busca  a  NF-e  ainda  encontre-se  em processamento  na  SEFAZ,  um  novo  agendamento  será  realizado  até  que  todas  as  NF-e's  tenham  a respectiva resposta da SEFAZ.

## Exemplo :

Como  ainda  temos  NF-e's  com  a  situação  Em  processamento  na  SEFAZ,  o  Software  realizará  um agendamento da Busca pelos retornos.

Após  a  transmissão  de  10  NF-e's  para  a  SEFAZ,  estas  ficam  com  a  situação Em  processamento  na SEFAZ . Logo a seguir, a Busca pelos retornos destas NF-e's na SEFAZ é iniciado pelo Software Emissor. Depois desta primeira busca, temos que 5 das NF-e's ainda encontram-se em Processamento na SEFAZ, e as outras 5 já receberam a resposta (autorização, denegação ou rejeição).

- O  tempo  de  espera  até  esta  nova  busca  é  definida  no  parâmetro Intervalo  entre  consultas  de processamentos pendentes , que está em 10 segundos.

Assim, passados 10 segundos, uma nova busca será realizada.

Caso exista um agendamento, o usuário poderá terminá-lo.

## Pré-condição :

1. Acessar o menu Notas Fiscais -&gt; Consultar Pendências na SEFAZ
2. -Um emitente deverá estar previamente iniciado.
2. Na tela de pendências de buscas, clicar no botão Parar Agendamento .

Importante: Na próxima Busca de retornos , TODAS as NF-e's em processamento na SEFAZ pendentes que deixaram de ser consultadas pelo agendamento serão pesquisadas na SEFAZ.

## V.7 - Imprimindo o DANF-e

Após  a  autorização  de  uma  NF-e,  deverá  ser  impresso  o  DANF-e  (Documento  Auxiliar  da  Nota  Fiscal eletrônica) para realizar a circulação da mercadoria.

O DANF-e poderá ser impresso a partir de dois casos:

1. A partir de uma NF-e do tipo "Normal" e com situação igual a "Autorizada"

Lembrando que um DANF-e a ser impresso a partir de uma NF-e em Contingência SEMPRE precisará ser realizado em Formulário de Segurança.

2. A partir de uma NF-e do tipo "Contingência" com situação igual a "Assinada" ou "Autorizada"

## Pré-condição :

-  Deve(m)  ser  selecionado(s)  NF-e('s)  do  tipo  "Normal"  em  situação  igual  a  "Autorizada"  ou do  tipo "Contingência" em situação igual a "Assinada" ou "Autorizada"
- Um emitente deverá estar previamente iniciado.

Existem duas formas para a realização da impressão do DANF-e:

## 1ª) Pela tela de Detalhamento/Edição da NF-e:

2. Na tela de seleção das opções de DANF-e, preencher conforme o desejado:
1. Na tela de detalhamento/edição de NF-e, acessar a opção Imprimir DANFE
1. Formato de Impressão: "Frente" ou "Frente e Verso" - Opção para gerar o modelo para impressão apenas utilizando a frente do papel ou gerar o modelo para impressão utilizando a frente e o verso do papel (IMPORTANTE: o Software Emissor gera APENAS o modelo a ser  impresso.  A  impressão  frente  ou  frente  e  verso  é  de  responsabilidade  do  usuário, configurando ou acertando corretamente o papel e a impressora).
3. Após a seleção, clicar em Visualizar .
2. Com Formulário Pré-Impresso - Caso esteja selecionado com a opção "Sim", o Software gerará um modelo a ser impresso apenas com os dados da NF-e, sendo que o usuário tem a responsabilidade de acertar o papel já com o modelo de DANF-e a ser utilizado.
4. O software Emissor NF-e irá gerar o modelo de DANF-e conforme os dados da NF-e e a seleção das opções de DANF-e. O modelo também poderá ser salvo em formato PDF.
5. O Software marcará que o DANFE da NF-e foi impresso.

## 2ª) Pela tela de Gerenciamento de NF-e's:

2. Realizar  a  pesquisa  pela(s)  nota(s) do  tipo  "Normal"  em  situação  igual  a  "Autorizada"  ou do  tipo "Contingência" em situação igual a "Assinada" ou "Autorizada"
1. Acessar o menu: Notas Fiscais -&gt; Gerenciar Notas
3. Selecionar a(s) nota(s) a ser(em) assinada(s) e clicar em Imprimir DANFE
5. O  software  Emissor  NF-e  irá  gerar  o  modelo  de  DANF-e  conforme  os  dados  da(s)  NF-e('s)  e  a seleção das opções de DANF-e. O modelo também poderá ser salvo em formato PDF..
4. Após a seleção das opções de DANF-e, clicar em Visualizar
6. O Software marcará que o DANFE da(s) NF-e('s) foi(ram) impresso(s).

## V.8 - Cancelando uma NF-e

Após a autorização de uma NF-e, esta poderá ser cancelada a partir da operação de Cancelamento de NFe. Apenas NF-e's autorizadas podem ser canceladas.

IMPORTANTE: a exclusão de Nota Fiscal eletrônica pela opção Excluir não realiza o cancelamento da NFe.

## Pré-condição :

- Deve(m) ser selecionado(s) NF-e('s) em situação igual a "Autorizada"
- Um emitente deverá estar previamente iniciado.

Existem duas formas para a realização do cancelamento:

## 1ª) Pela tela de Detalhamento/Edição da NF-e:

2. Escrever a Justificativa para o Cancelamento (mínimo de 15 caracteres)
1. Na tela de detalhamento/edição de NF-e, acessar a opção Cancelar NF-e
3. Na  janela de  seleção  de  Certificado  Digital, escolher  o Arquivo (para  Certificado tipo A1), informando a senha, ou Repositório (para Certificado tipo A3)
5. O software Emissor NF-e irá realizar a transmissão da solicitação de Cancelamento da NF-e para a SEFAZ correspondente, exibindo ao final se a NF-e foi cancelada com sucesso. Caso a NF-e foi cancelada a situação da nota passará para "Cancelada".
4. Após a seleção, clicar em Selecionar.

## 2ª) Pela tela de Gerenciamento de NF-e's:

1. Acessar o menu: Notas Fiscais -&gt; Gerenciar Notas
2. Realizar a pesquisa pela(s) nota(s) com situação "Autorizada" que será(ão) cancelada(s)
4. Escrever a Justificativa para o Cancelamento (mínimo de 15 caracteres).
3. Selecionar a(s) nota(s) a ser(em) assinada(s) e clicar em Cancelar NF-e
5. Na  janela de  seleção  de  Certificado  Digital, escolher  o Arquivo (para  Certificado tipo A1), informando a senha, ou Repositório (para Certificado tipo A3)
7. O software Emissor NF-e irá realizar a transmissão da solicitação de Cancelamento da NF-e para a SEFAZ correspondente, exibindo ao final se a(s) NF-e('s) foi(ram) cancelada(s) com sucesso. Caso a(s) NF-e('s) foi(ram) cancelada(s) a situação da(s) nota(s) passará(ão) para "Cancelada".
6. Após a seleção, clicar em Selecionar.

## V.9 - Excluindo uma NF-e

A opção de exclusão de NF-e do Software Emissor NF-e. Esta ação apaga a NF-e do software, não sendo possível a sua recuperação posteriormente.

IMPORTANTE: a exclusão de uma NF-e autorizada, cancelada ou denegada no software não remove a respectiva NF-e da base de dados da SEFAZ.

## IMPORTANTE: não é permitido a exclusão de NF-e:

- com a situação igual a "Em processamento NA SEFAZ"
- com a situação igual a "assinada", tipo "contingência" e DANFE impresso

Pré-condição : Um emitente deverá estar previamente iniciado.

Existem duas formas para a realização da validação:

## 1ª) Pela tela de Inclusão/Edição da NF-e:

2. Caso  a  NF-e  satisfaça  as  condições  para  a  exclusão,  a  nota  será  removida  do  sistema,  não podendo mais ser recuperada.
1. Na tela de inclusão ou edição de NF-e, acessar a opção Excluir

## 2ª) Pela tela de Gerenciamento de NF-e's:

1. Acessar o menu: Notas Fiscais -&gt; Gerenciar Notas
3. Selecionar a(s) nota(s) a ser(em) excluída(s) e clicar em Excluir
2. Realizar a pesquisa pela(s) nota(s) a ser(em) removida(s)
4. Caso a(s) NF-e('s) satisfaça(m) as condições para a exclusão, a(s) nota(s) será(ão) removida(s) do sistema, não podendo mais ser(em) recuperada(s).

## V.10 - Outras Funções

Funções acessórias do Software Emissor NF-e disponíveis para o usuário:

## a) Consulta de NF-e não cadastrada no Software

A consulta de NF-e's não cadastradas no Software permite que o usuário, através da Chave de Acesso, pesquise  a  situação  da  nota  na  SEFAZ,  verificando  se  está  autorizada,  denegada  ou  cancelada. Apenas NF-e's não cadastradas no Software poderão ser consultadas desta maneira. Se for fornecida uma Chave de Acesso que está cadastrado no Software, o aplicativo gerará uma mensagem informando para realizar a consulta através da opção Consulta Situação SEFAZ do Gerenciamento de Notas .

O retorno desta consulta de NF-e não cadastrada poderá ser:

1. NF-e Autorizada: significando que a NF-e encontra-se autorizada
3. NF-e Cancelada: a NF-e foi canelada pelo emitente
2. NF-e Denegada: a NF-e encontra-se denegada
4. NF-e inexistente: a Chave de Acesso fornecida não corresponde com nenhuma NF-e na SEFAZ.

IMPORTANTE: Conforme indicado na seção de Chave de Acesso, este número de 44 dígitos contém o código da UF. Baseado neste código, o Software realizará a consulta de NF-e não cadastrada na SEFAZ correspondente àquela UF.

Pré-condição : Um emitente deverá estar previamente iniciado.

2. Digitar os 44 dígitos da Chave de Acesso da NF-e a ser pesquisada e clicar em Consultar .
1. Acessar o menu: Notas Fiscais -&gt; Consultar NF-e não cadastrada no Software
3. Na  janela de  seleção  de  Certificado  Digital, escolher  o Arquivo (para  Certificado tipo A1), informando a senha, ou Repositório (para Certificado tipo A3)
5. O software  Emissor  NF-e  irá  realizar  a  consulta,  exibindo  ao  final  se  a  situação  da  NF-e  com  a chave de acesso informada
4. Após a seleção, clicar em Selecionar.

## b) Cancelar NF-e não cadastrada no Software

O  cancelamento  de  NF-e's  não  cadastradas  no  Software  permite  que  o  usuário,  através  da  Chave  de Acesso, número do protocolo de autorização e informando a justificativa, cancelar a NF-e que encontra-se na SEFAZ mas não está cadastrada no Software (exemplo: a NF-e autorizada indevidamente excluída pelo usuário,  mas  este  guardou  em  outro  local  a  Chave  de  Acesso  e  o  número  do  protocolo  da  NF-e). Apenas NF-e's não cadastradas no Software poderão ser canceladas desta maneira. Se for fornecida uma Chave de Acesso que está cadastrada no Software, o aplicativo gerará uma mensagem informando para realizar o cancelamento através da opção Cancelar NF-e no Gerenciamento de Notas .

Após  o  cancelamento,  o  Software  armazenará  a  operação  de  Cancelamento  (ou  seja,  o  protocolo  de cancelamento emitido pela SEFAZ estará disponível  na pesquisa no Gerenciamento de notas), mas não será possível a visualização dos dados da NF-e, pois somente teremos informações do cancelamento.

IMPORTANTE: O Certificado Digital deverá conter o CNPJ do emitente e deverá ser o mesmo da NF-e que pretende-se cancelar.

Pré-condição : Um emitente deverá estar previamente iniciado.

1. Acessar o menu: Notas Fiscais -&gt; Cancelar NF-e não cadastrada no Software
2. Digitar os 44 dígitos da Chave de Acesso da NF-e, o protocolo de autorização e a justificativa do cancelamento
4. Na  janela de  seleção  de  Certificado  Digital, escolher  o Arquivo (para  Certificado tipo A1), informando a senha, ou Repositório (para Certificado tipo A3)
3. Clicar em Cancelar NF-e
5. Após a seleção, clicar em Selecionar.
6. O software Emissor NF-e irá realizar o cancelamento, exibindo ao final se a operação ocorreu com sucesso ou houve algum erro

O Software armazenará o cancelamento, mas não será possível ver as informações da NF-e.

## c) Inutilização de Faixas de Numeração

Conforme o Ajuste SINIEF 07/05, existe a seguinte obrigação com relação à Inutilização: "O contribuinte deverá solicitar, mediante Pedido de Inutilização de Número da NF-e, até o 10 (décimo) dia do mês subseqüente, a inutilização de números de NF-es não utilizados, na eventualidade de quebra de seqüência da numeração da NF-e."

Recomenda-se ao emitente, na geração e transmissão das NF-e's, utilizar a numeração seqüencial das NFe's para cada série.

Entretanto,  podem  ocorrer  os  seguintes  fatos  para  uma  parcial  "quebra"  da  numeração  de  autorizações (considerando o mesmo emitente e uma mesma série):

2. Uma  NF-e  de  numeração  maior  foi  autorizada  na  SEFAZ,  mas  existem  NF-e's  de  numeração inferior  em  situação  "Em  Digitação",  "Validada"  ou  "Assinada"  (ou  seja,  ainda  não  autorizadas), formando uma lacuna na numeração na SEFAZ.
1. A  NF-e  transmitida  para  a  SEFAZ  foi  rejeitada  por  algum  motivo,  sendo  que  a  NF-e  deverá  ser revista.  Neste  caso,  como  a  NF-e  não  foi  autorizada  ou  denegada  pela  SEFAZ,  é  considerada omissão do número (lacuna) na SEFAZ.
3. Uma  NF-e  de  numeração  maior  foi  autorizada  na  SEFAZ  e  não  existem NF-e's  de  numeração inferior, formando uma lacuna na numeração na SEFAZ.

Tais números poderão ser utilizados pelo usuário (exemplo: pode-se corrigir a NF-e rejeitada, contanto que não  seja  rejeição  por  duplicidade,  e  enviá-la  novamente  para  a  SEFAZ  para  autorização).  Entretanto, conforme o Ajuste SINIEF citado, até o décimo dia do mês subseqüente, deve-ser realizar a inutilização dos números não utilizados.

A Inutilização é o processo de informar à SEFAZ que determinada faixa de numeração não foi e não poderá mais ser utilizada sendo, portanto, vedado a autorização posterior de NF-e's com os números da faixa.

Exemplo: considere as NF-e's de série 18 com as seguintes numerações:

|   Número | Situação            |   Número | Situação     |
|----------|---------------------|----------|--------------|
|        1 | Autorizada          |        7 | Assinada     |
|        2 | Em Digitação        |        8 | Validada     |
|        3 | Rejeitada           |        9 | Autorizada   |
|        4 | Não foi criada NF-e |       10 | Denegada     |
|        5 | Não foi criada NF-e |       11 | Em Digitação |
|        6 | Cancelada           |          |              |

Neste caso, é necessário inutilizar as seguintes faixas:

- Numeração de 2 a 5 (ou seja, os números 2, 3, 4 e 5)
- Numeração de 7 a 8 (ou seja, os números 7 e 8)

Pré-condição : Um emitente deverá estar previamente iniciado.

2. Realizar a pesquisa pelas faixas a serem inutilizadas, informando a série, numeração inicial e final, clicando em Pesquisar ao final para realização da busca.
1. Acessar o menu: Notas Fiscais -&gt; Inutilizar faixa de numeração
3. O Software realizará a busca e retornará as faixas possíveis de inutilização do intervalo informado.
5. Após a seleção, clicar em Inutilizar .
4. Selecionar as faixas desejadas.
6. Confirmar que as NF-e's contidas na faixa serão excluídas.
7. Na  janela de  seleção  de  Certificado  Digital, escolher  o Arquivo (para  Certificado tipo A1), informando a senha, ou Repositório (para Certificado tipo A3)
9. O  software  Emissor  NF-e  irá  realizar  a  transmissão  do  pedido  de  Inutiilzação  para  a  SEFAZ correspondente,  exibindo  ao  final  se  a(s)  faixa(s)  foram  inutilizadas  com  sucesso.  A  partir  deste momento, os números da(s) faixa(s) inutilizada(s) não estará(ão) mais disponível(is) para utilização.
8. Após a seleção, clicar em Selecionar .

## OBSERVAÇÕES SOBRE A INUTILIZAÇÃO NO SOFTWARE EMISSOR:

1. A  inutilização  no  Software  Emissor  NF-e,  caso  com  sucesso, excluirá  TODAS  as  NF-e's  em situação "Em Digitação", "Validada", "Assinada" ou "Rejeitada" que estiverem contidos na faixa de numeração  inutilizada.  O  Software,  antes  de  realizar  a  Inutilização,  solicitará  a  confirmação  do processo para continuar.

2. Para  buscar todas as faixas  a serem  inutilizadas  possíveis  do  Software  Emissor  NF-e,  realizar  a pesquisa com o filtro em branco.
3. Para inutilizar uma faixa específica, informar esta faixa específica no filtro e realizar a pesquisa (no exemplo dado, caso apenas deseje-se inutilizar apenas os números 4 e 5 - apenas os números não criados -, informar no filtro de pesquisa a Série 1 e como número inicial 4 e final 5. Apenas esta faixa será retornada e poderão inutilizar-se apenas estes números).

## VI - Cadastro de Clientes

O  Cadastro  de  Clientes  é  uma  opção  para  facilitar  o  preenchimento  das  Notas  Fiscais  eletrônicas. Durante a criação da NF-e, o usuário poderá carregar as informações do cliente previamente cadastrado na Nota Fiscal.

Este cadastro permite a inserção, alteração e exclusão e pesquisa dos clientes do Emitente.

Acesso pelo Menu:

Cadastro -&gt; Cliente

## VI.1 - Pesquisa de clientes cadastrados

Opção para a pesquisa dos clientes cadastrados do Emitente atual.

Pré-condição

: Um emitente deverá estar previamente iniciado.

Acessar o menu: Cadastro -&gt; Cliente

Na tela de pesquisa de Clientes Cadastrados, preencher com o filtro de pesquisa de cliente desejado.

Clicar em Pesquisar

Para limpar os campos do filtro, clicar em Limpar Filtro

| CNPJ/CPF           | Preenchimento de até 14 dígitos; A pesquisa retornará todos os clientes cujo CNPJ ou CPF inicie com o número digitado              |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Inscrição Estadual | Preenchimento de até 14 dígitos; A pesquisa retornará todos os clientes cuja IE inicie com o número digitado                       |
| Nome/Razão Social  | Preenchimento de até 60 caracteres; A pesquisa retornará todos os clientes cujo Nome ou Razão Social contenha a expressão digitada |

## Observações:

2. Caso não sejam preenchidos dados nos campos do filtro, a pesquisa retornará TODOS os clientes cadastrados do emitente atual
1. Os campos do filtro de pesquisa somam-se na busca: caso seja preenchido o campo CNPJ/CPF e o campo Inscrição Estadual ,  a  busca utilizará  os  dois  campos  para  realizar  a  pesquisa; caso  seja preenchido o campo CNPJ/CPF ,  o  campo Inscrição Estadual e o campo Nome/Razão Social ,  a busca utilizará os três campos para realizar a pesquisa

## Resultados da pesquisa:

Após  a  pesquisa,  os  clientes  encontrados  são  apresentados  em  uma  lista,  conforme  imagem  abaixo. Caso  seja  clicado  o  título  da  coluna,  a  listagem  será  ordenada  em  ordem  crescente  de  acordo  com  a coluna. Caso seja clicada novamente, será ordenada em ordem inversa.

## VI.2 - Inclusão de novo cliente

Opção de Inclusão de novo cliente para o Emitente atual.

Pré-condição : Um emitente deverá estar previamente iniciado.

1. Acessar o menu: Cadastro -&gt; Cliente
3. Na tela de Inclusão de Clientes, preencher corretamente os campos do cliente
2. Na tela de pesquisa de Clientes Cadastrados, acessar a opção Incluir

4. Após o preenchimento dos campos corretamente, selecionar a opção Incluir

## Pré-condição : Um emitente deverá estar previamente iniciado.

2. Realizar a pesquisa pelo cliente cadastrado que será editado
1. Acessar o menu: Cadastro -&gt; Cliente
3. Selecionar o cliente a ser editado;
5. A tela de detalhamento com os dados do cliente selecionado será apresentada. Selecionar a opção Editar para a edição dos campos do cliente
4. Após a seleção do cliente, a opção de Detalhar ficará disponível. Selecionar a opção Detalhar
6. Após finalizar a edição dos campos, clicar em Alterar para salvar as modificações

## VI.3 - Exclusão de cliente cadastrado

Opção de exclusão de um ou mais clientes cadastrados do Emitente atual.

Pré-condição

: Um emitente deverá estar previamente iniciado.

Existem duas formas de exclusão de cliente:

## 1ª) Pela listagem de clientes cadastrados

1. Acessar o menu: Cadastro -&gt; Cliente
3. Selecionar o(s) cliente(s) a ser(em) excluído(s);
2. Realizar a pesquisa pelo(s) cliente(s) cadastrado(s) que será(ão) excluído(s);
4. Selecionar a opção Excluir
5. Confirmar a exclusão

## 2ª) Pela tela de detalhe do cliente

2. Confirmar a exclusão
1. Na  tela  de  detalhe  dos  dados  do  cliente,  selecionar  a  opção Excluir para  excluir  o  cliente selecionado

## VII - Importação e exportação de dados

## VII.1 - Importação de Dados

O  processo  de  importação  permite  a  carga  dos  arquivos  gerados  pelo  Software  de  volta  ou  em  outro Software similar, facilitando a troca de informações.

Pré-condição : Um emitente deverá estar previamente iniciado.

2. Selecionar o tipo de informação a ser importado: Emitentes , Clientes , Produtos , Transportadoras ou Notas Fiscais
1. Acessar o menu: Sistema -&gt; Importar
3. Selecionar o tipo de arquivo a ser importado: " Arquivo TXT " ou " Arquivo XML "
4. Caso Arquivo TXT ,  escolher o arquivo com os dados, digitando ou clicando no botão Localizar e selecionando arquivo. Caso Arquivo XML , escolher o diretório com os arquivos a serem importados digitando ou clicando no botão Localizar e selecionando o diretório.
5. Clicar em Importar
6. Ao final, será apresentado o resultado da importação no quadro Dados do Processamento

## Considerações sobre a importação:

a) Para Importação de Notas Fiscais:

Só é possível importar NF-e's do MESMO emitente, ou seja, o CNPJ emitente da NF-e deve ser IGUAL ao CNPJ emitente atual do software.

Importação TXT:

TODAS as NF-e's importadas de arquivo TXT serão colocadas com a situação " Em Digitação " no Software Caso já exista a NF-e no Software (verifica-se a série, número, ano, mês e CNPJ emitente), o aplicativo perguntará ao usuário se deseja sobrescrever.

## Importação XML:

Caso já  exista  a  NF-e  no  Software  (verifica-se  a  Chave  de  Acesso  da  NF-e),  o  aplicativo  perguntará  ao usuário se deseja sobrescrever.

## b) Para Importação de Emitentes:

Caso já exista o cadastro no Software (verifica-se o CNPJ do emitente), o aplicativo perguntará ao usuário se deseja sobrescrever.

## c) Para Importação de Cadastro de produto, clientes e transportadoras:

As informações podem vir de do cadastro de outros emitentes. Caso já exista o cadastro no Software, o aplicativo perguntará ao usuário se deseja sobrescrever.

Para Produto, verificará se já existe o código do produto cadastrado

Para Cliente, verificará se já existe o CNPJ/CPF cadastrado

Para Transportadora, verificará se já existe o CNPJ/CPF já cadastrado

Caso já existam os cadastros, o aplicativo perguntará se deseja sobrescrever.

## VII.2 - Exportação de Dados

O processo  de  exportação permite  a  geração  em  um  ou  mais  arquivos  dos  dados  contidos  no  Software Emissor NF-e, para transferência para outro software ou para outro sistema de informação.

1. Notas Fiscais eletrônicas

É possível a exportação dos seguintes tipos de dados:

2. Emitentes
3. Clientes
5. Transportadoras
4. Produtos

## Tipos de arquivos a serem exportados:

1. TXT (Arquivo texto)
2. XML (Arquivo EXtensible Markup Language no formato e estrutura definido pelo projeto Nota Fiscal eletrônica)

## a) Exportação em TXT

A exportação em TXT das NF-e's sempre gera UM arquivo contendo os registros selecionados.

Pré-condição: Um emitente deverá estar previamente iniciado.

Qualquer NF-e pode ser exportados para TXT, mas perderá a assinatura, a autorização, o cancelamento ou a denegação, caso existirem. Ao importar, todas serão colocadas em situação "Em Digitação".

Existem duas formas:

## 1ª) Pelo gerenciamento de Notas

1. Acessar o menu: Notas Fiscais -&gt; Gerenciar Notas
2. Realizar a pesquisa pela(s) NF-e(s) cadastrada(s) que será(ão) exportada(s);
4. Selecionar a opção Exportar...
3. Selecionar a(s) NF-e(s) a ser(em) exportadas(s);
5. Selecionar o tipo de arquivo a ser gerado como " Arquivo TXT "
6. Na tela  de  exportação  de  arquivos,  escolher  o  local  e  o  arquivo,  digitando  ou  clicando  no  botão Localizar e selecionando o local e arquivo.
8. Ao final, será apresentado o resultado da exportação no quadro Dados do Processamento
7. Clicar em Exportar

## 2ª) Pela tela de detalhe da NF-e

1. Na tela de detalhamento da NF-e (Cuidado: A tela de edição ou inclusão de NF-e não permitem a exportação) Selecionar a opção Exportar...
2. Selecionar o tipo de arquivo a ser gerado como " Arquivo TXT "
4. Clicar em Exportar
3. Na tela  de  exportação  de  arquivos,  escolher  o  local  e  o  arquivo,  digitando  ou  clicando  no  botão Localizar e selecionando o local e arquivo.
5. Ao final, será apresentado o resultado da exportação no quadro Dados do Processamento

## a1) Exportação em TXT: Emitentes

A exportação de dados de emitentes só conterá os dados dos emitentes, não vinculando os dados de NFe's, cadastros, etc.

Existem duas formas:

## 1ª) Pela tela de escolha de emitente

2. Selecionar o(s) emitente(s) a ser(em) exportados(s);
1. Iniciar o software ou acessar o menu: Emitente -&gt; Selecionar Emitente
3. Selecionar a opção Exportar...
5. Na tela  de  exportação  de  arquivos,  escolher  o  local  e  o  arquivo,  digitando  ou  clicando  no  botão Localizar e selecionando o local e arquivo.
4. Selecionar o tipo de arquivo a ser gerado como " Arquivo TXT "
6. Clicar em Exportar
7. Ao final, será apresentado o resultado da exportação no quadro Dados do Processamento

## 2ª) Pela tela de dados do Emitente atual

2. Selecionar o tipo de arquivo a ser gerado como " Arquivo TXT "
1. Na tela de dados do emitente atual selecionar a opção Exportar...
3. Na tela  de  exportação  de  arquivos,  escolher  o  local  e  o  arquivo,  digitando  ou  clicando  no  botão Localizar e selecionando o local e arquivo.
4. Clicar em Exportar
5. Ao final, será apresentado o resultado da exportação no quadro Dados do Processamento

## a2) Exportação em TXT: Cadastros

A exportação de dados de cadastro (Clientes, Produtos e Transportadoras).

Existem duas formas:

## 1ª) Pela tela de pesquisa de Cadastro dos respectivos itens (Clientes, Produtos ou Transportadoras)

2. Selecionar o(s) itens(s) a ser(em) exportados(s);
1. Iniciar o software ou acessar o menu: Cadastro -&gt; Cliente ou Cadastro -&gt; Produto ou Cadastro -&gt; Transportadora
3. Selecionar a opção Exportar...
5. Na tela  de  exportação  de  arquivos,  escolher  o  local  e  o  arquivo,  digitando  ou  clicando  no  botão Localizar e selecionando o local e arquivo.
4. Selecionar o tipo de arquivo a ser gerado como " Arquivo TXT "
6. Clicar em Exportar
7. Ao final, será apresentado o resultado da exportação no quadro Dados do Processamento

## 2ª) Pela tela de detalhe do item de Cadastro (Clientes, Produtos ou Transportadoras)

1. Na tela de dados do item de Cadastro, selecionar a opção Exportar...
3. Na tela  de  exportação  de  arquivos,  escolher  o  local  e  o  arquivo,  digitando  ou  clicando  no  botão Localizar e selecionando o local e arquivo.
2. Selecionar o tipo de arquivo a ser gerado como " Arquivo TXT "
4. Clicar em Exportar
5. Ao final, será apresentado o resultado da exportação no quadro Dados do Processamento

## b) Exportação em XML

A exportação em XML dos itens gera um arquivo XML para cada um dos itens selecionados. Ou seja, caso sejam  selecionados  3  Produtos  para  exportar  em  XML,  serão  gerados  3  arquivos  XML,  um  para  cada produto.

Pré-condição

: Um emitente deverá estar previamente iniciado.

## b1) Exportação em XML: Notas Fiscais eletrônicas

APENAS  NF-e's  em  situação  assinada,  autorizada,  denegada  ou  cancelada  poderão  ser  exportadas. Qualquer outra situação será impedida de exportar em XML. Caso existam cancelamentos dentre as NF-e's exportadas, poderão ser gerados mais arquivos XML do que o número de NF-e's selecionadas. Exemplo: caso  sejam  exportadas  para  XML  duas  NF-e's,  uma  assinada  e  outra  cancelada,  serão  gerados  três arquivos XML.

Existem duas formas:

## 1ª) Pelo gerenciamento de Notas

2. Realizar  a  pesquisa  pela(s)  NF-e(s)  cadastrada(s)  assinada(s),  autorizada(s),  denegada(s)  ou cancelada(s) que será(ão) exportada(s);
1. Acessar o menu: Notas Fiscais -&gt; Gerenciar Notas
3. Selecionar a(s) NF-e(s) a ser(em) exportadas(s);
5. Selecionar o tipo de arquivo a ser gerado como " Arquivo XML "
4. Selecionar a opção Exportar...
6. Na tela de exportação de arquivos, escolher o diretório onde serão gerados os arquivos, digitando ou clicando no botão Localizar e selecionando o diretório.
8. Ao final, será apresentado o resultado da exportação no quadro Dados do Processamento
7. Clicar em Exportar

## 2ª) Pela tela de detalhe da NF-e

2. Selecionar o tipo de arquivo a ser gerado como " Arquivo XML "
1. Na tela de detalhamento da NF-e (Cuidado: A tela de edição ou inclusão de NF-e não permitem a exportação) Selecionar a opção Exportar...
3. Na tela de exportação de arquivos, escolher o diretório onde serão gerados os arquivos, digitando ou clicando no botão Localizar e selecionando o diretório.
4. Clicar em Exportar
5. Ao final, será apresentado o resultado da exportação no quadro Dados do Processamento

## b2) Exportação em XML: Emitentes

A exportação de dados de emitentes só conterá os dados dos emitentes, não vinculando os dados de NFe's, cadastros, etc.

Existem duas formas:

## 1ª) Pela tela de escolha de emitente

2. Selecionar o(s) emitente(s) a ser(em) exportados(s);
1. Iniciar o software ou acessar o menu: Emitente -&gt; Selecionar Emitente
3. Selecionar a opção Exportar...
4. Selecionar o tipo de arquivo a ser gerado como " Arquivo XML "
6. Clicar em Exportar
5. Na tela de exportação de arquivos, escolher o diretório onde serão gerados os arquivos, digitando ou clicando no botão Localizar e selecionando o diretório.
7. Ao final, será apresentado o resultado da exportação no quadro Dados do Processamento

## 2ª) Pela tela de dados do Emitente atual

1. Na tela de dados do emitente atual selecionar a opção Exportar...
2. Selecionar o tipo de arquivo a ser gerado como " Arquivo XML "
4. Clicar em Exportar
3. Na tela de exportação de arquivos, escolher o diretório onde serão gerados os arquivos, digitando ou clicando no botão Localizar e selecionando o diretório.
5. Ao final, será apresentado o resultado da exportação no quadro Dados do Processamento

## b3) Exportação em XML: Cadastros

A exportação de dados de cadastro (Clientes, Produtos e Transportadoras).

Existem duas formas:

## 1ª) Pela tela de pesquisa de Cadastro dos respectivos itens (Clientes, Produtos ou Transportadoras)

1. Iniciar o software ou acessar o menu: Cadastro -&gt; Cliente ou Cadastro -&gt; Produto ou Cadastro -&gt; Transportadora
3. Selecionar a opção Exportar...
2. Selecionar o(s) itens(s) a ser(em) exportados(s);
4. Selecionar o tipo de arquivo a ser gerado como " Arquivo XML "
6. Clicar em Exportar
5. Na tela de exportação de arquivos, escolher o diretório onde serão gerados os arquivos, digitando ou clicando no botão Localizar e selecionando o diretório.
7. Ao final, será apresentado o resultado da exportação no quadro Dados do Processamento

## 2ª) Pela tela de detalhe do item de Cadastro (Clientes, Produtos ou Transportadoras)

1. Na tela de dados do item de Cadastro, selecionar a opção Exportar...
3. Na tela de exportação de arquivos, escolher o diretório onde serão gerados os arquivos, digitando ou clicando no botão Localizar e selecionando o diretório.
2. Selecionar o tipo de arquivo a ser gerado como " Arquivo XML "
4. Clicar em Exportar
5. Ao final, será apresentado o resultado da exportação no quadro Dados do Processamento

## VIII - Funções de sistema

## VIII.1 - Avisos

O Aviso  do Software Emissor NF-e é a tela de informações das pendências encontradas pelo aplicativo. Tais pendências são:

2. NF-e's  do  tipo Contingência com  DANFE  impresso que  ainda  não  foram  transmitidas  para  a SEFAZ
1. NF-e's em  processamento  na  SEFAZ ou com  problemas  na  transmissão/com  pendência (Retornos pendentes) que ainda não foram consultadas pela busca de retornos do Software
3. Faixas de Numeração a serem inutilizadas

Exceção :  caso  o  parâmetro  de  sistema Aviso  de  inutilização  apenas  mensal estiver  selecionado,  a condição de Faixas a serem inutilizadas só  será considerada  para apresentação ao usuário no  início do Emitente apenas no começo de cada mês (baseado na data do sistema operacional). Entretanto, caso o usuário  acesse  a  tela  de  Aviso  através  do  menu  (ver  abaixo),  serão  apresentados  as  faixas  a  serem inutilizadas, caso existam.

O usuário também poderá acessar a tela de Aviso através do Menu.

Pré-condição : Um emitente deverá estar previamente iniciado.

2. A tela de aviso do emitente será apresentada, informando se existem pendências.
1. Acessar o menu: Sistema -&gt; Aviso

## Retornos pendentes da SEFAZ:

Caso existam NF-e's em processamento, será apresentado o botão para iniciar a Busca de Retornos de forma  manual.  Clicando  no  botão,  o  usuário  é  redirecionado  para  a  tela  da  função  de Consultar pendências na SEFAZ , onde pode iniciar a busca.

## NF-e's em contingência não transmitidas:

Caso existam NF-e's do tipo Contingência com DANFE impresso e não transmitidas para a SEFAZ, será apresentado o botão para visualizar tais NF-e's. Clicando no botão, o usuário é redirecionado para a tela de gerenciamento de NF-e's indicando as NF-e's com a situação citada. A partir da tela de gerenciamento, o usuário poderá selecionar as NF-e's e transmiti-las para a SEFAZ.

## Faixas de numeração a serem inutilizadas:

Caso existam "buracos" na numeração da NF-e (ver Inutilização ), será apresentado o botão para visualizar as faixas a serem inutilizadas. Clicando no botão, o usuário é redirecionado para a tela de Inutilização com todas as faixas encontradas para inutilizar. O usuário então poderá selecionar as faixas e inutilizá-las.

## VIII.2 - Parâmetros do sistema

Compreende os dados relativos as propriedades básicas do sistema.

Acesso por: Sistema -&gt; Parâmetros

Não é necessário um emitente iniciado para o acesso.

## Configurações de Acesso a Internet

Caso a máquina necessite de configuração de Proxy para a conexão com a Internet, configurar os campos abaixo. Contatar o administrador de rede para a configuração correta.

| Campo   | Obrigatório           | Tipo de dado          | Formato e Tamanho   | Observações    |
|---------|-----------------------|-----------------------|---------------------|----------------|
| Não     | Caractere e/ou número | -                     | -                   | Servidor Proxy |
| Não     | Numérico              | -                     | -                   | Porta          |
| Não     | Caractere e/ou número |                       | - -                 | Usuário        |
| Não     |                       | Caractere e/ou número | - -                 | Senha          |

## Outras Configurações:

## Intervalo entre tentativas de transmissão

Caso  durante  a  transmissão  ocorra  algum  erro,  o  Software  Emissor  NF-e  tentará  realizar novamente a transmissão após o intervalo de tempo especificado neste parâmetro.

Formato:

Numérico de 10 a 600 segundos

Obrigatório:

Sim

## Intervalo entre consultas de processamento pendentes

Durante  a  consulta  pelos  protocolos  de  autorização  das  NF-e's  logo  após  a  realização  da transmissão, caso a NF-e ainda estiver  em  processamento  na  SEFAZ  (processamento pendente), o Software Emissor NF-e agendará uma nova consulta e realizará uma nova consulta após o intervalo de tempo especificado neste parâmetro.

Formato:

Numérico de 10 a 600 segundos

Obrigatório:

Sim

## Número de registros por página de consulta

O número máximo de registros exibidos em uma tela de consulta (ou seja, caso uma pesquisa retorne  100  itens  e  o  número  de  registros  por  página  de  consulta  esteja  igual  a  10,  serão mostrados apenas 10 registros por vez).

Parâmetro útil para números grandes de registros retornados em uma pesquisa.

Formato:

Numérico de 1 a 10000 registros por página de consulta

Obrigatório:

Sim

## Aviso de Inutilização  apenas mensal

Por  padrão,  a  cada  vez  que  o  Software  for  executado,  este  informará  as  faixas  a  serem inutilizadas.

Caso  este  parâmetro  esteja  habilitado,  o  Software  somente  informará  as  faixas  a  serem inutilizadas no início de cada mês, com base na data configurada do Sistema Operacional.

Formato:

Habilitado/Desabilitado

Obrigatório:

Não

## VIII.3 - Relatório Gerencial

Com  o  objetivo  de  consolidar  as  informações  relevantes  sobre  NF-e's  no  período,  o  relatório  gerencial apresenta,  de  forma  resumida,  as  Notas  Fiscais,  suas  situações  e  seus  valores  principais.  Pode  trazer também as Inutilizações realizadas no período, caso o usuário assim escolha.

Pré-condição: Um emitente deverá estar previamente iniciado.

1. Acessar o menu: Sistema -&gt; Relatório Gerencial

2. Preencher a data inicial e final para busca das NF-e's ou inutilizações.
3. Selecionar se o Relatório deverá trazer as inutilizações, as Notas Fiscais ou ambas.
4. Caso seja selecionado para buscar as NF-e's, selecionar o tipo (Normal, Contingência ou ambas) e as situações (escolha e uma ou mais).
6. Ao final, será apresentado o resultado das NF-e's. Cada situação será apresentada em uma aba. Caso a inutilização foi selecionada, esta virá em uma aba de Inutilizações.
5. Clicar em Gerar Relatório
7. Clicar em Imprimir para visualizar o Relatório para impressão.

## VIII.4 - Backup e Restauração dos dados

Como  medida  de  segurança  contra  a  perda  de  dados,  o  software  apresenta  as  funções  de Backup e Restauração de TODOS os dados do aplicativo.

## Backup

O Backup é  o  processo  de  cópia  dos  dados  para  posterior  recuperação,  caso  haja  necessidade  ou problemas com os dados originais.

No Software Emissor NF-e, o backup realizará uma cópia total dos dados de todos os Emitentes, suas NFe's, Cadastros, etc.

Observação : Nenhum emitente poderá estar iniciado.

2. Selecionar  o  local  para  o Backup clicando  no  botão Selecionar e  escolhendo  o  diretório  onde  o arquivo de Backup será gerado.
1. Acessar o menu: Sistema -&gt; Backup
3. Clicar  em Iniciar .  Confirmar  e  aguardar  o  processamento.  O backup será  gerado  no  diretório selecionado e o Software informará a conclusão do Backup .

## Arquivo de Backup:

Formato:

.zip

Nomenclatura gerada pelo Software: NFE + ANO + MÊS + DIA + HORA + MINUTO .zip Exemplo: backup gerado no dia 01/01/2007 às 15:30hs - Nomenclatura: NFE200701011530.zip

## Restauração:

Na restauração, TODOS os dados atuais são excluídos e os dados do Backup inseridos, de forma que o Software retorna para o estado do período do Backup .

O processo de Restauração é a volta dos dados contidos no arquivo de Backup .

É  o  método  também  utilizado  caso  ocorra  perda  dos  dados  originais.  Entretanto,  as  autorizações, denegações ou cancelamentos realizados  que NÃO estão contidos  no Backup ,  mas  estão  na  respectiva SEFAZ não poderão ser retornados.

Observação : Nenhum emitente poderá estar iniciado.

1. Acessar o menu: Sistema -&gt; Restaurar
2. Selecionar o arquivo do Backup clicando no botão Selecionar e escolhendo o arquivo.
4. Confirmar a restauração de dados, com a conseqüente perda dos dados atuais
3. Clicar em Iniciar .
5. O Software irá realizar a restauração de dados a partir do arquivo de Backup e informará o sucesso da operação

## IX - Atualizações automáticas

O Software Emissor NF-e também poderá ser atualizado automaticamente. Ao detectar novas atualizações, o Software informará o usuário e solicitará a confirmação.

Para realizar o download das atualizações, clicar em OK . Após o download, o Software irá executar com as atualizações  já  instaladas.  Caso  não  deseje  realizar  a  atualização,  clicar  em Cancel .  O  programa  irá executar sem realizar a atualização.
## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/manuais/manual-emissor-nfe/source.json)
- [Dados normalizados](../../../../normalized/nfe/manuais/manual-emissor-nfe/normalized.json)
- [Changelog](../../../../changelog/nfe/manuais/manual-emissor-nfe.md)
- [Proveniência resumida](../../../../sources/provenance/manual-emissor-nfe.json)

## Documentos relacionados
_Nenhum documento relacionado conhecido._
