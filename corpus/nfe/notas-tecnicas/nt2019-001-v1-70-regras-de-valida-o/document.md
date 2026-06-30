---
title: "Sistema Nota Fiscal Eletrônica"
slug: "nt2019-001-v1-70-regras-de-valida-o"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "8c03e1d53893f211b4967a5f6da0a1a5f9c46b0862e23ee5b63816657e79ff00"
converted_at_utc: "2026-06-25T16:41:39.698049+00:00"
status: "published"
type: "nota_tecnica"
---
![Image](assets/image_000000_1fb3ccd0d292af92d1440a35514f59f67282ecf98dcd979562836ddbc502f2fb.png)

![Image](assets/image_000001_7c3f84fb39a2dff3fd08d905df7eb397320b78c7c2996007be7e7bb8270a30d7.png)

## Sistema Nota Fiscal Eletrônica

Nota Técnica 2019.001

Criação e Atualização de Regras de Validação

Versão 1.70 - Agosto de 2025

![Image](assets/image_000002_7992e63cde80c6efbe159d5e61b2b56a9b71285b8f3e0302de6d6c975f580494.png)

## Nota Fiscal Eletrônica

## Sumário

| Controle de Versões ............................................................................................................................4                                                                                        |                                                                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Resumo.........................................................................................................................................7                                                                                         |                                                                                                                                                      |
| 1                                                                                                                                                                                                                                        |                                                                                                                                                      |
| e/NFC-e versão 4.0, com os seguintes objetivos: .........................................................................7 1.2 Ajuste nas regras de validação referentes a CST e Código de Benefício Fiscal e insere                     | uma                                                                                                                                                  |
| para ordem sequencial do 1.3 Remoção da Regra 1C03-10...................................................................................................7                                                                                | item:....................................................................................................7                                           |
| 1.4 Correção na Descrição da Regra de Validação N12-90..........................................................7                                                                                                                        |                                                                                                                                                      |
| 1.5 Regras N18-10 e N18-20 Facultativas ....................................................................................7                                                                                                            |                                                                                                                                                      |
| 1.6 Criação de Novo Valor para o Campo N18 .............................................................................7                                                                                                                |                                                                                                                                                      |
| 1.7 Comentários Sobre o Código de Benefício Fiscal ...................................................................7                                                                                                                  |                                                                                                                                                      |
| 1.8 Novas Datas de Vigência para Algumas Regras de Validação................................................7                                                                                                                            |                                                                                                                                                      |
| 1.9 Criação da Regra de Validação N12-98..................................................................................8                                                                                                              |                                                                                                                                                      |
| 1.10 Criação de Exceções para as Regras de Validação N12-85, N12-86, N1290, N12-94, e N12-98.......................................................................................................................................8     | N12-97                                                                                                                                               |
| 1.11 Quadro com datas de ativação das RV, respectivas exceções e possíveis modelos para que ativaram/estão ativando tais RV.............................................................................................8                | UF ..........................................................................8                                                                       |
| 1.12 Prorrogação de implantação em Produção                                                                                                                                                                                              |                                                                                                                                                      |
| 1.13 Publicidade das Tabelas cBenef x                                                                                                                                                                                                    | CST................................................................................9                                                                 |
| 1.14 Exceção na Regra de Validação                                                                                                                                                                                                       | N12-98..............................................................................9                                                                |
| 1.15 Alteração na Regra de Validação N28-20                                                                                                                                                                                              | ............................................................................9                                                                        |
| 1.16 Ativação da Regra de Validação N12-98 para o Distrito                                                                                                                                                                               | Federal..........................................9                                                                                                   |
| 1.17 Ativação das Regras de Validação N12-85, N12-86, N12-90, N12-94, N12-97 e N12-98 Goiás............................................................................................................................................9 | para                                                                                                                                                 |
| 1.18 Ativação das Regras de Validação N12-85, N12-86 e N12-94 para Distrito Federal .............9 1.19 Alteração da data de ativação em produção para NF-e, pelo Distrito Federal, das regras                                           | de                                                                                                                                                   |
| validação N12-85, N12-86 e N12-94.............................................................................................9 1.20 Alteração da data de ativação em produção para NF-e, pelo Distrito Federal e Goiás,                 |                                                                                                                                                      |
| regras de validação N12-85, N12-86, N12-90 (GO), N12-94 e N12-97 (GO) ..............................10                                                                                                                                   | das                                                                                                                                                  |
| 1.21 Inclusão da Regra de Validação I08-171............................................................................10                                                                                                                |                                                                                                                                                      |
| 1.23 Inclusão de campos para as informações do crédito presumido. ........................................10                                                                                                                             |                                                                                                                                                      |
| 1.24 Inclusão de campo para código de benefício fiscal de redução de base de cálculo dentro CST51 quando acumular com o diferimento. ..............................................................................10                    | do                                                                                                                                                   |
| 1.25 Prorrogação da implantação da versão 1.60 em homologação e informar sobre                                                                                                                                                           |                                                                                                                                                      |
| publicação do schema..................................................................................................................................10                                                                                 |                                                                                                                                                      |
| 1.26 Alteração do leiaute, nomeando a tag do grupo de Crédito                                                                                                                                                                            |                                                                                                                                                      |
| Presumido...............................10 1.27 Alteração das Regras de Validação que tratam das operações de aquisição ou serviços.                                                                                                     | prestação de .....................................................................................................................................10 |
| 1.28 Alteração da data de ativação das Regras de Validação referentes à tabela de cBenef                                                                                                                                                 | por                                                                                                                                                  |
| CST para o Distrito Federal.                                                                                                                                                                                                             |                                                                                                                                                      |
| .......................................................................................................10                                                                                                                                |                                                                                                                                                      |

![Image](assets/image_000003_b4660e833e724426c58020f3b5a6b8abeea254d139f8fe0878b1126902936d12.png)

![Image](assets/image_000004_79ac8dbf5b80c9eda32f8c56897fba5fc7030f04062e542c324c43cdce3c4f11.png)

SNFeNFCe

eonic

| 1.29 Inclusão da obrigatoriedade de código de benefício fiscal para o Espírito Santo................11                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.30 Observação: o schema entra em produção em 06/05/2024. ..............................................11                                                                                                                                                |
| 1.31 Alteração da data de ativação das Regras de Validação referentes à tabela de cBenef por CST para o Distrito Federal. .......................................................................................................11                        |
| 1.32 Criação da Regra de Validação I05g-10.............................................................................11                                                                                                                                  |
| 1.33 Adequação de textos de Regra de Validação para conformidade com NT 2020.005 v1.10.                                                                                                                                                                    |
| ...................................................................................................................................................11                                                                                                      |
| 1.34 Publicação de cronograma de ativação de regras de validação para SC. ..........................11                                                                                                                                                     |
| 1.35 Inclusão das regras de validação N14a-10, N14a-20 e I05h-10 a critério da UF................11                                                                                                                                                        |
| 1.36 Publicação de cronograma de ativação de regras de validação para SP. ..........................11                                                                                                                                                     |
| 1.37 Alteração das datas de ativação das Regras de Validação referentes à tabela de cBenef por                                                                                                                                                             |
| CST para Santa Catarina............................................................................................................11                                                                                                                      |
| 2 Detalhamento das Validações .....................................................................................................13                                                                                                                      |
| 3 Regras de Validação - Serviço de Autorização NF-e ..................................................................15 3.1 Grupo B. Identificação da NF-e.............................................................................................15 |
| Grupo BA. Documento Referenciado ....................................................................................15                                                                                                                                    |
| 3.2                                                                                                                                                                                                                                                        |
| 3.4 Detalhamento Produtos e Serviços .......................................................................................16                                                                                                                             |
| 3.5 Grupo I. Produtos e Serviços da NF-e...................................................................................16                                                                                                                              |
| 3.6 Grupo N. Item / Tributo: ICMS...............................................................................................17                                                                                                                         |
| 3.6.1 Datas, Exceções e Modelos para Regras de Validação: N12-85, N12-86, N12-90, N12-94, N12-97, N12-98, N14a-10, N14a-20 e I05h-10 ...........................................................................20                                         |
| 3.6.2 Arquivo no Portal Nacional da NF-e contendo os endereços das tabelas de 'cBenef x CST' das UF:.......................................................................................................................................22              |
| 3.7 Grupo W. Total da NF-e........................................................................................................22                                                                                                                       |
| 3.8 Banco de Dados: Emitente....................................................................................................22                                                                                                                         |
| 3.9 Banco de Dados: Destinatário...............................................................................................23                                                                                                                          |
| 4 Regras de Validação - Serviço Autorização Evento Prévio de Emissão em Contingência ...........23                                                                                                                                                         |
| 5 Novos Códigos de Rejeição.........................................................................................................24                                                                                                                     |
| 6 Alteração de Leiaute....................................................................................................................25                                                                                                               |
| 6.1 Grupo N. Grupo Tributação do ICMS= 10 .............................................................................25                                                                                                                                  |
| 6.2 Grupo N. Grupo Tributação do ICMS= 30 .............................................................................25                                                                                                                                  |
| Grupo N07. Grupo Tributação do ICMS= 51 .........................................................................26                                                                                                                                        |
| 6.4                                                                                                                                                                                                                                                        |

## Controle de Versões

|   Versão | Publicação     | Descrição         |
|----------|----------------|-------------------|
|     1.70 | Agosto/2025    | Alteração da NT   |
|     1.64 | Setembro/2024  | Alteração da NT   |
|     1.63 | Agosto/2024    | Alteração da NT   |
|     1.62 | Março/2024     | Alteração da NT   |
|     1.61 | Janeiro/2024   | Alteração da NT.  |
|     1.60 | Dezembro/2023  | Alteração da NT.  |
|     1.54 | Dezembro/2023  | Alteração da NT.  |
|     1.53 | Fevereiro/2023 | Alteração da NT.  |
|     1.52 | Agosto/2022    | Alteração da NT.  |
|     1.51 | Setembro/2020  | Alteração da NT.  |
|     1.50 | Abril/2020     | Alteração da NT.  |
|     1.40 | Dezembro/2019  | Alteração da NT.  |
|     1.30 | Agosto/2019    | Alteração da NT.  |
|     1.20 | Agosto/2019    | Alteração da NT.  |
|     1.10 | Julho/2019     | Alteração da NT.  |
|     1.00 | Abril/2019     | Publicação da NT. |

## Histórico de Alterações / Cronograma

|   Versão | Histórico de atualizações                                                                                                                                                                                                                                                                                 | Implantação Implantação          | Implantação Implantação          |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|----------------------------------|
|     1.70 | • Ativação das regras de validação para SP • Alteração da data de ativação em produção da regra de validação N12-85 para Santa Catarina.                                                                                                                                                                  | Teste 12/01/2026 04/11/2024      | Produção 06/04/2026 01/09/2025   |
|     1.64 | • Ativação da regra de validação N12-85 na NF-e para SC. • Ativação da regra de validação N12-85 na NFC-e para SC. • Inclusão das regras de validação N14a-20 e I05h-10 a critério da UF; e ativação das regras de validação N12-94, N12-98, N14a-20 e I05h- 10 para SC. •                                | 04/11/2024 04/11/2024 02/12/2024 | 03/02/2025 01/04/2025 28/04/2025 |
|     1.63 | Inclusão da regra de validação N14a-10 a critério da UF; e ativação das regras de validação N12-86 e N14a-10 para SC. Alteração da data de ativação em produção para NFC-e (modelo                                                                                                                        | 02/12/2024                       | 01/09/2025 02/09/2024            |
|          | • 65), pelo DF, das regras de validação N12-85, N12-86 e N12-94. • Inclusão da regra de validação I05g-10 a critério da UF. • Adequação dos textos das RV 5E17-10, 5E17-30, 5E17-46, 5E17- 80, 6P31-30 e 6P31-46 conforme NT 2020.005 v.1.10, excluindo os comentários referentes à expressão '(*7)'.     | 05/10/2020 02/08/2024            | 02/09/2024                       |
|     1.62 | • Alteração das Regras de Validação que tratam das operações de aquisição ou prestação de Serviços (RV I08-160 e I08-70); e eliminação da RV I08-17, sobre o mesmo assunto. • Alteração da data de ativação em produção para NFC-e (modelo 65), pelo DF, das regras de validação N12-85, N12-86 e N12-94. | Até 25/03/2024                   | 01/07/2024                       |

![Image](assets/image_000005_b28f7296b1b4b8271fe4411a9496572dbe267347e36fefdc36de4fb393cb156b.png)

![Image](assets/image_000006_79ac8dbf5b80c9eda32f8c56897fba5fc7030f04062e542c324c43cdce3c4f11.png)

SNFeNFCe

eonic SNFeNFCe

|   Versão |       | Histórico de atualizações                                                                                                                                                                                                                                                                                                                      | Implantação Implantação   | Implantação Implantação   |
|----------|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|---------------------------|
|     1.62 | • •   | Atualização do Schema Alteração do leiaute, nomeando a tag do grupo de Crédito Presumido (tag:gCred, Id:I05g);                                                                                                                                                                                                                                 | Teste Até 25/03/2024      | Produção 06/05/2024       |
|     1.61 | •     | Prorrogação da implantação da versão 1.60 em homologação e informar sobre publicação do schema.                                                                                                                                                                                                                                                | 11/03/2024                | 01/04/2024                |
|     1.60 | • •   | Inclusão de campos para as informações do crédito presumido. Inclusão de campo para código de benefício fiscal de redução de base de cálculo dentro do CST51 quando acumular com o diferimento.                                                                                                                                                | 04/03/2024                | 01/04/2024                |
|     1.54 | • •   | Alteração da data de ativação em produção para NF-e, pelo DF, das regras de validação N12-85, N12-86 e N12-94 Alteração da data de ativação em produção para NF-e, por Goiás, das regras de validação N12-85, N12-86, N12-90, N12-94, N1297 e N12-98                                                                                           | 05/10/2020 01/10/2022     | 04/09/2023 01/07/2023     |
|     1.53 | •     | Alteração da data de ativação em produção para NF-e, pelo DF, das regras de validação N12-85, N12-86 e N12-94                                                                                                                                                                                                                                  | 05/10/2020                | 01/03/2023                |
|     1.52 | • • • | GO ativará as regras de validações N12-85, N12-86, N12-90, N12- 94, N1297 e N12-98 Correção do texto relativo a ativação da regra de validação do DF na versão 1.51 DF ativará as regras de validações N12-85, N12-86 e N12-94                                                                                                                 | 01/10/2022                | 01/01/2023                |
|     1.51 | • • • | DF ativará a regra de validação N12-98 Inclusão de novos CFOP na regra de validação N28-20. Como EXCEÇÃO, a alteração nessa regra entrará em homologação e produção no dia 28/9/2020 . Alteração do texto da N12-86                                                                                                                            | 05/10/2020                | 02/11/2020                |
|     1.50 | • • • | Prorroga a implantação em Produção Informa como e onde serão publicadas as tabelas de cBenef x CST de cada UF (na data de publicação desta versão da NT) Adiciona exceção à RV N12-98, informando que não se aplica ao Simples Nacional                                                                                                        | 16/03/2020                | 10/08/2020                |
|     1.40 | • • • | Modifica a RV N12-94 para deixar mais específica a rejeição, criando assim a RV N12-98 com sua respectiva rejeição Adiciona as exceções e modelos para as RV N12-85, N12-86, N12- 90, N12-94, N12-97 e N12-98 Informa as Exceções e Datas aplicáveis as UF que ativaram as RV N12-85, N12-86, N12-90, N12-94 e N12-97; e que ativarão a N12-98 | 16/03/2020                | 11/05/2020                |
|     1.30 | • • • | Retira o modelo 65 da validação da RV B03-10 Informados os locais de publicação das tabelas de códigos de benefícios fiscais e de regras de validação opcionais por unidade federada Novas datas de vigência para algumas regras de validação                                                                                                  | Ver item 1.8              | Ver item 1.8              |
|     1.20 | • • • | Remoção da Regra 1C03-10 Correção na Descrição da Regra de Validação N12-90 Torna facultativas as regras N18-10 e N18-20 Criado novo Valor para o Campo N18                                                                                                                                                                                    | Até 26/08/2019            | 02/09/2019                |
|     1.10 | • •   | Criação/Alteração de regras de validação referentes a CST e a Código de Benefício Fiscal, corrigindo algumas regras da versão anterior.                                                                                                                                                                                                        | Até 22/07/2019            | 02/09/2019                |

![Image](assets/image_000007_79ac8dbf5b80c9eda32f8c56897fba5fc7030f04062e542c324c43cdce3c4f11.png)

|   Versão | Histórico de atualizações                                                                                                                                                                                                 | Implantação Implantação   | Implantação Implantação   |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|---------------------------|
|          |                                                                                                                                                                                                                           | Teste                     | Produção                  |
|          | • Criação de regra de validação correspondente rejeição 927, para informar os números dos itens em ordem sequencial. • Define que a regra de validação referente ao valor máximo da base de cálculo é por modelo de DF-e. |                           |                           |
|     1.00 | • Criação de novas regras de validação e alteração de regras existentes                                                                                                                                                   | Até 01/07/2019            | 02/09/2019                |

## 1 Resumo

## 1.1 Esta Nota Técnica divulga novas regras de validação e atualiza regras existentes da NF-e/NFC-e versão 4.0, com os seguintes objetivos:

- Dificultar utilização de código de segurança fraco
- Melhorar o controle de documentos referenciados e da identificação do destinatário
- Descrever benefícios fiscais e informações da tributação do ICMS com mais precisão
- Criação de valor máximo para a base de cálculo do ICMS, por unidade federada
- Melhor gerenciamento de informações sobre o destinatário, tanto no serviço de autorização de NF-e quanto no serviço de registro de EPEC

## 1.2 Ajuste nas regras de validação referentes a CST e Código de Benefício Fiscal e insere uma para ordem sequencial do item:

- Foram realizados ajustes nas regras  de validação,  inclusive  nos  nomes,  referentes a  CST e Código de Benefício Fiscal, de utilização a critério da UF. Criou-se mais uma regra de validação para complementar essas citadas.
- Criou-se  a  regra  de  validação  para  informar  os  números  do  item  em  ordem  sequencial, correspondente ao código de rejeição já existente na versão 1.00.
- Define que a regra de validação referente ao valor máximo da base de cálculo é por modelo de DF-e.

## 1.3 Remoção da Regra 1C03-10

A  Regra  1C03-10  exigia  que  Razão  Social  do  emitente  informada  na  tag  emit\xNome  fosse exatamente igual ao cadastro da SEFAZ, o que se demonstrou problemático.

## 1.4 Correção na Descrição da Regra de Validação N12-90

Retirada informação de aplicação somente em casos de operação interna.

## 1.5 Regras N18-10 e N18-20 Facultativas

Os tempos de implementação destas regras variam muito entre as diversas Sefaz autorizadoras, por isto a partir da versão 1.20 desta nota técnica estas regras são de aplicação facultativa.

## 1.6 Criação de Novo Valor para o Campo N18

A tag modBCST passa a aceitar a opção '6=Valor da Operação'.

## 1.7 Comentários Sobre o Código de Benefício Fiscal

O código de benefício fiscal (tag:  cBenef), por tratar de situações particulares de cada unidade federada, tem sua definição também especificada pelas UF que o utilizam.

Estas definições constam de tabela publicada no Portal Nacional da NF-e, na área 'Diversos' da aba 'Documentos'.

Esta tabela tem sofrido atualizações com frequência maior do que a desejável, em virtude do fato que  o  uso  dos  códigos  pelas  empresas  no  ambiente  de  homologação  tem  evidenciado  a necessidade  de  ações  de  correção  de  natureza  emergencial  por  parte  das  Administrações Tributárias envolvidas. É esperado que em futuro próximo a tabela tenha a estabilidade necessária.

## 1.8 Novas Datas de Vigência para Algumas Regras de Validação

Em função de necessidades ditadas pelas legislações de algumas unidades federadas, e atendendo a pleitos de contribuintes e de entidades associativas, as datas de início de exigência das regras de validação N12-85, N12-86, N12-90, N12-94 e N12-97 obedecerão ao disposto na tabela a seguir:

![Image](assets/image_000008_b4660e833e724426c58020f3b5a6b8abeea254d139f8fe0878b1126902936d12.png)

|           | Regra de validação   | Regra de validação   | Regra de validação   | Regra de validação   | Regra de validação   |
|-----------|----------------------|----------------------|----------------------|----------------------|----------------------|
| UF        | N12-85               | N12-86               | N12-90               | N12-94               | N12-97               |
| MT        | (3)                  | (3)                  | (2)                  | (3)                  | (*)                  |
| PR        | (1)                  | (1)                  | (*)                  | (2)                  | (1)                  |
| RJ        | (2)                  | (2)                  | (2)                  | (2)                  | (2)                  |
| RS        | (2)                  | (2)                  | (2)                  | (2)                  | (2)                  |
| demais UF | (*)                  | (*)                  | (*)                  | (*)                  | (*)                  |

Onde a respectiva data de início de vigência corresponde a:

- (*) Regra de validação não será aplicada

(1)  Aplicação a partir de 02/09/2019

- (2)  Aplicação a partir de 01/10/2019
- (3)  Aplicação a partir de 01/01/2020

As datas aqui definidas, juntamente com todas as demais informações a respeito das regras de validação opcionais por UF, podem ser consultadas em tabela publicada no Portal Nacional da NFCe, na área 'Regras de Validação' da aba 'Desenvolvedor'.

Para contribuintes estabelecidos no estado do Rio Grande do Sul, no caso das regras N12-85, N1286 e N12-94, o ambiente de autorização em produção, até 31/3/2020, e o ambiente de

autorização em homologação até 09/2/2020, aceitarão três situações para o campo cBenef:

- NULO (sem preenchimento do campo);
- com a descrição "SEM CBENEF"; ou
- com  o  código  do  benefício;  neste último caso, é realizada a  devida validação  de compatibilidade com o CST informado.

## 1.9 Criação da Regra de Validação N12-98

Criada a Regra de Validação N12-98 a ser ativada a partir de 11/05/2020 em produção, verificando a existência e a vigência do cBenef. Assim, a RV N12-94, a partir dessa data, passará a verificar apenas se o cBenef é compatível com o CST. Essa nova regra permite que determinada UF possa validar apenas a existência do cBenef, caso não opte por validar a compatibilidade com o CST.

A criação da RV N12-98 não traz impacto para os sistemas emissores que já estão preparados para a validação da RV N12-94, salvo o possível tratamento da mensagem da rejeição.

## 1.10 Criação de Exceções para as Regras de Validação N12-85, N12-86, N1290, N12-94, N12-97 e N12-98

Trata-se de exceções que já haviam sido criadas e implementadas, tendo sido comunicadas por meio de aviso disponibilizado no Portal Nacional da NF-e.

## 1.11 Quadro com datas de ativação das RV, respectivas exceções e possíveis modelos para UF que ativaram/estão ativando tais RV

Quadro já disponibilizado no Portal da NF-e. A única diferença é a indicação das opções de modelos (55; 65; ou 55/65). Tal quadro demonstra quais UF estão ativando as RV, bem como as exceções aplicadas e os modelos que de DF-e (55 e 65) em que se aplicam a tais RV.

## 1.12  Prorrogação de implantação em Produção

A pedido das empresas de sistemas, em decorrência da COVID-19, fica prorrogada a implantação em produção das alterações realizadas na versão 1.40 para 10/8/2020.

Observação 1: a Regra de Validação N12-98 (que passará a verificar a existência e a validade do cBenef) já está em homologação, tendo sua produção para 10/8/2020.

![Image](assets/image_000009_b4660e833e724426c58020f3b5a6b8abeea254d139f8fe0878b1126902936d12.png)

![Image](assets/image_000010_b4660e833e724426c58020f3b5a6b8abeea254d139f8fe0878b1126902936d12.png)

Observação 2: a  Regra  de  Validação  N12-94, em  produção,  continua  verificando: existência  e validade  do  cBenef,  bem  como  sua  a  compatibilidade  com  o  CST.  Em  10/8/2020,  verificará apenas a compatibilidade com o CST.

Observação 3: Datas, Exceções e Modelos para Regras de Validação: N12-85, N12-86, N12-90, N1294, N12-97, que já tinham sido informadas por aviso no Portal da NF-e e trazidas para a versão 1.40 já estão em produção.

## 1.13  Publicidade das Tabelas cBenef x CST

O código de benefício fiscal (tag: cBenef), por tratar de situações particulares de cada unidade federada, tem sua definição também especificada pelas UF que o utilizam.

Considerando a necessidade de atualizações constantes que virão durante e depois da COVID-19 e a existência de apenas três UF que utilizam essa tabela e respectivas Regras de Validação, as Secretarias de Fazenda dos Estados do Paraná, Rio de Janeiro e Rio Grande do Sul disponibilizarão endereços eletrônicos em suas páginas contendo as respectivas tabelas para download, a partir da data de publicação dessa versão 1.50 desta NT.

## 1.14  Exceção na Regra de Validação N12-98

Depois de criada a Regra de Validação N12-98, verificou-se a necessidade de explicitar que tal Regra não se aplica às empresas do Simples Nacional. Nas RV que explicitam o termo CST, não há necessidade de colocar essa exceção, visto que empresas do Simples Nacional utilizam CSOSN.

## 1.15  Alteração na Regra de Validação N28-20

Alterada a Regra de Validação N28-20, incluindo os CFOP 6.905 e 6.923, para serem utilizados nas operações isentas destinadas à Zona Franca de Manaus.

É uma EXCEÇÃO às datas previstas nesta NT; assim, a alteração dessa regra de validação entrará em homologação e produção no dia 28/9/2020.

## 1.16  Ativação da Regra de Validação N12-98 para o Distrito Federal

Conforme legislação interna o Distrito Federal ativará a regra de validação N12-98.

## 1.17 Ativação das Regras de Validação N12-85, N12-86, N12-90, N12-94, N12-97 e N12-98 para Goiás

Conforme legislação interna o Estado de Goiás ativará as regras de validação N12-85, N12-86, N1290, N12-94, N12-97 e N12-98.

## 1.18 Ativação das Regras de Validação N12-85, N12-86 e N12-94 para Distrito Federal

Conforme legislação interna o Distrito Federal ativará as  regras de validação N12-85, N12-86 e N1294.  As  novas  RV  serão  ativadas  por  modelo  de  documento,  conforme  cronograma  de implantação estabelecido no item 3.6.1.

## 1.19 Alteração da data de ativação em produção para NF-e, pelo Distrito Federal, das regras de validação N12-85, N12-86 e N12-94

Alterada a data de ativação em produção das regras de validação N12-85, N12-86 e N12-94 para NF-e. A nova data está estabelecida no item 3.6.1, opção D6

![Image](assets/image_000011_b4660e833e724426c58020f3b5a6b8abeea254d139f8fe0878b1126902936d12.png)

SNFeNFCe

eonic

## 1.20 Alteração da data de ativação em produção para NF-e, pelo Distrito Federal e Goiás, das regras de validação N12-85, N12-86, N12-90 (GO), N12-94 e N12-97 (GO)

Alteradas as datas de ativação em produção das regras de validação N12-85, N12-86, N12-90 (GO), N12-94 e N12-97 (GO) para NF-e. As novas datas estão estabelecidas nos itens 3.6.1, opções D5 e D6

## 1.21  Inclusão da Regra de Validação I08-171

Incluída regra de validação para NF-e, vedando o uso de CFOPs específicos no grupo de tributação do ICMS (tag:imposto/ICMS).

## 1.22  Inclusão da obrigatoriedade para Santa Catarina

Incluída a obrigatoriedade de preenchimento do código de benefício fiscal e valor desonerado para Santa Catarina conforme legislação interna do estado.

## 1.23 Inclusão de campos para as informações do crédito presumido.

No Grupo I. Produtos e Serviços da NF-e foi incluído um grupo opcional contendo campos para as informações do crédito presumido, que serão utilizados a critério de cada UF.

- 1.24 Inclusão de campo para código de benefício fiscal de redução de base de cálculo dentro do CST51 quando acumular com o diferimento.

No Grupo N07. Grupo Tributação do ICMS= 51 foi incluído um campo chamado cBenefRBC para informar  o  código de benefício fiscal  de  redução  de  base de  cálculo dentro do  CST51  quando acumular com o diferimento. O campo será utilizado a critério de cada UF.

## 1.25 Prorrogação da implantação da versão 1.60 em homologação e informar sobre publicação do schema.

Prorrogação da implantação da versão 1.60 em homologação para dia 11/03/2024 e informar que o schema da versão 1.60 desta nota técnica será publicado em conjunto com o schema da nota técnica 2023.004.

## 1.26 Alteração do leiaute, nomeando a tag do grupo de Crédito Presumido.

Alteração do leiaute, nomeando a tag do grupo de Crédito Presumido (tag:gCred, Id:I05g);

- 1.27 Alteração das Regras de Validação que tratam das operações de aquisição ou prestação de serviços.

Alteração  das  Regras  de  Validação  que  tratam  das  operações  de  aquisição  ou  prestação  de Serviços (RV I08-160 e I08-70); e eliminação da RV I08-17, sobre o mesmo assunto.

## 1.28 Alteração da data de ativação das Regras de Validação referentes à tabela de cBenef por CST para o Distrito Federal.

Alteração da data de  ativação em produção para NFC-e (modelo 65), pelo Distrito Federal, das regras de validação N12-85, N12-86 e N12-94.

![Image](assets/image_000012_b4660e833e724426c58020f3b5a6b8abeea254d139f8fe0878b1126902936d12.png)

## 1.29  Inclusão da obrigatoriedade de código de benefício fiscal para o Espírito Santo

Incluída a obrigatoriedade de preenchimento, na NF-e modelo 55, do código de benefício fiscal para o Espírito Santo conforme legislação interna do Estado.

## 1.30  Observação: o schema entra em produção em 06/05/2024.

## 1.31  Alteração da data de ativação das Regras de Validação referentes à tabela de cBenef por CST para o Distrito Federal.

Alteração da data de ativação em produção para NFC-e (modelo 65), pelo Distrito Federal, das regras de validação N12-85, N12-86 e N12-94

## 1.32  Criação da Regra de Validação I05g-10.

Criada a Regra de Validação I05g-10 a ser ativada a partir de 02/09/2024 em produção, verificando a permissão de utilização do grupo de informações sobre crédito presumido na UF. Essa nova regra permite que determinada UF possa validar o correto preenchimento da tag: gCred. Inclusão de exceção que exclui a NFF da aplicação da regra.

## 1.33  Adequação de textos de Regra de Validação para conformidade com NT 2020.005 v1.10.

Adequação  dos  textos  das  RV  5E17-10,  5E17-30,  5E17-46,  5E17-80,  6P31-30  e  6P31-46  conforme  NT 2020.005 v.1.10, excluindo os comentários referentes à expressão '(*7)'.

## 1.34  Publicação de cronograma de ativação de regras de validação para SC.

Publicação de cronograma com data de ativação em homologação e produção de regras de validação para o Estado de Santa Catarina, conforme datas estabelecidas no item 3.6.1.

## 1.35  Inclusão das regras de validação N14a-10, N14a-20 e I05h-10 a critério da UF.

Incluída regras de validação N14a-10, N14a-20 para NF-e, visando validar respectivamente a obrigatoriedade e o correto preenchimento do campo código de benefício fiscal de redução de BC do Grupo Tributação do ICMS= 51  (tag:ICMS51/cBenefRBC).

Incluída regra de validação I05h-10 para NF-e e NFC-e, visando validar o correto preenchimento do campo código de crédito presumido (tag: cCredPresumido).

Estas regras de validação serão aplicadas neste momento apenas para o Estado de Santa Catarina, conforme datas estabelecidas no item 3.6.1.

## 1.36  Publicação de cronograma de ativação de regras de validação para SP.

Publicação de cronograma com data de ativação em homologação e produção de regras de validação para o Estado de São Paulo, conforme datas estabelecidas no item 3.6.1.

## 1.37  Alteração das datas de ativação das Regras de Validação referentes à tabela de cBenef por CST para Santa Catarina.

Alteração das datas de ativação em produção das regras de validação N12-85, N12-86, N12-94, N12-98, I05h-10, N14a-10 e N14a-20 para Santa Catarina.

![Image](assets/image_000013_b28f7296b1b4b8271fe4411a9496572dbe267347e36fefdc36de4fb393cb156b.png)

## 2 Detalhamento das Validações

- Grupo B. Identificação da NF-e : criada a Regra de Validação B03-10 , para dificultar a utilização de um código de segurança fraco.
- Grupo BA. Documento Referenciado :
- o alterada a Regra de Validação BA10-40 , possibilitando a utilização do CNPJ 8 com o objetivo de identificar que a nota foi emitida pelo mesmo contribuinte, a critério da unidade federada.
- o criada  a  Regra  de  Validação BA10-50 ,  exigindo  que  uma  contranota  de  produtor  rural somente possa referenciar uma nota emitida por outro produtor rural, a critério da unidade federada.
- o criada a Regra de Validação BA20-20 , impedindo que seja referenciado um documento fiscal de  uso  exclusivo  para  operações  internas  em  uma  operação  destinada  a  outra  unidade federada ou para o exterior.
- o criada a Regra de Validação BA20-30 , impedindo referência a um Cupom Fiscal, a critério da unidade federada.

## · Grupo E. Identificação do Destinatário :

- o criada a Regra de Validação E03a-30 , impedindo o uso simultâneo de IE e de identificação de  estrangeiro  para  o  destinatário. o criada  a  Regra  de  Validação E14-30 ,  impedindo informação de país de destino 'Brasil' em operações destinadas ao estrangeiro.
- o criada a Regra de Validação E16a-40 , exigindo a indicação de 'operação com consumidor final' quando se indica que a operação é destinada a não contribuinte.
- Detalhamento Produtos e Serviços : criada a Regra de Validação H02-10 , com o objetivo de informar os números do item em ordem sequencial.
- Grupo I.  Produtos e Serviços da NF-e :  criadas  regras  de  validação  tornando  obrigatória  a informação do Motivo da Desoneração e do Valor do ICMS desonerado, caso seja informado o Código do Benefício Fiscal:
- o criada a Regra de Validação I05f-10 , impedindo a informação de um código de benefício fiscal  juntamente  com  um  CST  que  não  prevê  benefício  fiscal,  a  critério  da  unidade federada.
- o criada a Regra de Validação I05f-20 , impedindo a informação de um código de benefício fiscal que não corresponda ao CST utilizado, a critério da unidade federada.
- o criada  a  Regra  de  Validação I05f-30 ,  exigindo  que  seja  informado  o  valor  do  ICMS desonerado ou o motivo de desoneração quando se utiliza um código de benefício fiscal, a critério da unidade federada

## · Grupo N. Item / Tributo: ICMS :

- o criada a Regra de Validação N12-97 N07-10 ,  exigindo  informações sobre o diferimento quando se utiliza um CST de diferimento, a critério da unidade federada.
- o criada a Regra de Validação N12-85 N12-84 , exigindo o código de benefício fiscal quando se utiliza um CST de benefício fiscal, a critério da unidade federada. o criada a Regra de Validação N12-86 ,  impedindo que se informe o código de benefício fiscal para CST de benefício fiscal, a critério da unidade federada.
- o criada a Regra de Validação N12-94 N12-88 , exigindo que o CST corresponda ao tipo de código de benefício fiscal informado, a critério da unidade federada.
- o criada a Regra de Validação N12-98 ,  que  verifica  a  existência  do  cBenef,  a  critério  da unidade federada, exceto para Simples Nacional. o criada a Regra de Validação N12-90 , exigindo  valor  do  ICMS desonerado  e o motivo  da  desoneração, a  critério  da  unidade federada.
- o criada a Regra de Validação N18-10 , exigindo a informação do percentual da margem de valor Adicionado do ICMS ST Informada caso a modalidade de determinação da BC da ST seja MVA, a critério da unidade federada.
- o criada a Regra de Validação N18-20 , não permitindo informação do percentual da margem de valor Adicionado do ICMS ST Informada caso a modalidade de determinação da BC da ST não for MVA, a critério da unidade federada. o alterada a Regra de Validação N28-20, incluindo os CFOP 6.905 e 6.923. Entrará em homologação e produção no dia 28/9/2020. o alterado o texto da Regra de Validação N12-86.

![Image](assets/image_000014_b4660e833e724426c58020f3b5a6b8abeea254d139f8fe0878b1126902936d12.png)

## Nota Fiscal Eletrônica

SNFeNFCe

![Image](assets/image_000015_9e022581adbbaafe60fc7c67475a5653161a0220472401208c35cadc09aafab9.png)

- Grupo W. Total da NF-e : Criada a Regra de Validação W03-20 , por modelo de DF-e, impedindo a  informação  de  um  valor  de  Base  de  Cálculo  superior  ao  valor  máximo  estabelecido  pela respectiva SEFAZ.
- Banco de Dados: Emitente : Criada a Regra de Validação 1C03-10, impedindo a informação de Razão Social do emitente diferente da existente no cadastro da Sefaz.
- Banco de Dados: Destinatário : Criadas as Regras de Validação 5E17-10, 5E17-20, 5E17-30, 5E17-40, 5E17-43, 5E17-46, 5E17-50, 5E17-60, 5E17-63, 5E17-70 e 5E17-80 , para verificar se o  destinatário  está  sendo  informado  corretamente  ou  se está  em  situação que  o  impeça  de constar na NF-e como destinatário na operação com mercadoria ou prestação de serviços.
- Serviço  Autorização  EPEC :  Criadas  as  Regras  de  Validação 6P31-10,  6P31-20,  6P31-30, 6P31-40, 6P31-43, 6P31-46, 6P31-50, 6P31-60 e 6P31-63 , para verificar se o destinatário está sendo informado corretamente ou se está em situação que o impeça de constar na NF-e como destinatário na operação com mercadoria ou prestação de serviços.

## 3 Regras de Validação - Serviço de Autorização NF-e

## 3.1 Grupo B. Identificação da NF-e

| Campo-Seq   | Modelo   | Regra de Validação                                                                                                                                                                                                                                                                                      | Aplic.   |   Msg | Efeito   | Descrição Erro                                |
|-------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|-----------------------------------------------|
| B03-10      | 55/65    | Verificar formação do cNF: - cNF não pode ser igual a 00000000, 11111111, 22222222, 33333333, 44444444, 55555555, 66666666, 77777777, 88888888, 99999999, 12345678, 23456789, 34567890, 45678901, 56789012, 67890123, 78901234, 89012345, 90123456, 01234567. - cNF não pode ser igual a nNF (id: B08). | Obrig.   |   897 | Rej.     | Rejeição: Código numérico em formato inválido |

## 3.2 Grupo BA. Documento Referenciado

| Campo-Seq   | Modelo   | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                   |
|-------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|--------------------------------------------------------------------------------------------------|
| BA10-40     | 55       | Contranota de Produtor referencia somente Nota Fiscal de outro emitente. Não existe nenhuma das ocorrências abaixo: - IE da NF de Produtor referenciada (tag: refNFP/IE) idêntica à IE do Emitente (tag: emit/IE) ou do Remetente (tag: dest/IE); - IE do emitente da NF referenciada (tag: emit/IE) idêntica à IE do Emitente (tag: emit/IE) ou do Remetente (tag: dest/IE). Observação 1 : Identificação de Contranota de Produtor conforme Observação 1 da regra BA10-20. Observação 2 : A utilização e controle da Contranota de Produtor é opcional, a critério da UF. Observação 3 : A critério da UF, a validação da IE do emitente da NF referenciada (tag: emit/IE) pode ser substituída por: - CNPJ-8 do emitente da NF referenciada (tag:emit/CNPJ) idêntico ao CNPJ-8 do Emitente (tag: emit/CNPJ) ou do Remetente (tag: dest/CNPJ). | Facult.  |   320 | Rej.     | Rejeição: Contranota de Produtor referencia somente NF de outro emitente                         |
| BA10-50     | 55       | Contranota de Produtor só pode referenciar NF-e (tag: refNFe) ou NF de Produtor Modelo 4 (tag: refNFP): Observação 1 : Identificação de Contranota de Produtor conforme Observação 1 da regra BA10-20. Observação 2 : Regra opcional, a critério da UF.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Facult.  |   922 | Rej.     | Rejeição: Contranota de Produtor só pode referenciar NF-e ou NF de Produtor Modelo 4             |
| BA20-20     | 55       | Informado Cupom Fiscal referenciado (tag: refECF) ou informado NF modelo 1 ou 2 referenciada (tag: refNF) em NF-e de operação interestadual ou com o exterior (tag: idDest<>1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Facult.  |   923 | Rej.     | Rejeição: Referenciado documento de operação interna em operação interestadual ou com o exterior |
| BA20-30     | 55/65    | InformadoCupom Fiscal referenciado (tag: refECF) em UFque não permite essa referência. Observação : Regra de validação opcional, a critério da UF.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Facult.  |   924 | Rej.     | Rejeição: Informado Cupom Fiscal referenciado                                                    |

![Image](assets/image_000016_6d7b7d8bf9bf06bc72b5443df25801d1a7307d0ded575c3f4ab989f3d32cda82.png)

## 3.3 Grupo E. Identificação do Destinatário

| Campo-Seq Modelo   | Campo-Seq Modelo   | Regra de Validação Aplic.                                                                                                                                                                                                | Msg Efeito   |   Msg Efeito | Descrição Erro   | Descrição Erro                                                                                   |
|--------------------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|--------------|------------------|--------------------------------------------------------------------------------------------------|
| E03a-30            | 55/65              | Se informado 'idEstrangeiro' não pode ser informada 'IE' do destinatário (tag: dest/IE).                                                                                                                                 | Obrig.       |          925 | Rej.             | Rejeição: NF-e com identificação de estrangeiro e inscrição estadual informada para destinatário |
| E14-30             | 55/65              | Se endereço do destinatário é no Exterior (tag: dest/UF = 'EX"): - Código do país 'cPais' (id: E14) não pode ser 1058 (Brasil).                                                                                          | Obrig        |          926 | Rej              | Rejeição: Operação com Exterior e país de destino igual a Brasil                                 |
| E16a-40            | 55                 | Informado indicador de IE do Destinatário não-contribuinte (tag: indIEDest=9) e não é operação com consumidor final (tag: indFinal<>1) em operação de saída (tag: tpNF=1) que não é com exterior (tag:idDest<>3). Obrig. |              |          696 | Rej.             | Rejeição: Operação com não contribuinte deve indicar operação com consumidor final               |

## 3.4 Detalhamento Produtos e Serviços

| Campo-Seq Modelo   | Regra de Validação                                                                                                                                                        | Aplic.   |   Msg | Efeito   | Descrição Erro                                     |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|----------------------------------------------------|
| H02-10 55/65       | Número sequencial do item no arquivo XML 'nItem' fora de ordem incremental, consecutiva, a partir de 1. Observação : Regra de validação opcional, a critério da UF. Obrig |          |   927 | Rej.     | Rejeição: Número do item fora da ordem sequencial. |

## 3.5 Grupo I. Produtos e Serviços da NF-e

| Campo-Seq   | Modelo   | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                 | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                                             |
|-------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|----------------------------------------------------------------------------------------------------------------------------|
| I05f-10     | 55/65    | Informado código de benefício fiscal (tag: cBenef) para CST sem benefício fiscal (CST = 00, 10, 60), conforme Tabela de apoio publicada no Portal Nacional da NF-e Observação : Implementação a critério da UF, por CST e por modelo de DF-e.                                                                                                                                                      | Facul.   |   928 | Rej      | Rejeição: Informado código de benefício fiscal para CST sem benefício fiscal [nItem: nnn]                                  |
| I05f-20     | 55/65    | Se informado código de benefício fiscal (tag: cBenef): - verificar se tipo de código do benefício corresponde ao CST com benefício fiscal. Exemplo : Código de benefício fiscal de isenção deve ser utilizado com CST de isenção. Observação 1: Implementação a critério da UF, por modelo de DF-e. Observação 2: Tabela de código de benefício fiscal por UF publicada no Portal Nacional da NF-e | Facult.  |   931 | Rej.     | Rejeição: CST não corresponde ao tipo de código de benefício fiscal [nItem: nnn]                                           |
| I05f-30     | 55/65    | Se informado código de benefício fiscal (tag: cBenef), obrigatório informar valor do ICMS desonerado (tag: vICMSDeson) e o motivo de desoneração (tag: motDesICMS) Observações : Implementação a critério da UF                                                                                                                                                                                    | Facult.  |   934 | Rej.     | Rejeição: Não informado valor do ICMS desonerado ou o Motivo de desoneração [nItem: nnn]                                   |
| I05g-10     | 55/65    | Grupo de informações sobre o Crédito Presumido (tag: gCred) não permitido para UF Exceção: Não se aplica para (tpEmis = 3-NFF) (NT 2021.002) Observação: Regra a critério da UF                                                                                                                                                                                                                    | Facult.  |   507 | Rej.     | Grupo de informações sobre o Crédito Presumido não permitido                                                               |
| I05h-10     | 55/65    | Se informado código de crédito presumido (tag: cCredPresumido): - Verificar se código de crédito presumido existe, está vigente e corresponde a um código de crédito presumido, conforme tabela de código de benefício fiscal por UF publicada no Portal da Secretaria de Fazenda da respectiva UF (NT 2019.001).                                                                                  | Facult.  |   664 | Rej.     | Rejeição: Informado código de crédito presumido (cCredPresumido) incorreto, inexistente ou incompatível na UF [nItem: nnn] |
| I08-160     | 55/65    | NF-e com CFOP=1.933, 2.933, 5.933 ou 6.933 (Aquisição ou prestação de serviço), sem o grupo de tributação pelo ISSQN (tag: imposto/ISSQN) (NT2015.002) Obrig.                                                                                                                                                                                                                                      |          |   374 | Rej.     | Rejeição: CFOP incompatível com o grupo de tributação [nItem:999]                                                          |

![Image](assets/image_000017_6d7b7d8bf9bf06bc72b5443df25801d1a7307d0ded575c3f4ab989f3d32cda82.png)

![Image](assets/image_000018_19a4c364c6a91bfbc04f9aab918422f085a8072d0c64278e52637c246b4078f7.png)

| Campo-Seq   | Modelo   | Regra de Validação                                                                                                                                                        | Aplic.   |   Msg | Efeito   | Descrição Erro                                                    |
|-------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|-------------------------------------------------------------------|
| I08-170     | 55/65    | NF-e com CFOP diferente de 1.933, 2.933, 5.933 e 6.933 (Aquisição ou prestação de serviço), com o grupo de tributação pelo ISSQN (tag: imposto/ISSQN) (NT2015.002) Obrig. |          |   374 | Rej.     | Rejeição: CFOP incompatível com o grupo de tributação [nItem:999] |
| I08-171     | 55       | NF-e (mod=55) com os CFOP=1.933, 2.933, 5.933 e 6.933 (Aquisição ou prestação de serviço), no grupo de tributação do ICMS (tag:imposto/ICMS). Obrig.                      |          |   374 | Rej      | Rejeição: CFOP incompatível com o grupo de tributação [nItem:nnn] |

## 3.6 Grupo N. Item / Tributo: ICMS

| Campo-Seq   | Modelo   | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Aplic. Msg Efeito   |   Aplic. Msg Efeito | Aplic. Msg Efeito   | Descrição Erro                                                                               |
|-------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|---------------------|---------------------|----------------------------------------------------------------------------------------------|
| N07-10      | 55       | Não informados campos de valores do CST 51 (Diferimento): - modBC (id: N13), pRedBC (id: N14), vBC (id: N15), pICMS (id: N16), vICMSOp (id: N16a), pDif (id: N16b), vICMSDif (id: N16c), vICMS (id: N17) Observações : Implementação a critério da UF                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Facult.             |                 929 | Rej.                | Rejeição: Informado CST de diferimento sem as informações de diferimento [nItem: nnn]        |
| N12-84      | 55/65    | Se informado CST com benefício fiscal (CST = 20, 30, 40, 41, 50, 51, 60, 70 ou 90): - Obrigatório informar o código de benefício fiscal (tag: cBenef) Observação 1: Implementação a critério da UF, por modelo de DF-e e por CST. Observação 2: Tabela de código de benefício fiscal por UF publicada no Portal Nacional da NF-e Exceção : Não se aplica esta regra de validação no caso de CST=90 e: -Percentual de Redução de Base de Cálculo (tag: pRedBC) igual a zero; -e (Percentual de Redução de Base de Cálculo do ICMS-ST (tag: pRedBCST) igual a zero e operação interna (idDest=1).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Facult.             |                 930 | Rej.                | Rejeição: CST com benefício fiscal e não informado o código de benefício fiscal [nItem: nnn] |
| N12-85      | 55/65    | Se informado CST e não informado código de benefício fiscal: - Verificar se CST exige código de benefício fiscal (tag: cBenef), conforme tabela de código de benefício fiscal por UF publicada no Portal Nacional da NF-e da Fazenda da respectiva UF. Observação 1 : Implementação a critério da UF, por modelo de DF-e e por CST. Observação 2 : Para o CST informado, o sistema autorizador apenas verifica se existe qualquer cBenef na tabela publicada no Portal da NFe Fazenda da respectiva UF, sem verificar a compatibilidade. Exceção 1: a RV não se aplica quando Finalidade de emissão da NFe (tag: finNFe) igual a Devolução de Mercadoria e Identificador de local de destino da operação (tag: idDest) igual a Operação interestadual ou com o Exterior; Exceção 2: a critério da UF, a RV não se aplica quando Finalidade de emissão da NF-e (tag: finNFe) igual a Devolução de Mercadoria; Exceção 3: a critério da UF, a RV não se aplica quando Finalidade de emissão da NF-e (tag: finNFe) igual a NF-e de Ajuste; Exceção 4: a critério da UF, a RV não se aplica quando Tipo de Operação (tag: tpNF) igual à Entrada. | Facult.             |                 930 | Rej.                | Rejeição: CST com benefício fiscal e não informado o código de benefício fiscal [nItem: nnn] |
| N12-86      | 55/65    | Se informado CST e informado código de benefício fiscal: - Verificar se CST não possui código de benefício fiscal, conforme tabela de código de benefício fiscal por UF publicada no Portal Nacional da NF-e da Fazenda da respectiva UF. Observação 1 : Implementação a critério da UF, e por modelo de DF-e e CST.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Facult.             |                 928 | Rej.                | Rejeição: Informado código de benefício fiscal para CST sem benefício fiscal [nItem: nnn]    |

## Nota Fiscal Eletrônica

![Image](assets/image_000019_6d7b7d8bf9bf06bc72b5443df25801d1a7307d0ded575c3f4ab989f3d32cda82.png)

| Campo-Seq   | Modelo   | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                           |
|-------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|------------------------------------------------------------------------------------------|
|             |          | Observação 2 : Para o CST informado, o sistema apenas verifica se não existe qualquer cBenef na tabela publicada no Portal da NF-e Fazenda da respectiva UF, sem verificar a compatibilidade. Exceção 1: a RV não se aplica quando Finalidade de emissão da NFe (tag: finNFe) igual a Devolução de Mercadoria e Identificador de local de destino da operação (tag: idDest) igual a Operação interestadual ou com o Exterior. Exceção 2: a critério da UF, a RV não se aplica quando Finalidade de emissão da NF-e (tag: finNFe) igual a Devolução de Mercadoria; Exceção 3: a critério da UF, a RV não se aplica quando Finalidade de emissão da NF-e (tag: finNFe) igual a NF-e de Ajuste; Exceção 4: a critério da UF, a RV não se aplica quando Tipo de Operação (tag: tpNF) igual à Entrada.                                                                                                                                                                                                                                               |          |       |          |                                                                                          |
| N12-88      | 55/65    | Se informado código de benefício fiscal (tag: cBenef): - verificar se tipo de código do benefício corresponde ao CST com benefício fiscal. Exemplo : Código de benefício fiscal de isenção deve ser utilizado com CST de isenção. Observação 1 : Implementação a critério da UF, por modelo de DF-e e por CST. Observação 2 : Tabela de código de benefício fiscal por UF publicada no Portal Nacional da NF-e                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Facult   |   931 | Rej.     | Rejeição: CST não corresponde ao tipo de código de benefício fiscal [nItem: nnn]         |
| N12-90      | 55/65    | Se CST de ICMS = (20, 30, 40, 41, 50, 70 ou 90): - Verificar se informado Obrigatório informar o valor do ICMS desonerado (tag:vICMSDeson) e o Motivo da Desoneração (tag: motDesICMS). Observação 1 : Implementação a critério da UF, por modelo de DF-e e por CST. Observação 2: Tabela de código de benefício fiscal por UF publicada no Portal Nacional da NF-e Exceção 1: a RV não se aplica quando Finalidade de emissão da NFe (tag: finNFe) igual a Devolução de Mercadoria e Identificador de local de destino da operação (tag: idDest) igual a Operação interestadual ou com o Exterior; Exceção 2: a critério da UF, a RV não se aplica quando Finalidade de emissão da NF-e (tag: finNFe) igual a Devolução de Mercadoria; Exceção 3: a critério da UF, a RV não se aplica quando Finalidade de emissão da NF-e (tag: finNFe) igual a NF-e de Ajuste; Exceção 4: a critério da UF, a RV não se aplica quando Tipo de Operação (tag: tpNF) igual à Entrada. Exceção 1 5: Não se aplica esta regra de validação no caso de CST=90 e: | Facult.  |   934 | Rej.     | Rejeição: Não informado valor do ICMS desonerado ou o Motivo de desoneração [nItem: nnn] |
| N12-94      | 55/65    | Se informado CST e informado código de benefício fiscal: - Verificar se código de benefício fiscal está vigente e corresponde ao CST informado, conforme tabela de código de benefício fiscal por UF publicada no Portal Nacional da NF-e da Fazenda da respectiva UF. Observação : Implementação a critério da UF, por modelo de DF-e e por CST.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Facult.  |   931 | Rej.     | Rejeição: Informado código de benefício fiscal incompatível com CST e UF [nItem: nnn]    |

## Nota Fiscal Eletrônica

![Image](assets/image_000020_6d7b7d8bf9bf06bc72b5443df25801d1a7307d0ded575c3f4ab989f3d32cda82.png)

| Campo-Seq   | Modelo   | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Aplic.         |   Msg | Efeito   | Descrição Erro                                                                                                                        |
|-------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|-------|----------|---------------------------------------------------------------------------------------------------------------------------------------|
| N12-97      | 55       | Exceção 1: a RV não se aplica quando Finalidade de emissão da NFe (tag: finNFe) igual a Devolução de Mercadoria e Identificador de local de destino da operação (tag: idDest) igual a Operação interestadual ou com o Exterior. Exceção 2: a critério da UF, a RV não se aplica quando Finalidade de emissão da NF-e (tag: finNFe) igual a Devolução de Mercadoria; Exceção 3: a critério da UF, a RV não se aplica quando Finalidade de emissão da NF-e (tag: finNFe) igual a NF-e de Ajuste; Exceção 4: a critério da UF, a RV não se aplica quando Tipo de Operação (tag: tpNF) igual à Entrada. Nota : Para itens sem benefício fiscal, a UF poderá exigir a informação da literal 'SEM CBENEF' para alguns CST, vide tabela publicada no Portal Nacional da NF-e da Fazenda da respectiva UF. Não informados campos de valores do CST 51 (Diferimento): - modBC (id: N13), pRedBC (id: N14), vBC (id: N15), pICMS (id: N16), vICMSOp (id: pDif (id: N16b), vICMSDif (id: N16c), vICMS (id: N17) | N16a), Facult. |   929 | Rej.     | Rejeição: Informado CST de diferimento sem as informações de diferimento [nItem: nnn]                                                 |
| N12-98      | 55/65    | à Entrada. Se informado código de benefício fiscal: - Verificar se código de benefício fiscal existe e está vigente, conforme tabela de código de benefício fiscal por UF publicada no Portal Nacional da NF-e da Fazenda da respectiva UF. Observação : Implementação a critério da UF e por modelo de DF-e. Exceção 1: a RV não se aplica quando Finalidade de emissão da NFe (tag: finNFe) igual a Devolução de Mercadoria e Identificador de local de destino da operação (tag: idDest) igual a Operação interestadual ou com o Exterior. Exceção 2: a critério da UF, a RV não se aplica quando Finalidade de emissão da NF-e (tag: finNFe) igual a Devolução de Mercadoria; Exceção 3: a critério da UF, a RV não se aplica quando Finalidade de emissão da NF-e                                                                                                                                                                                                                               | Facult.        |   946 | Rej.     | Rejeição: Informado código de benefício fiscal incorreto ou inexistente na UF [nItem: nnn]                                            |
| N14a-10     | 55       | Exceção 5: essa RV não se aplica quando informado CSOSN (Simples Nacional). Se CST de ICMS = 51 (diferimento) e informado tag:ICMS51/pRedBC (id:N14) maior que zero, é obrigatório informar cBenefRBC (id:N14a) (NT 2019.001). Observação: Implementação a critério da UF.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Facult.        |   665 | Rej.     | Rejeição: Não informado código de benefício fiscal de redução de BC (cBenefRBC) quando percentual de redução de BC for maior que zero |

![Image](assets/image_000021_6d7b7d8bf9bf06bc72b5443df25801d1a7307d0ded575c3f4ab989f3d32cda82.png)

| Campo-Seq   |   Modelo | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                                                        |
|-------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|---------------------------------------------------------------------------------------------------------------------------------------|
|             |          | Exceção 1: a RV não se aplica quando Finalidade de emissão da NFe (tag: finNFe) igual a Devolução de Mercadoria e Identificador de local de destino da operação (tag: idDest) igual a Operação interestadual ou com o Exterior. Exceção 2: a critério da UF, a RV não se aplica quando Finalidade de emissão da NF-e (tag: finNFe) igual a Devolução de Mercadoria; Exceção 3: a critério da UF, a RV não se aplica quando Finalidade de emissão da NF-e (tag: finNFe) igual a NF-e de Ajuste; Exceção 4: a critério da UF, a RV não se aplica quando Tipo de Operação (tag: tpNF) igual à Entrada.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |          |   666 |          | no grupo de tributação de diferimento [nItem: nnn]                                                                                    |
| N14a-20     |       55 | Se CST de ICMS = 51 (diferimento) e informado tag:ICMS51/cBenefRBC (id:N14a): - Verificar se código de benefício fiscal de redução de BC (cBenefRBC) existe, está vigente e corresponde a um código de benefício de redução de base de cálculo (coluna CST 20 = SIM), conforme tabela de código de benefício fiscal por UF publicada no Portal da Secretaria de Fazenda da respectiva UF (NT 2019.001). Observação: Implementação a critério da UF. Exceção 1: a RV não se aplica quando Finalidade de emissão da NFe (tag: finNFe) igual a Devolução de Mercadoria e Identificador de local de destino da operação (tag: idDest) igual a Operação interestadual ou com o Exterior. Exceção 2: a critério da UF, a RV não se aplica quando Finalidade de emissão da NF-e (tag: finNFe) igual a Devolução de Mercadoria; Exceção 3: a critério da UF, a RV não se aplica quando Finalidade de emissão da NF-e (tag: finNFe) igual a NF-e de Ajuste; Exceção 4: a critério da UF, a RV não se aplica quando Tipo de Operação (tag: tpNF) igual à Entrada. | Facult.  |       | Rej.     | Rejeição: Informado código de benefício fiscal de redução de BC (cBenefRBC) incorreto, inexistente ou incompatível na UF [nItem: nnn] |
| N18-10      |       55 | Se o campo modBCST = '4' Margem Valor Agregado, obrigatório o preenchimento do campo pMVAST Nota : Regra de Validação opcional a critério da UF.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Facult.  |   932 | Rej.     | Rejeição: Informada modalidade de determinação da BCda ST comoMVAenão informado o campo pMVAST [nItem: nnn]                           |
| N18-20      |       55 | Se o campo modBCST <> '4' Margem Valor Agregado, não deverá ser preenchido o campo pMVAST Nota : Regra de Validação opcional a critério da UF.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Facult.  |   933 | Rej.     | Rejeição: Informada modalidade de determinação da BC da ST diferente de MVA e informado o campo pMVAST [nItem: nnn]                   |
| N28-20      |       55 | Se informado tag:motDesICMS = 7 (desoneração Suframa): - deve ser informado um dos CFOP abaixo: 1203, 1204, 1208, 1209, 2203, 2204, 2208, 2209, 5109, 5110, 5120, 5151, 5152, 5651, 5652, 5654, 5655, 5658, 5659, 5910, 6905, 6109, 6110, 6120, 6122, 6123, 6151, 6152, 6651, 6652, 6654, 6655, 6658, 6659, 6910, 6923 (NT2012.003) (NT2013.005 v1.10)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Facul.   |   626 | Rej.     | Rejeição: CFOP de operação isenta para ZFM diferente do previsto [nItem: 999]                                                         |

## 3.6.1 Datas, Exceções e Modelos para Regras de Validação: N12-85, N12-86, N12-90, N12-94, N12-97, N12-98, N14a-10, N14a-20 e I05h-10

A tabela a seguir substitui a do item anterior (1.8), pois adiciona exceções e modelo aplicável.

Na tabela a seguir encontram-se as Unidades da Federação que implementarão as Regras de Validação N12-85, N12-86, N12-90, N12-94, N12-97 e N1298, previstas nesta Nota Técnica. Na legenda são encontradas as datas de aplicação, as exceções e os modelos aplicáveis (55/65), a critério da UF.

![Image](assets/image_000022_6d7b7d8bf9bf06bc72b5443df25801d1a7307d0ded575c3f4ab989f3d32cda82.png)

| UF        | Regra de validação - Aplicação e Exceções   | Regra de validação - Aplicação e Exceções   | Regra de validação - Aplicação e Exceções   | Regra de validação - Aplicação e Exceções   | Regra de validação - Aplicação e Exceções   | Regra de validação - Aplicação e Exceções   | Regra de validação - Aplicação e Exceções   | Regra de validação - Aplicação e Exceções   | Regra de validação - Aplicação e Exceções   |
|-----------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|
| UF        | N12-85                                      | N12-86                                      | N12-90                                      | N12-94                                      | N12-97                                      | N12-98                                      | N14a-10                                     | N14a-20                                     | I05h-10                                     |
| DF        | (D6), (55/65)                               | (D6), (55/65)                               | (D*)                                        | (D6), (55/65)                               | (D*)                                        | (D4), (55/65)                               | (D*)                                        | (D*)                                        | (D*)                                        |
| DF        | (E2, E3, E4)                                | (E2, E3, E4)                                | (D*)                                        | (E2, E3, E4)                                | (D*)                                        | (E2, E3, E4)                                |                                             |                                             |                                             |
| ES        | (D*), (55)                                  | (D*), (55)                                  | (D*), (55)                                  | (D*), (55)                                  | (D*), (55)                                  | (D*), (55)                                  | (D*)                                        | (D*)                                        | (D*)                                        |
| GO        | (D5), (55 / 65)                             | (D5), (55 / 65)                             | (D5), (55 / 65)                             | (D5), (55 / 65)                             | (D5), (55 / 65)                             | (D5), (55 / 65)                             | (D*)                                        | (D*)                                        | (D*)                                        |
| GO        | (E2, E3, E4)                                | (E2, E3, E4)                                | (E2, E3)                                    | (E2, E3)                                    | (E2, E3)                                    | (E2, E3)                                    |                                             |                                             |                                             |
| PR        | (D1), (55/65)                               | (D1), (55/65)                               | (D*)                                        | (D2), (55/65)                               | (D1), (55/65)                               | (D3), (55/65)                               | (D*)                                        | (D*)                                        | (D*)                                        |
| PR        | (D2), (55/65)                               | (D2), (55/65)                               | (D2), (55/65)                               | (D2), (55/65)                               | (D2), (55/65)                               | (D3), (55/65)                               | (D*)                                        | (D*)                                        | (D*)                                        |
| RJ        | (E2, E3)                                    | (E2, E3)                                    | (E2, E3)                                    | (E2, E3)                                    | (E2, E3)                                    | (E2, E3)                                    |                                             |                                             |                                             |
| RS        | (D2), (55/65)                               | (D2), (55/65)                               | (D*)                                        | (D*)                                        | (D*)                                        | (D3), (55/65)                               | (D*)                                        | (D*)                                        | (D*)                                        |
| SC        | (E3,E4)                                     | (E3,E4)                                     |                                             |                                             |                                             | (E3,E4)                                     |                                             |                                             |                                             |
|           | (D7), (55/65)                               | (D8), (55/65)                               | (D*)                                        | (D8), (55/65)                               | (D*)                                        | (D8), (55/65)                               | (D9), (55)                                  | (D9), (55)                                  | (D8), (55/65)                               |
|           | (E2,E3,E4)                                  | (E2,E3,E4)                                  |                                             | (E2,E3,E4)                                  |                                             | (E2,E3,E4)                                  | (E2,E3,E4)                                  | (E2,E3,E4)                                  |                                             |
| SP        | (D10) (55/65)                               | (D10) (55/65)                               | (D*)                                        | (D10) (55/65)                               | (D10) (55)                                  | (D10) (55/65)                               | (D*)                                        | (D*)                                        | (D*)                                        |
| SP        | (E2, E3, E4)                                | (E2, E3, E4)                                |                                             | (E2, E3, E4)                                | (E2, E3, E4)                                | (E2, E3, E4) (D*)                           |                                             |                                             |                                             |
| Demais UF | (D*)                                        | (D*)                                        | (D*)                                        | (D*)                                        | (D*)                                        |                                             |                                             |                                             |                                             |

Datas para aplicação das Regras de validação (D), com respectivo Modelo de DF-e:

- (D*) - Regra de validação não será aplicada
- (D1) - Aplicação a partir de 02/09/2019
- (D2) - Aplicação a partir de 01/10/2019
- (D3) - Aplicação a partir de 11/05/2020 10/8/2020 em Produção (Homologação: 16/03/2020)
- (D4) - Aplicação a partir de 01/02/2021 em Produção (Homologação: 05/10/2020)
- (D5) - Aplicação a partir de 01/01/2023 01/07/2023 em Produção (Homologação: 01/10/2022)
- (D6) - Aplicação a partir de: NF-e - 01/02/2023 01/03/2023 04/09/2023 em Produção (Homologação: 05/10/2020); NFC-e - 01/06/2023 01/04/2024 01/07/2024 02/09/2024 em Produção (Homologação: 05/10/2020)
- (D7) - Aplicação a partir de NF-e: 03/02/2025 01/09/2025 em Produção; NFC-e: 01/04/2025 01/09/2025 em Produção; (Homologação: 04/11/2024)
- (D8) - Aplicação a partir de 28/04/2025 03/11/2025 em Produção; (Homologação: 02/12/2024)
- (D9) - Aplicação a partir de 01/09/2025 06/04/2026 em Produção; (Homologação: 02/12/2024)
- (D10) - Aplicação a partir de 06/04/2026 em Produção; (Homologação: 12/01/2026)

Aplicação aos Modelos de DF-e: (55); (65); ou (55/65)

Exceções constantes nas Regras de Validação, a critério da UF:

- (E1) - Exceção 1: a RV não se aplica quando Finalidade de emissão da NF-e (tag: finNFe) igual a Devolução de Mercadoria e Identificador de local de destino da operação (tag: idDest) igual a Operação interestadual ou com o Exterior;
- (E2) - Exceção 2: a RV não se aplica quando Finalidade de emissão da NF-e (tag: finNFe) igual a Devolução de Mercadoria;
- (E3) - Exceção 3: a RV não se aplica quando Finalidade de emissão da NF-e (tag: finNFe) igual a NF-e de ajuste;
- (E4) - Exceção 4: a RV não se aplica quando Tipo de Operação (tag: tpNF) igual a Entrada.

Observação: A Exceção 1, constante nas respectivas Regras de Validação, aplica-se a todas as UF. Assim, não necessita estar no quadro acima.

As datas aqui definidas, juntamente com todas as demais informações a respeito das regras de validação opcionais por UF, podem ser consultadas em tabela publicada no Portal Nacional da NFC-e, na área 'Regras de Validação' da aba 'Desenvolvedor'.

Para contribuintes estabelecidos no Estado do Rio Grande do Sul, as Regras de Validação N12-85 e N12-86 permitirão informar qualquer CST até 31/03/2020 09/08/2020 no ambiente de autorização em produção, conforme tabela disponibilizada no Portal da NF-e. Em homologação, o contribuinte já pode testar a validação dessa Regras:

- A RV N12-94 será desativada para o Rio Grande do Sul a partir da publicação desta NT.
- A RV N12-98 será ativada conforme as datas de homologação e produção previstas nesta NT.

## 3.6.2 Arquivo no Portal Nacional da NF-e contendo os endereços das tabelas de 'cBenef x CST' das UF:

Na área 'Diversos' da aba 'Documentos' no Portal Nacional da NF-e, consta o arquivo contendo os endereços onde estão disponibilizadas as Tabelas de 'cBenef x CST' nos portais das Secretarias de Fazenda do Distrito Federal e dos Estados do Paraná, Rio de Janeiro e Rio Grande do Sul.

## 3.7 Grupo W. Total da NF-e

| Campo-Seq Modelo   | Regra de Validação                                                                                                                                                                                                           |   Aplic. Msg | Efeito   | Descrição Erro                                                                                                                        |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|----------|---------------------------------------------------------------------------------------------------------------------------------------|
| W03-20 55/65       | Valor total da base de cálculo tag 'vBC' (id:W03) superior ao valor limite estabelecido pela SEFAZ por modelo de DF-e. Observação : o valor total máximo da base de cálculo é de R$ 200.000,00 (Duzentos mil reais). Facult. |          935 | Rej.     | Rejeição: Valor total da Base de Cálculo superior ao valor limite estabelecido [Valor Limite: R$ XXX.XXX,XX] (valor definido pela UF) |

## 3.8 Banco de Dados: Emitente

| Campo-Seq Modelo   | Regra de Validação   | Aplic. Msg Efeito   | Descrição Erro   |
|--------------------|----------------------|---------------------|------------------|

![Image](assets/image_000023_6d7b7d8bf9bf06bc72b5443df25801d1a7307d0ded575c3f4ab989f3d32cda82.png)

![Image](assets/image_000024_6d7b7d8bf9bf06bc72b5443df25801d1a7307d0ded575c3f4ab989f3d32cda82.png)

| 1C03-10   | 55/65   | Razão Social (tag: emit\xNome) do emitente diverge do informado no cadastro da SEFAZ. Observação: Regra de validação opcional, a critério da UF. Facult. 936   | Rej   | Rejeição: Razão Social do emitente diverge do informado no cadastro da SEFAZ   |
|-----------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|--------------------------------------------------------------------------------|

## 3.9 Banco de Dados: Destinatário

| Campo-Seq Modelo Regra de Validação   |   Campo-Seq Modelo Regra de Validação | Campo-Seq Modelo Regra de Validação                                                                                                                                                                                                           | Aplic. Msg Efeito   |   Aplic. Msg Efeito | Aplic. Msg Efeito   | Descrição Erro                                           |
|---------------------------------------|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|---------------------|---------------------|----------------------------------------------------------|
| 5E17-10                               |                                    55 | Se informada IE do Destinatário: - Acessar Cadastro de Contribuinte da UF (Chave: UF Dest, IE Dest.) (*5) - IE destinatário não cadastrada (*7)                                                                                               | Obrig.              |                 233 | Rej.                | Rejeição: IE do destinatário não cadastrada              |
| 5E17-20                               |                                    55 | - Se informado CNPJ do destinatário e IE destinatário não vinculada ao CNPJ (tratar Regime Especial de IE Única)                                                                                                                              | Obrig.              |                 234 | Rej.                | Rejeição: IE do destinatário não vinculada ao CNPJ       |
| 5E17-30                               |                                    55 | - Se informado CPF do destinatário e IE destinatário não vinculada ao CPF (*7)                                                                                                                                                                | Obrig.              |                 624 | Rej.                | Rejeição: IE Destinatário não vinculada ao CPF           |
| 5E17-40                               |                                    55 | - Destinatário em situação irregular perante o Fisco, vedada operação na UF (CCC.cSitCNPJ=3-Vedado)                                                                                                                                           | Obrig.              |                 302 | Den.                | Uso Denegado: Irregularidade fiscal do destinatário      |
| 5E17-43                               |                                    55 | - Destinatário bloqueado na UF (CCC.cSitCNPJ=2-Bloqueado)                                                                                                                                                                                     | Obrig.              |                 305 | Rej.                | Rejeição: Destinatário bloqueado na UF                   |
| 5E17-46                               |                                    55 | - IE do Destinatário não está ativa na UF (CCC.cSitIE=0-Não habilitado) (*7)                                                                                                                                                                  | Obrig.              |                 306 | Rej.                | Rejeição: IE do destinatário não está ativa na UF        |
| 5E17-50                               |                                    55 | Se IE Destinatário não informada e informado CNPJ do destinatário: - Acessar Cadastro Contribuinte da UF (Chave: UF-Dest, CNPJ-Dest) (*6) - Destinatário possui IE ativa na UF (CCC.cSitIE=1-Habilitado) e CCC.IndIEDestOpc = 0 - Obrigatório | Obrig.              |                 232 | Rej.                | Rejeição: IE do destinatário não informada               |
| 5E17-60                               |                                    55 | - Destinatário com CNPJ vedado na UF (CCC.cSitCNPJ=3-Vedado)                                                                                                                                                                                  | Obrig.              |                 303 | Den.                | Uso Denegado: Destinatário não habilitado a operar na UF |
| 5E17-63                               |                                    55 | - Destinatário bloqueado na UF (CCC.cSitCNPJ=2-Bloqueado)                                                                                                                                                                                     | Obrig.              |                 305 | Rej.                | Rejeição: Destinatário bloqueado na UF                   |
| 5E17-70                               |                                    55 | Mensagens opcionais se informada IE do destinatário e IE não vinculada ao CNPJ/CPF. - Acessar Cadastro de Pessoa Jurídica ou Pessoa Física: - CNPJ destinatário não cadastrado                                                                | Facult.             |                 246 | Rej.                | Rejeição: CNPJ Destinatário não cadastrado               |
| 5E17-80                               |                                    55 | - CPF destinatário não cadastrado (*7)                                                                                                                                                                                                        | Facult.             |                 623 | Rej.                | Rejeição: CPF Destinatário não cadastrado                |

## 4 Regras de Validação - Serviço Autorização Evento Prévio de Emissão em Contingência

|   Campo-Seq | Modelo                                                                                                                                     | Regra de Validação   |   Aplic. Msg Efeito | Aplic. Msg Efeito   | Aplic. Msg Efeito                                   | Descrição Erro   |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------|----------------------|---------------------|---------------------|-----------------------------------------------------|------------------|
|          55 | Se informada IE do Destinatário: - Acessar Cadastro de Contribuinte da UF (Chave: UF Dest, IE Dest.) (*5) - IE destinatário não cadastrada | Obrig.               |                 233 | Rej.                | Rejeição: IE do destinatário não cadastrada         | 6P31-10          |
|          55 | - Se informado CNPJ do destinatário e IE destinatário não vinculada ao CNPJ (tratar Regime Especial de IE Única)                           | Obrig.               |                 234 | Rej.                | Rejeição: IE do destinatário não vinculada ao CNPJ  | 6P31-20          |
|          55 | - Se informado CPF do destinatário e IE destinatário não vinculada ao CPF (*7)                                                             | Obrig.               |                 624 | Rej.                | Rejeição: IE Destinatário não vinculada ao CPF      | 6P31-30          |
|          55 | - Destinatário em situação irregular perante o Fisco, vedada operação na UF (CCC.cSitCNPJ=3-Vedado)                                        | Obrig.               |                 302 | Rej.                | Uso Denegado: Irregularidade fiscal do destinatário | 6P31-40          |

![Image](assets/image_000025_19a4c364c6a91bfbc04f9aab918422f085a8072d0c64278e52637c246b4078f7.png)

|   6P31-43 | 55                                                                                                                                                                                                                                            | - Destinatário bloqueado na UF (CCC.cSitCNPJ=2-Bloqueado)   |   Obrig. | 305   | Rej.                                                     | Rejeição: Destinatário bloqueado na UF   |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|----------|-------|----------------------------------------------------------|------------------------------------------|
|        55 | - IE do Destinatário não está ativa na UF (CCC.cSitIE=0-Não habilitado) (*7)                                                                                                                                                                  | Obrig.                                                      |      306 | Rej.  | Rejeição: IE do destinatário não está ativa na UF        | 6P31-46                                  |
|        55 | Se IE Destinatário não informada e informado CNPJ do destinatário: - Acessar Cadastro Contribuinte da UF (Chave: UF-Dest, CNPJ-Dest) (*6) - Destinatário possui IE ativa na UF (CCC.cSitIE=1-Habilitado) e CCC.IndIEDestOpc = 0 - Obrigatório | Obrig.                                                      |      232 | Rej.  | Rejeição: IE do destinatário não informada               | 6P31-50                                  |
|        55 | - Destinatário com CNPJ vedado na UF (CCC.cSitCNPJ=3-Vedado)                                                                                                                                                                                  | Obrig.                                                      |      303 | Den.  | Uso Denegado: Destinatário não habilitado a operar na UF | 6P31-60                                  |
|        55 | - Destinatário bloqueado na UF (CCC.cSitCNPJ=2-Bloqueado)                                                                                                                                                                                     | Obrig.                                                      |      305 | Rej.  | Rejeição: Destinatário bloqueado na UF                   | 6P31-63                                  |

## 5 Novos Códigos de Rejeição

|   Código | MOTIVO DE NÃO ATENDIMENTO DA SOLICITAÇÃO                                                                                                                                                 |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      305 | Rejeição: Destinatário bloqueado na UF                                                                                                                                                   |
|      306 | Rejeição: IE do destinatário não está ativa na UF                                                                                                                                        |
|      507 | Grupo de informações sobre o Crédito Presumido não permitido                                                                                                                             |
|      626 | Rejeição: CFOP de operação isenta para ZFM diferente do previsto [nItem: 999]                                                                                                            |
|      664 | Rejeição: Informado código de crédito presumido (cCredPresumido) incorreto, inexistente ou incompatível na UF [nItem: nnn]                                                               |
|      665 | Rejeição: Não informado código de benefício fiscal de redução de BC (cBenefRBC) quando percentual de redução de BC for maior que zero no grupo de tributação de diferimento [nItem: nnn] |
|      666 | Rejeição: Informado código de benefício fiscal de redução de BC (cBenefRBC) incorreto, inexistente ou incompatível na UF [nItem: nnn]                                                    |
|      922 | Rejeição: Contranota de Produtor só pode referenciar NF-e ou NF de Produtor Modelo 4                                                                                                     |
|      923 | Rejeição: Referenciado documento de operação interna em operação interestadual ou com o exterior                                                                                         |
|      924 | Rejeição: Informado Cupom Fiscal referenciado.                                                                                                                                           |
|      925 | Rejeição: NF-e com identificação de estrangeiro e inscrição estadual informada para destinatário                                                                                         |
|      926 | Rejeição: Operação com Exterior e país de destino igual a Brasil.                                                                                                                        |
|      927 | Rejeição: Número do item fora da ordem sequencial.                                                                                                                                       |
|      928 | Rejeição: Informado código de benefício fiscal para CST sem benefício fiscal [nItem: nnn]                                                                                                |
|      929 | Rejeição: Informado CST de diferimento sem as informações de diferimento [nItem: nnn]                                                                                                    |
|      930 | Rejeição: CST com benefício fiscal e não informado o código de benefício fiscal [nItem: nnn]                                                                                             |
|      931 | Rejeição: CST não corresponde ao tipo de código de benefício fiscal [nItem: nnn]                                                                                                         |
|      932 | Rejeição: Informada modalidade de determinação da BC da ST como MVA e não informado o campo pMVAST [nItem: nnn]                                                                          |
|      933 | Rejeição: Informada modalidade de determinação da BC da ST diferente de MVA e informado o campo pMVAST [nItem: nnn]                                                                      |
|      934 | Rejeição: Não informado valor do ICMS desonerado ou o Motivo de desoneração [nItem: nnn]                                                                                                 |

![Image](assets/image_000026_6d7b7d8bf9bf06bc72b5443df25801d1a7307d0ded575c3f4ab989f3d32cda82.png)

|   935 | Rejeição: Valor total da Base de Cálculo superior ao valor limite estabelecido [Valor Limite: R$ XXX.XXX,XX] (valor definido pela UF)   |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------|
|   936 | Rejeição: Razão Social do emitente diverge do informado no cadastro da SEFAZ                                                            |
|   946 | Rejeição: Informado código de benefício fiscal incorreto ou inexistente na UF [nItem: nnn]                                              |

## 6 Alteração de Leiaute

A tag modBCST passa a admitir uma sexta modalidade de determinação, que é o próprio valor da operação.

Esta  alteração  viabiliza,  entre  outras  necessidades,  o  preenchimento  da  NF-e  em  operações  realizadas  por  contribuintes  substitutos  tributários responsáveis pelo pagamento:

- do diferencial de alíquota, na venda de mercadorias destinadas a integrar o ativo fixo do adquirente/contribuinte do ICMS
- da ST, como na saída interestadual não tributada de energia ou de combustível e entrada no outro território tributada, com retenção por ST (Convênios ICMS 83/2000 e 110/2007).

## 6.1 Grupo N. Grupo Tributação do ICMS= 10

|   # | ID   | Campo   | Descrição                                   | Ele   | Pai   | Tipo   | Ocor.   |   Tam. | Observação                                                                                                                                                                         |
|-----|------|---------|---------------------------------------------|-------|-------|--------|---------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 179 | N18  | modBCST | Modalidade de determinação da BC do ICMS ST | E     | N03   | N      | 1-1     |      1 | 0=Preço tabelado ou máximo sugerido; 1=Lista Negativa (valor); 2=Lista Positiva (valor); 3=Lista Neutra (valor); 4=Margem Valor Agregado (%); 5=Pauta (valor); 6=Valor da Operação |

## 6.2 Grupo N. Grupo Tributação do ICMS= 30

|   # | ID   | Campo   | Descrição                                   | Ele   | Pai   | Tipo   | Ocor.   |   Tam. | Observação                                                                                                                                                                         |
|-----|------|---------|---------------------------------------------|-------|-------|--------|---------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 196 | N18  | modBCST | Modalidade de determinação da BC do ICMS ST | E     | N05   | N      | 1-1     |      1 | 0=Preço tabelado ou máximo sugerido; 1=Lista Negativa (valor); 2=Lista Positiva (valor); 3=Lista Neutra (valor); 4=Margem Valor Agregado (%); 5=Pauta (valor); 6=Valor da Operação |

Inclusão de grupo opcional após o campo cBenef contendo campos para as informações do crédito presumido:

## 6.3 Grupo I. Produtos e Serviços da NF-e

|      # | ID   | Campo          | Descrição                                                              | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Observação                                                                                                                                                                              |
|--------|------|----------------|------------------------------------------------------------------------|-------|-------|--------|---------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 104.07 | I05g | gCred          | Grupo de informações sobre o Crédito Presumido                         | G     | I01   |        | 0-4     |        | Grupo opcional para informações do Crédito Presumido. Obs .: A exigência do preenchimento das informações do crédito presumido fica a critério de cada UF. (Incluído na NT 2019.001)    |
| 104.08 | I05h | cCredPresumido | Código de Benefício Fiscal de Crédito Presumido na UF aplicado ao item | E     | I05g  | C      | 1-1     | 8,10   | Código de Benefício Fiscal de Crédito Presumido utilizado pela UF, aplicado ao item. Obs .: Deve ser utilizado o mesmo código adotado na EFD e outras declarações, nas UF que o exigem. |
| 104.09 | I05i | pCredPresumido | Percentual do Crédito Presumido                                        | E     | I05g  | N      | 1-1     | 3v2-4  | Informar o percentual do crédito presumido relativo ao código do crédito presumido informado.                                                                                           |
| 104.10 | I05j | vCredPresumido | Valor do Crédito Presumido                                             | E     | I05g  | N      | 1-1     | 13v2   | Informar o valor do crédito presumido relativo ao código do crédito presumido informado.                                                                                                |

Inclusão do campo cBenefRBC após o campo pRedBC para informar código de benefício fiscal de redução de base de cálculo dentro do CST51 quando acumular com o diferimento:

## 6.4 Grupo N07. Grupo Tributação do ICMS= 51

|      # | ID   | Campo     | Descrição                                                            | Ele   | Pai Tipo   | Ocor.   | Tam.   | Observação                                                                                                                                                                                                     |
|--------|------|-----------|----------------------------------------------------------------------|-------|------------|---------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 209.01 | N14a | cBenefRBC | Código de Benefício Fiscal na UF aplicado ao item quando houver RBC. | E N07 | C          | 0-1     | 8,10   | Código de Benefício Fiscal utilizado pela UF, aplicado ao item quando houver RBC. Obs .: Deve ser utilizado o mesmo código adotado na EFD e outras declarações, nas UF que o exigem. (Incluído na NT 2019.001) |

![Image](assets/image_000027_1857d0fdbddd456703a491b1e68deb7977929d61dae22cc62682c66e16668aba.png)
## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt2019-001-v1-70-regras-de-valida-o/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt2019-001-v1-70-regras-de-valida-o/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt2019-001-v1-70-regras-de-valida-o.md)
- [Proveniência resumida](../../../../sources/provenance/nt2019-001-v1-70-regras-de-valida-o.json)


## Documentos relacionados

- [[anexo-i-leiaute-e-regra-de-valida-o-nf-e-e-nfc-e]]
- [[moc-nfag-anexo-i-leiaute-e-regras-de-valida-o-v1-00k]]
- [[moc-nfgas-anexo-i-leiaute-e-regras-de-valida-o-v1-00f]]
- [[nt2020-005-v1-21-regras-de-valida-o]]
- [[nt2022-004-v1-10-regras-de-valida-o-issqn]]
