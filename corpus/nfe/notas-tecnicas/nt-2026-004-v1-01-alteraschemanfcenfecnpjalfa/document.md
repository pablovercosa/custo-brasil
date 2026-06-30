---
title: "CNPJ Alfanumérico -Atualizações"
slug: "nt-2026-004-v1-01-alteraschemanfcenfecnpjalfa"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "5f24a25351e790692754b07bbefac42ac67e70167a62a7806395d880f56675be"
converted_at_utc: "2026-06-25T15:54:53.242329+00:00"
status: "published"
type: "nota_tecnica"
---

## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt-2026-004-v1-01-alteraschemanfcenfecnpjalfa/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt-2026-004-v1-01-alteraschemanfcenfecnpjalfa/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt-2026-004-v1-01-alteraschemanfcenfecnpjalfa.md)
- [Proveniência resumida](../../../../sources/provenance/nt-2026-004-v1-01-alteraschemanfcenfecnpjalfa.json)

## CNPJ Alfanumérico -Atualizações

Nota Técnica 2026.004 Versão 1.01

![Image](assets/image_000002_39bad78d24e991b7e8d91f8509c7d31cad7342a188327a42b48a83bead57e497.png)

![Image](assets/image_000003_4337642970b704c9a6a4ac058f9a21324925d6dd4d4e999449a5ddd35d843f35.png)

![Image](assets/image_000004_1a5ecd553be5d245f1e478c733990a6d0b14a9e63743371d6eea89acb2a04cfd.png)

![Image](assets/image_000005_02c023d416c70d0c122bf4b6495e27eb9e6eb80d93252c28ea8efd3979b8dc29.png)

![Image](assets/image_000006_5bf930cbb8fb6e510f52b02c5a661cea31f62ea77c6cbd0f0b8c712d4dc9e092.png)

## Sumário

|   1. | Introdução................................................................................................................................4   |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------|
|   2. | Leiaute da NF-e (Modelo 55 e 65) ...........................................................................................5                 |
|   3. | Web Service - NfeRetAutorizacao...........................................................................................9                   |
|   4. | Web Service - NFeRecepcaoEvento - Parte Geral...............................................................10                                |
|   5. | Web Service - NfeConsultaProtocolo ....................................................................................11                     |
|   6. | Web Service - NfeConsultaCadastro.....................................................................................11                      |
|   7. | Web Service - NfeDistribuicaoDFe........................................................................................12                    |
|   8. | Web Service - NFeRecepcaoEvento- Cancelamento/Cancelamento por Substituição..........13                                                       |
|   9. | Web Service - NFeRecepcaoEvento - EPEC .......................................................................13                              |
|  10. | Web Service - NFeRecepcaoEvento - Ator Interessado na NF-e - Transportador ................14                                                 |
|  11. | Web Service - NfeInutilizacao ...............................................................................................14               |

## Controle de Versões

|   Versão | Publicação   | Descrição                                                                                           |
|----------|--------------|-----------------------------------------------------------------------------------------------------|
|     1.00 | 04/2026      | Publicação da NT                                                                                    |
|     1.01 | 06/2026      | Alteração da data de implantação em homologação e inclusão do layout do Web Service NFeInutilizacao |

## Histórico de Alterações / Cronograma

|   Versão | Histórico de atualizações                                                                                                                                           | Implantação Teste   | Implantação Produção   |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|------------------------|
|     1.00 | - Atualização do schema da NF-e/NFC-e para adequação ao CNPJ alfanumérico, com alteração dos campos do tipo CNPJ e Chave de Acesso (de numérico para alfanumérico). | 01/06/2026          | 01/07/2026             |
|     1.01 | Alteração da data de implantação em homologação e inclusão do layout do Web Service NFeInutilizacao                                                                 | Até 15/06/2026      | 01/07/2026             |

## 1.  Introdução

Esta  Nota  Técnica  2026.004  complementa  a  Nota  Técnica  Conjunta  DFe  2025.001  (CNPJ Alfanumérico)  e  apresenta  as  alterações  de  schema  do  ecossistema  NF-e/NFC-e  necessárias para adequar esses documentos ao novo padrão de identificação do contribuinte pessoa jurídica.

A  NT  Conjunta  2025.001  já  estabeleceu  de  forma  detalhada  as  diretrizes,  regras  de  formação, validação e impactos do CNPJ alfanumérico no ambiente dos DFe. Assim, esta Nota Técnica tem caráter complementar e operacional, concentrando-se especificamente na evolução dos schemas XML, com destaque para a atualização dos campos do tipo CNPJ, e chaves de acesso de DFe de forma a permitir a recepção de caracteres alfanuméricos.

A motivação para essas alterações decorre das mudanças introduzidas pela Receita Federal do Brasil  que  publicou  a  Instrução  Normativa  nº  2.229,  de  15  de  outubro  de  2024,  que  modifica  a regra  de  formação  do  CNPJ  no  Brasil.  Essa  ação  visa  ampliar  a  capacidade  de  geração  de números de CNPJ para abertura de empresas, em função do esgotamento do modelo atual.

## 2.  Leiaute da NF-e (Modelo 55 e 65)

A  lista  a  seguir  apresenta  apenas  os  campos  que  foram  atualizados  de  numérico  para  alfanumérico  (char),  em  função  da  adoção  do  CNPJ alfanumérico.

Grupo BA. Documento Fiscal Referenciado

| #      | ID    | Campo     | Descrição                                                                           | Ele   | Pai   | Tipo   | Ocor.   |   Tam. | Observação                                                                                                                                                                                                        |
|--------|-------|-----------|-------------------------------------------------------------------------------------|-------|-------|--------|---------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 29x.1  | BA01  | NFref     | Informação de Documentos Fiscais referenciados                                      | G     | B01   |        | 0-999   |        | Grupo com informações de Documentos Fiscais referenciados. Informação utilizada nas hipóteses previstas na legislação. (Ex.: Devolução de mercadorias, Substituição de NF cancelada, Complementação de NF, etc.). |
| 29x.2  | BA02  | refNFe    | Chave de acesso da NF-e referenciada                                                | CE    | BA01  | C      | 1-1     |     44 | Referencia uma NF-e (modelo 55) emitida anteriormente, vinculada a NF-e atual, ou uma NFC-e (modelo 65)                                                                                                           |
| 29x.2a | BA02a | refNFeSig | Chave da NF-e com código numérico zerado ([NT 2022.003](../nt2022-003v1-11-referenciamento/document.md))                              | CE    | BA01  | C      | 1-1     |     44 | Referencia uma NF-e (modelo 55) emitida anteriormente pela sua Chave de Acesso com código numérico zerado, permitindo manter o sigilo da NF-e referenciada.                                                       |
| 29x.3  | BA03  | refNF     | Informação da NF modelo 1/1A ou NF modelo 2 referenciada (alterado pela [NT2016.002](../nt-2016-002-v1-61/document.md)) | CG    | BA01  |        | 1-1     |        |                                                                                                                                                                                                                   |
| 29x.6  | BA06  | CNPJ      | CNPJ do emitente                                                                    | E     | BA03  | C      | 1-1     |     14 | Informar o CNPJ do emitente da NF                                                                                                                                                                                 |
| 29x.10 | BA10  | refNFP    | Informações da NF de produtor rural referenciada                                    | CG    | BA01  |        | 1-1     |        |                                                                                                                                                                                                                   |
| 29x.13 | BA13  | CNPJ      | CNPJ do emitente                                                                    | CE    | BA10  | C      | 1-1     |     14 | Informar o CNPJ do emitente da NF de produtor (v2.0)                                                                                                                                                              |
| 29x.19 | BA19  | refCTe    | Chave de acesso do CT-e referenciada                                                | CE    | BA01  | C      | 1-1     |     44 | Utilizar esta TAG para referenciar um CT-e emitido anteriormente, vinculada a NF-e atual - (v2.0).                                                                                                                |

Grupo C. Identificação do Emitente da Nota Fiscal eletrônica

|   # | ID   | Campo   | Descrição                         | Ele   | Pai   | Tipo   | Ocor.   |   Tam. | Observação                                                                                                                                                                                         |
|-----|------|---------|-----------------------------------|-------|-------|--------|---------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  30 | C01  | emit    | Identificação do emitente da NF-e | G     | A01   |        | 1-1     |        |                                                                                                                                                                                                    |
|  31 | C02  | CNPJ    | CNPJ do emitente                  | CE    | C01   | C      | 1-1     |     14 | Informar o CNPJ do emitente. Na emissão de NF-e avulsa pelo Fisco, as informações do remetente serão informadas neste grupo. O CNPJ ou CPF deverão ser informados com os zeros não significativos. |

Grupo E. Identificação do Destinatário da Nota Fiscal eletrônica

![Image](assets/image_000007_58d140ef13ba77aaafb47aecbd8f6903d106bc355d0ccd88991a0ca8a19fdbf2.png)

![Image](assets/image_000008_544faf92cda3c73cd6abc4d402c66b55da521f8230877692b64f4a466602793c.png)

![Image](assets/image_000009_eb81bbba2f39c4b0fcf350cbc8ddfb0546bd33665f608fd2461b283f6dee3270.png)

![Image](assets/image_000010_de1640a9d1df46401f27bc5a18deeb8839b64219ad68f44444585d14765293f7.png)

|   # | ID   | Campo   | Descrição                             | Ele   | Pai   | Tipo   | Ocor.   |   Tam. | Observação                                                                                                                                                                           |
|-----|------|---------|---------------------------------------|-------|-------|--------|---------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  62 | E01  | dest    | Identificação do Destinatário da NF-e | G     | A01   |        | 0-1     |        | Grupo obrigatório para a NF-e (modelo 55).                                                                                                                                           |
|  63 | E02  | CNPJ    | CNPJ do destinatário                  | CE    | E01   | C      | 1-1     |     14 | Informar o CNPJ ou o CPF do destinatário, preenchendo os zeros não significativos. No caso de operação com o exterior, ou para comprador estrangeiro informar a tag "idEstrangeiro'. |

## Grupo F. Identificação do Local de Retirada

|   # | ID   | Campo    | Descrição                          | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Observação                                                   |
|-----|------|----------|------------------------------------|-------|-------|--------|---------|--------|--------------------------------------------------------------|
|  80 | F01  | retirada | Identificação do Local de retirada | G     | A01   |        | 0-1     |        | Informar somente se diferente do endereço do remetente.      |
|  81 | F02  | CNPJ     | CNPJ                               | CE    | F01   | C      | 1-1     | 0 ou   | Informar CNPJ ou CPF. Preencher os zeros não significativos. |

## Grupo G. Identificação do Local de Entrega

|   # | ID   | Campo   | Descrição                         | Ele   | Pai   | Tipo   | Ocor.   | Tam.    | Observação                                                          |
|-----|------|---------|-----------------------------------|-------|-------|--------|---------|---------|---------------------------------------------------------------------|
|  89 | G01  | entrega | Identificação do Local de entrega | G     | A01   |        | 0-1     |         | Informar somente se diferente do endereço destinatário.             |
|  90 | G02  | CNPJ    | CNPJ                              | CE    | G01   | C      | 1-1     | 0 ou 14 | Informar CNPJ ou CPF. Preencher os zeros não significativos. (v2.0) |

## Grupo GA. Autorização para obter XML

| #     | ID   | Campo   | Descrição                                   | Ele   | Pai   | Tipo   | Ocor.   |   Tam. | Observação                                                   |
|-------|------|---------|---------------------------------------------|-------|-------|--------|---------|--------|--------------------------------------------------------------|
| 97a.1 | GA01 | autXML  | Pessoas autorizadas a acessar o XML da NF-e | G     | A01   |        | 0-10    |        |                                                              |
| 97a.2 | GA02 | CNPJ    | CNPJ Autorizado                             | CE    | GA01  | C      | 1-1     |     14 | Informar CNPJ ou CPF. Preencher os zeros não significativos. |

## Grupo I. Produtos e Serviços da NF-e

|      # | ID   | Campo   | Descrição                           | Ele   | Pai   | Tipo   | Ocor.   |   Tam. | Observação                                                                                                    |
|--------|------|---------|-------------------------------------|-------|-------|--------|---------|--------|---------------------------------------------------------------------------------------------------------------|
|    100 | I01  | prod    | Detalhamento de Produtos e Serviços | G     |       | H01    | 1-1     |        |                                                                                                               |
| 104.02 | l05b | -x-     | Sequência XML                       |       | G     | I01    | 0-1     |        | (Incluído na [NT 2016.002](../nt-2016-002-v1-61/document.md))                                                                                     |
| 104.05 | l05e | CNPJFab | CNPJ do Fabricante Mercadoria       | da    | E     | I05b C | 0-1     |     14 | CNPJ do Fabricante da Mercadoria, obrigatório para produto em escala NÃO relevante. (Incluído na [NT 2016/002](../nt-2016-002-v1-61/document.md)) |

## Grupo I01. Produtos e Serviços / Declaração de Importação

|      # | ID   | Campo   | Descrição                             | Ele   | Pai   | Tipo   | Ocor.   |   Tam. | Observação                                                                                                              |
|--------|------|---------|---------------------------------------|-------|-------|--------|---------|--------|-------------------------------------------------------------------------------------------------------------------------|
|    117 | I18  | DI      | Declaração de Importação              | G     | I01   |        | 0-100   |        | Informar dados da importação                                                                                            |
| 122.04 | I23d | CNPJ    | CNPJ do adquirente ou do encomendante | CE    | I18   | C      | 0-1     |     14 | Obrigatória a informação no caso de importação por conta e ordem ou por encomenda. Informar os zeros não significativos |

## Grupo I03. Produtos e Serviços / Grupo de Exportação

|      # | ID   | Campo     | Descrição                                        | Ele   | Pai   | Tipo   | Ocor.   |   Tam. | Observação                                                                                                                                                  |
|--------|------|-----------|--------------------------------------------------|-------|-------|--------|---------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 128.20 | I50  | detExport | Grupo de informações de exportação para o item   | G     | I01   |        | 0-500   |        | Informar apenas no Drawback e nas exportações                                                                                                               |
| 128.22 | I52  | exportInd | Grupo sobre exportação indireta                  | G     | I50   |        | 0-1     |        |                                                                                                                                                             |
| 128.24 | I54  | chNFe     | Chave de Acesso da NF-e recebida para exportação | E     | I52   | C      | 1-1     |     44 | NF-e recebida com fim específico de exportação Observação: No caso de operação com CFOP 3.503, informar a chave de acesso da NF-e que efetivou a exportação |

## Grupo O. Imposto sobre Produtos Industrializados

|   # | ID   | Campo    | Descrição                                                                                                          | Ele   | Pai   | Tipo   | Ocor.   |   Tam. | Observação                                       |
|-----|------|----------|--------------------------------------------------------------------------------------------------------------------|-------|-------|--------|---------|--------|--------------------------------------------------|
| 246 | O01  | IPI      | Grupo IPI                                                                                                          | CG    | M01   |        | 0-1     |        | Informar apenas quando o item for sujeito ao IPI |
| 248 | O03  | CNPJProd | CNPJ do produtor da mercadoria, quando diferente do emitente. Somente para os casos exportação direta ou indireta. | de E  | O01   | C      | 0-1     |     14 | Informar os zeros não significativos             |

![Image](assets/image_000011_bbfed4ec82606326e3cd87cc7d4377fea67cd58c75f78f3e1d16c6d13448cb5e.png)

![Image](assets/image_000012_d768c3a95f86da1a494e60d982f640a132fa118b67997bbc7750c57015e20184.png)

## Grupo X. Informações do Transporte da NF-e

|   # | ID   | Campo      | Descrição                    | Ele   | Pai   | Tipo   | Ocor.   |   Tam. | Observação                             |
|-----|------|------------|------------------------------|-------|-------|--------|---------|--------|----------------------------------------|
| 356 | X01  | transp     | Grupo Informações Transporte | G     | A01   |        | 1-1     |        |                                        |
| 358 | X03  | transporta | Grupo Transportador          | G     | X01   |        | 0-1     |        |                                        |
| 359 | X04  | CNPJ       | CNPJ do Transportador        | CE    | X03   | C      | 0-1     |     14 | Preencher os zeros não significativos. |

## Grupo YA. Informações de Pagamento

| #        | ID    | Campo   | Descrição                      | Ele   | Pai   | Tipo   | Ocor.   |   Tam. | Observação                                                                                                                                                                                               |
|----------|-------|---------|--------------------------------|-------|-------|--------|---------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 398.01   | YA01  | pag     | Grupo de Informações Pagamento | de G  | A01   |        | 1-1     |        | Obrigatório o preenchimento do Grupo Informações de Pagamento para NF-e e NFC-e. Para as notas com finalidade de Ajuste ou Devolução o campo Meio de Pagamento deve ser preenchido com 90=Sem Pagamento. |
| 398.10   | YA01a | detPag  | Grupo Detalhamento Pagamento   | do G  | YA01  |        | 1-100   |        |                                                                                                                                                                                                          |
| 398.13 b | YA03b | -x-     | Sequência XML                  | G     | YA01  |        | 0-1     |        | Grupo opcional.                                                                                                                                                                                          |
| 398.13 c | YA03c | CNPJPag | CNPJ transacional do pagamento | E     | YA03b | C      | 1-1     |     14 | Preencher informando o CNPJ do estabelecimento onde o pagamento foi processado/transacionado/recebido quando a emissão do documento fiscal ocorrer em estabelecimento distinto.                          |

## Grupo YB. Informações do Intermediador da Transação

|      # | ID   | Campo       | Descrição                                                                                                                 | Ele   | Pai   | Tipo   | Ocor.   |   Tam. | Observação                                                                                                                                                                                            |
|--------|------|-------------|---------------------------------------------------------------------------------------------------------------------------|-------|-------|--------|---------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 398.26 | YB01 | infIntermed | Grupo do Intermediador da Transação                                                                                       | G     | A01   |        | 0-1     |        | Obrigatório o preenchimento do Grupo de Informações do Intermediador da Transação nos casos de 'operação não presencial pela internet em site de terceiros (intermediadores) (Incluído na [NT2020.006](../nt2020-006-v1-31-intermediador-e-marketplace/document.md)) |
| 398.27 | YB02 | CNPJ        | CNPJ do Intermediador da Transação (agenciador, plataforma de delivery, marketplace e similar) de serviços e de negócios. | E     | YB01  | C      | 1-1     |     14 | Informar o CNPJ do Intermediador da Transação (agenciador, plataforma de delivery, marketplace e similar) de serviços e de negócios.                                                                  |

![Image](assets/image_000013_de1640a9d1df46401f27bc5a18deeb8839b64219ad68f44444585d14765293f7.png)

## Grupo VC. Referenciamento de item de outro Documento Fiscal Eletrônico - DF-e

| #    | ID   | Campo            | Descrição                                | Ele   | Pai   | Tipo   | Ocor.   |   Tam. | Observação                                         |
|------|------|------------------|------------------------------------------|-------|-------|--------|---------|--------|----------------------------------------------------|
| 325i | VC01 | DFeReferenc iado | Documento Fiscal Eletrônico Referenciado | G     | H01   |        | 0-1     |        | Grupo para referenciamento de itens de outro DF-e. |
| 325j | VC02 | chaveAcesso      | Chave de acesso do DF-e referenciado     | E     | VC01  | C      | 1-1     |     44 | Chave de acesso do DF-e referenciado.              |

## Grupo ZD. Informações do Responsável Técnico

| #    | ID   | Campo      | Descrição                                                                        | Ele                   | Pai   | Tipo   | Ocor.   |   Tam. | Observação                                                                                                       |
|------|------|------------|----------------------------------------------------------------------------------|-----------------------|-------|--------|---------|--------|------------------------------------------------------------------------------------------------------------------|
| 423a | ZD01 | infRespTec | Informações do Responsável Técnico pela emissão do DF-e                          | G                     | A01   |        | 0-1     |        | Grupo para informações do responsável técnico pelo sistema de emissão do DF-e                                    |
| 423b | ZD02 | CNPJ       | CNPJ da pessoa responsável pelo utilizado na emissão documento fiscal eletrônico | jurídica sistema do E | ZD01  | C      | 1-1     |     14 | Informar o CNPJ da pessoa jurídica responsável pelo sistema utilizado na emissão do documento fiscal eletrônico. |

## 3.  Web Service -NfeRetAutorizacao

Método: nfeRetAutorizacao

## 1.2. Leiaute Mensagem de Retorno Schema XML: retConsReciNFe\_v4.00.xsd

| #    | Campo   | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Descrição/Observação                                     |
|------|---------|-------|-------|--------|---------|--------|----------------------------------------------------------|
| PR01 | protNFe | Raiz  | -     | -      | -       | -      | TAG raiz do Protocolo de recebimento da NFe              |
| PR03 | infProt | G     | PR01  | -      | 1-1     | -      | Informações do Protocolo de resposta. TAG a ser assinada |
| PR07 | chNFe   | E     | PR03  | C      | 1-1     | 44     | Chave de Acesso da NF-e                                  |

![Image](assets/image_000014_a3b774df998650d7044203de49bbcb70bce6ad403cf3cbd95e5f4915c25fea6c.png)

![Image](assets/image_000015_d768c3a95f86da1a494e60d982f640a132fa118b67997bbc7750c57015e20184.png)

## 4.  Web Service -NFeRecepcaoEvento -Parte Geral

## Método: nfeRecepcaoEvento

## 1.1. Leiaute Mensagem de Entrada (Parte Geral)

O Web Service de Registro de Evento possui uma interface genérica, complementada por uma área específica para cada tipo de evento. Segue abaixo o leiaute da parte geral da mensagem de entrada para os eventos.

## Schema XML: envEvento\_v1.00.xsd

| #   | Campo     | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Descrição/Observação                                   |
|-----|-----------|-------|-------|--------|---------|--------|--------------------------------------------------------|
| P01 | envEvento | Raiz  | -     | -      | -       | -      | TAG raiz                                               |
| P04 | evento    | G     | P01   | xml    | 1-20    | -      | Evento, um lote pode conter até 20 eventos             |
| P06 | infEvento | G     | P04   | -      | 1-1     | -      | Grupo de informações do registro do Evento             |
| P10 | CNPJ      | CE    | P06   | C      | 1-1     | 14     | CNPJ do autor do evento                                |
| P12 | chNFe     | E     | P06   | C      | 1-1     | 44     | Chave de Acesso da NF-e à qual o evento será vinculado |

## 1.2. Leiaute Mensagem de Retorno (Parte Geral) Schema XML: retEnvEvento\_v1.00.xsd

![Image](assets/image_000016_4d1303b884874f6a1f7f7f21b1715fb97ce64ecc7cb0aba7532e1d7feb4b6c4a.png)

![Image](assets/image_000017_92c139952a91aeaa61d1119e1b16976626f5642ea1916b5b59e32bb89eaa50a2.png)

![Image](assets/image_000018_bec31dc2fa2a9172145da306ab47d1f83479a80307eef9826358cb37a0a2ca1c.png)

| #   | Campo         | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Descrição/Observação                                                                                                                                                           |
|-----|---------------|-------|-------|--------|---------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R01 | retEnvEvent o | Raiz  | -     | -      | -       | -      | TAG raiz da mensagem de retorno                                                                                                                                                |
| R09 | retEvento     | G     | R01   | -      | 0-20    | -      | Grupo do resultado do processamento do Evento                                                                                                                                  |
| R11 | infEvento     | G     | R09   |        | 1-1     | -      | Grupo de informações do registro do Evento                                                                                                                                     |
| R18 | chNFe         | E     | R11   | C      | 0-1     | 44     | Idem a mensagem de entrada                                                                                                                                                     |
| R23 | CNPJDest      | CE    | R11   | C      | 0-1     | 14     | Informar o CNPJ do destinatário da NF-e. Específico para evento 110111 - Cancelamento                                                                                          |
| R27 | chNFePend     | E     | R11   | C      | 0-50    | 44     | Relação de Chaves de Acesso de EPEC pendentes de conciliação, existentes no AN. Específico para evento: 110140 - EPEC Obs: Esta tag não é preenchida no evento de manifestação |

![Image](assets/image_000019_bbfed4ec82606326e3cd87cc7d4377fea67cd58c75f78f3e1d16c6d13448cb5e.png)

![Image](assets/image_000020_07e6b7e821e12ef5770f73b1602af4814e8a56428c0d3d3735f2341dd6a67e8a.png)

## 5.  Web Service -NfeConsultaProtocolo

## 1.1. Leiaute Mensagem de Entrada Schema XML: consSitNFe\_4.00.xsd

| #    | Campo      | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Descrição/Observação     |
|------|------------|-------|-------|--------|---------|--------|--------------------------|
| EP01 | consSitNFe | Raiz  | -     | -      | -       | -      | TAG raiz                 |
| EP05 | chNFe      | E     | EP01  | C      | 1-1     | 44     | Chave de Acesso da NF-e. |

## 1.2. Leiaute Mensagem de Retorno Schema XML: retConsSitNFe\_v4.00.xsd

| #           | Campo          | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Descrição/Observação                |
|-------------|----------------|-------|-------|--------|---------|--------|-------------------------------------|
| ER01        | retConsSitN Fe | Raiz  | -     | -      | -       | -      | TAG raiz da Resposta                |
| ER07b chNFe | ER07b chNFe    | E     | ER01  | C      | 1-1     | 44     | Chave de Acesso da NF-e consultada. |

## 6.  Web Service -NfeConsultaCadastro

Método: consultaCadastro

## 1.1. Leiaute Mensagem de Entrada

## Schema XML: consCad\_v2.00.xsd

| #    | Campo   | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Descrição/Observação   |
|------|---------|-------|-------|--------|---------|--------|------------------------|
| GP01 | ConsCad | Raiz  | -     | -      | -       | -      | TAG raiz               |
| GP03 | infCons | G     | GP01  | -      | 1-1     | -      | Dados da consulta      |
| GP07 | CNPJ    | CE    | GP03  | C      | 1-1     | 3-14   | CNPJ do contribuinte   |

![Image](assets/image_000021_bbfed4ec82606326e3cd87cc7d4377fea67cd58c75f78f3e1d16c6d13448cb5e.png)

![Image](assets/image_000022_07e6b7e821e12ef5770f73b1602af4814e8a56428c0d3d3735f2341dd6a67e8a.png)

## 1.2. Leiaute Mensagem de Retorno Schema XML: retConsCad\_v2.00.xsd

| #     | Campo      | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Descrição/Observação                                                                                                                                                                                                                                                        |
|-------|------------|-------|-------|--------|---------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GR01  | retConsCad | Raiz  | -     | -      | -       | -      | TAG raiz da solicitação                                                                                                                                                                                                                                                     |
| GR03  | infCons    | G     | GR01  | -      | 1-1     | -      | Dados da consulta                                                                                                                                                                                                                                                           |
| GR06c | CNPJ       | CE    | GR03  | C      | 1-1     | 3-14   | CNPJ consultado                                                                                                                                                                                                                                                             |
| GR07  | infCad     | G     | GR03  | -      | 0-N     | -      | Dados da situação cadastral Esta estrutura existe somente para as consultas realizadas com sucesso cStat=111, com possibilidade de múltiplas ocorrências (Ex.: consulta por IE de contribuinte com Inscrição Única - retorno de todos os estabelecimentos do contribuinte). |
| GR09  | CNPJ       | CE    | GR07  | C      | 1-1     | 3-14   | CNPJ do contribuinte                                                                                                                                                                                                                                                        |

## 7.  Web Service -NfeDistribuicaoDFe

## Método: nfeDistDFeInteresse

## 1.1. Leiaute Mensagem de Entrada Schema XML: distDFeInt\_v9.99.xsd

![Image](assets/image_000023_8f3e12770fe33189f73b04cff46233e862543adab885de06a25b8d83f9c9c26d.png)

| #   | Campo      | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Descrição/Observação                               |
|-----|------------|-------|-------|--------|---------|--------|----------------------------------------------------|
| A01 | distDFeInt | Raiz  | -     | -      | -       | -      | TAG raiz                                           |
| A05 | CNPJ       | CE    | A01   | C      | 1-1     | 14     | CNPJ do interessado no DF-e                        |
| A11 | consChNFe  | CG    | A01   | -      | 1-1     | -      | Grupo para consultar uma NF-e pela chave de acesso |
| A12 | chNFe      | E     | A11   | C      | 1-1     | 44     | Chave de acesso específica.                        |

![Image](assets/image_000024_bbfed4ec82606326e3cd87cc7d4377fea67cd58c75f78f3e1d16c6d13448cb5e.png)

![Image](assets/image_000025_d768c3a95f86da1a494e60d982f640a132fa118b67997bbc7750c57015e20184.png)

## 1.6. Leiautes Resumidos

1.6.1. Leiaute Resumo da NF-e

Schema XML: resNFe\_v1.01.xsd

| #   | Campo   | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Descrição/Observação                                                                                                                        |
|-----|---------|-------|-------|--------|---------|--------|---------------------------------------------------------------------------------------------------------------------------------------------|
| C01 | resNFe  | G     | -     | -      | -       | -      | TAG raíz com o conjunto de informações resumidas da NF-e. Este conjunto de informação será gerado quando a NF-e for autorizada ou denegada. |
| C03 | chNFe   | E     | C01   | C      | 1-1     | 44     | Chave de acesso da NF-e                                                                                                                     |
| C04 | CNPJ    | CE    | C01   | C      | 1-1     | 14     | CNPJ do Emitente                                                                                                                            |

## 1.6.2. Leiaute Resumo da NF-e Schema XML: resEvento\_ v1.01.xsd

| #   | Campo     | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Descrição/Observação    |
|-----|-----------|-------|-------|--------|---------|--------|-------------------------|
| D01 | resEvento | Raiz  | -     | -      | -       | -      | TAG raíz                |
| D04 | CNPJ      | CE    | D01   | C      | 1-1     | 14     | CNPJ do Emitente        |
| D06 | chNFe     | E     | D01   | C      | 1-1     | 44     | Chave de acesso da NF-e |

## 8.  Web Service -NFeRecepcaoEvento- Cancelamento/Cancelamento por Substituição

| #   | Campo    | Ele   | Pai   | Tipo   | Ocor.   | Tam. Descrição/Observação                                                                                                                          |
|-----|----------|-------|-------|--------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| P31 | chNFeRef | E     | P17   | C      | 1-1     | 44 Informa a chave de acesso da NF-e substituta da NF-e a ser cancelada. Nota: Campo exclusivo do Evento '110112 - Cancelamento por substituição'. |

## 9.  Web Service -NFeRecepcaoEvento -EPEC

## 1.1. Leiaute Mensagem de Entrada

Schema XML: envEPEC\_v1.00.xsd

![Image](assets/image_000026_a3b774df998650d7044203de49bbcb70bce6ad403cf3cbd95e5f4915c25fea6c.png)

![Image](assets/image_000027_ec2e8219e626b2d7ceedf6f22fc07e22fcc078ce2d551c88d198cfb9e627909e.png)

![Image](assets/image_000028_bbfed4ec82606326e3cd87cc7d4377fea67cd58c75f78f3e1d16c6d13448cb5e.png)

![Image](assets/image_000029_d768c3a95f86da1a494e60d982f640a132fa118b67997bbc7750c57015e20184.png)

| #   | Campo   | Ele   | Pai   | Tipo   | Ocor.   |   Tam. | Descrição/Observação                                                                                                                                                                                                                                                                                 |
|-----|---------|-------|-------|--------|---------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| P26 | dest    | G     | P17   |        | 1-1     |        |                                                                                                                                                                                                                                                                                                      |
| P28 | CNPJ    | CE    | P26   | C      | 1-1     |     14 | Informar o CPF ou o CNPJ do destinatário, preenchendo os zeros não significativos. No caso de operação com exterior, ou para comprador estrangeiro, informar a tag 'idEstrangeiro', com o número do passaporte, ou outro documento legal (campo aceita valor Nulo no caso de operação com exterior). |

## 1.2. Leiaute Mensagem de Retorno

Schema XML: retEnvEPEC\_v1.00

| #   | Campo     | Ele   | Pai   | Tipo   | Ocor.   | Tam. Descrição/Observação                                                          |
|-----|-----------|-------|-------|--------|---------|------------------------------------------------------------------------------------|
| R32 | chNFePend | E     | R11   | C      | 0-50    | 44 Relação de Chaves de Acesso de EPEC pendentes de conciliação, existentes no AN. |

## 10. Web Service -NFeRecepcaoEvento -Ator Interessado na NF-e - Transportador

## 1.1. Leiaute Mensagem de Entrada Schema XML: envEventoAtorInteressado\_v1.00.xsd

| #   | Campo   | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Descrição/Observação                        |
|-----|---------|-------|-------|--------|---------|--------|---------------------------------------------|
| P23 | autXML  | G     | P17   | -      | 1-1     | -      | Pessoas autorizadas a acessar o XML da NF-e |
| P24 | CNPJ    | CE    | P23   | C      | 1-1     | 3-14   | CNPJ autorizado                             |

## 11. Web Service -NfeInutilizacao

## 1.1. Leiaute Mensagem de Entrada

Schema XML: inutNFe\_v4.00.xsd

| # Campo   | Ele   | Pai   | Tipo Ocor. Tam.   | Descrição/Observação   |
|-----------|-------|-------|-------------------|------------------------|
| DP09 CNPJ | E     | DP03  | C 1-1             | 14 CNPJ do emitente    |

## 1.2. Leiaute Mensagem de Retorno

Schema XML: retInutNFe\_v4.00.xsd

| # Campo   | Ele    | Pai   | Tipo Ocor. Tam.   | Descrição/Observação   |
|-----------|--------|-------|-------------------|------------------------|
| DR11      | CNPJ E | DR03  | C 0-1             | 14 CNPJ do emitente    |

## Documentos relacionados
_Nenhum documento relacionado conhecido._
