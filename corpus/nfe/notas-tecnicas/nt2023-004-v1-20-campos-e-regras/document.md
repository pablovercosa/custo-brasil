---
title: "Sistema Nota Fiscal Eletrônica"
slug: "nt2023-004-v1-20-campos-e-regras"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "1c6db64a5c32b176f8e60baf2ebbfed24632169ddfcd80632c1b5cc65b9ac71d"
converted_at_utc: "2026-06-25T16:33:13.364631+00:00"
status: "published"
type: "nota_tecnica"
---
![Image](assets/image_000000_12abad640688560b87aa138dc2b5c3723be4e6072054c37416ad32f18d363724.png)

![Image](assets/image_000001_1a476f9ce664e712b3ca549b66575e1f9362576b665691bd79632997d97b6db2.png)

## Sistema Nota Fiscal Eletrônica

Nota Técnica 2023.004

Informações de Pagamentos e Outros

![Image](assets/image_000002_b1d57f527174d840bdfda0649573fb644d47282768140b37ffc42592134299b5.png)

![Image](assets/image_000003_75bd47ee99d5ee93bcf24d2ff2b62ec2238f4d53a4f6138f08a9669114cc8cf8.png)

![Image](assets/image_000004_6bdea32d03f8756197bb1b4d5190f0c4df6116e667ce104474446fd74ae8d5ba.png)

## Sumário

| Controle de Versões..............................................................................................................................    | Controle de Versões..............................................................................................................................    |   3 |
|------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| Histórico de Alterações / Cronograma ...................................................................................................             | Histórico de Alterações / Cronograma ...................................................................................................             |   3 |
| 1. Resumo........................................................................................................................................... | 1. Resumo........................................................................................................................................... |   4 |
| 2. Visão Geral...................................................................................................................................... | 2. Visão Geral...................................................................................................................................... |   4 |
| 2.1.                                                                                                                                                 | Webservice de Evento...............................................................................................................                  |   4 |
| 2.2.                                                                                                                                                 | Alteração de Campos................................................................................................................                  |   4 |
| 2.3.                                                                                                                                                 | Alterações de Regras de Validação...........................................................................................                         |   5 |
| 2.4.                                                                                                                                                 | Alterações introduzidas na versão 1.10.....................................................................................                          |   5 |
| 2.5.                                                                                                                                                 | Alteração introduzida na versão 1.11.........................................................................................                        |   6 |
| 2.6.                                                                                                                                                 | Alteração introduzida na versão 1.20.........................................................................................                        |   6 |
| 3. Leiaute da Nota Fiscal Eletrônica....................................................................................................             | 3. Leiaute da Nota Fiscal Eletrônica....................................................................................................             |   7 |
| 3.1. Grupo I01. Produtos e Serviços / Declaração de Importação ....................................................                                  | 3.1. Grupo I01. Produtos e Serviços / Declaração de Importação ....................................................                                  |   7 |
| 3.2.                                                                                                                                                 | Grupo N04. Grupo Tributação do ICMS= 20..............................................................................                                |   8 |
| 3.3.                                                                                                                                                 | Grupo N05. Grupo Tributação do ICMS= 30..............................................................................                                |   9 |
| 3.4.                                                                                                                                                 | Grupo N06. Grupo Tributação do ICMS= 40, 41, 50..................................................................                                    |   9 |
| 3.5.                                                                                                                                                 | Grupo N09. Grupo Tributação do ICMS= 70............................................................................                                  |  10 |
| 3.6.                                                                                                                                                 | Grupo N10. Grupo Tributação do ICMS= 90............................................................................                                  |  11 |
| 3.7.                                                                                                                                                 | Grupo YA. Informações de Pagamento ...................................................................................                               |  11 |
| 3.8.                                                                                                                                                 | Grupo Z. Informações Adicionais da NF-e...............................................................................                               |  12 |
| 4. Regras de Validação.....................................................................................................................          | 4. Regras de Validação.....................................................................................................................          |  13 |
| 4.1. I01. Produtos e Serviços / Declaração de Importação .............................................................                               | 4.1. I01. Produtos e Serviços / Declaração de Importação .............................................................                               |  13 |
| 4.2.                                                                                                                                                 | N. Item / Tributo: ICMS............................................................................................................                  |  14 |
| 4.3.                                                                                                                                                 | X. Transporte da NF-e.............................................................................................................                   |  14 |
| 4.4.                                                                                                                                                 | YA. Formas de Pagamento .....................................................................................................                        |  14 |
| 4.5.                                                                                                                                                 | W. Total da NF-e.....................................................................................................................                |  15 |
| 4.6.                                                                                                                                                 | Banco de Dados: Emitente......................................................................................................                       |  16 |
| 5.                                                                                                                                                   | Novos códigos de rejeição ............................................................................................................               |  16 |

![Image](assets/image_000005_b9049b6f2362d647d339213a371ff1fe2d45a66f7262e29d1b3c0deb9acc773f.png)

## Controle de Versões

|   Versão | Publicação    | Descrição                 |
|----------|---------------|---------------------------|
|     1.00 | Dezembro/2023 | Publicação da NT          |
|     1.10 | Janeiro/2024  | Publicação da Versão 1.10 |
|     1.11 | Março/2024    | Publicação da Versão 1.11 |
|     1.20 | Outubro/2024  | Publicação da Versão 1.20 |

## Histórico de Alterações / Cronograma

|   Versão | Histórico de atualizações   | Implantação Teste   | Implantação Produção   |
|----------|-----------------------------|---------------------|------------------------|
|     1.00 | Publicação da NT            | 05/02/2024          | 01/04/2024             |
|     1.10 | Versão 1.10                 | 11/03/2024          | 01/04/2024             |
|     1.11 | Atualização do Schema       | Até 25/03/2024      | 06/05/2024             |
|     1.11 | Versão 1.11                 | Até 25/03/2024      | 01/07/2024             |
|     1.20 | Versão 1.20                 | Imediata            | Imediata               |

![Image](assets/image_000006_97f5ff7ff3b3737ac4ac9cff202ce68759448782444a79ac76ed0ddd6675892f.png)

## 1. Resumo

Esta nota técnica tem o objetivo de prover aos atores envolvidos nos processos da NF-e/NFC-e a possibilidade  de  anotar  no  documento  fiscal  eletrônico  as  transações  financeiras  relacionadas, facilitando a vinculação entre documentos fiscais e recursos financeiros recebidos.

Busca-se encontrar uma solução para pagamentos que ocorrem distantes da data do fato gerador e da emissão do documento fiscal. Portanto, para que seja possível às empresas informarem que o recebimento de  recurso  está  relacionado  a  determinado  documento  fiscal,  está  sendo  criado  o Evento de Conciliação Financeira - ECONF. Os Ajustes SINIEF nº 3/2023 e 10/2023 prevêem este evento.

A utilização do Evento de Conciliação Financeira - ECONF é facultativa e tem o objetivo de auxiliar as empresas que buscam demonstrar a existência de conformidade fiscal entre as informações financeiras e de meios de pagamentos e os documentos fiscais emitidos.

Nessa NT, foram criados novos campos no grupo YA. Informações de Pagamento e nos Grupos Tributação do ICMS que possuem ICMS desonerado.

Também foram alterados campos dos grupos I01. Produtos e Serviços / Declaração de Importação e Z. Informações Adicionais da NF-e.

A versão 1.10 dessa Nota Técnica transfere o ECONF para outra Nota Técnica que tratará apenas do referido evento. Também divulga alteração de campos e regras de validação da NF-e versão 4.0.

Esta versão 1.11 prorroga a data de implantação de produção para 01/07/2024. Faz correções em regras de validação. Observação: o schema entrará em produção no dia 06/05/2024.

A versão 1.20 apenas aumenta o valor máximo do troco previsto na Regra de Validação YA09-20, com entrada imediata em homologação e produção.

## 2. Visão Geral

## 2.1.  Webservice de Evento

A Sefaz autorizadora disponibilizará um WebService de eventos que será utilizado para autorização do ECONF. Os eventos especificados nesta NT estarão disponíveis para os modelos 55 e 65.

## 2.2.  Alteração de Campos

## 2.2.1.  Inclusão dos campos

Novos campos foram adicionados ao "Grupo YA. Informações de Pagamento':

- Os  campos  CNPJPag e  UFPag  são de  preenchimento  facultativo  pelo    emitente  que deseja informar o CNPJ e UF do estabelecimento onde o pagamento foi processado/transacionado/recebido  nos  casos em que  a  emissão  do documento fiscal ocorrer em estabelecimento distinto.
- Os campos CNPJReceb e idTermPag são destinados a informar o CNPJ do beneficiário do pagamento e o Identificador  do  terminal de pagamento  para fins de  integração do pagamento com a emissão do documento fiscal eletrônico.

Nos 'Grupos Tributação do ICMS' que possuem ICMS Desonerado, foi criado o campo 'indDeduzDeson' para indicar se o valor do ICMS desonerado (vICMSDeson) deduz do valor do item (vProd).

![Image](assets/image_000007_314f14d24076d01498016260c59a4929453bc6892bf12c485d14981035254b69.png)

## 2.2.2.  Alteração dos Campos

No 'Grupo I01. Produtos e Serviços / Declaração de Importação', o campo atual 'CNPJ' passa a ser 'CNPJ/CPF' foi criado o campo CPF, permitindo também que pessoa física seja adquirente ou encomendante.

No 'Grupo Z. Informações Adicionais da NF-e', foram adicionadas novas opções para identificar procedimentos, benefícios e regimes concedidos no âmbito do CONFAZ.

## 2.3.  Alterações de Regras de Validação

## 2.3.1.  Inclusão das regras YA04-20, YA09-20 e YA10-10

Inclusão da regra de validação YA04-20 para somente permitir o grupo de cartões ou boletos para os meios de pagamento corretos.

Inclusão da regra de validação YA09-20, que limita o valor do troco.

Inclusão da regra de validação YA10-10 para verificar o correto preenchimento do CNPJ beneficiário do pagamento.

## 2.3.2.  Desabilitação das regras X03-10 e X03-20

Desabilita as regras X03-10 e X03-20.

## 2.3.3.  Alteração da regra de validação

A regra da W16-10 é alterada para substituir a Exceção 3 pela Exceção 4, em que não há rejeição quado o campo 'indDeduzDeson' não for preenchido ou preenchido com a indicação de 'Valor do ICMS desonerado (vICMSDeson) não deduz do valor do item (vProd) / total da NF-e'. Cria Exceção para não aplicar a regra 1C17-34 quando emissão de NFA-e.

Cria Exceção para não aplicar a regra 1C17-34 quando emissão de NFA-e.

## 2.4.  Alterações introduzidas na versão 1.10

- Retirado o evento ECONF desta Nota Técnica e transferido para outra Nota Técnica que conterá apenas o referido evento.
- Inclusão do campo CPF (I23d1).
- No grupo YA. Informações de Pagamento, houve: inclusão do campo dPag (YA03a) e ajustes na descrição dos ID dos campos YA03a, YA03b, YA03c, YA03d, YA07a, YA07b. Foi alterada a descrição do campo cAut para deixar claro que o preenchimento é também para PIX, boletos e outros pagamentos eletrônicos.
- A regra de validação I23d-10 teve pequeno ajuste na descrição.
- A regra de validação I23d-20 volta a ter apenas o CNPJ, sendo criada a I23d1-10 para validar o CPF.
- As regras de validação YA03b-10, YA04-20 e YA09-20 tiveram os números das mensagens de rejeição corrigidos.
- A regra de validação YA04-10 prevê que, no pagamento por PIX, deve-se informar o grupo de cartões.
- A regra de validação W16-10 foi corrigida para considerar na regra o valor do ICMS Monofásico sujeito a retenção no faturamento direto de veículos novos (Exceção 1).
- Incluída regra de validação N28-12 específica para desoneração para o motivo de desoneração 7 - SUFRAMA

![Image](assets/image_000008_b9049b6f2362d647d339213a371ff1fe2d45a66f7262e29d1b3c0deb9acc773f.png)

## 2.5.  Alteração introduzida na versão 1.11

- Prorrogação da data de ativação em produção para 01/07/2024.
- O schema entra em produção em 06/05/2024.
- A regra de validação YA09-20 será ativada em 01/10/2024.
- Correção das exceções 1 e 4 da regra de validação W16-10.

## 2.6.  Alteração introduzida na versão 1.20

- Aumenta o limite do valor do troco (id:YA09, tag:vTroco) de R$ 1.000,00 para R$ 300.000,00, constante na Regra de Validação YA09-20.

![Image](assets/image_000009_314f14d24076d01498016260c59a4929453bc6892bf12c485d14981035254b69.png)

## 3.  Leiaute da Nota Fiscal Eletrônica

## 3.1.   Grupo I01. Produtos e Serviços / Declaração de Importação

|      # | ID    | Campo        | Descrição                                                                                                               | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Observação                                                                                                                                                                           |
|--------|-------|--------------|-------------------------------------------------------------------------------------------------------------------------|-------|-------|--------|---------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    117 | I18   | DI           | Declaração de Importação                                                                                                | G     | I01   |        | 0-100   |        | Informar dados da importação                                                                                                                                                         |
|    118 | I19   | nDI          | Número do Documento de Importação (DI, DSI, DIRE, DUImp)                                                                | E     | I18   | C      | 1-1     | 1 - 15 | (NT 2011/004)                                                                                                                                                                        |
|    119 | I20   | dDI          | Data de Registro do documento                                                                                           | E     | I18   | D      | 1-1     |        | Formato: 'AAAA -MM- DD'                                                                                                                                                              |
|    120 | I21   | xLocDesemb   | Local de desembaraço                                                                                                    | E     | I18   | C      | 1-1     | 1 - 60 |                                                                                                                                                                                      |
|    121 | I22   | UFDesemb     | Sigla da UF onde ocorreu o Desembaraço Aduaneiro                                                                        | E     | I18   | C      | 1-1     | 2      |                                                                                                                                                                                      |
|    122 | I23   | dDesemb      | Data do Desembaraço Aduaneiro                                                                                           | E     | I18   | D      | 1-1     |        | Formato: 'AAAA -MM- DD'                                                                                                                                                              |
| 122.01 | I23a  | tpViaTransp  | Via de transporte internacional informada na Declaração de Importação (DI) ou na Declaração Única de Importação (DUImp) | E     | I18   | N      | 1-1     | 2      | 1=Marítima 2=Fluvial 3=Lacustre 4=Aérea 5=Postal 6=Ferroviária; 7=Rodoviária 8=Conduto/Rede Transmissão 9=Meios Próprios 10=Entrada/Saída Ficta 11=Courier 12=Em mãos 13=Por reboque |
| 122.02 | I23b  | vAFRMM       | ValordaAFRMM - Adicional ao Frete para Renovação da Marinha Mercante                                                    | E     | I18   | N      | 0-1     | 13v2   | A tag deve ser informada no caso da via de transporte marítima.                                                                                                                      |
| 122.03 | I23c  | tpIntermedio | Forma de importação quanto a intermediação                                                                              | E     | I18   | N      | 1-1     | 1      | 1=Importação por conta própria; 2=Importação por conta e ordem; 3=Importação por encomenda                                                                                           |
| 122.04 | I23d  | CNPJ         | CNPJ do adquirente ou do encomendante                                                                                   | CE    | I18   | N      | 0-1     | 14     | Obrigatória a informação no caso de importação por conta e ordem ou por encomenda. Informar os zeros não significativos                                                              |
| 122.05 | I23d1 | CPF          | CPF do adquirente ou do encomendante                                                                                    | CE    | I18   | N      | 0-1     | 11     | Obrigatória a informação no caso de importação por conta e ordem ou por encomenda. Informar os zeros não significativos                                                              |
| 122.06 | I23e  | UFTerceiro   | Sigla da UF do adquirente ou do encomendante                                                                            | E     | I18   | C      | 0-1     | 2      | Obrigatória a informação no caso de importação por conta e ordem ou por encomenda. Não aceita o valor "EX".                                                                          |
|    123 | I24   | cExportador  | Código do Exportador                                                                                                    | E     | I18   | C      | 1-1     | 1 - 60 | Código do Exportador, usado nos sistemas internos de informação do emitente da NF-e                                                                                                  |
|    124 | I25   | adi          | Adições e/ou itens                                                                                                      | G     | I18   |        | 1-999   |        | (NT 2011/004)                                                                                                                                                                        |
|    125 | I26   | nAdicao      | Número da Adição                                                                                                        | E     | I25   | N      | 0-1     | 1 - 3  | No caso de DUImp esse campo não deverá ser preenchido                                                                                                                                |

![Image](assets/image_000010_4c36d268e647941e06d8fc2bd50db6ef04b9e7d267bda1aeb9ea6c3e0f42a40a.png)

![Image](assets/image_000011_3ef87c6efc422eec0ff1573a9d8c9fbfe90897a4871f7a44e8bba9493eccf2b8.png)

| #      | ID   | Campo       | Descrição                                      | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Observação                                                                                                                                                                                                                              |
|--------|------|-------------|------------------------------------------------|-------|-------|--------|---------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 126    | I27  | nSeqAdic    | Número sequencial do item                      | E     | I25   | N      | 1-1     | 1 - 5  |                                                                                                                                                                                                                                         |
| 127    | I28  | cFabricante | Código do fabricante estrangeiro               | E     | I25   | C      | 1-1     | 1 - 60 | Código do fabricante estrangeiro, usado nos sistemas internos de informação do emitente da NF-e                                                                                                                                         |
| 128    | I29  | vDescDI     | Valor do desconto do item                      | E     | I25   | N      | 0-1     | 13v2   |                                                                                                                                                                                                                                         |
| 128.01 | I29a | nDraw       | Número do ato concessório de Drawback          | E     | I25   | C      | 0-1     | 1-20   | O número do Ato Concessório de Suspensão deve ser preenchido com 11 dígitos (AAAANNNNNND) e o número do Ato Concessório de Drawback Isenção deve ser preenchido com 9 dígitos (AANNNNNND). (Observação incluída na NT 2013/005 v. 1.10) |
| 128.20 | I50  | detExport   | Grupo de informações de exportação para o item | G     | I01   |        | 0-500   |        | Informar apenas no Drawback e nas exportações                                                                                                                                                                                           |
| 128g   | I51  | nDraw       | Número do ato concessório de Drawback          | E     | I50   | C      | 0-1     | 1-20   | O número do Ato Concessório de Suspensão deve ser preenchido com 11 dígitos (AAAANNNNNND) e o número do Ato Concessório de Drawback Isenção deve ser preenchido com 9 dígitos (AANNNNNND). (Observação incluída na NT 2013/005 v. 1.10) |

## 3.2.  Grupo N04. Grupo Tributação do ICMS= 20

| #     | ID    | Campo         | Descrição                                                                         | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Observação                                                                                                                                                                                                              |
|-------|-------|---------------|-----------------------------------------------------------------------------------|-------|-------|--------|---------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 185   | N04   | ICMS20        | Grupo Tributação do ICMS = 20                                                     | CG    | N01   |        | 1-1     |        | Tributação com redução de base de cálculo                                                                                                                                                                               |
| ...   | ...   | ...           | ...                                                                               | ...   | ...   | ...    | ...     | ...    | ...                                                                                                                                                                                                                     |
| 192.1 | N27.1 | -x-           | Sequência XML                                                                     | G     | N04   |        | 0-1     |        | Grupo opcional.                                                                                                                                                                                                         |
| 192.2 | N28a  | vICMSDeson    | Valor do ICMS desonerado                                                          | E     | N27.1 | N      | 1-1     | 13v2   | Informar apenas nos motivos de desoneração documentados abaixo.                                                                                                                                                         |
| 192.3 | N28   | motDesICMS    | Motivo da desoneração do ICMS                                                     | E     | N27.1 | N      | 1-1     | 2      | Campo será preenchido quando o campo anterior estiver preenchido. Informar o motivo da desoneração: 3=Uso na agropecuária; 9=Outros; 12=Órgão de fomento e desenvolvimento agropecuário.                                |
| 192.4 | N28b  | indDeduzDeson | Indica se o valor do ICMS desonerado (vICMSDeson) deduz do valor do item (vProd). | E     | N27.1 | N      | 0-1     | 1      | O campo só pode ser preenchido com: 0=Valor do ICMS desonerado (vICMSDeson) não deduz do valor do item (vProd) / total da NF-e. 1=Valor do ICMS desonerado (vICMSDeson) deduz do valor do item (vProd) / total da NF-e. |

## 3.3.  Grupo N05. Grupo Tributação do ICMS= 30

| #     | ID    | Campo         | Descrição                                                                         | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Observação                                                                                                                                                                                                                                                     |
|-------|-------|---------------|-----------------------------------------------------------------------------------|-------|-------|--------|---------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 193   | N05   | ICMS30        | Grupo Tributação do ICMS = 30                                                     | CG    | N01   |        | 1-1     |        | Tributação Isenta ou não tributada e com cobrança do ICMS por substituição tributária                                                                                                                                                                          |
| ...   | ...   | ...           | ...                                                                               | ...   | ...   | ...    | ...     | ...    | ...                                                                                                                                                                                                                                                            |
| 201.1 | N27.1 | -x-           | Sequência XML                                                                     | G     | N05   |        | 0-1     |        | Grupo opcional.                                                                                                                                                                                                                                                |
| 201.2 | N28a  | vICMSDeson    | Valor do ICMS desonerado                                                          | E     | N27.1 | N      | 1-1     | 13v2   | Informar apenas nos motivos de desoneração documentados abaixo.                                                                                                                                                                                                |
| 201.3 | N28   | motDesICMS    | Motivo da desoneração do ICMS                                                     | E     | N27.1 | N      | 1-1     | 2      | Campo será preenchido quando o campo anterior estiver preenchido. Informar o motivo da desoneração: 6=Utilitários e Motocicletas da Amazônia Ocidental e Áreas de Livre Comércio (Resolução 714/88 e 790/94 - CONTRAN e suas alterações); 7=SUFRAMA; 9=Outros; |
| 201.4 | N28b  | indDeduzDeson | Indica se o valor do ICMS desonerado (vICMSDeson) deduz do valor do item (vProd). | E     | N27.1 | N      | 0-1     | 1      | O campo só pode ser preenchido com: 0=Valor do ICMS desonerado (vICMSDeson) não deduz do valor do item (vProd) / total da NF-e. 1=Valor do ICMS desonerado (vICMSDeson) deduz do valor do item (vProd) / total da NF-e.                                        |

## 3.4.  Grupo N06. Grupo Tributação do ICMS= 40, 41, 50

| #      | ID    | Campo      | Descrição                          | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Observação                                                                                                                                                                                                                                                                                                                                                   |
|--------|-------|------------|------------------------------------|-------|-------|--------|---------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 202    | N06   | ICMS40     | Grupo Tributação ICMS = 40, 41, 50 | CG    | N01   |        | 1-1     |        | Tributação Isenta, Não tributada ou Suspensão.                                                                                                                                                                                                                                                                                                               |
| ...    | ...   | ...        | ...                                | ...   | ...   | ...    | ...     | ...    | ...                                                                                                                                                                                                                                                                                                                                                          |
| 204.00 | N27.1 | -x-        | Sequência XML                      | G     | N06   |        | 0-1     |        | Grupo opcional.                                                                                                                                                                                                                                                                                                                                              |
| 204.01 | N28a  | vICMSDeson | Valor do ICMS desonerado           | E     | N27.1 | N      | 1-1     | 13v2   | Informar nas operações: a) com produtos beneficiados com a desoneração condicional do ICMS. b) destinadas à SUFRAMA, informando-se o valor que seria devido se não houvesse isenção. c) de venda a órgão da administração pública direta e suas fundações e autarquias comisenção do ICMS. (NT 2011/004 d) demais casos solicitados pelo Fisco. (NT2016.002) |

![Image](assets/image_000012_4c36d268e647941e06d8fc2bd50db6ef04b9e7d267bda1aeb9ea6c3e0f42a40a.png)

NT 2023.004 - Informações de Pagamentos e Outros

![Image](assets/image_000013_3ef87c6efc422eec0ff1573a9d8c9fbfe90897a4871f7a44e8bba9493eccf2b8.png)

|      # | ID   | Campo         | Descrição                                                                         | Ele   | Pai   | Tipo   | Ocor.   |   Tam. | Observação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------|------|---------------|-----------------------------------------------------------------------------------|-------|-------|--------|---------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 204.02 | N28  | motDesICMS    | Motivo da desoneração do ICMS                                                     | E     | N27.1 | N      | 1-1     |      2 | Campo será preenchido quando o campo anterior estiver preenchido. Informar o motivo da desoneração: 1=Táxi; 3=Produtor Agropecuário; 4=Frotista/Locadora; 5=Diplomático/Consular; 6=Utilitários e Motocicletas da Amazônia Ocidental e Áreas de Livre Comércio (Resolução 714/88 e 790/94 - CONTRAN e suas alterações); 7=SUFRAMA; 8=Venda a Órgão Público; 9=Outros. (NT 2011/004); 10=Deficiente Condutor (Convênio ICMS 38/12); 11=Deficiente Não Condutor (Convênio ICMS 38/12). 16=Olimpíadas Rio 2016 (NT 2015.002); 90=Solicitado pelo Fisco (NT2016.002) Revogada a partir da versão 3.10 a possibilidade de usar o motivo 2=Deficiente Físico |
| 204.03 | N28b | indDeduzDeson | Indica se o valor do ICMS desonerado (vICMSDeson) deduz do valor do item (vProd). | E     | N27.1 | N      | 0-1     |      1 | O campo só pode ser preenchido com: 0=Valor do ICMS desonerado (vICMSDeson) não deduz do valor do item (vProd) / total da NF-e. 1=Valor do ICMS desonerado (vICMSDeson) deduz do valor do item (vProd) / total da NF-e.                                                                                                                                                                                                                                                                                                                                                                                                                                |

## 3.5.  Grupo N09. Grupo Tributação do ICMS= 70

| #     | ID    | Campo      | Descrição                     | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Observação                                                                                                                                                                            |
|-------|-------|------------|-------------------------------|-------|-------|--------|---------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 218   | N09   | ICMS70     | Grupo Tributação do ICMS = 70 | CG    | N01   |        | 1-1     |        | Tributação ICMS com redução de base de cálculo e cobrança do ICMS por substituição tributária                                                                                         |
| ...   | ...   | ...        | ...                           | ...   | ...   | ...    | ...     | ...    | ...                                                                                                                                                                                   |
| 231.1 | N27.1 | -x-        | Sequência XML                 | G     | N09   |        | 0-1     |        | Grupo opcional.                                                                                                                                                                       |
| 231.2 | N28a  | vICMSDeson | Valor do ICMS desonerado      | E     | N27.1 | N      | 1-1     | 13v2   | Informar apenas nos motivos de desoneração documentados abaixo.                                                                                                                       |
| 231.3 | N28   | motDesICMS | Motivo da desoneração do ICMS | E     | N27.1 | N      | 1-1     | 2      | Campo será preenchido quando o campo anterior estiver preenchido. Informar o motivo da desoneração: 3=Uso na agropecuária 9=Outros 12=Órgão de fomento e desenvolvimento agropecuário |

![Image](assets/image_000014_3ef87c6efc422eec0ff1573a9d8c9fbfe90897a4871f7a44e8bba9493eccf2b8.png)

|     # | ID   | Campo         | Descrição                                                                         | Ele   | Pai   | Tipo   | Ocor.   |   Tam. | Observação                                                                                                                                                                                                              |
|-------|------|---------------|-----------------------------------------------------------------------------------|-------|-------|--------|---------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 231.4 | N28b | indDeduzDeson | Indica se o valor do ICMS desonerado (vICMSDeson) deduz do valor do item (vProd). | E     | N27.1 | N      | 0-1     |      1 | O campo só pode ser preenchido com: 0=Valor do ICMS desonerado (vICMSDeson) não deduz do valor do item (vProd) / total da NF-e. 1=Valor do ICMS desonerado (vICMSDeson) deduz do valor do item (vProd) / total da NF-e. |

## 3.6.  Grupo N10. Grupo Tributação do ICMS= 90

| #     | ID    | Campo         | Descrição                                                                         | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Observação                                                                                                                                                                                                              |
|-------|-------|---------------|-----------------------------------------------------------------------------------|-------|-------|--------|---------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 232   | N10   | ICMS90        | Grupo Tributação do ICMS = 90                                                     | CG    | N01   |        | 1-1     |        | Tributação ICMS: Outros                                                                                                                                                                                                 |
| ...   | ...   | ...           | ...                                                                               | ...   | ...   | ...    | ...     | ...    | ...                                                                                                                                                                                                                     |
| 245.1 | N27.1 | -x-           | Sequência XML                                                                     | G     | N10   |        | 0-1     |        | Grupo opcional.                                                                                                                                                                                                         |
| 245.2 | N28a  | vICMSDeson    | Valor do ICMS desonerado                                                          | E     | N27.1 | N      | 1-1     | 13v2   | Informar apenas nos motivos de desoneração documentados abaixo.                                                                                                                                                         |
| 245.3 | N28   | motDesICMS    | Motivo da desoneração do ICMS                                                     | E     | N27.1 | N      | 1-1     | 2      | Campo será preenchido quando o campo anterior estiver preenchido. Informar o motivo da desoneração: 3=Uso na agropecuária; 9=Outros; 12=Órgão de fomento e desenvolvimento agropecuário.                                |
| 245.4 | N28b  | indDeduzDeson | Indica se o valor do ICMS desonerado (vICMSDeson) deduz do valor do item (vProd). | E     | N27.1 | N      | 0-1     | 1      | O campo só pode ser preenchido com: 0=Valor do ICMS desonerado (vICMSDeson) não deduz do valor do item (vProd) / total da NF-e. 1=Valor do ICMS desonerado (vICMSDeson) deduz do valor do item (vProd) / total da NF-e. |

## 3.7.  Grupo YA. Informações de Pagamento

|      # | ID    | Campo   | Descrição                         | Ele   | Pai   | Tipo   | Ocor.   |   Tam. | Observação                                                                                                                                                                                               |
|--------|-------|---------|-----------------------------------|-------|-------|--------|---------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 398.01 | YA01  | pag     | Grupo de Informações de Pagamento | G     | A01   |        | 1-1     |        | Obrigatório o preenchimento do Grupo Informações de Pagamento para NF-e e NFC-e. Para as notas com finalidade de Ajuste ou Devolução o campo Meio de Pagamento deve ser preenchido com 90=Sem Pagamento. |
| 398.10 | YA01a | detPag  | Grupo Detalhamento do Pagamento   | G     | YA01  |        | 1-100   |        |                                                                                                                                                                                                          |
| 398.11 | YA01b | indPag  | Indicador da Forma de Pagamento   | E     | YA01a | N      | 0-1     |      1 | 0= Pagamento à Vista 1= Pagamento à Prazo (Incluído na NT2016.002)                                                                                                                                       |
| 398.12 | YA02  | tPag    | Meio de pagamento                 | E     | YA01a | N      | 1-1     |      2 | Utilizar a Tabela de códigos dos meios de pagamentos publicada no Portal Nacional da Nota Fiscal Eletrônica Atualizado na NT 2020.006                                                                    |

![Image](assets/image_000015_4c36d268e647941e06d8fc2bd50db6ef04b9e7d267bda1aeb9ea6c3e0f42a40a.png)

| #       | ID    | Campo     | Descrição                                                                                   | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Observação                                                                                                                                                                                                                                                                                                |
|---------|-------|-----------|---------------------------------------------------------------------------------------------|-------|-------|--------|---------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 398.12a | YA02a | xPag      | Descrição do Meio de Pagamento                                                              | E     | YA01a | C      | 0-1     | 2-60   | Descrição do meio de pagamento. Preencher informando o meio de pagamento utilizado quando o código do meio de pagamento for informado como 99-outros.                                                                                                                                                     |
| 398.13  | YA03  | vPag      | Valor do Pagamento                                                                          | E     | YA01a | N      | 1-1     | 13v2   |                                                                                                                                                                                                                                                                                                           |
| 398.13a | YA03a | dPag      | Data do Pagamento                                                                           | E     | YA01a | D      | 0-1     |        |                                                                                                                                                                                                                                                                                                           |
| 398.13b | YA03b | -x-       | Sequência XML                                                                               | G     | YA01  |        | 0-1     |        | Grupo opcional.                                                                                                                                                                                                                                                                                           |
| 398.13c | YA03c | CNPJPag   | CNPJ transacional do pagamento                                                              | E     | YA03b | N      | 1-1     | 14     | Preencher informando o CNPJ do estabelecimento onde o pagamento foi processado/transacionado/recebido quando a emissão do documento fiscal ocorrerem estabelecimento distinto.                                                                                                                            |
| 398.13d | YA03d | UFPag     | UF do CNPJ do estabelecimento onde o pagamento foi processado/transacionado/recebido        | E     | YA03b | C      | 1-1     | 2      | UF do CNPJ do estabelecimento onde o pagamento foi processado/transacionado/recebido.                                                                                                                                                                                                                     |
| 398.20  | YA04  | card      | Grupo de Cartões, PIX, Boletos e outros Pagamentos Eletrônicos                              | G     | YA01a |        | 0-1     |        |                                                                                                                                                                                                                                                                                                           |
| 398.21  | YA04a | tpIntegra | Tipo de Integração para pagamento                                                           | E     | YA04  | N      | 1-1     | 1      | Tipo de Integração do processo de pagamento com o sistema de automação da empresa: 1=Pagamento integrado com o sistema de automação da empresa (Ex.: equipamento TEF, Comércio Eletrônico, POS Integrado) 2= Pagamento não integrado com o sistema de automação da empresa (Ex.: equipamento POS Simples) |
| 398.22  | YA05  | CNPJ      | CNPJ da instituição de pagamento                                                            | E     | YA04  | C      | 0-1     | 14     | Informar o CNPJ da instituição de pagamento, adquirente ou subadquirente. Caso o pagamento seja processado pelo intermediador da transação, informar o CNPJ do intermediador.                                                                                                                             |
| 398.23  | YA06  | tBand     | Bandeira da operadora de cartão de crédito e/ou débito                                      | E     | YA04  | N      | 0-1     | 2      | Utilizar a Tabela de Códigos das Operadoras de cartão de crédito e/ou débito publicada no Portal Nacional da Nota Fiscal Eletrônica.                                                                                                                                                                      |
| 398.24  | YA07  | cAut      | Número de autorização da operação com cartões, PIX, boletos e outros pagamentos eletrônicos | E     | YA04  | C      | 0-1     | 1-128  | Identifica o número da autorização da transação da operação com cartões, PIX, boletos e outros pagamentos eletrônicos                                                                                                                                                                                     |
| 398.24a | YA07a | CNPJReceb | CNPJ do beneficiário do pagamento                                                           | E     | YA04  | C      | 0-1     | 14     | Informar o CNPJ do estabelecimento beneficiário do pagamento                                                                                                                                                                                                                                              |
| 398.24b | YA07b | idTermPag | Identificador do terminal de pagamento                                                      | E     | YA04  | C      | 0-1     | 40     | Identificar o terminal emque foi realizado o pagamento                                                                                                                                                                                                                                                    |
| 398.25  | YA09  | vTroco    | Valor do troco                                                                              | E     | YA01  | N      | 0-1     | 13v2   | Valor do troco (Incluído na NT2016.002)                                                                                                                                                                                                                                                                   |

## 3.8.  Grupo Z. Informações Adicionais da NF-e

|   # | ID   | Campo   | Descrição                       | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Observação   |
|-----|------|---------|---------------------------------|-------|-------|--------|---------|--------|--------------|
| 399 | Z01  | infAdic | Grupo de Informações Adicionais | G     | A01   |        | 0-1     |        |              |

![Image](assets/image_000016_4c36d268e647941e06d8fc2bd50db6ef04b9e7d267bda1aeb9ea6c3e0f42a40a.png)

| #    | ID   | Campo      | Descrição                                               | Ele   | Pai   | Tipo   | Ocor.   | Tam.     | Observação                                                                                                                                                                                           |
|------|------|------------|---------------------------------------------------------|-------|-------|--------|---------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 400  | Z02  | infAdFisco | Informações Adicionais de Interesse do Fisco            | E     | Z01   | C      | 0-1     | 1 - 2000 | (v2.0)                                                                                                                                                                                               |
| 401  | Z03  | infCpl     | Informações Complementares de interesse do Contribuinte | E     | Z01   | C      | 0-1     | 1 - 5000 |                                                                                                                                                                                                      |
| 401a | Z04  | obsCont    | Grupo Campo de uso livre do contribuinte                | G     | Z01   |        | 0-10    |          | Campo de uso livre do contribuinte, Informar o nome do campo no atributo xCampo e o conteúdo do campo no xTexto                                                                                      |
| 401b | Z05  | xCampo     | Identificação do campo                                  | A     | Z04   | C      | 1-1     | 1 - 20   | Identificação do campo                                                                                                                                                                               |
| 401c | Z06  | xTexto     | Conteúdo do campo                                       | E     | Z04   | C      | 1-1     | 1 - 60   | Conteúdo do campo                                                                                                                                                                                    |
| 401d | Z07  | obsFisco   | Grupo Campo de uso livre do Fisco                       | G     | Z01   |        | 0-10    |          | Campodeusolivre doFisco.Informaronomedocampono atributo xCampo e o conteúdo do campo no xTexto                                                                                                       |
| 401e | Z08  | xCampo     | Identificação do campo                                  | A     | Z07   | C      | 1-1     | 1 - 20   | Identificação do campo                                                                                                                                                                               |
| 401f | Z09  | xTexto     | Conteúdo do campo                                       | E     | Z07   | C      | 1-1     | 1 - 60   | Conteúdo do campo                                                                                                                                                                                    |
| 401g | Z10  | procRef    | Grupo Processo referenciado                             | G     | Z01   |        | 0-100   |          | (NT 2012/003)                                                                                                                                                                                        |
| 401h | Z11  | nProc      | Identificador do processo ou ato concessório            | E     | Z10   | C      | 1-1     | 1 - 60   | Identificador do processo ou ato concessório                                                                                                                                                         |
| 401i | Z12  | indProc    | Indicador da origem do processo                         | E     | Z10   | N      | 1-1     | 1        | 0=SEFAZ; 1=Justiça Federal; 2=Justiça Estadual; 3=Secex/RFB; 4=CONFAZ 9=Outros                                                                                                                       |
| 401j | Z13  | tpAto      | Tipo do ato concessório                                 | E     | Z10   | N      | 0-1     | 2        | Para origem do Processo na SEFAZ (indProc=0), informar o tipo de ato concessório: (NT 2021.004) 08=Termo de Acordo; 10=Regime Especial; 12=Autorização específica; 14=Ajuste SINIEF 15=Convênio ICMS |

## 4. Regras de Validação

## 4.1.  I01. Produtos e Serviços / Declaração de Importação

| Campo-Seq   |   Modelo | Regra de Validação                                                                                                                | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                              |
|-------------|----------|-----------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|---------------------------------------------------------------------------------------------|
| I23d-10     |       55 | Informar o CNPJ ou CPF do adquirente ou do encomendante na importação por conta e ordem ou encomenda (tag:DI/tpIntermedio=2 ou 3) | Obrig.   |   331 | Rej.     | Rejeição: Informar o CNPJ ou CPF do adquirente ou do encomendante nesta forma de importação |
| I23d-20     |       55 | Se informado CNPJ do adquirente ou do encomendante: - CNPJ inválido (zeros, nulo ou DV inválido)                                  | Obrig.   |   332 | Rej.     | Rejeição: CNPJ/CPF do adquirente ou do encomendante da importação inválido                  |
| I23d1-10    |       55 | Se informado CPF do adquirente ou do encomendante: - CPF inválido (zeros, nulo ou DV inválido)                                    | Obrig.   |   332 | Rej.     | Rejeição: CNPJ/CPF do adquirente ou do encomendante da importação inválido '                |

## 4.2.  N. Item / Tributo: ICMS

| Campo-Seq Modelo   | Regra de Validação                                                                        | Aplic. Msg Efeito   | Descrição Erro                                                                |
|--------------------|-------------------------------------------------------------------------------------------|---------------------|-------------------------------------------------------------------------------|
| N28-12 55          | Se informado motDesICMS = 7 (desoneração Suframa): - tag indDeduzDeson deve ser igual a 1 | Obrig 652 Rej.      | Rejeição: informado indicador de desoneração inválido para a ZFM [nItem: 999] |

## 4.3.  X. Transporte da NF-e

| Campo-Seq   |   Modelo | Regra de Validação                                                                         | Aplic.   |   Msg | Efeito   | Descrição Erro                                                    |
|-------------|----------|--------------------------------------------------------------------------------------------|----------|-------|----------|-------------------------------------------------------------------|
| X03-10      |       65 | NFC-e com dados do Transportador e não é entrega a domicílio (tag:transporta e indPres<>4) | Obrig    |   754 | Rej.     | Rejeição: NFC-e com dados do Transportador                        |
| X03-20      |       65 | NFC-e sem dados do Transportador (tag:transporta) e é entrega a domicílio (indPres=4)      | Obrig.   |   786 | Rej.     | Rejeição: NFC-e de entrega a domicílio sem dados do Transportador |

## 4.4.  YA. Formas de Pagamento

| Campo-Seq   | Modelo   | Regra de Validação                                                                                                                                                                                                                                                                                                                                          | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                                     |
|-------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|--------------------------------------------------------------------------------------------------------------------|
| YA03a-10    | 55/65    | Se informada a Data de Pagamento (tag:dPag, id:YA03a) - Data de Pagamento posterior a data de recebimento do XLM                                                                                                                                                                                                                                            | Obrig    |   657 | Rej.     | Rejeição: Data de Pagamento inválida [nOcor:999]                                                                   |
| YA03c-10    | 55/65    | Se informado CNPJPag (campo: YA03c) - CNPJ com zeros ou dígito inválido                                                                                                                                                                                                                                                                                     | Obrig.   |   961 | Rej.     | Rejeição: CNPJ transacional do pagamento inválido [nOcor:999]                                                      |
| YA04-10     | 65       | Se informado o grupo de pagamentos (tag:pag): - Se o Pagamento for por cartão (tag:tPag=03, 04) ou PIX (tpag=17), deve ser informado o grupo de cartões (tag:card) Observação : Implementação por padrão, opcional a critério da UF. Exceção : A regra de validação não se aplica, em produção, para Nota Fiscal com Data de Emissão anterior a 01/04/2016. | Facult.  |   391 | Rej.     | Rejeição: Não informados os dados do cartão de crédito / débito nas Formas de Pagamento da Nota Fiscal [nOcor:999] |
| YA04-20     | 55/65    | Se Meio de Pagamento (tag: tPag) diferente de 03, 04, 10, 11, 12, 13, 15, 17 e 18: - Não pode preencher o grupo de cartões (tag: card)                                                                                                                                                                                                                      | Obrig.   |   963 | Rej.     | Rejeição: Tipo de pagamento não aceita o grupo de cartões ou boletos. [nOcor:999]                                  |
| YA07a       | 55/65    | Se informado CNPJReceb (campo: YA07a) - CNPJ com zeros ou dígito inválido                                                                                                                                                                                                                                                                                   | Obrig.   |   796 | Rej.     | Rejeição: CNPJ recebedor do pagamento inválido [nOcor:999]                                                         |

![Image](assets/image_000017_3ef87c6efc422eec0ff1573a9d8c9fbfe90897a4871f7a44e8bba9493eccf2b8.png)

![Image](assets/image_000018_3ef87c6efc422eec0ff1573a9d8c9fbfe90897a4871f7a44e8bba9493eccf2b8.png)

| Campo-Seq   | Modelo   | Regra de Validação                                                                                                                                | Aplic. Msg   | Efeito   | Descrição Erro                              |
|-------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------|--------------|----------|---------------------------------------------|
| YA09-20     | 55/65    | Valor do troco (id:YA09, tag:vTroco) superior a R$ 1.000,00 300.000,00. Observação: Essa regra de validação será ativada emproduçãoem 01/10/2024. | Obrig. 965   | Rej.     | Rejeição: Valor do troco acima do permitido |

## 4.5.  W. Total da NF-e

| Campo-Seq   | Modelo   | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                  |
|-------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|---------------------------------------------------------------------------------|
| W16-10      | 55/65    | -Total do vNF (id:W16) difere do somatório de: (+) vProd (id:W07) (-) vDesc (id:W10) (-) vICMSDeson (id: W04a) (+) vST (id:W06) (+) vFCPST (id:W06a) (+)vICMSMonoReten (id:W06d) (+) vFrete (id:W08) (+) vSeg (id:W09) (+) vOutro (id:W15) (+) vII (id:W11) (+) vIPI (id:W12) (+) vIPIDevol (id: W12a) (+) vServ (id:W18) (*3) (NT 2011/005) (+) vPIS (id: R06, campo: PISST/vPIS), se indSomaPISST=1 (+) vCofins (id: T06, campo: COFINSST/vCOFINS ), se indSomaCOFINSST =1 Exceção 1: Faturamento direto de veículos novos: Se informada operação de Faturamento Direto para veículos novos (tpOp = 2, id:J02): - Total do vNF (id:W16) difere do somatório de: (+) vProd (id:W07) (-) vDesc (id:W10) (-) vICMSDeson (id:W04a) (+) vFrete (id:W08) (+)vICMSMonoReten (id:W06d) (+) vSeg (id:W09) (+) vOutro (id:W15) (+) vII (id:W11) (+) vIPI (id:W12) (+) vServ (id:W18) (*3) (NT 2011/005) (+) vPIS (id: R06, campo: PISST/vPIS), se indSomaPISST=1 (+) vCofins(id: T06, campo: COFINSST/vCOFINS ), se indSomaCOFINSST =1 Exceção 2 : Esta regra não se aplica nas operações de importação (CFOP inicia com '3') . | Facult.  |   610 | Rej.     | Rejeição: Total daNF difere do somatório dos Valores compõe o valor Total da NF |

![Image](assets/image_000019_3ef87c6efc422eec0ff1573a9d8c9fbfe90897a4871f7a44e8bba9493eccf2b8.png)

| Campo-Seq   | Modelo   | Regra de Validação                                                                                                                                                                              | Aplic.   | Msg   | Efeito   | Descrição Erro   |
|-------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|------------------|
|             |          | Exceção 3 (NT 2013/005 v 1.22): Esta regra de validação não deverá causar rejeição caso não tenha sido subtraído o valor do ICMS Desonerado (vICMSDeson) do valor total da NF-e. (NT 2016.002). |          |       |          |                  |

## 4.6.  Banco de Dados: Emitente

| Campo-Seq   | Modelo   | Regra de Validação                                                                                                                 | Aplic.   | Msg   | Efeito   | Descrição Erro                                        |
|-------------|----------|------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|-------------------------------------------------------|
| ...         | ...      | ...                                                                                                                                | ...      | ...   | ...      | ...                                                   |
| 1C17-34     | 55       | Se informada IE do Emitente: - Emitente não autorizado para emissão de NF-e Exceção: Esta regra não se aplica na emissão da NFA-e. | Obrig.   | 203   | Rej.     | Rejeição: Emissor não habilitado para emissão da NF-e |

## 5. Novos códigos de rejeição

|   CÓDIGO | MOTIVO DE NÃO ATENDIMENTO DA SOLICITAÇÃO                                        |
|----------|---------------------------------------------------------------------------------|
|      652 | Rejeição: informado indicador de desoneração inválido para a ZFM [nItem: 999]   |
|      657 | Rejeição: Data de Pagamento inválida [nOcor:999 [nOcor:999]                     |
|      796 | Rejeição: CNPJ recebedor do pagamento inválido[nOcor:999]                       |
|      961 | Rejeição: CNPJ transacional do pagamento inválido [nOcor:999]                   |
|      963 | Rejeição: Tipo de pagamento não aceita o grupo de cartões ou boletos[nOcor:999] |
|      965 | Rejeição: Valor do troco acima do permitido                                     |
## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt2023-004-v1-20-campos-e-regras/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt2023-004-v1-20-campos-e-regras/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt2023-004-v1-20-campos-e-regras.md)
- [Proveniência resumida](../../../../sources/provenance/nt2023-004-v1-20-campos-e-regras.json)


## Documentos relacionados

- [nt2021-004v1-35-novos-campos-e-regras](../nt2021-004v1-35-novos-campos-e-regras/document.md)
