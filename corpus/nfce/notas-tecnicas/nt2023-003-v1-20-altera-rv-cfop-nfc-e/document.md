---
title: "Projeto Nota Fiscal Eletrônica"
slug: "nt2023-003-v1-20-altera-rv-cfop-nfc-e"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "cba9a2750a6df08c4d2b54d28c1838e172e2a434b677fb52e909f7071579ba3b"
converted_at_utc: "2026-06-25T16:09:17.946136+00:00"
status: "published"
type: "nota_tecnica"
---
![Image](assets/image_000000_6c545e385dc554d4f2538dc5f2f8e123229188ad3a37c64853552479f699396f.png)

![Image](assets/image_000001_5dd5d5e16748c7abcded3a0035d3a12ebd8073cdc66cfc62ca495386dd8ab477.png)

## Projeto Nota Fiscal Eletrônica

Nota Técnica 2023.003

Alteração em Regras de Validação CFOP para NFC-e

Versão 1.20 -setembro 2024

![Image](assets/image_000002_91189f7fc509f0ccd75af5037d915e019a009c231f3e7cc19b7730f03913ea6f.png)

## Sumário

| Controle de Versões ............................................................................................................................3      | Controle de Versões ............................................................................................................................3      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Histórico de Alterações / Cronograma..................................................................................................3                | Histórico de Alterações / Cronograma..................................................................................................3                |
| 1. Resumo ...........................................................................................................................................4 | 1. Resumo ...........................................................................................................................................4 |
| 2. Visão Geral......................................................................................................................................5  | 2. Visão Geral......................................................................................................................................5  |
| 2.1.1. Alteração das Regras de Validação N12-40 e N12a-40 ...................................................................                          | 5                                                                                                                                                      |
| 2.1.2. . Alteração da Regra de Validação I08-150 ......................................................................................                | 5                                                                                                                                                      |
| 2.1.3. Alteração das Regras de Validação N12-70 .....................................................................................                  | 5                                                                                                                                                      |
| 3. Regras de Validação........................................................................................................................6        | 3. Regras de Validação........................................................................................................................6        |
| 3.1. Produtos e Serviços ..................................................................................................................6           | 3.1. Produtos e Serviços ..................................................................................................................6           |
| 3.2. N. Item / Tributo: ICMS..............................................................................................................7            | 3.2. N. Item / Tributo: ICMS..............................................................................................................7            |

![Image](assets/image_000003_02fca134f695c2e32ef51f532b5e0eea994c0b11545d0be7d9613bdfc06c0e6e.png)

## Controle de Versões

|   Versão | Publicação    | Descrição                 |
|----------|---------------|---------------------------|
|     1.00 | Junho 2023    | Publicação da NT.         |
|     1.10 | Agosto 2023   | Publicação da Versão 1.10 |
|     1.20 | Setembro 2024 | Publicação da Versão 1.20 |

## Histórico de Alterações / Cronograma

|   Versão | Histórico de atualizações        | Implantação Teste   | Implantação Produção   |
|----------|----------------------------------|---------------------|------------------------|
|     1.00 | Alteração em regras de validação | 05/06/2023          | 03/07/2023             |
|     1.10 | Alteração em regras de validação | 21/08/2023          | Até 04/09/2023         |
|     1.20 | Alteração em regras de validação | 14/10/2024          | 21/10/2024             |

## 1. Resumo

Essa Nota Técnica divulga alteração de Regras de Validação da NF-e versão 4.0.

O prazo previsto para a implementação das mudanças é:

- o Ambiente de Homologação (ambiente de teste das empresas): 05/06/2023
- o Ambiente de Produção : 03/07/2023

A versão 1.10 dessa Nota Técnica divulga alteração de Regra de Validação da NF-e versão 4.0.

O prazo previsto para a implementação das mudanças é:

- o Ambiente de Homologação (ambiente de teste das empresas): 21/08/2023
- o Ambiente de Produção : 04/09/2023

A versão 1.20 dessa Nota Técnica divulga alterações de Regras de Validação da NFC-e versão 4.0 exclusivas para a UF de SP. Também descreve a motivação das outras exceções criadas nas versões anteriores.

## O prazo previsto para a implementação das mudanças é:

- o Ambiente de Homologação (ambiente de teste das empresas): 30/09/2024
- o Ambiente de Produção : 07/10/2024

## 2. Visão Geral

Essa Nota Técnica tem o objetivo de permitir a emissão de NFC-e utilizando o CFOP para 5.949 para casos específicos, a critério da UF.

## 2.1.1. Alteração das Regras de Validação N12-40 e N12a-40

Para permitir a emissão NFC-e utilizando o CFOP 5.403, 5.405 ou 5.949 com o CST 90 ou com o CSOSN 900  para  atender  Recurso  Extraordinário  574.706/PR  -  STF  na  UF  do  CE  e  atender  a obrigatoriedade de integração de meios de pagamentos eletrônicos na UF do RS.

Para permitir a emissão de NFC-e, em SP, utilizando o CFOP 5.949 com o CST 40 ou com o CSOSN 900, para registro de gorjeta na UF de SP.

## 2.1.2. . Alteração da Regra de Validação I08-150

Para permitir a emissão NFC-e utilizando o CFOP 5.949 com o CST 90 ou com o CSOSN 900 para atender a obrigatoriedade de integração de meios de pagamentos eletrônicos na UF do RS.

Para permitir a emissão de NFC-e utilizando o CFOP 5.949 com CSOSN=900 ou CST=40, para registro de gorjeta na UF de SP.

## 2.1.3. Alteração das Regras de Validação N12-70

Para permitir a emissão NF-e utilizando o CFOP 5.403 ou 5.405 com o CST 90 ou com o CSOSN 900 para atender Recurso Extraordinário 574.706/PR - STF na UF do CE.

## 3. Regras de Validação

## 3.1. Produtos e Serviços

| I08-150   |   Modelo | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Aplic.   |   Msg | Efeito   | Descrição Erro                               |
|-----------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|----------------------------------------------|
| I08-150   |       65 | NFC-e (mod=65) com CFOP inválido. Aceitar unicamente os CFOP: - 5.101: Venda de produção do estabelecimento; - 5.102: Venda de mercadoria de terceiros; - 5.103: Venda de produção do estabelecimento efetuada fora do estabelecimento; - 5.104: Venda de mercadoria adquirida ou recebida de terceiros, efetuada fora do estabelecimento; - 5.115: Venda de mercadoria de terceiros, recebida anteriormente em consignação mercantil; - 5.405: Venda de mercadoria de terceiros, sujeita a ST, como contribuinte substituído; - 5.656: Venda de combustível ou lubrificante de terceiros, destinados a consumidor final; - 5.667: Venda de combustível ou lubrificante a consumidor ou usuário final estabelecido em outra Unidade da Federação; - 5.933: Prestação de serviço tributado pelo ISSQN (Nota Fiscal conjugada); (NT 2013/005 v 1.20) (NT 2015.002) Observação: Para a UF do RS, poderá ser permitido o uso do CFOP 5.949 com CSOSN=900 ou CST=90. Observação: Para a UF de SP, poderá ser permitido o uso do CFOP 5.949 com CSOSN=900 ou CST=40. | Obrig.   |   725 | Rej.     | Rejeição: NFC-e com CFOP inválido[nItem:nnn] |

![Image](assets/image_000004_172046c910dde3cdfc8b722d58b7adea447d6b78b9c6295481f1c2b9b3e8da81.png)

## 3.2. N. Item / Tributo: ICMS

| Campo-Seq   |   Modelo | Regra de Validação                                                                                       | Aplic.   |   Msg | Efeito   | Descrição Erro                                                |
|-------------|----------|----------------------------------------------------------------------------------------------------------|----------|-------|----------|---------------------------------------------------------------|
| N12-40      |       65 | NFC-e com CST=00, 20, 40, 41 ou 90 e - CFOP diferente de 5.101, 5.102, 5.103, 5.104, 5.115 (NT 2015.002) | Obrig.   |   382 | Rej.     | Rejeição: CFOP não permitido para o CST informado [nItem:nnn] |

| Campo-Seq   |   Modelo | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                         | Aplic.   |   Msg | Efeito   | Descrição Erro                                                   |
|-------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|------------------------------------------------------------------|
| N12a-40     |       65 | NFC-e com CSOSN=102, 103, 300, 400 ou 900 CFOP diferente de 5.101, 5.102, 5.103, 5.104, 5.115 (NT 2015.002) Observação 1: Para a UF do RS, poderá ser permitido o uso do CSOSN 900 com o CFOP 5.949. Observação 2: Para a UF do CE, poderá ser permitido o uso do CST 90 com o CFOP 5.403 ou 5.405. Observação 3: Para a UF de SP, poderá ser permitido o uso do CSOSN 900 com CFOP 5.949. | Obrig.   |   386 | Rej.     | Rejeição: CFOP não permitido para o CSOSN informado [nItem: nnn] |

![Image](assets/image_000005_4002d5dc7c889656f696f7f493496102872299836782a75ffefeae0c859982cc.png)

![Image](assets/image_000006_0d50c3a80af8835e752218ac7c463c2c8ec35562e23ef298d8bd605bc748deca.png)

| Campo-Seq   |   Modelo | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Aplic.   |   Msg | Efeito   | Descrição Erro                                                           |
|-------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|--------------------------------------------------------------------------|
| N12-70      |       55 | Operação com Não Contribuinte (indIEDest=9) e CST difere da relação abaixo: - 00-Tributada integralmente; - 20-Com redução da Base de Cálculo; - 40-Isenta; - 41-Não tributada; - 60-ICMS cobrado anteriormente por substituição tributária; - 61- Tributação monofásica sobre combustíveis cobrada anteriormente; Exceção 1: A regra de validação acima não se aplica para NF-e de entrada (tpNF=0-Entrada). Exceção 2: A regra de validação acima não se aplica, para o CST=50 (Suspensão), nas operações com CFOP de Retorno de Mercadorias (Tabela CFOP, indRetor=1), nem nas operações com CFOP de Remessa de Mercadorias (Tabela CFOP, indRemes=1), e nem nas operações com CFOP 5.949 ou 6.949. Exceção 3: A regra de validação acima não se aplica quando houver ao menos um item de venda de veículos novos (grupo 'veicProd'). Exceção 4: A regra de validação não se aplica, em produção, para Nota Fiscal com data de emissão anterior a 01/07/2016. Exceção 5: A regra de validação não se aplica para o CST=30 (Isenta ou não tributada e com cobrança do ICMS por substituição tributária), em operação interestadual (idDest=2) comcombustíveis (tag: comb) derivados de petróleo (código ANP diferente de: 820101001, 820101010, 810102001, 810102004, 810102002, 810102003, 810101002, 810101001, 810101003, 220101003, 220101004, 220101002, 220101001, 220101005, 220101006, 560101001). Exceção 6: A regra de validação acima não se aplica, para os CST=50 (Suspensão) e 51 (Diferimento), nas operações de devolução (finNFe=4). Exceção 7: A regra de validação acima não se aplica, para o CST=51 (Diferimento), nas operações com CFOP 5.123, 5.922, 6.123 e 6.922, nem nas operações internas (idDest=1).de retorno de Mercadoria depositada em depósito fechado ou armazém geral (CFOP 5.906 ou 5.907). Exceção 8: A critério da UF a regra de validação não se aplica para o CST=10 (Tributada e com cobrança do ICMS por substituição tributária) em operação interna (idDest=1). (NT 2017.002 / NT 2015.003). | Obrig.   |   508 | Rej.     | Rejeição: CST incompatível na operação com Não Contribuinte [nItem: 999] |

![Image](assets/image_000007_b7defce071bf54435f6bb6f093b24843baa8f259360c757fc19cc7d9eddb7be2.png)

| Exceção 9: A regra de validação não se aplica para o CST=30 (Isenta ou não tributada e com cobrança do ICMS por substituição tributária), em operação interestadual (idDest=2) na aquisição de energia elétrica em Ambiente de Contratação Livre (ACL) com NCM: 27160000 (NT 2020.005). Observação: Para a UF do CE, poderá ser permitido o uso do CST 90 com o CFOP 5.403 ou 5.405.   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|