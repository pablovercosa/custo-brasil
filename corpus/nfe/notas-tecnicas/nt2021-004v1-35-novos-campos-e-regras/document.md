---
title: "Projeto Nota Fiscal Eletrônica"
slug: "nt2021-004v1-35-novos-campos-e-regras"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "e33f067c25a024e3cddd99162baa337eaa7c090f4476c44af394059de3e3ae16"
converted_at_utc: "2026-06-25T16:52:09.975861+00:00"
status: "published"
type: "nota_tecnica"
---
![Image](assets/image_000000_6c545e385dc554d4f2538dc5f2f8e123229188ad3a37c64853552479f699396f.png)

![Image](assets/image_000001_5dd5d5e16748c7abcded3a0035d3a12ebd8073cdc66cfc62ca495386dd8ab477.png)

## Projeto Nota Fiscal Eletrônica

Nota Técnica 2021.004

Regras de Validação e Novos Campos NT 2021.004 v1.34 - Regras de Validação e Novos Campos

![Image](assets/image_000002_dcc3c7cc916b9434e700acdd56cf2f07d67a194b320d67c11f0c44c610574156.png)

![Image](assets/image_000003_b1eeba97115b031a27671ec58f09a7d4eb840d55032020fa8409bd25e4cdc9a1.png)

## Sumário

| Controle de Versões ............................................................................................................................4                                                                                                                                              | Controle de Versões ............................................................................................................................4                                                                                                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Histórico de Alterações / Cronograma..................................................................................................4 1. Resumo ...........................................................................................................................................5 | Histórico de Alterações / Cronograma..................................................................................................4 1. Resumo ...........................................................................................................................................5 |
| 1.1. Alterações Introduzidas na Versão 1.10 ....................................................................................5                                                                                                                                                              | 1.1. Alterações Introduzidas na Versão 1.10 ....................................................................................5                                                                                                                                                              |
| 1.2. Alterações Introduzidas na Versão 1.20 ....................................................................................5                                                                                                                                                              | 1.2. Alterações Introduzidas na Versão 1.20 ....................................................................................5                                                                                                                                                              |
| 1.3. Alterações Introduzidas na Versão 1.21 ....................................................................................5                                                                                                                                                              | 1.3. Alterações Introduzidas na Versão 1.21 ....................................................................................5                                                                                                                                                              |
| 1.4. Alterações Introduzidas na Versão 1.30 ....................................................................................5                                                                                                                                                              | 1.4. Alterações Introduzidas na Versão 1.30 ....................................................................................5                                                                                                                                                              |
| 1.5. Alterações Introduzidas na Versão 1.31 ....................................................................................6                                                                                                                                                              | 1.5. Alterações Introduzidas na Versão 1.31 ....................................................................................6                                                                                                                                                              |
| 1.6. Alterações Introduzidas na Versão 1.32 ....................................................................................6                                                                                                                                                              | 1.6. Alterações Introduzidas na Versão 1.32 ....................................................................................6                                                                                                                                                              |
| 1.7. Alterações Introduzidas na Versão 1.33 ....................................................................................6                                                                                                                                                              | 1.7. Alterações Introduzidas na Versão 1.33 ....................................................................................6                                                                                                                                                              |
| 1.8. Alterações Introduzidas na Versão 1.34 ....................................................................................6                                                                                                                                                              | 1.8. Alterações Introduzidas na Versão 1.34 ....................................................................................6                                                                                                                                                              |
| 1.9. Alterações Introduzidas na Versão 1.35 ....................................................................................6                                                                                                                                                              | 1.9. Alterações Introduzidas na Versão 1.35 ....................................................................................6                                                                                                                                                              |
| 2. Visão Geral......................................................................................................................................7                                                                                                                                          | 2. Visão Geral......................................................................................................................................7                                                                                                                                          |
| 2.1. Alterações de Campos ..............................................................................................................7                                                                                                                                                      | 2.1. Alterações de Campos ..............................................................................................................7                                                                                                                                                      |
| 2.1.1. Inclusão do grupo de FCP ST no Grupo de Partilha do ICMS (Grupo N10a). .................................                                                                                                                                                                                | 7                                                                                                                                                                                                                                                                                              |
| 2.1.2. Inclusão do Grupo Observações de uso livre do Fisco (para o item da NF-e).................................                                                                                                                                                                              | 7                                                                                                                                                                                                                                                                                              |
| 2.1.3. Inclusão do campo Tipo do Ato Concessório (campo: tpAto) no Grupo de Informações Adicionais                                                                                                                                                                                             | da ............................................................................................................. 7                                                                                                                                                                             |
| 2.2. Alterações de Regras de Validação...........................................................................................7                                                                                                                                                             | 2.2. Alterações de Regras de Validação...........................................................................................7                                                                                                                                                             |
| 2.2.1. Criação da Regra de Validação K01-10............................................................................................                                                                                                                                                        | 7 7                                                                                                                                                                                                                                                                                            |
| 2.2.2. Criação das Regras de Validação J19-10, J20-10 e J20-20............................................................. 2.2.3. Criação da Regra de Validação U06-10............................................................................................                            | 7                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                | 7                                                                                                                                                                                                                                                                                              |
| 2.2.4. Criação da Regra de Validação X03-30............................................................................................                                                                                                                                                        | 2.2.4. Criação da Regra de Validação X03-30............................................................................................                                                                                                                                                        |
| 2.2.5. Criação das Regras de Validação X04-30, X04-40 e X04-50 e X04-60 ...........................................                                                                                                                                                                            | 7                                                                                                                                                                                                                                                                                              |
| 2.2.6. Criação das Regras de Validação X04-70, X04-80, X04-90 e X04-100 ...........................................                                                                                                                                                                            | 8                                                                                                                                                                                                                                                                                              |
| 2.2.7. Criação da Regra de Validação Z13-10............................................................................................ 2.2.8. Alteração da Regra de Validação                                                                                                                 | 8                                                                                                                                                                                                                                                                                              |
| 3BA02-10.....................................................................................                                                                                                                                                                                                  | 8                                                                                                                                                                                                                                                                                              |
| 2.2.9. Criação das Regras de Validação 5AF15-10, 5AF15-20, 5AF15-30, 5BF15-10, 5BF15-20, .................................................................................................................................................                                                     | 5BF15-30 8                                                                                                                                                                                                                                                                                     |
| 2.3. Alterações introduzidas na versão 1.20.....................................................................................8                                                                                                                                                              | 2.3. Alterações introduzidas na versão 1.20.....................................................................................8                                                                                                                                                              |
| 2.3.1. Atualização da documentação dos campos tpComb, tpVeic e tpEspecie do Detalhamento de Veículos Novos ..................................................................................................................                                                                  | específico 8                                                                                                                                                                                                                                                                                   |
| 2.3.2. Alteração da Regra de Validação I08-140 ........................................................................................                                                                                                                                                        | 8                                                                                                                                                                                                                                                                                              |
| 2.3.3. Atualização da documentação da Regra K01-10..............................................................................                                                                                                                                                               | 8                                                                                                                                                                                                                                                                                              |
| 2.3.4. Atualização da documentação da Regra de Validação U06-10........................................................                                                                                                                                                                        | 8                                                                                                                                                                                                                                                                                              |
| 2.3.5. Criação das Regras de Validação Z02-10 e Z02-20.........................................................................                                                                                                                                                                | 8                                                                                                                                                                                                                                                                                              |
| 2.3.6. Alteração na forma de divulgação de mudanças do item 3.6.1 da NT 2019.001 v1.51 ...................                                                                                                                                                                                     | 9                                                                                                                                                                                                                                                                                              |
| 2.4. Alterações Introduzidas na Versão 1.21 ....................................................................................9                                                                                                                                                              | 2.4. Alterações Introduzidas na Versão 1.21 ....................................................................................9                                                                                                                                                              |
| 2.5. Alterações Introduzidas na Versão 1.30 ....................................................................................9                                                                                                                                                              | 2.5. Alterações Introduzidas na Versão 1.30 ....................................................................................9                                                                                                                                                              |
| 2.6. Alterações Introduzidas na Versão 1.31 ....................................................................................9 2.7. Alterações Introduzidas na Versão 1.32 ....................................................................................9                            | 2.6. Alterações Introduzidas na Versão 1.31 ....................................................................................9 2.7. Alterações Introduzidas na Versão 1.32 ....................................................................................9                            |
| 2.8. Alterações Introduzidas na Versão 1.33 ....................................................................................9                                                                                                                                                              | 2.8. Alterações Introduzidas na Versão 1.33 ....................................................................................9                                                                                                                                                              |
| 2.9. Alterações Introduzidas na Versão 1.34 ....................................................................................9 2.10. Alterações Introduzidas na Versão 1.35                                                                                                                 | 2.9. Alterações Introduzidas na Versão 1.34 ....................................................................................9 2.10. Alterações Introduzidas na Versão 1.35                                                                                                                 |
| ................................................................................10                                                                                                                                                                                                             | ................................................................................10                                                                                                                                                                                                             |
| 3. Leiaute da Nota Fiscal                                                                                                                                                                                                                                                                      | 3. Leiaute da Nota Fiscal                                                                                                                                                                                                                                                                      |
| Eletrônica...................................................................................................11                                                                                                                                                                                | Eletrônica...................................................................................................11                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                | novos..........................................................11 ................................................................................11                                                                                                                                           |
| 3.2. Grupo N10a. Grupo de Partilha do ICMS 3.3. Grupo K. Detalhamento Específico de Medicamento e de matérias-primas farmacêuticas......12 3.4. Grupo VA. Observações de uso livre (para o item da NF-e)....................................................13                                 | 3.2. Grupo N10a. Grupo de Partilha do ICMS 3.3. Grupo K. Detalhamento Específico de Medicamento e de matérias-primas farmacêuticas......12 3.4. Grupo VA. Observações de uso livre (para o item da NF-e)....................................................13                                 |
| 3.5. Grupo Z. Informações Adicionais da NF-e...............................................................................13                                                                                                                                                                  | 3.5. Grupo Z. Informações Adicionais da NF-e...............................................................................13                                                                                                                                                                  |

![Image](assets/image_000004_02fca134f695c2e32ef51f532b5e0eea994c0b11545d0be7d9613bdfc06c0e6e.png)

## Projeto Nota Fiscal Eletrônica

NT 2021.004 v1.34 - Regras de Validação e Novos Campos

![Image](assets/image_000005_02fca134f695c2e32ef51f532b5e0eea994c0b11545d0be7d9613bdfc06c0e6e.png)

| 4. Detalhamento das Validações-Autorização....................................................................................14   |                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| 4.1. I. Produtos e Serviços                                                                                                        | .............................................................................................................14                  |
| 4.2. JA. Detalhamento Específico de Veículos Novos                                                                                 | ....................................................................14                                                           |
| 4.3. K.                                                                                                                            | Item/Medicamentos.............................................................................................................15 |
| 4.4. U. Item/Tributo:                                                                                                              | ISSQN............................................................................................................15              |
| 4.4 X. Informações                                                                                                                 | do Transporte da NF-e.....................................................................................15                     |
| 4.5 Z.                                                                                                                             | Informação Adicional da NF-e..............................................................................................18     |
| 4.6 3A. Banco                                                                                                                      | de Dados: NF-e Referenciada.................................................................................18                   |
| 4.7 5A. Banco de Dados: Local de                                                                                                   | Retirada...................................................................................19                                    |
| 4.8 5B. Banco de Dados: Local de                                                                                                   | Entrega....................................................................................19                                    |
| 5. Novos códigos de                                                                                                                | Rejeição............................................................................................................20           |

## Controle de Versões

|   Versão | Publicação     | Descrição                                                        |
|----------|----------------|------------------------------------------------------------------|
|     1.00 | Novembro 2021  | Publicação da NT.                                                |
|     1.10 | Janeiro 2022   | Alteração do prazo de implementação da NT                        |
|     1.20 | Fevereiro 2022 | Inclusão das Regras Z02-10 e Z02-20 para modelo 65               |
|     1.30 | Maio 2022      | Alteração do tamanho do campo K01a e do prazo de implementação.  |
|     1.31 | Julho 2022     | Alterações de regras do grupo de Transportador e da Regra K01-20 |
|     1.32 | Julho 2022     | Alterações na documentação da Regra K01-20                       |
|     1.33 | Agosto 2022    | Postergação da implementação de algumas regras                   |
|     1.34 | Setembro 2022  | Suspensão da regra K01-10 e alteração na regra K01-20            |
|     1.35 | Outubro 2022   | Implementação futura para as regras Z02-10 e Z02-20              |

## Histórico de Alterações / Cronograma

|   Versão | Histórico de atualizações                                                                                                                                            | Implantação Teste   | Implantação Produção   |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|------------------------|
|     1.00 | Novas regras de validação e novos campos                                                                                                                             | 01/02/2022          | 04/04/2022             |
|     1.10 | Alteração do prazo de implementação de toda a NT                                                                                                                     | 14/03/2022          | 16/05/2022             |
|     1.20 | Inclusão das Regras Z02-10 e Z02-20 Alterações de documentação de campos e regras Alteração da Regra de Validação U06-10. Exceção adicionada à regra I08-140         | 14/03/2022          | 16/05/2022             |
|     1.21 | Inserida Observação nas Regras X04-50, X04-60, X04-90 e X04-100                                                                                                      | 08/04/2022          | 16/05/2022             |
|     1.30 | Alteração no prazo de entrada em Produção de toda a NT                                                                                                               | 14/03/2022          | 08/08/2022             |
|     1.31 | Alteração do texto das regras X04-50, X04-60, X04-90 e X04-100 Adicionada exceção na Regra K01-20                                                                    | Até 25/07/2022      | 12/09/2022             |
|     1.32 | Alterações na documentação da Regra K01-20                                                                                                                           | Até 25/07/2022      | 12/09/2022             |
|     1.33 | Suspensão da implementação das regras X04-50, X04-60, X04-90 e X04-100 (ver itens 1.7 e 2.8) e alteração na documentação das regras X04-30, X04-50, X04-80 e X04-100 | Até 12/09/2022      | 12/09/2022             |
|     1.34 | Suspensão da regra K01-10 e alteração na regra K01-20                                                                                                                | Até 23/09/2022      | Até 27/09/2022         |
|     1.35 | Altera para implementação futura as regras Z02-10 e Z02-20                                                                                                           | -                   | -                      |

![Image](assets/image_000006_8836b50d81a285debfbe4bfa65a2f17612aa7dbadc4cb8ec5ba6457a282b7e96.png)

## 1. Resumo

Essa Nota Técnica divulga novas regras de validação e atualiza regras existentes da NF-e/NFC-e versão 4.0.

O prazo previsto para a implementação das mudanças é:

- o Ambiente de Homologação (ambiente de teste das empresas): 01/02/2022
- o Ambiente de Produção
- : 04/04/2022

## 1.1. Alterações Introduzidas na Versão 1.10

A  versão  1.10  dessa  Nota  Técnica  traz  somente  novos  prazos  de  implementação,  sem  qualquer alteração em campos ou Regras de Validação.

O prazo previsto para a implementação das mudanças é:

- o Ambiente de Homologação (ambiente de teste das empresas): 14/03/2022
- o Ambiente de Produção : 16/05/2022

Toda a NT 2021.004 passa a ter esses prazos de implementação.

## 1.2. Alterações Introduzidas na Versão 1.20

A versão 1.20 dessa Nota Técnica traz a inclusão das Regras de Validação Z02-10 e Z02-20 aplicáveis ao modelo 65 e à UF: Santa Catarina. O prazo previsto para a entrada em homologação e produção destas  regras  se  encontra  na  descrição  delas.  Como  as  demais  alterações  são  meramente documentais ou sem impacto em novas rejeições, o prazo de implementação está mantido.

O prazo previsto para a implementação das mudanças é:

- o Ambiente de Homologação (ambiente de teste das empresas): 14/03/2022
- o Ambiente de Produção : 16/05/2022

## 1.3. Alterações Introduzidas na Versão 1.21

A versão 1.21 dessa Nota Técnica traz a inclusão de uma Observação nas Regras de Validação X0450, X04-60, X04-90 e X04-100. Como essas alterações visam reduzir o número de rejeições e não causarão impacto grande de desenvolvimento para as empresas, a data de Produção foi mantida para essa NT.

O prazo previsto para a implementação das mudanças é:

- o Ambiente de Homologação (ambiente de teste das empresas): 08/03/2022
- o Ambiente de Produção : 16/05/2022

## 1.4. Alterações Introduzidas na Versão 1.30

A versão 1.30 dessa Nota Técnica traz a alteração das datas de entrada em Produção de toda a Nota Técnica e adequação do tamanho do campo de Código de Produto da ANVISA (cProdANVISA) para aceitar também 11 caracteres, caso de alguns produtos farmacêuticos.

O prazo previsto para a implementação das mudanças é:

- o Ambiente de Homologação (ambiente de teste das empresas):14/03/2022
- o Ambiente de Produção : 08/08/2022

![Image](assets/image_000007_8836b50d81a285debfbe4bfa65a2f17612aa7dbadc4cb8ec5ba6457a282b7e96.png)

## 1.5. Alterações Introduzidas na Versão 1.31

A versão 1.31 dessa Nota Técnica modifica o texto de algumas regras do grupo de Informações do Transporte. Além disso, adiciona exceção na Regra K01-20, do grupo de medicamentos. Com  essas  alterações,  o  prazo  da  entrada  em  homologação  destas  alterações  fica  para  até 25/07/2022, enquanto o prazo de entrada em produção de TODA a NT, incluindo as alterações desta versão, fica para 12/09/2022:

- o Ambiente de Homologação (ambiente de teste das empresas): até 25/07/2022
- o Ambiente de Produção : 12/09/2022

## 1.6. Alterações Introduzidas na Versão 1.32

A  versão  1.32  dessa  Nota  Técnica  corrige  a  documentação  da  Regra  K01-20  para  melhorar  o entendimento.  Além  disso,  os  CFOP  da  Exceção  3  desta  mesma  regra  foram  substituídos  pelos corretos na operação de Venda para Entrega Futura. Como são alterações meramente documentais, o prazo da NT se mantém o mesmo da versão 1.31, ou seja:

- o Ambiente de Homologação (ambiente de teste das empresas): até 25/07/2022
- o Ambiente de Produção : 12/09/2022

## 1.7. Alterações Introduzidas na Versão 1.33

A versão 1.33 dessa Nota Técnica traz a suspensão do prazo de implementação das regras X04-50, X04-60, X04-90 e X04-100.

- o Ambiente de Homologação (ambiente de teste das empresas): até 12/09/2022
- o Ambiente de Produção: Implementação futura

Houve ainda alteração da documentação das regras X04-30, X04-50, X04-80 e X04-100.

Observação: O prazo de entrada em produção dessa NT permanece o mesmo: 12/09/2022, EXCETO para as regras X04-50, X04-60, X04-90 e X04-100.

## 1.8. Alterações Introduzidas na Versão 1.34

A versão 1.34 suspende o prazo de implementação da regra K01-10 e altera a documentação da regra K01-20

- o Ambiente de Homologação (ambiente de teste das empresas): até 23/09/2022
- o Ambiente de Produção: até 27/09/2022

Por se tratar de alteração para facilitar a emissão de notas, a desativação da regra K01-10 deverá ser imediata por parte dos ambientes autorizadores.

## 1.9. Alterações Introduzidas na Versão 1.35

A versão 1.35 altera para implementação futura as regras Z02-10 e Z02-20. Por  se  tratar  de  alteração  que  muda  para  implementação  futura  não  haverá  data  de  entrada  em

produção e homologação desta versão de nota técnica.

![Image](assets/image_000008_87f98b73fe7e446b1fdb93ad8b70ac790d0e1dfffda92589371edc1f75e04cd4.png)

## 2. Visão Geral

## 2.1. Alterações de Campos

## 2.1.1. Inclusão do grupo de FCP ST no Grupo de Partilha do ICMS (Grupo N10a).

Essa alteração tornou-se necessária com a publicação do Decreto 8.242 de 2021 do Estado do Paraná que institui a cobrança do Fundo de Combate à Pobreza nas operações com veículos automotores novos sujeitos a Substituição Tributária. Como não havia as tags  específicas de FCP neste grupo tornou-se  necessária  essa  alteração  que  poderá  ser  aproveitada  futuramente  para  outras  UF  que optarem por fazer esta cobrança.

## 2.1.2. Inclusão do Grupo Observações de uso livre do Fisco (para o item da NF-e)

Grupo criado para Observações de uso livre do Fisco e do Contribuinte, de forma semiestruturada, a exemplo do que ocorre no grupo de Informações Adicionais da NF-e ampliando a utilização para que possa ocorrer a nível de item.

## 2.1.3. Inclusão do campo Tipo do Ato Concessório (campo: tpAto) no Grupo de Informações Adicionais da NF-e (campo: infAdic)

Este campo, que fica por sua vez dentro do Grupo de Processo Referenciado (campo: procRef) visa trazer  uma  identificação  a  mais  para  os  Atos  Concessórios  cujo  indicador  da  origem  do  processo (campo: indProc) seja informado como originado na SEFAZ (indProc = 0).

## 2.2. Alterações de Regras de Validação

## 2.2.1. Criação da Regra de Validação K01-10

Regra de validação para obrigar o preenchimento do grupo de medicamento (campo: med) quando o código NCM do produto for de medicamento (NCMs que começam com 3001, 3002, 3003, 3004, 3005 e 3006).

## 2.2.2. Criação das Regras de Validação J19-10, J20-10 e J20-20

Regras de validação para verificar se o Tipo e Espécie do Veículo (campos tpVeic e espVeic) existem e são compatíveis entre si conforme Tabela de Tipo e Espécie de Veículo publicada no Portal Nacional da NF-e. Foi detectado que o preenchimento destes campos, que já existem há um bom tempo, não atende a tabela específica citada, e por isso torna-se necessária a validação.

## 2.2.3. Criação da Regra de Validação U06-10

Regra de Validação para verificar o correto preenchimento do campo Item da Lista de Serviços (campo: cListServ). Esse campo tinha seu preenchimento verificado pelo schema e passará a ser validado através de tabela a ser publicada no Portal Nacional da NF-e.

## 2.2.4. Criação da Regra de Validação X03-30

Regra de Validação para proibir o preenchimento do grupo de transporte (campo: transporta) quando foi informado na Modalidade do Frete que não houve transporte (campo: modFrete = 9).

## 2.2.5. Criação das Regras de Validação X04-30, X04-40 e X04-50 e X04-60

Regras de Validação para verificar o correto preenchimento do transportador (campo: transporta) no caso de Transporte Próprio por conta do Remetente (campo: modFrete = 3 ).

![Image](assets/image_000009_aee40fa54c541d677d09185322ffd51be00158e740bab37d003dd62a49230e21.png)

![Image](assets/image_000010_aee40fa54c541d677d09185322ffd51be00158e740bab37d003dd62a49230e21.png)

## 2.2.6. Criação das Regras de Validação X04-70, X04-80, X04-90 e X04-100

Regras de Validação para verificar o correto preenchimento do transportador (campo: transporta) no caso de Transporte Próprio por conta do Destinatário (campo: modFrete = 4).

## 2.2.7. Criação da Regra de Validação Z13-10

Regra para verificar o preenchimento correto do Tipo do Ato Concessório (campo: tpAto), no caso de Termo de Acordo ou Regime Especial validando o preenchimento de acordo com a Tabela de Padrões de Regime Especial de cada UF publicada na aba 'Documentos', opção 'Diversos' do Portal Nacional da NF-e (www.nfe.fazenda.gov.br).

## 2.2.8. Alteração da Regra de Validação 3BA02-10

Cria uma condição para que a exceção da regra não seja aplicada caso a NF-e referenciada tenha o Ano-Mês de emissão inferior a 1 mês da data da emissão da NF-e que a referência.

## 2.2.9. Criação das Regras de Validação 5AF15-10, 5AF15-20, 5AF15-30, 5BF15-10, 5BF15-20, 5BF15-30

Regras para verificar o correto preenchimento dos dados do Local de Entrega e do Local de Retirada, conforme CCC (Cadastro Centralizado de Contribuintes). Como esses grupos impactam na distribuição da NF-e, a informação precisa estar correta e de acordo com o cadastro de contribuintes de cada UF.

## 2.3.  Alterações introduzidas na versão 1.20

## 2.3.1. Atualização da documentação dos campos tpComb, tpVeic e tpEspecie do Detalhamento específico de Veículos Novos

Alterações meramente documentais, excluindo exemplos desatualizados que estavam presentes na Observação dos campos. Como o campo tpComb sempre aceitou valores numéricos e os campos tpVeic  e  tpEspecie  passarão  a  ser  validados  por  tabelas  externas,  tornaram-se  desnecessários  (e desatualizados) os exemplos.

## 2.3.2. Alteração da Regra de Validação I08-140

O Ajuste SINIEF nº 22/2021 trata da devolução simbólica de gás natural, e em seu inciso V da Clausula quarta pede que a NF-e de devolução seja emitida com CFOP 5.949 ou 6.949, conforme o caso. Ocorre que caso a devolução fosse feita dessa forma, a nota seria rejeitada pela redação anterior da Regra I08-140.  Portanto,  foi  inserida  exceção  nessa  regra  para  permitir  a  devolução  conforme  manda  o referido Ajuste.

## 2.3.3. Atualização da documentação da Regra K01-10

A Regra K01-10 havia sido publicada erroneamente como pertencente ao grupo I. Produtos e Serviços, quando o correto é o grupo K. Item/Medicamentos. Mais uma alteração meramente documental.

## 2.3.4. Atualização da documentação da Regra de Validação U06-10

O campo cListServ também é aplicado para o modelo 65, portanto a validação por tabela também deve ser aplicada para esse modelo de documento. Como se trata somente de uma troca da validação por schema pela validação por tabela, não há impacto para as empresas em seus processos.

## 2.3.5. Criação das Regras de Validação Z02-10 e Z02-20

Inclusão  das  Regras  Z02-10  e  Z02-20  para  o  modelo  65,  que  obrigam  o  preenchimento  das Informações Adicionais de Interesse do Fisco (campo:infAdFisco) com o mínimo de 251 caracteres para  os  contribuintes  de  Santa  Catarina.  Essas  regras  serão  válidas  a  partir  de  01/02/2023  em homologação e 03/04/2023 em produção.

![Image](assets/image_000011_529460152304a50603f1e40661fd7fe27fb9cfc92a4a3f5117df0d34447a7edf.png)

## 2.3.6.  Alteração na forma de divulgação de mudanças do item 3.6.1 da NT 2019.001 v1.51

O item 3.6.1 da NT 2019.001 v1.51 traz um detalhamento da aplicação de Regras de Validação do Código  de  Benefício  Fiscal.  Esse  detalhamento,  a  partir  dessa  NT,  não  será  mais  atualizado  via reedição de Nota Técnica. As futuras ativações que vierem a acontecer serão  publicadas em Informe Técnico, que visa atualizar critérios de aplicação de  Regras de Validação já existentes.

## 2.4. Alterações Introduzidas na Versão 1.21

Introdução de uma Observação nas Regras de Validação X04-50, X04-60, X04-90 e X04-100 para permitir a informação de CNPJ Base ou CPF do transportador igual ao do Emitente ou Destinatário conforme a modalidade do frete, quando a operação é com combustíveis. Essa alteração visa evitar Rejeições  pela  Regra  X04-10,  que  obriga  a  informação  do  Transportador  nas  operações  com indComb=2 conforme tabela de CFOP

## 2.5. Alterações Introduzidas na Versão 1.30

Alteração do tamanho do campo K01a (cProdANVISA) para aceitar também códigos de 11 caracteres, caso de alguns produtos farmacêuticos.

## 2.6. Alterações Introduzidas na Versão 1.31

Alterações no texto das regras X04-50, X04-60, X04-90 e X04-100. Essas alterações visam evitar rejeições em operações cuja contratação do transportador seja por conta do Remetente e a empresa contratada é uma filial do Destinatário, ou vice-versa.

Exceção  adicionada  na  Regra  K01-20.  Esta  regra  obrigava  o  preenchimento  do  grupo  de Rastreabilidade  de  produto  (tag:  rastro)  sempre  que  houvesse  o  preenchimento  do  Detalhamento Específico de Medicamentos (tag: med). No entanto, essa informação nem sempre está disponível quando envolve venda pela internet ou quando se trata da NF-e de devolução de mercadoria ou de venda para entrega futura.

Foi corrigida ainda a documentação das regras de validação J19-10, J20-10, J20-20 e U06-10 para adicionar o número do item, facilitando a identificação da rejeição.

## 2.7. Alterações Introduzidas na Versão 1.32

Alteração na documentação da Regra K01-20 para desambiguar as diferentes exceções.  Alterados ainda os CFOP da Exceção 3 para os de  venda para entrega futura.

## 2.8. Alterações Introduzidas na Versão 1.33

Suspensão do prazo de implementação das regras X04-50, X04-60, X04-90 e X04-100 em ambiente de homologação e implementação futura em ambiente de produção.

Foram ainda corrigidas as documentações das Regras de Validação X04-30, X04-50, X04-80 e X04100 para que elas se refiram ao id correto do campo CPF (id: C02a) do Destinatário nas operações de entrada (tpNF=0).

## 2.9. Alterações Introduzidas na Versão 1.34

A  versão  1.34  dessa  Nota  Técnica  traz  a  suspensão  da  regra  K01-10,  por  estar  exigindo  o preenchimento do grupo de medicamentos para produtos que não se enquadram como medicamentos. Também altera a regra K01-20 para se aplicar somente nas operações de saída, e não exigir o grupo de rastreabilidade nas operações de venda a ordem (CFOPs 5118, 6118, 5119, 6119, 5120 e 6120), ou quando for NFe de ajuste, complementar ou entrada.

NT 2021.004 v1.34 - Regras de Validação e Novos Campos

2.10. Alterações Introduzidas na Versão 1.35

A versão 1.35 dessa Nota Técnica traz somente a alteração para implementação futura das regras Z02-10 e Z02-20.

![Image](assets/image_000012_02fca134f695c2e32ef51f532b5e0eea994c0b11545d0be7d9613bdfc06c0e6e.png)

## 3. Leiaute da Nota Fiscal Eletrônica

## 3.1. Grupo JA. Detalhamento Específico de Veículos novos

| #   | ID   | Campo    | Descrição                      | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Observação                                         |
|-----|------|----------|--------------------------------|-------|-------|--------|---------|--------|----------------------------------------------------|
| 129 | J01  | veicProd | Detalhamento de Veículos novos | CG    | I90   |        | 1-1     |        | Informar apenas quando se tratar de veículos novos |
| 139 | J11  | tpComb   | Tipo de combustível            | E     | J01   | C      | 1-1     | 1 - 2  | Utilizar Tabela RENAVAM                            |
| ... | ...  | ...      | ...                            | ...   | ...   | ...    | ...     |        | ...                                                |
| 147 | J19  | tpVeic   | Tipo de Veículo                | E     | J01   | N      | 1-1     | 1 - 2  | Utilizar Tabela RENAVAM                            |
| 148 | J20  | espVeic  | Espécie de Veículo             | E     | J01   | N      | 1-1     | 1      | Utilizar Tabela RENAVAM                            |

## 3.2. Grupo N10a. Grupo de Partilha do ICMS

|      # | ID   | Campo    | Descrição                                                                                      | Ele   | Pai   | Tipo   | Ocor.   |   Tam. | Observação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------|------|----------|------------------------------------------------------------------------------------------------|-------|-------|--------|---------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 245.01 | N10a | ICMSPart | Grupo de Partilha do ICMS entre a UF de origem e UF de destino ou a UF definida na legislação. | CG    | N01   |        | 1-1     |        | Operação interestadual para consumidor final com partilha do ICMS devido na operação entre a UF de origem e a do destinatário, ou a UF definida na legislação. (Ex. UF da concessionária de entrega do veículo) (v2.0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 245.02 | N11  | orig     | Origem da mercadoria                                                                           | E     | N10a  | N      | 1-1     |      1 | 0 - Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8; 1 - Estrangeira - Importação direta, exceto a indicada no código 6; 2 - Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7; 3 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70%; 4 - Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam as legislações citadas nos Ajustes; 5 - Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40%; 6 - Estrangeira - Importação direta, sem similar nacional, constante em lista da CAMEX e gás natural; 7 - Estrangeira - Adquirida no mercado interno, sem similar nacional, constante lista CAMEX e gás natural. 8 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70%; |
| 245.03 | N12  | CST      | Tributação do ICMS                                                                             | E     | N10a  | N      | 1-1     |      2 | 10=Tributada e com cobrança do ICMS por substituição tributária; 90=Outros.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

![Image](assets/image_000013_2e9cdcac39774b1d072e3e38a2684a748682e24ca53e08a94a156e82f15e0ebe.png)

## Projeto Nota Fiscal Eletrônica

NT 2021.004 v1.33 - Regras de Validação e Novos Campos

![Image](assets/image_000014_903a93573ed064d2084510f59de7b4f4b4aa7d0fbe340ae4b3fcb7a91670d47d.png)

| #       | ID    | Campo    | Descrição                                           | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Observação                                                                                                                                                 |
|---------|-------|----------|-----------------------------------------------------|-------|-------|--------|---------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 245.04  | N13   | modBC    | Modalidade de determinação da BC do ICMS            | E     | N10a  | N      | 1-1     | 1      | 0=Margem Valor Agregado (%) 1=Pauta (Valor) 2=Preço Tabelado Máx. (valor) 3=Valor da operação                                                              |
| 245.05  | N15   | vBC      | Valor da BC do ICMS                                 | E     | N10a  | N      | 1-1     | 13v2   | (v2.0)                                                                                                                                                     |
| 245.06  | N14   | pRedBC   | Percentual da Redução de BC                         | E     | N10a  | N      | 0-1     | 3v2-4  | (v2.0)                                                                                                                                                     |
| 245.07  | N16   | pICMS    | Alíquota do imposto                                 | E     | N10a  | N      | 1-1     | 3v2-4  | (v2.0)                                                                                                                                                     |
| 245.08  | N17   | vICMS    | Valor do ICMS                                       | E     | N10a  | N      | 1-1     | 13v2   |                                                                                                                                                            |
| 245.09  | N18   | modBCST  | Modalidade de determinação da BC do ICMS ST         | E     | N10a  | N      | 1-1     | 1      | 0=Preço tabelado ou máximo sugerido 1=Lista Negativa (valor) 2=Lista Positiva (valor); 3=Lista Neutra (valor) 4=Margem Valor Agregado (%); 5=Pauta (valor) |
| 245.10  | N19   | pMVAST   | Percentual da margem de valor Adicionado do ICMS ST | E     | N10a  | N      | 0-1     | 3v2-4  | (v2.0)                                                                                                                                                     |
| 245.11  | N20   | pRedBCST | Percentual da Redução de BC do ICMS ST              | E     | N10a  | N      | 0-1     | 3v2-4  | (v2.0)                                                                                                                                                     |
| 245.12  | N21   | vBCST    | Valor da BC do ICMS ST                              | E     | N10a  | N      | 1-1     | 13v2   | (v2.0)                                                                                                                                                     |
| 245.13  | N22   | pICMSST  | Alíquota do imposto do ICMS ST                      | E     | N10a  | N      | 1-1     | 3v2-4  | (v2.0)                                                                                                                                                     |
| 245.14  | N23   | vICMSST  | Valor do ICMS ST                                    | E     | N10a  | N      | 1-1     | 13v2   | Valor do ICMS ST(v2.0)                                                                                                                                     |
| 245.14a | N23.1 | -x-      | Sequência XML                                       | G     | N10a  |        | 0-1     |        | Grupo opcional para informações do FCP retido por ST                                                                                                       |
| 245.14b | N23a  | vBCFCPST | Valor da Base de Cálculo do FCP ST                  | E     | N23.1 | N      | 1-1     | 13v2   | Informar o valor da Base de Cálculo do FCP retido por Substituição Tributária                                                                              |
| 245.14c | N23b  | pFCPST   | Percentual do FCP ST                                | E     | N23.1 | N      | 1-1     | 3v2-4  | Percentual relativo ao Fundo de Combate à Pobreza (FCP) retido por substituição tributária.                                                                |
| 245.14d | N23d  | vFCPST   | Valor do FCP ST                                     | E     | N23.1 | N      | 1-1     | 13v2   | Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) retido por substituição tributária.                                                             |
| 245.15  | N25   | pBCOp    | Percentual da BC operação própria                   | E     | N10a  | N      | 1-1     | 3v2-4  | Percentual para determinação do valor da Base de Cálculo da operação própria. (v2.0)                                                                       |
| 245.16  | N24   | UFST     | UF para qual é devido o ICMS ST                     | E     | N10a  | C      | 1-1     | 2      | Sigla da UF para qual é devido o ICMS ST da operação. Informar "EX" para Exterior. (v2.0)                                                                  |

## 3.3. Grupo K. Detalhamento Específico de Medicamento e de matérias-primas farmacêuticas

| #    | ID   | Campo       | Descrição                                                       | Ele   | Pai   | Tipo   | Ocor.   | Tam.    | Observação                                                                                                                                                                                                                             |
|------|------|-------------|-----------------------------------------------------------------|-------|-------|--------|---------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 152  | K01  | med         | Detalhamento de Medicamentos e de matérias-primas farmacêuticas | CG    | I90   |        | 1-1     |         | Informar apenas quando se tratar de medicamentos ou de matérias-primas farmacêuticas, permite ocorrências.                                                                                                                             |
| 152a | K01a | cProdANVISA | Código de Produto da ANVISA                                     | E     | K01   | C      | 1-1     | 6,11,13 | Utilizar o número do registro ANVISA ou preencher com o literal 'ISENTO', no caso de medicamento isento de registro na ANVISA ou quando o produto não possuir registro específico. (Incluído na NT2016.002. Atualizado na NT 2018.005) |

Projeto

Nota Fiscal Eletrônica

![Image](assets/image_000015_9d13660773437bad702a1654bdcad5d72186799c9e72b0e787b22dfcf2a14d66.png)

| #    | ID   | Campo          | Descrição                   | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Observação                                                                                                                                                                                             |
|------|------|----------------|-----------------------------|-------|-------|--------|---------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 152b | K01b | xMotivoIsencao | Motivo da isenção da ANVISA | E     | K01   | C      | 0-1     | 1-255  | Obs.: Para medicamento isento de registro na ANVISA, informar o número da decisão que o isenta, como por exemplo o número da Resolução da Diretoria Colegiada da ANVISA (RDC). (Criado na NT 2018.005) |
| 157  | K06  | vPMC           | Preço máximo consumidor     | E     | K01   | N      | 1-1     | 13v2   |                                                                                                                                                                                                        |

- 3.4. Grupo VA. Observações de uso livre (para o item da NF-e)
- 3.5. Grupo Z. Informações Adicionais da NF-e

| #    | ID   | Campo    | Descrição                                               | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Observação                                                                                                                           |
|------|------|----------|---------------------------------------------------------|-------|-------|--------|---------|--------|--------------------------------------------------------------------------------------------------------------------------------------|
| 325a | VA01 | obsItem  | Grupo de observações de uso livre (para o item da NF-e) | G     | H01   |        | 0-1     |        |                                                                                                                                      |
| 325b | VA02 | obsCont  | Grupo de observações de uso livre do Contribuinte       | G     | VA01  |        | 0-1     |        | Campo de uso livre do Contribuinte para o item da NF-e. Informar o nome do campo no atributo xCampo e o conteúdo do campo no xTexto. |
| 325c | VA03 | xCampo   | Identificação do campo                                  | A     | VA02  | C      | 1-1     | 1-20   | Identificação do campo                                                                                                               |
| 325d | VA04 | xTexto   | Conteúdo do campo                                       | E     | VA02  | C      | 1-1     | 1-60   | Conteúdo do campo                                                                                                                    |
| 325e | VA05 | obsFisco | Grupo de observações de uso livre do Fisco              | G     | VA01  |        | 0-1     |        | Campo de uso livre do Fisco para o item da NF-e. Informar o nome do campo no atributo xCampo e o conteúdo do campo no xTexto.        |
| 325f | VA06 | xCampo   | Identificação do campo                                  | A     | VA05  | C      | 1-1     | 1-20   | Identificação do campo                                                                                                               |
| 325g | VA07 | xTexto   | Conteúdo do campo                                       | E     | VA05  | C      | 1-1     | 1-60   | Conteúdo do campo                                                                                                                    |

| #     | ID   | Campo   | Descrição                                    | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Observação                                                                                                                                           |
|-------|------|---------|----------------------------------------------|-------|-------|--------|---------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [...] |      |         |                                              |       |       |        |         |        |                                                                                                                                                      |
| 401g  | Z10  | procRef | Grupo Processo referenciado                  | G     | Z01   |        | 0-100   |        | (NT 2012/003)                                                                                                                                        |
| 401h  | Z11  | nProc   | Identificador do processo ou ato concessório | E     | Z10   | C      | 1-1     | 1-60   | Identificador do processo ou ato concessório                                                                                                         |
| 401i  | Z12  | indProc | Indicador da origem do processo              | E     | Z10   | N      | 1-1     | 1      | 0=SEFAZ; 1=Justiça Federal; 2=Justiça Estadual; 3=Secex/RFB; 9=Outros                                                                                |
| 401j  | Z13  | tpAto   | Tipo do ato concessório                      | E     | Z10   | N      | 0-1     | 2      | Para origem do Processo na SEFAZ (indProc=0), informar o tipo de ato concessório: 08=Termo de Acordo; 10=Regime Especial; 12=Autorização específica; |

NT 2021.004 v1.33 - Regras de Validação e Novos Campos

## 4. Detalhamento das Validações-Autorização

## 4.1. I. Produtos e Serviços

| Campo-Seq   |   Modelo | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                |
|-------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|-----------------------------------------------------------------------------------------------|
| I08-140     |       55 | Para as NF-e com finalidade de devolução de mercadoria (tag:finNFe=4), somente serão aceitos CFOP de devolução de mercadoria. Observação : Vide relação de CFOP de devolução de mercadoria natabela de apoio publicada no Portal da NF-e (Tabela CFOP, indDevol=1). Exceção 1 : Aceitar os CFOP 1.949 e 2.949 na devolução de venda para não Contribuinte. Para estes CFOP verificar a condição: tag:finNFe = 4 (devolução) e tag:indIEDest = 9 (não Contribuinte) (NT 2015.002) Exceção 2 : Aceitar os CFOP 5.949 e 6.949 na devolução simbólica de gás natural (NCM 27112100) nos termos do Ajuste SINIEF nº 22/21 | Obrig.   |   327 | Rej.     | Rejeição: CFOP inválido para Nota Fiscal com finalidade de devolução de mercadoria[nItem:nnn] |

## 4.2. JA. Detalhamento Específico de Veículos Novos

| Campo-Seq   |   Model o | Regra de Validação                                                                                                                                                                                                                                            | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                         |
|-------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|----------------------------------------------------------------------------------------|
| J19-10      |        55 | Verificar se o código do tipo de veículo (campo: tpVeic) consta na Tabela de Tipo e Espécie de Veículo Observação 1: Tabela de Tipo e Espécie de Veículo publicada na aba 'Documentos', opção 'Diversos' do Portal Nacional da NF -e (www.nfe.fazenda.gov.br) | Obrig.   |   841 | Rej.     | Rejeição: Código do Tipo de Veículo Inexistente [nItem:nnn]                            |
| J20-10      |        55 | Verificar se o código da espécie de veículo (campo: espVeic) consta na Tabela de Tipo e Espécie de Veículo                                                                                                                                                    | Obrig.   |   842 | Rej.     | Rejeição: Código da espécie de Veículo Inexistente [nItem:nnn]                         |
| J20-20      |        55 | Verificar se o código da espécie de veículo (campo: espVeic) é compatível com o tipo de veículo (campo: tpVeic) conforme Tabela de Tipo e Espécie de Veículo                                                                                                  | Obrig.   |   843 | Rej.     | Rejeição: Código da espécie de Veículo incompatível com o tipo do Veículo. [nItem:nnn] |

![Image](assets/image_000016_2e9cdcac39774b1d072e3e38a2684a748682e24ca53e08a94a156e82f15e0ebe.png)

NT 2021.004 v1.33 - Regras de Validação e Novos Campos

![Image](assets/image_000017_903a93573ed064d2084510f59de7b4f4b4aa7d0fbe340ae4b3fcb7a91670d47d.png)

| 1: Tabela de Tipo e Espécie de Veículo publicada na aba 'Documentos', opção 'Diversos' do Portal Nacional da NF -e (www.nfe.fazenda.gov.br)   | Observação   |
|-----------------------------------------------------------------------------------------------------------------------------------------------|--------------|

## 4.3. K. Item/Medicamentos

| Campo-Seq   |   Modelo | Regra de Validação                                                                                                                                  | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                |
|-------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|-----------------------------------------------------------------------------------------------|
| K01-10      |       55 | Informado NCM de medicamento é obrigatório o preenchimento do Grupo de Medicamento (tag: med).                                                      | Facult.  |   840 | Rej.     | Rejeição: NCM de medicamento e não informado o grupo de medicamento (med) [nItem:nnn]         |
| K01-20      |       55 | Observação 4: Implementação futura. Se informado Grupo de Medicamentos (tag :med) obrigatório preenchimento do grupo rastro (id: I80) (NT 2016.002) | Obrig.   |   873 | Rej      | Rejeição: Operação com medicamentos e não informado os campos de rastreabilidade [nItem: nnn] |

## 4.4. U. Item/Tributo: ISSQN

| Campo-Seq   | Modelo   | Regra de Validação                                                                                                   | Aplic.   |   Msg | Efeito   | Descrição Erro                                                         |
|-------------|----------|----------------------------------------------------------------------------------------------------------------------|----------|-------|----------|------------------------------------------------------------------------|
| U06-10      | 55/65    | Verificar se o Item da Lista de Serviços (campo: cListServ) consta na Tabela de Códigos de Item da Lista de Serviços | Obrig.   |   844 | Rej.     | Rejeição: Código de Item da Lista de Serviços inexistente. [nItem:nnn] |

## 4.4 X. Informações do Transporte da NF-e

## Projeto Nota Fiscal Eletrônica

NT 2021.004 v1.33 - Regras de Validação e Novos Campos

![Image](assets/image_000018_c5190fa12899d50a6921c9494eaa96d551b7ac1fd45983fc88afb536b0dc386e.png)

| Campo-Seq   |   Modelo | Regra de Validação                                                                                                                                                                                                                                                                                               | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                                                       |
|-------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|--------------------------------------------------------------------------------------------------------------------------------------|
| X03-30      |       55 | Se Modalidade do Frete = 9 (id: X02, campo: modFrete), o Grupo Transportador (id: X03, campo: transporta) não pode ser informado.                                                                                                                                                                                | Obrig.   |   845 | Rej.     | Rejeição: O Grupo Transportador não pode ser preenchido para Modalidade do frete informada                                           |
| X04-30      |       55 | Se for NF-e de saída (tpNF=1) e Modalidade do Frete = 3 (id: X02, campo: modFrete), o CNPJ Base (id: X04, campo: CNPJ) ou CPF (id: X05, campo: CPF) do transportador deve ser IGUAL ao CNPJ Base (id: C02, campo: CNPJ) ou CPF do Remetente (id: C02a, campo: CPF)                                               | Obrig.   |   846 | Rej.     | Rejeição: Transporte próprio por conta do Remetente e CNPJ Base ou CPF do Transportador difere do CNPJ Base ou CPF do Remetente      |
| X04-40      |       55 | transportador não for informado. Se for NF-e de entrada (tpNF=0) e Modalidade do Frete = 3 (id: X02, campo: modFrete), o CNPJ Base (id: X04, campo: CNPJ) ou CPF (id: X05, campo: CPF) do transportador deve ser IGUAL ao CNPJ Base (id: E02, campo: CNPJ) ou CPF do Remetente (id: E03, campo: CPF)             | Obrig.   |   846 | Rej.     | Rejeição: Transporte próprio por conta do Remetente e CNPJ Base ou CPF do Transportador difere do CNPJ Base ou CPF do Remetente      |
| X04-50      |       55 | transportador não for informado. Se for NF-e de saída (tpNF=1) e Modalidade do Frete <> 1, 2 ou 3 (id: X02, campo: modFrete), o CNPJ Base (id: X04, campo: CNPJ) ou CPF (id: X05, campo: CPF) do transportador deve ser DIFERENTE do CNPJ Base (id: C02, campo: CNPJ) ou CPF do Remetente (id: C02a, campo: CPF) | Obrig.   |   847 | Rej.     | Rejeição: Transporte não é próprio por conta do Remetente e CNPJ Base ou CPF do Transportador igual ao CNPJ Base ou CPF do Remetente |

## Projeto Nota Fiscal Eletrônica

NT 2021.004 v1.33 - Regras de Validação e Novos Campos

![Image](assets/image_000019_c5190fa12899d50a6921c9494eaa96d551b7ac1fd45983fc88afb536b0dc386e.png)

| Campo-Seq   |   Modelo | Regra de Validação                                                                                                                                                                                                                                                                                                                                | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                                                             |
|-------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|--------------------------------------------------------------------------------------------------------------------------------------------|
| X04-60      |       55 | Se for NF-e de entrada (tpNF=0) e Modalidade do Frete <> 1, 2 ou 3 (id: X02, campo: modFrete), o CNPJ Base (id: X04, campo: CNPJ) ou CPF (id: X05, campo: CPF) do transportador deve ser DIFERENTE do CNPJ Base (id: E02, campo: CNPJ) ou CPF do Remetente (id: E03, campo: CPF)                                                                  | Obrig.   |   847 | Rej.     | Rejeição: Transporte não é próprio por conta do Remetente e CNPJ Base ou CPF do Transportador igual ao CNPJ Base ou CPF do Remetente       |
| X04-60      |       55 | Observação 1: Regra de validação não se aplica quando CNPJ/CPF do transportador não for informado. Observação 2: Regra de validação não se aplica quando CNPJ Base ou CPF do emitente for igual ao CNPJ Base ou CPF do destinatário e CFOP é de operação com combustíveis (indComb= 2), conforme Tabela CFOP. Observação 3: Implementação futura. | Obrig.   |   847 | Rej.     | Rejeição: Transporte não é próprio por conta do Remetente e CNPJ Base ou CPF do Transportador igual ao CNPJ Base ou CPF do Remetente       |
| X04-70      |       55 | Se for NF-e de saída (tpNF=1) e Modalidade do Frete = 4 (id: X02, campo: modFrete), o CNPJ Base (id: X04, campo: CNPJ) ou CPF (id: X05, campo: CPF) do transportador deve ser IGUAL ao CNPJ Base (id: E02, campo: CNPJ) ou CPF do Destinatário (id: E03, campo: CPF)                                                                              | Obrig.   |   848 | Rej.     | Rejeição: Transporte próprio por conta do Destinatário e CNPJ Base ou CPF do Transportador difere do CNPJ Base ou CPF do Destinatário      |
| X04-70      |       55 | Observação: Regra de validação não se aplica quando CNPJ/CPF do transportador não for informado.                                                                                                                                                                                                                                                  | Obrig.   |   848 | Rej.     | Rejeição: Transporte próprio por conta do Destinatário e CNPJ Base ou CPF do Transportador difere do CNPJ Base ou CPF do Destinatário      |
| X04-80      |       55 | Se for NF-e de entrada (tpNF=0) e Modalidade do Frete = 4 (id: X02, campo: modFrete), o CNPJ Base (id: X04, campo: CNPJ) ou CPF (id: X05, campo: CPF) do transportador deve ser IGUAL ao CNPJ Base (id: C02, campo: CNPJ) ou CPF do Destinatário (id: C02a, campo: CPF)                                                                           | Obrig.   |   848 | Rej.     | Rejeição: Transporte próprio por conta do Destinatário e CNPJ Base ou CPF do Transportador difere do CNPJ Base ou CPF do Destinatário      |
| X04-80      |       55 | Observação: Regra de validação não se aplica quando CNPJ/CPF do transportador não for informado.                                                                                                                                                                                                                                                  | Obrig.   |   848 | Rej.     | Rejeição: Transporte próprio por conta do Destinatário e CNPJ Base ou CPF do Transportador difere do CNPJ Base ou CPF do Destinatário      |
| X04-90      |       55 | Se for NF-e de saída (tpNF=1) e Modalidade do Frete <>0, 2 ou 4 (id: X02, campo: modFrete), o CNPJ Base (id: X04, campo: CNPJ) ou CPF (id: X05, campo: CPF) do transportador deve ser DIFERENTE do CNPJ Base (id: E02, campo: CNPJ) ou CPF do Destinatário (id: E03, campo: CPF)                                                                  | Obrig.   |   849 | Rej.     | Rejeição: Transporte não é próprio por conta do Destinatário e CNPJ Base ou CPF do Transportador igual ao CNPJ Base ou CPF do Destinatário |
| X04-90      |       55 | Observação 1: Regra de validação não se aplica quando CNPJ/CPF do transportador não for informado. Observação 2: Regra de validação não se aplica quando CNPJ Base ou CPF do emitente for igual ao CNPJ Base ou CPF do destinatário e CFOP é de operação com combustíveis (indComb= 2), conforme Tabela CFOP. Observação 3: Implementação futura. | Obrig.   |   849 | Rej.     | Rejeição: Transporte não é próprio por conta do Destinatário e CNPJ Base ou CPF do Transportador igual ao CNPJ Base ou CPF do Destinatário |

## Projeto Nota Fiscal Eletrônica

NT 2021.004 v1.33 - Regras de Validação e Novos Campos

![Image](assets/image_000020_903a93573ed064d2084510f59de7b4f4b4aa7d0fbe340ae4b3fcb7a91670d47d.png)

| Campo-Seq   |   Modelo | Regra de Validação                                                                                                                                                                                                                                                                   | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                                                             |
|-------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|--------------------------------------------------------------------------------------------------------------------------------------------|
| X04-100     |       55 | Se for NF-e de entrada (tpNF=0) e Modalidade do Frete <> 0, 2 ou 4 (id: X02, campo: modFrete), o CNPJ Base (id: X04, campo: CNPJ) ou CPF (id: X05, campo: CPF) do transportador deve ser DIFERENTE do CNPJ Base (id: C02, campo: CNPJ) ou CPF do Destinatário (id: C02a, campo: CPF) | Obrig.   |   849 | Rej.     | Rejeição: Transporte não é próprio por conta do Destinatário e CNPJ Base ou CPF do Transportador igual ao CNPJ Base ou CPF do Destinatário |

## 4.5 Z. Informação Adicional da NF-e

| Campo-Seq   | Modelo   | Regra de Validação                                                                                                                                                                                                                                                                                                                            | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                   |
|-------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|--------------------------------------------------------------------------------------------------|
| Z02-10      | 65       | NFC-e sem preenchimento das Informações Adicionais de Interesse do Fisco (campo:infAdFisco). Observação 1 : Regra de validação restrita a UF de SC. Observação 2 : Implementação futura.                                                                                                                                                      | Facul.   |   949 | Rej      | Rejeição: NFC-e sem preenchimento das Informações Adicionais de Interesse do Fisco               |
| Z02-20      | 65       | Tamanho das Informações Adicionais de Interesse do Fisco (campo:infAdFisco) não atende ao tamanho mínimo exigido                                                                                                                                                                                                                              | Facul.   |   950 | Rej.     | Rejeição: Informações Adicionais de Interesse do Fisco abaixo do tamanho mínimo exigido pela UF. |
| Z13-10      | 55/65    | Se Tipo do ato concessório (campo: tpAto) for igual a 08 ou 10, campo nProc não segue o padrão de regime especial da UF. Observação 1: Regra de validação a critério da UF Observação 2: Tabela de Padrões de Regime Especial de cada UF publicada na aba 'Documentos', opção 'Diversos' do Portal Nacional da NF -e (www.nfe.fazenda.gov.br) | Facul.   |   941 | Rej.     | Rejeição: Número do Regime especial inválido.                                                    |

## 4.6 3A. Banco de Dados: NF-e Referenciada

## Projeto Nota Fiscal Eletrônica

NT 2021.004 v1.33 - Regras de Validação e Novos Campos

![Image](assets/image_000021_903a93573ed064d2084510f59de7b4f4b4aa7d0fbe340ae4b3fcb7a91670d47d.png)

| Campo-Seq   |   Modelo | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Aplic.   |   Msg | Efeito   | Descrição Erro                                                 |
|-------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|----------------------------------------------------------------|
| 3BA02-10    |       55 | Para cada NF-e referenciada (tag:refNFe), se a UF da Chave de Acesso referenciada for igual a UF do Emitente: - Acessar BD NFE com Chave de Acesso referenciada (se mod=55) - NF-e referenciada inexistente Exceção: A NF-e referenciada pode não existir no caso de Emissão em Contingência (tpEmis = 2, 4 ou 5) (NT 2013/003) desde que a Chave de Acesso da NF-e referenciada tenha o Ano-Mês de Emissão inferior a 1 mês da data atual ou desde que exista o EPEC. • Observação: A exceção acima não se aplica para 'finNFe=2" (NF -e Complementar). | Facul.   |   267 | Rej.     | Rejeição: Chave de Acesso referenciada inexistente [nRef: xxx] |

## 4.7 5A. Banco de Dados: Local de Retirada

| Campo-Seq   |   Modelo | Regra de Validação                                                                                                                                            | Aplic.   |   Msg | Efeito   | Descrição Erro                                          |
|-------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|---------------------------------------------------------|
| 5AF15-10    |       55 | Se informada IE do Local de Retirada: -Acessar Cadastro de Contribuinte da UF (Chave: UF Retirada , IE Retirada) (*5) -IE do local de retirada não cadastrada | Obrig.   |   942 | Rej.     | Rejeição: IE do local de retirada não cadastrada        |
| 5AF15-20    |       55 | Se informado CNPJ do local de retirada e IE do local de retirada não vinculada ao CNPJ (tratar Regime Especial de IE Única)                                   | Obrig.   |   943 | Rej.     | Rejeição: IE do local de retirada não vinculada ao CNPJ |
| 5AF15-30    |       55 | Se informado CPF do local de retirada e IE do local de retirada não vinculada ao CPF                                                                          | Obrig.   |   944 | Rej.     | Rejeição: IE do local de retirada não vinculada ao CPF  |

## 4.8 5B. Banco de Dados: Local de Entrega

| Campo-Seq   |   Modelo | Regra de Validação                                                                                                                                        | Aplic.   |   Msg | Efeito   | Descrição Erro                                         |
|-------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|--------------------------------------------------------|
| 5BG15-10    |       55 | Se informada IE do local de entrega: -Acessar Cadastro de Contribuinte da UF (Chave: UF Entrega , IE Entrega) (*5) -IE do local de entrega não cadastrada | Obrig.   |   945 | Rej.     | Rejeição: IE do local de entrega não cadastrada        |
| 5BG15-20    |       55 | Se informado CNPJ do local de entrega e IE do local de entrega não vinculada ao CNPJ (tratar Regime Especial de IE Única)                                 | Obrig.   |   947 | Rej.     | Rejeição: IE do local de entrega não vinculada ao CNPJ |
| 5BG15-30    |       55 | Se informado CPF do local de entrega e IE do local de entrega não vinculada ao CPF                                                                        | Obrig.   |   948 | Rej.     | Rejeição: IE do local de entrega não vinculada ao CPF  |

## Projeto Nota Fiscal Eletrônica

NT 2021.004 v1.33 - Regras de Validação e Novos Campos

## 5. Novos códigos de Rejeição

|   CÓDIGO | MOTIVO DE NÃO ATENDIMENTO DA SOLICITAÇÃO                                                                                                   |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------|
|      840 | Rejeição: NCM de medicamento e não informado o grupo de medicamento (med) [nItem:nnn]                                                      |
|      841 | Rejeição: Código do Tipo de Veículo Inexistente [nItem:nnn]                                                                                |
|      842 | Rejeição: Código da espécie de Veículo Inexistente[nItem:nnn]                                                                              |
|      843 | Rejeição: Código da espécie de Veículo incompatível com o tipo do Veículo. [nItem:nnn]                                                     |
|      844 | Rejeição: Código de Item da Lista de Serviços inexistente. [nItem:nnn]                                                                     |
|      845 | Rejeição: O Grupo Transportador não pode ser preenchido para Modalidade do frete informada                                                 |
|      846 | Rejeição: Transporte próprio por conta do Remetente e CNPJ Base ou CPF do Transportador difere do CNPJ Base ou CPF do Remetente            |
|      847 | Rejeição: Transporte não é próprio por conta do Remetente e CNPJ Base ou CPF do Transportador igual ao CNPJ Base ou CPF do Remetente       |
|      848 | Rejeição: Transporte próprio por conta do Destinatário e CNPJ Base ou CPF do Transportador difere do CNPJ Base ou CPF do Destinatário      |
|      849 | Rejeição: Transporte não é próprio por conta do Destinatário e CNPJ Base ou CPF do Transportador igual ao CNPJ Base ou CPF do Destinatário |
|      941 | Rejeição: Número do Regime especial inválido.                                                                                              |
|      942 | Rejeição: IE do local de retirada não cadastrada                                                                                           |
|      943 | Rejeição: IE do local de retirada não vinculada ao CNPJ                                                                                    |
|      944 | Rejeição: IE do local de retirada não vinculada ao CPF                                                                                     |
|      945 | Rejeição: IE do local de entrega não cadastrada                                                                                            |
|      947 | Rejeição: IE do local de entrega não vinculada ao CNPJ                                                                                     |
|      948 | Rejeição: IE do local de entrega não vinculada ao CPF                                                                                      |
|      949 | Rejeição: NFC-e sem preenchimento das Informações Adicionais de Interesse do Fisco                                                         |
|      950 | Rejeição: Informações Adicionais de Interesse do Fisco abaixo do tamanho mínimo exigido pela UF.                                           |

![Image](assets/image_000022_c5190fa12899d50a6921c9494eaa96d551b7ac1fd45983fc88afb536b0dc386e.png)
## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt2021-004v1-35-novos-campos-e-regras/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt2021-004v1-35-novos-campos-e-regras/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt2021-004v1-35-novos-campos-e-regras.md)
- [Proveniência resumida](../../../../sources/provenance/nt2021-004v1-35-novos-campos-e-regras.json)


## Documentos relacionados

- [[nt2023-004-v1-20-campos-e-regras]]
