---
title: "Sistema Nota Fiscal Eletrônica"
slug: "nt2022-001-v1-00-ws-consulta-gtin"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "de3174af7330d510f8fa4ec6b9f44047086be761f978029c6fbb660376fb1a22"
converted_at_utc: "2026-06-25T16:29:14.576141+00:00"
status: "published"
type: "nota_tecnica"
---
![Image](assets/image_000000_432cda0046c79349e50be53f9e1e0ac0d089c1aaecc2b26a1fd272c1c7c53589.png)

![Image](assets/image_000001_5a878eecc1a7ccead95a841b65d9d367b947a062ba9278f04b104538a79e52f9.png)

## Sistema Nota Fiscal Eletrônica

Nota Técnica 2022.001

Consulta GTIN via Web Service

Versão 1.00 - Maio 2022

![Image](assets/image_000002_b40708a05c65a27eec51ec0b8535fe62f57d90254631b11dd1a49fa1a59771fa.png)

![Image](assets/image_000003_541e18e4d3695f3e2a0ef76c1dfc97cfd06e398abff5209e9c4162e8b0bb2aae.png)

## Sumário

| Controle de Versões.....................................................................................................................3          |
|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Histórico de Alterações / Cronograma........................................................................................3                      |
| 01. Resumo....................................................................................................................................4    |
| 02. Sobre o GTIN e sobre o CCG .................................................................................................5                  |
| 02.1 Sobre o GTIN......................................................................................................................5           |
| 02.2 Sobre o CCG.......................................................................................................................5           |
| 03. Arquitetura da Solução...........................................................................................................6             |
| 03.1 Modelo Conceitual...............................................................................................................6             |
| 03.2 Padrões Técnicos................................................................................................................6             |
| 03.3 Web Services ......................................................................................................................6          |
| 04. Serviço de Consulta do GTIN.................................................................................................7                  |
| 04.1 Informações Gerais .............................................................................................................7             |
| 04.2 Leiaute Mensagem de Entrada............................................................................................8                      |
| 04.3 Leiaute Mensagem de Retorno............................................................................................8                      |
| 04.4 Validação do Certificado de Transmissão............................................................................8                          |
| 04.5 Validação Inicial da Mensagem no Web Service .................................................................8                               |
| 04.6 Validação da área de Dados - Geral...................................................................................9                        |
| 04.7 Validação das Regras de Negócio.......................................................................................9                       |
| 04.7.1 Sobre a Normalização do GTIN ......................................................................................................9        |
| 04.7.2 Regras de Validação .....................................................................................................................10 |
| 04.8 Final do Processamento....................................................................................................10                  |
| 90. Mensagens do Resultado do Processamento ....................................................................11                                 |
| 90.1 Código das Mensagens.....................................................................................................11                   |

![Image](assets/image_000004_dfedcbd7e49f96b46a109d76975d01e022a836cc5def669505e5297cf099d15e.png)

Eletronica

## Controle de Versões

|   Versão | Publicação   | Descrição                     |
|----------|--------------|-------------------------------|
|     1.00 | Maio/2022    | Consulta GTIN via Web Service |

## Histórico de Alterações / Cronograma

|   Versão | Histórico de atualizações     | Implantação Teste   | Implantação Produção   |
|----------|-------------------------------|---------------------|------------------------|
|     1.00 | Consulta GTIN via Web Service | 13/05/2022          | 31/05/2022             |

![Image](assets/image_000005_b1a205089cec443e89e2c7097889af6f29cec1e8ec381c2423f1d2d71c6ad51e.png)

## 01. Resumo

O Ajuste SINIEF 07/05 e o Ajuste SINIEF 19/16 obrigam o preenchimento dos campos cEAN e cEANTrib na Nota Fiscal Eletrônica (NF-e) e na Nota Fiscal de Consumidor Eletrônica (NFC-e) quando o produto comercializado possuir código de barras com GTIN.

Os Ajustes SINIEF citados também estipulam que os sistemas autorizadores da NF-e e NFC-e deverão  validar  as  informações  descritas  nos  campos  cEAN  e  cEANTrib  junto  ao  Cadastro Centralizado de GTIN (CCG), devendo as notas serem rejeitadas em caso de não conformidade com as informações contidas no CCG.

Estes Ajustes SINIEF podem ser encontrados seguintes endereços:

https://www.confaz.fazenda.gov.br/legislacao/ajustes/2005/AJ007\_05 https://www.confaz.fazenda.gov.br/legislacao/ajustes/2016/AJ\_019\_16

A Consulta dos dados reduzidos do GTIN está disponível na Internet no 'Portal dos Documentos Fiscais Eletrônicos - SVRS', para os Sistemas da Nota Fiscal Eletrônica (NF-e, NFC-e).

O objetivo desta Nota Técnica é viabilizar a consulta aos dados reduzidos do GTIN via Web Service, permitindo a consulta automatizada pelas empresas que desejarem usar essa funcionalidade.

![Image](assets/image_000006_059e3d5285e69aa8d631a7245bd8c145354852d751ea9ea61a4b794ed6801957.png)

NT 2022.001 - Consulta GTIN via Web Service

## 02. Sobre o GTIN e sobre o CCG

## 02.1 Sobre o GTIN

O GTIN, sigla de 'Global Trade Item Number' é um identificador para itens comerciais, desenvolvido e controlado pela GS1 Brasil (antiga EAN/UCC). O GTIN, anteriormente chamado de código EAN, é atribuído para qualquer item (produto ou serviço) que pode ser precificado, pedido ou faturado em qualquer ponto da cadeia de suprimentos, tendo sido desenvolvido especificamente para leitura no ponto de venda, devido à agilidade propiciada na captura da informação.

O GTIN é utilizado para recuperar informação pré-definida e abrange desde as matérias primas até produtos acabados. GTIN é um termo guarda-chuva para descrever toda a família de identificação das estruturas de dados GS1 para itens comerciais (produtos e serviços).

Uma faixa de códigos de GTIN pode ser disponibilizada pela GS1 para a empresa ' dona da marca ' que pretenda utilizar esta numeração internacional para identificar seus produtos.

Para  as  Empresas  e  para  as  SEFAZ  esta  informação  é  importante,  podendo  ser  decisiva  na identificação do produto que está sendo representado em cada item da NF-e / NFC-e.

## 02.2 Sobre o CCG

A  GS1  mantém  o  CNP  -  Cadastro  Nacional  de  Produtos,  onde  são  registrados  os  dados  dos produtos comercializados pelos seus Associados (' dono da marca '), juntamente com o código GTIN correspondente.

O Cadastro Centralizado de GTIN - CCG também é mantido pela GS1 Brasil e este cadastro é uma réplica  simplificada  do  CNP  -  Cadastro  Nacional  de  Produtos,  para  um  conjunto  reduzido  de informações. O Cadastro Centralizado de GTIN (CCG) é replicado para as SEFAZ, por meio de Web Service (WS) específico.

O objetivo do Cadastro Centralizado de GTIN - CCG disponibilizado para as SEFAZ é:

-  Auxiliar na identificação do produto que está sendo comercializado na NF-e / NFC-e;
-  Melhorar a qualidade da informação prestada na NF-e, a partir da validação de cada item da NF-e que possua a informação do GTIN contra este Cadastro Centralizado de GTIN - CCG.

![Image](assets/image_000007_059e3d5285e69aa8d631a7245bd8c145354852d751ea9ea61a4b794ed6801957.png)

## 03. Arquitetura da Solução

## 03.1 Modelo Conceitual

O  modelo  conceitual  das  consultas  através  de  Web  Service  compreende  a  existência  de  uma 'aplicação  servidora'  desenvolvida  pela  SVRS  e  uma  'aplicação  cliente'  desenvolvida  pelas Empresas.

## 03.2 Padrões Técnicos

Serão adotados os padrões técnicos normais do Sistema NFE:

-  Mensagens no formato XML;
-  Comunicação via Web Service;
-  Uso de Certificado Digital no padrão ICP-Brasil (X.509);
-  Protocolo de comunicação Internet TLS v1.2, com autenticação mútua;
-  Padrão de troca de mensagens via protocolo SOAP, versão 1.2;
-  Validação inicial das mensagens via Schema XML, previamente definido;
-  Padrão de compactação via Gzip (GNU zip), quando aplicável.

## 03.3 Web Services

Os Web Services disponibilizam os serviços que serão utilizados pelos aplicativos das Empresas. O mecanismo de utilização dos Web Services segue as seguintes premissas:

-  É disponibilizado um Web Service para cada tipo de serviço, podendo existir mais de um método para cada serviço;
-  O envio da solicitação e a obtenção do retorno serão realizados na mesma conexão, através de um único método;
-  A URL dos Web Services está documentada neste documento. Acessando a URL pode ser obtido o WSDL (Web Services Description Language) de cada Web Service;
-  O fluxo de comunicação sempre é iniciado pelo aplicativo da Empresa interessada através do envio de uma mensagem ao Web Service com a solicitação do serviço desejado;
-  A ocorrência de qualquer erro na validação dos dados recebidos interrompe o processo com a disponibilização de uma mensagem contendo o código e a descrição do erro;
-  Não serão usados parâmetros no SOAP Header.
-  Serão  mantidos  controles  para  identificar  as  situações  de  'uso  indevido',  no  consumo excessivo do Web Service em um curto espaço de tempo. As novas tentativas poderão ser rejeitadas com o erro '656-Rejeição: Consumo Indevido'.

![Image](assets/image_000008_dfedcbd7e49f96b46a109d76975d01e022a836cc5def669505e5297cf099d15e.png)

## 04. Serviço de Consulta do GTIN

## 04.1 Informações Gerais

## Objetivo

O objetivo deste serviço é disponibilizar a consulta reduzida ao Cadastro Centralizado de GTINCCG, mantido pela GS1, no Ambiente SEFAZ Virtual do RS (SVRS).

## Informações sobre o Serviço

| Nome do Web Service   | ccgConsGTIN   |
|-----------------------|---------------|
| Nome do Método        | ccgConsGTIN   |
| Processo              | Síncrono      |

## URL Ambiente de Produção

- https://dfe-servico.svrs.rs.gov.br/ws/ccgConsGTIN/ccgConsGTIN.asmx

## Envio das informações

Este  WebService  requer  autenticação  mútua  e  o  envio  das  informações  deverá  ser  feito  com Certificado Digital que contenha o CNPJ ou o CPF de Contribuinte emitente de NF-e ou NFC-e.

![Image](assets/image_000009_dfedcbd7e49f96b46a109d76975d01e022a836cc5def669505e5297cf099d15e.png)

## 04.2 Leiaute Mensagem de Entrada

## Schema XML: consGTIN\_v9.99.xsd

| #   | Campo    | Ele   | Pai   | Tipo   | Ocor.   | Tam.          | Descrição/Observação                     |
|-----|----------|-------|-------|--------|---------|---------------|------------------------------------------|
| P01 | consGTIN | Raiz  | -     | -      | -       | -             | Tag Raiz                                 |
| P02 | versao   | A     | P01   | N      | 1-1     | 2v2           | Versão do leiaute                        |
| P10 | GTIN     | N     | P01   | N      | 1-1     | 8, 12, 13, 14 | Informar o código GTIN a ser consultado. |

## 04.3 Leiaute Mensagem de Retorno

## Schema XML: retConsGTIN\_v9.99.xsd

| #   | Campo       | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Descrição/Observação                                                                                                                                                                                                                                              |
|-----|-------------|-------|-------|--------|---------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R01 | retConsGTIN | Raiz  | -     | -      | -       | -      | Tag Raiz da mensagem de retorno                                                                                                                                                                                                                                   |
| R02 | versao      | A     | R01   | N      | 1-1     | 2v2    | Idem mensagem de entrada, ou versão mais recente do leiaute                                                                                                                                                                                                       |
| R05 | verAplic    | E     | R01   | C      | 1-1     | 1-20   | Versão da aplicação que atendeu a requisição.                                                                                                                                                                                                                     |
| R07 | cStat       | E     | R01   | N      | 1-1     | 4      | Código do status da resposta. Se não tiver erro, será retornado: '9490 - Consulta realizada com sucesso'                                                                                                                                                          |
| R08 | xMotivo     | E     | R01   | C      | 1-1     | 1-255  | Descrição do status da resposta                                                                                                                                                                                                                                   |
| R09 | dhResp      | E     | R01   | DH     | 1-1     | -      | Data e hora da resposta no formato AAAA-MM- DDThh:mm:ssTZD (UTC - Universal Coordinate Time)                                                                                                                                                                      |
| R10 | GTIN        | E     | R01   | N      | 0-1     | 8-14   | Idem mensagem de entrada                                                                                                                                                                                                                                          |
| R11 | tpGTIN      | E     | R01   | N      | 0-1     | 1-2    | Tipos possíveis: 8, 12, 13, 14                                                                                                                                                                                                                                    |
| R12 | xProd       | E     | R01   | C      | 0-1     | 1-500  | Descrição do Produto, cadastrada pelo 'Dono da Marca' na GS1, para o GTIN consultado                                                                                                                                                                              |
| R13 | NCM         | E     | R01   | N      | 0-1     | 8      | Código do NCM, cadastrado pelo 'Dono da Marca' na GS1, para o GTIN consultado                                                                                                                                                                                     |
| R14 | CEST        | E     | R01   | N      | 0-3     | 7      | Código do CEST, cadastrado pelo 'Dono da Marca' na GS1. Normalmente um Produto (definido pelo código do GTIN) está vinculado a somente 1 CEST, mas existem situações pouco frequentes onde um Produto pode estar associado a mais de 1 CEST, conforme a operação. |

## 04.4 Validação do Certificado de Transmissão

Regras de validação idênticas aos demais Web Services, podendo gerar os erros:

- 

- 280: 'Rejeição: Certificado Transmissor inválido'

- 

281: 'Rejeição: Certificado Transmissor Data Validade'

- 

- 283: 'Rejeição: Certificado Transmissor - erro Cadeia de Certificação'

- 

- 286: 'Rejeição: Certificado Transmissor erro no acesso a LCR'

- 

- 284: 'Rejeição: Certificado Transmissor revogado'

- 

- 285: 'Rejeição: Certificado Transmissor difere ICP-Brasil'

-  282: 'Rejeição: Certificado Transmissor sem CNPJ/CPF'

## 04.5 Validação Inicial da Mensagem no Web Service

Regras de validação idênticas aos demais Web Services, podendo gerar os erros:

-  214: 'Rejeição: Tamanho da mensagem excedeu o limite estabelecido'
-  108: 'Serviço Paralisado Momentaneamente (curto prazo)'
-  109: 'Serviço Paralisado sem Previsão'
-  239: 'Rejeição: Versão do arquivo XML não suportada'

![Image](assets/image_000010_dfedcbd7e49f96b46a109d76975d01e022a836cc5def669505e5297cf099d15e.png)

## 04.6 Validação da área de Dados - Geral

Regras de validação idênticas aos demais Web Services, podendo gerar os erros:

-  516: 'Rejeição: Falha Schema XML, inexiste a tag raiz esperada para a mensagem'

-  517: 'Rejeição: Falha Schema XML, inexiste atributo versão na tag raiz da mensagem'

-  239: 'Rejeição: Falha Schema XML, versão não suportada'

-  215: 'Rejeição: Falha Schema XML'

-  587: 'Rejeição: Usar somente o namespace padrão da NF-e'

-  588: 'Rejeição: Não é permitida a presença de caracteres de edição no início/fim da mensagem ou entre as tags da mensagem'

-  404: 'Rejeição: Uso de prefixo de namespace não permitido'

-  402: 'Rejeição: XML da área de dados com codificação diferente de UTF-8'

## 04.7 Validação das Regras de Negócio

## 04.7.1 Sobre a Normalização do GTIN

## A. Prefixo GS1

A codificação do GTIN contém o "Prefixo GS1" que define a entidade GS1 que concedeu a faixa de códigos para a empresa usar na identificação dos seus produtos. Este 'Prefixo' é composto por 3 algarismos, que constam no início do código GTIN do produto.

## B. Como Identificar o "Prefixo GS1"

O GTIN pode possuir 8, 12, 13 ou 14 algarismos, e segue abaixo uma forma prática de identificar o "Prefixo GS1":

-  Normalizar o tamanho do campo em 14 posições numéricas, com zeros não significativos à esquerda;
-  Se as primeiras 6 posições do GTIN normalizado for = Zeros (GTIN-8):
- ­ Prefixo GS1: posições 7 a 9 do GTIN normalizado;
-  Se as primeiras 6 posições do GTIN normalizado for &lt;&gt; Zeros (GTIN-12, 13 ou 14):
- ­ Prefixo GS1: posições 2 a 4 do GTIN normalizado;
- Obs. 1 : A GS1-Brasil é identificada pelo Prefixo 789 e 790, e não temos o uso do GTIN-12 para produtos produzidos no País.
- Obs. 2 : O GTIN-14 na verdade é uma variação do GTIN-13, onde a primeira posição identifica um agrupamento dos produtos identificados pelo GTIN-13. O primeiro algarismo do GTIN-14 não pode ser zero.

## C. Prefixo GS1 não identificando um País

O "Prefixo GS1" identifica uma entidade GS1 associada e normalmente isso identifica também um País. Existem casos especiais, onde o prefixo GS1 não identifica um País, por exemplo:

-  Faixa de códigos GTIN que podem ser usados internamente na empresa;
-  Faixa de códigos GTIN para Jornais, Revistas periódicas e Livros;
-  Outros.

## D. "Prefixo GS1" para a GS1 Brasil

Para efeito dessa consulta, estão disponíveis somente os GTIN concedidos pela GS1 Brasil, identificados pelo 'Prefixo GS1' = 789 ou 790.

![Image](assets/image_000011_059e3d5285e69aa8d631a7245bd8c145354852d751ea9ea61a4b794ed6801957.png)

Eletronica

## 04.7.2 Regras de Validação

| #      | Regra de Validação                                                            | Aplic.   |   Msg | Descrição Erro                                        |
|--------|-------------------------------------------------------------------------------|----------|-------|-------------------------------------------------------|
| P10-10 | Normalizar GTIN com 14 posições: - Se GTIN com dígito de verificador inválido | Obrig.   |  9491 | Rejeição: GTIN com dígito verificador inválido        |
| P10-20 | - Se Prefixo GS1 diferente de 789, 790 (Brasil)                               | Obrig.   |  9492 | Rejeição: GTIN não possui prefixo 789 ou 790 (Brasil) |

| Banco de Dados: Cadastro Centralizado de Contribuintes 1P10-10 Acesso CCC-Cadastro Centralizado de Contribuintes (Chave: CNPJ/CPF do Certificado de Transmissão): - CNPJ/CPF do Certificado de Transmissão não é emitente de NF-e / NFC-e   | (CCC) Obrig.   | 9493   | Rejeição: CNPJ/CPF do Certificado de Transmissão não é emitente de NF-e ou NFC-e   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|--------|------------------------------------------------------------------------------------|

| *** Banco de Dados: Cadastro Centralizado de GTIN (CCG)   | *** Banco de Dados: Cadastro Centralizado de GTIN (CCG)                                                 | *** Banco de Dados: Cadastro Centralizado de GTIN (CCG)   | *** Banco de Dados: Cadastro Centralizado de GTIN (CCG)   | *** Banco de Dados: Cadastro Centralizado de GTIN (CCG)                                               |
|-----------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| 2P10-10                                                   | Acesso CCG-Cadastro Centralizado de GTIN (Chave: GTIN): - GTIN inexistente no CCG                       | Obrig.                                                    | 9494                                                      | Rejeição: GTIN inexistente no Cadastro Centralizado de GTIN (CCG)                                     |
| 2P10-20                                                   | - GTIN existe no CCG, com situação inválida (sitGTIN <> 1)                                              | Obrig.                                                    | 9495                                                      | Rejeição: GTIN existe no CCG com situação inválida. Solicitar ao dono da marca que entre              |
|                                                           | Nota: Não retornar os dados do CCG.                                                                     | Nota: Não retornar os dados do CCG.                       | Nota: Não retornar os dados do CCG.                       | em contato com a GS1                                                                                  |
| 2P10-30                                                   | - GTIN existe no CCG, mas Dono da Marca não autorizou a publicação das informações (indNaoAutoriza = 1) | Obrig.                                                    | 9496                                                      | Rejeição: GTIN existe no CCG, mas dono da marca não autorizou a publicação das informações. Entrar em |
|                                                           | Nota: Não retornar os dados do CCG.                                                                     | Nota: Não retornar os dados do CCG.                       | Nota: Não retornar os dados do CCG.                       | contato com o dono da marca                                                                           |
| 2P10-40                                                   | - GTIN existe no CCG com NCM não cadastrado Nota: Retornar os dados do CCG.                             | Obrig.                                                    | 9497                                                      | Rejeição: GTIN existe no CCG com NCM não cadastrado                                                   |
| 2P10-50                                                   | - GTIN existe no CCG com NCM inválido ou fora da vigência Nota: Retornar os dados do CCG.               | Obrig.                                                    | 9498                                                      | Rejeição: GTIN existe no CCG com NCM inválido                                                         |

## 04.8 Final do Processamento

A validação da mensagem de requisição poderá resultar em:

- ­ Rejeição: conforme as Regras de Validação definidas anteriormente, retornando o motivo da rejeição (tag: cStat e xMotivo);
- ­ Resultado da Consulta : Caso não haja rejeição, serão retornados os dados da consulta, com a mensagem: '9490 - Consulta realizada com sucesso'.

![Image](assets/image_000012_b1a205089cec443e89e2c7097889af6f29cec1e8ec381c2423f1d2d71c6ad51e.png)

## 90. Mensagens do Resultado do Processamento

## 90.1 Código das Mensagens

|   Código | Mensagem                                                                                                                          |
|----------|-----------------------------------------------------------------------------------------------------------------------------------|
|     9490 | Consulta realizada com sucesso                                                                                                    |
|     9491 | Rejeição: GTIN com dígito verificador inválido                                                                                    |
|     9492 | Rejeição: GTIN não possui prefixo 789 ou 790 (Brasil)                                                                             |
|     9493 | Rejeição: CNPJ/CPF do Certificado de Transmissão não é emitente de NF-e ou NFC-e                                                  |
|     9494 | Rejeição: GTIN inexistente no Cadastro Centralizado de GTIN (CCG)                                                                 |
|     9495 | Rejeição: GTIN existe no CCG com situação inválida. Solicitar ao Dono da Marca que entre em contato com a GS1                     |
|     9496 | Rejeição: GTIN existe no CCG, mas dono da marca não autorizou a publicação das informações. Entrar em contato com o Dono da Marca |
|     9497 | Rejeição: GTIN existe no CCG com NCM não informado                                                                                |
|     9498 | Rejeição: GTIN existe no CCG com NCM inválido                                                                                     |

![Image](assets/image_000013_dfedcbd7e49f96b46a109d76975d01e022a836cc5def669505e5297cf099d15e.png)