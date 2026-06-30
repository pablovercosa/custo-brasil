---
title: "Projeto Nota Fiscal Eletrônica"
slug: "nt2020-006-v1-31-intermediador-e-marketplace"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "449c1816a67555082891be24f509c57b8e71096f3f8efaf9a71fcb79c2640600"
converted_at_utc: "2026-06-25T16:24:15.493579+00:00"
status: "published"
type: "nota_tecnica"
---
![Image](assets/image_000000_fb7492c9815fc92aa4d06c7459e53a5e1b29f063408767ed6f687628e719d9ea.png)

![Image](assets/image_000001_9dcbed07271170bf8c86f9f1f3d5014c44077f81ee1c971c4c01859606c93129.png)

## Projeto Nota Fiscal Eletrônica

Nota Técnica 2020.006

Criação e Atualização de Regras de Validação

(Intermediador da Operação -Marketplace e outros)

![Image](assets/image_000002_c3d82fd5203afb5d61764680b6a4ae0b0c2a62e2db6bc6f5ce373c9742f9b68a.png)

![Image](assets/image_000003_a3a7983e441564952a0cd31ab6c4a5bb6f4700c1fb260b38386d070fb8fdf101.png)

NT 2020.006

## Sumário

| Controle de                                                                                                                                                                                                          | Versões........................................................................................................................3   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Histórico de Alterações / Cronograma.............................................................................................4                                                                                   |                                                                                                                                    |
| 1. Resumo.......................................................................................................................................5                                                                    |                                                                                                                                    |
| 2. Visão Geral .................................................................................................................................5                                                                    |                                                                                                                                    |
| 2.1. Alterações de Campos..........................................................................................................5                                                                                 |                                                                                                                                    |
| 2.1.1. Criação do campo indicativo do Intermediador/Marketplace (indIntermed).....................................6                                                                                                  |                                                                                                                                    |
| 2.1.2. Alteração no grupo YA (Informações de Pagamento) .....................................................................6                                                                                       |                                                                                                                                    |
| 2.1.3. Inclusão do grupo YB (Informações do Intermediador da Transação) ............................................6                                                                                                |                                                                                                                                    |
| 2.2. Alterações de Regras de Validação ......................................................................................6                                                                                       |                                                                                                                                    |
| 2.2.1. Criação da regra de validação B25c-10 e B25c-20 .........................................................................6                                                                                    |                                                                                                                                    |
| 2.2.2. Criação da regra de validação YA02-50 ..........................................................................................6                                                                             |                                                                                                                                    |
| 2.2.3. Criação da regra de validação YA05-20 ..........................................................................................6                                                                             |                                                                                                                                    |
| 2.2.4. Criação das regras de validação YB01-10, YB01-20 e YB02-10 ....................................................6                                                                                              |                                                                                                                                    |
| 2.3. Alterações introduzidas na versão 1.10                                                                                                                                                                          | ................................................................................6                                                  |
| 2.4. Alterações introduzidas na versão 1.20 ................................................................................7                                                                                        |                                                                                                                                    |
| 2.5. Alterações introduzidas na versão 1.30                                                                                                                                                                          | ................................................................................7                                                  |
| 2.6. Alterações introduzidas na versão 1.31                                                                                                                                                                          | ................................................................................7                                                  |
| 3. Leiaute da Nota Fiscal Eletrônica ................................................................................................8                                                                               |                                                                                                                                    |
| 3.1. Grupo B. Identificação da Nota Fiscal eletrônica...................................................................8                                                                                            |                                                                                                                                    |
| 3.2. Grupo YA. Informações de Pagamento.................................................................................8                                                                                            |                                                                                                                                    |
| 3.3. Grupo YB. Informações do Intermediador da Transação ......................................................9                                                                                                     |                                                                                                                                    |
| 4. Detalhamento das Validações- Autorização ..............................................................................10                                                                                         |                                                                                                                                    |
| 4.1. B. Identificação da Nota Fiscal eletrônica............................................................................10                                                                                        |                                                                                                                                    |
| 4.2. I. Produtos e Serviços.........................................................................................................10                                                                               |                                                                                                                                    |
| 4.3. YA. Informações de Pagamento .........................................................................................10                                                                                        |                                                                                                                                    |
| 4.4. YB. Informações do Intermediador da Transação ...............................................................11                                                                                                 |                                                                                                                                    |
| 5. Novos códigos de Rejeição .......................................................................................................11                                                                               |                                                                                                                                    |
| 6. Orientações de preenchimento do Intermediador da transação e CNPJ da instituição                                                                                                                                  | de                                                                                                                                 |
| pagamento. ...................................................................................................................................12                                                                     |                                                                                                                                    |
| 6.1. Conceito de operação com intermediador da transação .....................................................12 6.2. Diferença entre CNPJ do Intermediador e CNPJ da instituição de pagamento ...................12 |                                                                                                                                    |

## Controle de Versões

|   Versão | Publicação     | Descrição                                                                                                                                                                                      |
|----------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     1.00 | Setembro/2020  | Publicação da NT.                                                                                                                                                                              |
|     1.10 | Fevereiro/2021 | Inclusão das regras YB01-10, YB01-20 e YB02-10 para modelo 65 e alteração nas regras B25c-10, YA02-50 e I08-90                                                                                 |
|     1.20 | Março/2021     | Inclusão das regras YA06-10, YA02-60 e YA02a-10. Alterada data de homologação para regra B25c-10, alterado campo tPag para utilizar tabela externa e alterada regra YA02-50 que foi eliminada. |
|     1.30 | Julho/2021     | Alteração na regra B25c-10 para exigir o campo indIntermed somente para notas de saída com finalidade normal e o prazo de entrada em produção da regra passou para 04/04/2022                  |
|     1.31 | Setembro/2022  | Alteração da regra I08-90 para considerar local de entrega e retirada                                                                                                                          |

## Histórico de Alterações / Cronograma

|   Versão | Histórico de atualizações                                                                                                                                                                                                             | Implantação Teste   | Implantação Produção   |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|------------------------|
|     1.00 | Criação de campos e Regras de Validação - seção 2 desta NT                                                                                                                                                                            | 01/02/2021          | 05/04/2021             |
|     1.10 | Prazo de implantação desta NT v1.00 e v.1.10 para SV-AN, SP, MG e GO                                                                                                                                                                  | 01/03/2021          | 05/04/2021             |
|     1.10 | Inclusão das regras YB01-10, YB01-20 e YB02-10 para modelo 65                                                                                                                                                                         | 01/03/2021          | 05/04/2021             |
|     1.10 | Regra YA02-50 , observação 2                                                                                                                                                                                                          | 01/03/2021          | 05/04/2021             |
|     1.10 | Regra B25c-10, observação 2                                                                                                                                                                                                           | 05/04/2021          | 01/09/2021             |
|     1.10 | Regra I08-90, observação a critério da UF                                                                                                                                                                                             | 01/03/2021          | 05/04/2021             |
|     1.20 | Regras YA02-60, YA06-10 e B25c-10, YA02a-10 e YA02a-20, inclusão do campo YA02a                                                                                                                                                       | Até 03/05/2021      | 01/09/2021             |
|     1.20 | Regra YA02-50 foi eliminada                                                                                                                                                                                                           | Até 03/05/2021      | -                      |
|     1.30 | Alterada a regra B25c-10                                                                                                                                                                                                              | Até 23/08/2021      | 04/04/2022             |
|     1.31 | * Os campos B25c (indIntermed) e o grupo de intermediador (infIntermed) YB01 estão disponíveis desde 05/04/2021 em produção, porém, a validação da regra B25c-10 ocorrerá somente a partir do dia 04/04/2022. Alterada a regra I08-90 | Até 03/10/2022      | Até 10/10/2022         |

## 1. Resumo

Essa Nota Técnica divulga novos campos e regras de validação para a NF-e/NFC-e versão 4.0, visando a adequação ao disposto no Ajuste SINIEF 21/2020 e 22/2020, envolvendo a identificação do intermediador ou agenciador da operação.

O prazo previsto para a implementação das mudanças é:

- o Ambiente de Homologação (ambiente de teste das empresas): 01/02/2021
- o Ambiente de Produção: 05/04/2021

Para os ambientes autorizadores SV-AN, SP, GO, MG os prazos previstos para a Nota Técnica 2020.006 v1.00 e v1.10 são:

- o Ambiente de Homologação (ambiente de teste das empresas): 01/03/2021
- o Ambiente de Produção: 05/04/2021

O prazo previsto para a Nota Técnica 2020.006 v1.20 é:

- o Ambiente de Homologação (ambiente de teste das empresas): até 03/05/2021
- o Ambiente de Produção: 01/09/2021

* Os campos B25c (indIntermed) e o grupo de intermediador (infIntermed) YB01 estarão disponíveis a partir 05/04/2021 em produção, porém, a validação ocorrerá somente a partir do dia 01/09/2021.

O prazo previsto para a Nota Técnica 2020.006 v1.30 é:

- o Ambiente de Homologação (ambiente de teste das empresas): até 23/08/2021
- o Ambiente de Produção: 04/10/2021

*  Os  campos B25c (indIntermed) e o grupo de intermediador (infIntermed) YB01 estão disponíveis desde 05/04/2021 em produção, porém, a validação da regra B25c-10 ocorrerá somente a partir do dia 04/04/2022.

O prazo previsto para a Nota Técnica 2020.006 v1.31 é:

- o Ambiente de Homologação (ambiente de teste das empresas): até 03/10/2022

- o Ambiente de Produção: 10/10/2022

2. Visão Geral
2. 2.1. Alterações de Campos

![Image](assets/image_000004_30f1fab1951c71251b5a14f35df296d8e98a08666664a99a715866d398790ab3.png)

## 2.1.1. Criação do campo indicativo do Intermediador/Marketplace (indIntermed)

Inclusão do campo de indicativo da operação com intermediador/marketplace, que será obrigatório informar quando o indicador de presença for 1=Operação presencial; 2=Operação não presencial, pela Internet; 3=Operação não presencial, Teleatendimento; 4=NFC-e em operação com entrega a domicílio; ou 9=Operação não presencial, outros.

## 2.1.2. Alteração no grupo YA (Informações de Pagamento)

- Alteração da descrição do campo YA05 para 'CNPJ da instituição de pagamento' e na observação alterada para 'Informar o CNPJ da instituição de pagamento, adquirente ou subadquirente. Caso o pagamento seja processado pelo intermediador da transação, informar o CNPJ deste.
- Alteração do campo meio de pagamento YA02, incluindo os códigos: 16=Depósito Bancário, 17=Pagamento Instantâneo (PIX), 18=Transferência bancária, Carteira Digital, 19=Programa de fidelidade, Cashback, Crédito Virtual.

## 2.1.3. Inclusão do grupo YB (Informações do Intermediador da Transação)

Inclusão de campos com as informações do intermediador da transação: CNPJ do Intermediador da Transação, Identificador Cadastro Intermediador

## 2.2. Alterações de Regras de Validação

## 2.2.1. Criação da regra de validação B25c-10 e B25c-20

Regras de validação criadas para preenchimento do campo indPres com os códigos:

- 1=Operação presencial;
- 2=Operação não presencial, pela Internet;
- 3=Operação não presencial, Teleatendimento;
- 4=NFC-e em operação com entrega a domicílio;
- 9=Operação não presencial, outros.

## 2.2.2. Criação da regra de validação YA02-50

Regra de validação para impedir o preenchimento do meio de pagamento como '99 - Outros'

## 2.2.3. Criação da regra de validação YA05-20

Regra de validação para impedir o preenchimento errado do campo CNPJ da instituição de pagamento.

## 2.2.4. Criação das regras de validação YB01-10, YB01-20 e YB02-10

Regras para verificar o preenchimento do grupo Informações do Intermediador da Transação.

## 2.3. Alterações introduzidas na versão 1.10

![Image](assets/image_000005_30f1fab1951c71251b5a14f35df296d8e98a08666664a99a715866d398790ab3.png)

## Projeto Nota Fiscal Eletrônica

NT 2020.006

Inclusão das regras YB01-10, YB01-20 e YB02-10 para serem aplicadas na Nota Fiscal de Consumidor eletrônica, modelo 65.

Criada observação 2 na regra B25c-10 para se aplicar na Nota Fiscal Avulsa eletrônica a partir de 05/04/2021 para homologação e 01/09/2021 para produção.

Criada observação 2 na regra YA02-50 para não se aplicar à Nota Fiscal eletrônica avulsa emitida por Produtor Primário.

Correção no tamanho do campo YB03, idCadIntTran para ser de 2 a 60 caracteres.

Alterada a observação do campo YA05.

Alterada a regra B25c-10 e B25c-20 para considerar indPres=1 (Operação presencial).

Regra I08-90 passou a ser a critério da UF.

## 2.4. Alterações introduzidas na versão 1.20

Inclusão da regra YA06-10 que verifica se o código da bandeira de cartão de crédito/débito existe na tabela publicada no portal nacional.

Inclusão da regra YA02-60 que verifica se o código do meio de pagamento existe na tabela publicada no portal nacional.

Alterado o campo meio de pagamento (YA02, tPag) para utilizar a tabela de códigos dos meios de pagamentos publicada no portal nacional.

Alterada a regra YA02-50 que ficou desativada.

Alterada a regra B25c-10, retirando a obrigatoriedade de preenchimento do campo Indicativo do Intermediador (tag: indIntermed) quando indPres=1, para não ter um grande impacto na NF-e/NFC-e, tendo em vista o grande volume de operações presenciais sem intermediador.

Se em alguma operação presencial (indPres=1) houver intermediador, deve a empresa preencher indIntermed=1 e as informações do intermediador, por força da legislação tributária, mas não sendo obrigada pela regra de validação. Alterada a data de homologação para 03/05/2021. Corrigido a descrição da regra YB01-20 para considerar o Indicador do Intermediador.

Criação do campo Descrição do Meio de Pagamento (YA02a, xPag) para preenchimento do meio de pagamento quando for utilizado o código do meio de pagamento 99-outros

Inclusão da regra YA02a-10 e YA02a-20 que verifica se foi preenchida a descrição do meio de pagamento quando informado o meio de pagamento 99outros.

Incluído o capítulo 6 com orientações sobre o intermediador da transação.

## 2.5. Alterações introduzidas na versão 1.30

Alterada a regra B25c-10 para exigir o campo indIntermed quando for nota fiscal de saída e finalidade de emissão normal e o prazo de entrada em produção da  regra  passou  para  04/04/2022.  Incluído  alguns  CFOPs  na  exceção,  principalmente  para  não  se  exigir  quando  for  operação  de  energia  elétrica  e comunicação.

## 2.6. Alterações introduzidas na versão 1.31

Alterada a regra I08-90 para considerar o local de entrega e retirada, permitindo assim CFOP de operação interestadual, para operações com destino físico sendo interestadual.

![Image](assets/image_000006_30f1fab1951c71251b5a14f35df296d8e98a08666664a99a715866d398790ab3.png)

## 3. Leiaute da Nota Fiscal Eletrônica

## 3.1. Grupo B. Identificação da Nota Fiscal eletrônica

|     # | ID   | Campo       | Descrição                              | Ele   | Pai   | Tipo   | Ocor.   |   Tam. | Observação                                                                                                                               |
|-------|------|-------------|----------------------------------------|-------|-------|--------|---------|--------|------------------------------------------------------------------------------------------------------------------------------------------|
| 29.03 | B25c | indIntermed | Indicador de intermediador/marketplace | E     | B01   | N      | 0-1     |      1 | 0=Operação sem intermediador (em site ou plataforma própria) 1=Operação em site ou plataforma de terceiros (intermediadores/marketplace) |

## 3.2. Grupo YA. Informações de Pagamento

| #       | ID    | Campo     | Descrição                         | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Observação                                                                                                                                                                                                                                                                         |
|---------|-------|-----------|-----------------------------------|-------|-------|--------|---------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 398.01  | YA01  | pag       | Grupo de Informações de Pagamento | G     | A01   |        | 1-1     |        | Obrigatório o preenchimento do Grupo Informações de Pagamento para NF-e e NFC-e. Para as notas com finalidade de Ajuste ou Devolução o campo Meio de Pagamento deve ser preenchido com 90=Sem Pagamento.                                                                           |
| 398.10  | YA01a | detPag    | Grupo Detalhamento do Pagamento   | G     | YA01  |        | 1-100   |        |                                                                                                                                                                                                                                                                                    |
| 398.11  | YA01b | indPag    | Indicador da Forma de Pagamento   | E     | YA01a | N      | 0-1     | 1      | 0=Pagamento à Vista 1= Pagamento a Prazo                                                                                                                                                                                                                                           |
| 398.12  | YA02  | tPag      | Meio de pagamento                 | E     | YA01a | N      | 1-1     | 2      | Utilizar a Tabela de códigos dos meios de pagamentos publicada no Portal Nacional da Nota Fiscal Eletrônica.                                                                                                                                                                       |
| 398.12a | YA02a | xPag      | Descrição do Meio de Pagamento    | E     | YA01a | C      | 0-1     | 2-60   | Descrição do meio de pagamento. Preencher informando o meio de pagamento utilizado quando o código do meio de pagamento for informado como 99-outros.                                                                                                                              |
| 398.13  | YA03  | vPag      | Valor do Pagamento                | E     | YA01a | N      | 1-1     | 13v2   |                                                                                                                                                                                                                                                                                    |
| 398.20  | YA04  | card      | Grupo de Cartões                  | G     | YA01a |        | 0-1     |        |                                                                                                                                                                                                                                                                                    |
| 398.21  | YA04a | tpIntegra | Tipo de Integração para pagamento | E     | YA04  | N      | 1-1     | 1      | Tipo de Integração do processo de pagamento com o sistema de automação da empresa: 1=Pagamento integrado com o sistema de automação da empresa (Ex.: equipamento TEF, Comércio Eletrônico) 2= Pagamento não integrado com o sistema de automação da empresa (Ex.: equipamento POS) |
| 398.22  | YA05  | CNPJ      | CNPJ da instituição de pagamento  | E     | YA04  | C      | 0-1     | 14     | Informar o CNPJ da instituição de pagamento, adquirente ou subadquirente. Caso o pagamento seja processado pelo intermediador da transação, informar o CNPJ do intermediador.                                                                                                      |

![Image](assets/image_000007_30f1fab1951c71251b5a14f35df296d8e98a08666664a99a715866d398790ab3.png)

NT 2020.006

![Image](assets/image_000008_30f1fab1951c71251b5a14f35df296d8e98a08666664a99a715866d398790ab3.png)

|      # | ID   | Campo   | Descrição                                                        | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Observação                                                                                                                           |
|--------|------|---------|------------------------------------------------------------------|-------|-------|--------|---------|--------|--------------------------------------------------------------------------------------------------------------------------------------|
| 398.23 | YA06 | tBand   | Código da bandeira da operadora de cartão de crédito e/ou débito | E     | YA04  | N      | 0-1     | 2      | Utilizar a Tabela de Códigos das Operadoras de cartão de crédito e/ou débito publicada no Portal Nacional da Nota Fiscal Eletrônica. |
| 398.24 | YA07 | cAut    | Número de autorização da operação cartão de crédito e/ou débito  | E     | YA04  | C      | 0-1     | 1-20   | Identifica o número da autorização da transação da operação com cartão de crédito e/ou débito                                        |
| 398.25 | YA09 | vTroco  | Valor do troco                                                   | E     | YA01  | N      | 0-1     | 13v2   | Valor do troco                                                                                                                       |

## 3.3. Grupo YB. Informações do Intermediador da Transação

|      # | ID   | Campo        | Descrição                                                                                                                 | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Observação                                                                                                                                                                   |
|--------|------|--------------|---------------------------------------------------------------------------------------------------------------------------|-------|-------|--------|---------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 398.26 | YB01 | infIntermed  | Grupo de Informações do Intermediador da Transação                                                                        | G     | A01   |        | 0-1     |        | Obrigatório o preenchimento do Grupo de Informações do Intermediador da Transação nos casos de 'operação não presencial pela internet em site de terceiros (intermediadores) |
| 398.27 | YB02 | CNPJ         | CNPJ do Intermediador da Transação (agenciador, plataforma de delivery, marketplace e similar) de serviços e de negócios. | E     | YB01  | N      | 1-1     | 14     | Informar o CNPJ do Intermediador da Transação (agenciador, plataforma de delivery, marketplace e similar) de serviços e de negócios.                                         |
| 398.28 | YB03 | idCadIntTran | Identificador cadastrado no intermediador                                                                                 | E     | YB01  | C      | 1-1     | 2-60   | Nome do usuário ou identificação do perfil do vendedor no site do intermediador (agenciador, plataforma de delivery, marketplace e similar) de serviços e de negócios.       |

![Image](assets/image_000009_a27e3869843732de87b9cf2e6974679c348e50668ea26a2c26a30e1168e2e134.png)

## 4. Detalhamento das Validações- Autorização

## 4.1. B. Identificação da Nota Fiscal eletrônica

| Campo-Seq   | Modelo   | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Aplic.   |   Msg | Efeito   | Descrição Erro                                            |
|-------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|-----------------------------------------------------------|
| B25c-10     | 55/65    | Se informado indicativo de presença, tag: indPres, IGUAL a 1, 2, 3, 4 ou 9 e Tipo de operação, tag: tpNF, IGUAL 1-Saída e Finalidade de emissão, tag: finNFe, IGUAL 1-NF-e normal. - Obrigatório o preenchimento do campo Indicativo do Intermediador (tag: indIntermed) Observação 1: Regra válida a partir de 23/08/2021 para homologação e 04/04/2022 para produção Observação 2: Regra válida para Nota Fiscal Avulsa eletrônica a partir de 03/05/2021 para homologação e 01/09/2021 para produção Exceção 1: Regra não se aplica para os seguintes CFOP: 5205, 5206, 5207, 5251, 5252, 5253, 5254, 5255, 5256, 5257, 5258, 5301, 5302, 5303, 5304, 5305, 5306, 5307. | Obrig.   |   434 | Rej.     | Rejeição: NF-e sem indicativo do intermediador            |
| B25c-20     | 55/65    | Se Informado indicativo de presença, tag: indPres, DIFERENTE de 1, 2, 3, 4 ou 9 - Proibido o preenchimento do campo Indicativo do Intermediador igual a 1 (tag: indIntermed=1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Obrig.   |   435 | Rej.     | Rejeição: NF-e não pode ter o indicativo do intermediador |

## 4.2. I. Produtos e Serviços

| Campo-Seq   |   Modelo | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                               |
|-------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|----------------------------------------------------------------------------------------------|
| I08-90      |       55 | CFOP é de operação interestadual (inicia por 2 ou 6) e UF emitente = UF destinatário e CNPJ/CPF emissor diferente do CNPJ/CPF destinatário (NT 2010/004) Exceção 1: Se a tag UFCons (id:LA06) foi informada com UF diversa do emitente: CFOP iniciado com 2 ou 6 é válido. (NT 2010/010) Exceção 2: Se [UF emitente = UF destinatário] e [a tag finNFe (id:B25) indicar que esta é uma nota de ajuste (=3)]: será aceito o CFOP 6206 Exceção 3: A regra de validação acima não se aplica se informada UF do local de entrega (tag: entrega/UF) diferente da UF do emitente (tag: emit/enderEmit/UF). Exceção 4: A regra de validação não se aplica se informada UF do local de retirada (tag: retirada/UF) diferente da UF do destinatário (tag: enderDest/UF); Observação: Regra de validação opcional, a critério da UF | Facul.   |   523 | Rej.     | Rejeição: CFOP não é de Operação Estadual e UF emitente igual à UF destinatário [nItem: 999] |

## 4.3. YA. Informações de Pagamento

![Image](assets/image_000010_30f1fab1951c71251b5a14f35df296d8e98a08666664a99a715866d398790ab3.png)

NT 2020.006

![Image](assets/image_000011_30f1fab1951c71251b5a14f35df296d8e98a08666664a99a715866d398790ab3.png)

| Campo-Seq   | Modelo   | Regra de Validação                                                                                                                                                                                                                                                                                                 | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                 |
|-------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|--------------------------------------------------------------------------------|
| YA02-50     | 55/65    | Informado meio de pagamento tPag= 99 'Outros' Observação 1: Regra válida a partir de 01/02/2021 para homologação e 01/09/2021 para produção Observação 2: Regra de validação não se aplica para Nota Fiscal eletrônica Avulsa emitida por Produtor Primário                                                        | Obrig.   |   436 | Rej.     | Rejeição: Informado 99-Outros como meio de pagamento                           |
| YA02-60     | 55/65    | Verificar se o código do meio de pagamento (tag: tPag) existe na Tabela de códigos dos meios de pagamentos publicada no Portal Nacional da Nota Fiscal Eletrônica Observação 1: Regra válida a partir de 03/05/2021 para homologação e 01/09/2021 para produção                                                    | Obrig.   |   436 | Rej.     | Rejeição: Código do meio de pagamento inexistente.                             |
| YA02a-10    | 55/65    | Quando o código do meio de pagamento (tag: tPag) for preenchido com o código 99-outros, obrigatório o preenchimento da descrição do meio de pagamento (tag: xPag)                                                                                                                                                  | Obrig.   |   441 | Rej.     | Rejeição: Descrição do pagamento obrigatória para meio de pagamento 99- outros |
| YA02a-20    | 55/65    | Quando o código do meio de pagamento for diferente 99-outros (tag: tPag<>99), proibido o preenchimento da descrição do meio de pagamento (tag: xPag)                                                                                                                                                               | Obrig    |   442 | XXX      | Rejeição: Descrição do pagamento não permitida.                                |
| YA05-20     | 55/65    | Se informado o CNPJ da instituição de pagamento • Verificar CNPJ com zeros, nulo ou DV inválido                                                                                                                                                                                                                    | Obrig.   |   437 | Rej.     | Rejeição: CNPJ da instituição de pagamento inválido                            |
| YA06-10     | 55/65    | Verificar se o Código da bandeira de cartão de crédito e/ou débito (campo: tBand) existe na tabela de códigos das operadoras de cartão de crédito e/ou débito publicada no Portal Nacional da Nota Fiscal Eletrônica Observação 1: Regra válida a partir de 03/05/2021 para homologação e 01/09/2021 para produção | Obrig.   |   443 | Rej.     | Rejeição: Código da bandeira de cartão de crédito e/ou débito inexistente.     |

## 4.4. YB. Informações do Intermediador da Transação

| Campo-Seq   | Modelo   | Regra de Validação                                                                                                                                                                                                                                      | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                                   |
|-------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|------------------------------------------------------------------------------------------------------------------|
| YB01-10     | 55/65    | Se informado Indicador do Intermediador IGUAL a ' 1=Operação em site ou plataforma de terceiros (intermediadores/marketplace)' (indIntermed=1) • Obrigatório o preenchimento das Informações do Intermediador da Transação (tag: infIntermed)           | Obrig.   |   438 | Rej.     | Rejeição: Obrigatória as informações do intermediador da transação para operação por site de terceiros           |
| YB01-20     | 55/65    | Se informado Indicador do Intermediador DIFERENTE de ' 1=Operação em site ou plataforma de terceiros (intermediadores/marketplace)' (indIntermed<>1) • Não é permitido o preenchimento das Informações do Intermediador da Transação (tag: infIntermed) | Obrig.   |   439 | Rej.     | Rejeição: Informações do intermediador da transação para operação por site de terceiros preenchido indevidamente |
| YB02-10     | 55/65    | Se informada o CNPJ do intermediador da transação • Verificar CNPJ com zeros, nulo ou DV inválido                                                                                                                                                       | Obrig.   |   440 | Rej.     | Rejeição: CNPJ do intermediador da transação inválido                                                            |

## 5. Novos códigos de Rejeição

## Projeto Nota Fiscal Eletrônica

NT 2020.006

![Image](assets/image_000012_7de981e6d876980ce53655a6a69033462fac9ba15d37229e393f9ebe9571e215.png)

|   CÓDIGO | MOTIVO DE NÃO ATENDIMENTO DA SOLICITAÇÃO                                                                         |
|----------|------------------------------------------------------------------------------------------------------------------|
|      434 | Rejeição: NF-e sem indicativo do intermediador                                                                   |
|      435 | Rejeição: NF-e não pode ter o indicativo do intermediador                                                        |
|      436 | Rejeição: Informado 99-Outros como meio de pagamento                                                             |
|      436 | Rejeição: Código do meio de pagamento inexistente.                                                               |
|      437 | Rejeição: CNPJ da instituição de pagamento inválido                                                              |
|      438 | Rejeição: Obrigatória as informações do intermediador da transação para operação por site de terceiros           |
|      439 | Rejeição: Informações do intermediador da transação para operação por site de terceiros preenchido indevidamente |
|      440 | Rejeição: CNPJ do intermediador da transação inválido                                                            |
|      441 | Rejeição: Descrição do pagamento obrigatória para meio de pagamento 99-outros                                    |
|      442 | Rejeição: Descrição do pagamento não permitida.                                                                  |
|      443 | Rejeição: Código da bandeira de operadora de cartão de crédito e/ou débito inexistente.                          |

## 6. Orientações de preenchimento do Intermediador da transação e CNPJ da instituição de pagamento.

## 6.1. Conceito de operação com intermediador da transação

Os Ajustes SINIEF 21/2020 e 22/2020 introduziram a exigência da identificação do intermediador da transação comercial na NF-e e NFC-e. Sendo assim, foram criados 4 campos na NF-e/NFC-e, sendo eles: indIntermed (B25c), infIntermed (YB01), CNPJ (YB02) e idCadIntTran (YB03).

O campo Indicador de intermediador/marketplace (indIntermed) é uma 'flag' utilizada para o emitente da NF-e/NFC-e declarar quando a operação/venda ocorreu em site/marketplace ou plataforma de terceiro. Quando declarado que a operação for intermediada (indIntermed=1) será necessário informar os campos do grupo infIntermed (YB01): CNPJ (YB02) e idCadIntTran (YB03).

Caracteriza-se  venda  com intermediador  (indIntermed=1),  quando  o  vendedor/emitente  da  NF-e/NFC-e (CNPJ14)  for  diferente  do  CNPJ14  do site/marketplace ou plataforma que realizou a venda.

Em algumas situações, a venda/operação pode ocorrer com mais de um marketplace/intermediador, por exemplo quando o  'Vendedor A' anuncia no 'Marketplace M1' e este anuncia no 'Marketplace M2'. Nesse caso, na hipótese do 'Marketplace M1' ter enviado a informação para o 'Vendedor A', na NFe deve ser informado o CNPJ do 'Marketplace M1'.

Em resumo, independente da cadeia de plataformas envolvidas, deve-se informar o CNPJ do intermediador (campo YB02) de quem que enviou a informação da venda para o vendedor/emitente da NF-e/NFC-e.

## 6.2. Diferença entre CNPJ do Intermediador e CNPJ da instituição de pagamento

Não se deve confundir o CNPJ do intermediador da transação (YB02), com o CNPJ da instituição de pagamento (YA05). Porém, em algumas situações poderá ser o mesmo CNPJ. Por exemplo: caso o intermediador da transação seja o responsável por fazer o pagamento ao vendedor (emitente da NF-e), deve ser informado no campo CNPJ da instituição de pagamento o CNPJ do intermediador.

Projeto

## Nota Fiscal Eletrônica

NT 2020.006

Portanto, para efeitos do CNPJ da instituição de pagamento, deve ser informada a instituição/empresa que fez o repasse de pagamento para o vendedor/remetente. Em outras palavras, o CNPJ do adquirente, subadquirente, intermediador ou instituição similar que efetuou o pagamento ao vendedor.

![Image](assets/image_000013_da658237aa376966f8852e3b33a045ef546498c0d51671456e896bc157e4975b.png)
## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt2020-006-v1-31-intermediador-e-marketplace/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt2020-006-v1-31-intermediador-e-marketplace/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt2020-006-v1-31-intermediador-e-marketplace.md)
- [Proveniência resumida](../../../../sources/provenance/nt2020-006-v1-31-intermediador-e-marketplace.json)

## Documentos relacionados
_Nenhum documento relacionado conhecido._
