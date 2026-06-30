---
title: "Projeto Nota Fiscal Eletrônica Projeto Nota Fiscal Eletrônica Projeto Nota Fiscal Eletrônica"
slug: "nt2010-007"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "f255620d2677305325ed3981ec2985cf7cf78fbc4fe419bda7435208ca77719a"
converted_at_utc: "2026-06-25T14:55:55.967854+00:00"
status: "published"
type: "nota_tecnica"
---
![Image](assets/image_000000_cf0dd90c3722c3f434a6fdefc5694a09d60c3cce31f02fdf1132013c8c4c7f51.png)

## Projeto Nota Fiscal Eletrônica Projeto Nota Fiscal Eletrônica Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_befcd928f12a0b138eca7eb3bab70a1138c0679f02c5ebb49a6b3f2807d8b5cc.png)

## Nota Técnica 20 Nota Técnica 20 10/007

## Divulga aperfeiçoamento das campos da versão 2.00 da NF aperfeiçoamento das regras de validação dos campos da versão 2.00 da NF -e regras de validação dos

![Image](assets/image_000002_7447947dd07bfa176901fa3cfb0c795fc3a0b0ad8e5f6bff8997c05568bf0620.png)

Setembro-2010

![Image](assets/image_000003_e5493c7075b2bc1155b83f7554af0055fe6411733c1e0e7baa911a53dc68c058.png)

## 1.  Resumo

Divulgar aperfeiçoamento das regras de validação do s campos da nova versão da NF-e, a princípio, não haverá reflexo na aplicação dos co ntribuintes, pois as alterações têm o objetivo de aperfeiçoar as regras de validação que  causam a rejeição de NF-e emitidas em situações específicas que não seguem a regra ger al.

![Image](assets/image_000004_a6a215445ea1440ac95701e8eb18842ad63d7bac5c72eaffd169ebed921ace29.png)

## 2.  Regras de validação alteradas

|        |     | I - Produtos e Serviços                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         |     |      |                                                                                                                            |
|--------|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|-----|------|----------------------------------------------------------------------------------------------------------------------------|
| GI08.2 | I08 | CFOP de Operação com Exterior (inicia por 3 ou 7) e UF destinatário <> 'EX' Exceção: Verificar se a tag UFCons (id:L120) foi informada com 'EX', neste caso o CFOP iniciado com 3 ou 7 é válid o                                                                                                                                                                                                                                                                                                          | Facult. | 520 | Rej. | Rejeição: CFOP de Operação com Exterior e UF destinatário difere de 'EX'                                                   |
| GI08.3 | I08 | CFOP de Operação no Estado (inicia com 5) e UF emitente diferente UF destinatário e destinatário contribuin te do ICMS (tem IE) Exceção: Verificar se a tag UFCons (id:L120) foi informada com a mesma UF do emitente , neste caso o CFOP iniciado com 5 é válido.                                                                                                                                                                                                                                        | Facult. | 521 | Rej. | Rejeição: CFOP de Operação Estadual e UF do emitente difere da UF do destinatário para destinat ário contribuinte do ICMS. |
| GI08.4 | I08 | CFOP de Operação no Estado (inicia com 1) e UF emitente diferente da UF remetente e remetente contribuinte do ICMS (tem IE)                                                                                                                                                                                                                                                                                                                                                                               | Facult. | 522 | Rej. | Rejeição: CFOP de Operação Estadual e UF emitente difere da UF remetente para remetente contribuinte do ICMS.              |
| GI08.7 | I08 | CFOP de Importação (inicia por 3) e não informado a tag DI Exceção: a regra não se aplica para os seguintes C FOP: 3.201 - Devolução de venda de produção do estabelec imento 3.202 - Devolução de venda de mercadoria adquirida ou recebida de terceiros 3.211 - Devolução de venda de produção do estabelec imento sob o regime de 'drawback' 3.503 - Devolução de mercadoria exportada que tenha sido recebida com fim específico de exportação 3.553 - Devolução de venda de bem do ativo imobilizado | Facult. | 525 | Rej. | Rejeição: CFOP de Importação e não informado dados da DI                                                                   |
| GN17   | N17 | Se CST de ICMS = 00, 10, 20, 51, 70, 90 e tag finNFe (id:B25) = 1: - Valor ICMS (id:N17) difere de Base de Cálculo (id:N15) * Alíquota (id:N16) (*3)                                                                                                                                                                                                                                                                                                                                                      | Facult. | 528 | Rej. | Rejeição: Valor do ICMS difere do produto BC e Alíquota                                                                    |

![Image](assets/image_000005_a6a215445ea1440ac95701e8eb18842ad63d7bac5c72eaffd169ebed921ace29.png)

|      | W-Total da NF-e                                                                                                                                         |         |     |      |                                                       |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------|---------|-----|------|-------------------------------------------------------|
| GW04 | Total do ICMS (id:W04) difere do somatório do valor dos itens (id:N17) (*3). O Total não deve considerar o valor informado para os CST 40, 41, 50 e 51. | Facult. | 532 | Rej. | Rejeição: Total do ICMS difere do somatório dos itens |

## 3.  Aperfeiçoamento da Consulta Situação da NF-e

| Validação do Pedido de Consulta de situação de NF-e - Regras de Negócios   | Validação do Pedido de Consulta de situação de NF-e - Regras de Negócios                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Validação do Pedido de Consulta de situação de NF-e - Regras de Negócios   | Validação do Pedido de Consulta de situação de NF-e - Regras de Negócios   | Validação do Pedido de Consulta de situação de NF-e - Regras de Negócios   |
|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------|
| #                                                                          | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Aplic.                                                                     | Msg                                                                        | Efeito                                                                     |
| J04                                                                        | - Verificar se campo 'Código Numérico' informad o na Chave de Acesso é diferente do existente no BD. Se o CNPJ base do titular do certificado digital utilizado na transmissão da consulta for igual ao CNPJ base do emissor ou do destinatário da NF-e, a mensagem de erro será complementada com a Chave de Acesso da NF-e existente no BD. A chave de acesso também poderá ser disponibilizada nos casos em que o CNPJ base do titular do certificado digital utilizado na transmissão da consulta seja igual ao CNPJ base do transmissor da NF-e, nas UF que tenham esta informação. | Obrig.                                                                     | 562                                                                        | Rej.                                                                       |

![Image](assets/image_000006_a6a215445ea1440ac95701e8eb18842ad63d7bac5c72eaffd169ebed921ace29.png)

## Nota Fiscal Eletrônica

## 4.  Mensagens alteradas

522

Rejeição: CFOP de Operação Estadual e UF emitente d ifere da UF remetente para remetente contribuinte do ICMS.

562

Rejeição: Código numérico informado na Chave de Ace sso difere do Código Numérico da NF-e

[chNFe:99999999999999999999999999999999999999999999]
## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt2010-007/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt2010-007/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt2010-007.md)
- [Proveniência resumida](../../../../sources/provenance/nt2010-007.json)


## Documentos relacionados

- [nota-t-cnica-2010-002-publicada-em-29-11-2010](../nota-t-cnica-2010-002-publicada-em-29-11-2010/document.md)
- [nota-t-cnica-2010-005-publicada-em-06-07-2010](../nota-t-cnica-2010-005-publicada-em-06-07-2010/document.md)
- [nota-t-cnica-2010-009-publicada-em-10-12-2010](../nota-t-cnica-2010-009-publicada-em-10-12-2010/document.md)
