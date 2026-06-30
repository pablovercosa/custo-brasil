---
title: "Projeto Nota Fiscal Eletrônica"
slug: "nt2008-002"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "e93954e307cab8b8cdc26ad85fb7a51a253c9b22d4d49778ce4905b015e45ef9"
converted_at_utc: "2026-06-25T14:57:12.720361+00:00"
status: "published"
type: "nota_tecnica"
---
![Image](assets/image_000000_c4e6daffbc318bd841fc00aef9f87a94e2b919c94e64e8100d060f4f9064a90b.png)

## Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_97125cda11fbe48db007214ab43d4640ad74064abcf03deb1a40748683585098.png)

## Nota Técnica 2008-002

## Divulga errata do Manual de Integração do Contribuinte - versão 2.0.2

![Image](assets/image_000002_92184f8bd39470e2cf03d293f30a766371086dd26fbc979d64245d6a03989d07.png)

Janeiro-2008

![Image](assets/image_000003_03855e49621a60885bf4c39a53011576c07dc6f710dc2994f7e1ba3cb6605fe9.png)

## 1.  Resumo

Divulga  a  errata  de  correção  de  texto  do  Manual  de  Integração  do  Contribuinte  -  versão 2.0.2 que torna a ordem dos campos pRedBC (N14) e vBC (N15) do grupo ICMS90 (N10) da NF-e  compatível com a ordem do Schema XML em uso (nfe\_v1.10.xsd do PL\_005a).

![Image](assets/image_000004_ad26cc5286de90e8f937dbe735aa4b042e009b1a847f39bc348cedb1609f0e44.png)

## 2.  Correção de texto

## 2.1 Grupo de informações ICMS90 do leiaute da NF-e, página 106

## Aonde se lê:

|   232 | N10   | ICMS90   | TAG de grupo do CST = 90                            | CG   | N01   |    | 1-1   |    |    | CST - 90 - Outros                                                                                                                                                          |
|-------|-------|----------|-----------------------------------------------------|------|-------|----|-------|----|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   233 | N11   | Orig     | Origem da mercadoria                                | E    | N10   | N  | 1-1   |  1 |    | Origem da mercadoria: 0 - Nacional; 1 - Estrangeira - Importação direta; 2 - Estrangeira - Adquirida no mercado interno.                                                   |
|   234 | N12   | CST      | Tributação do ICMS                                  | E    | N10   | N  | 1-1   |  2 |    | Tributação pelo ICMS 90 - Outros                                                                                                                                           |
|   235 | N13   | modBC    | Modalidade de determinação da BC do ICMS            | E    | N10   | N  | 1-1   |  1 |    | 0 - Margem Valor Agregado (%); 1 - Pauta (Valor); 2 - Preço Tabelado Máx. (valor); 3 - valor da operação.                                                                  |
|   236 | N14   | pRedBC   | Percentual da Redução de BC                         | E    | N10   | N  | 0-1   |  5 |  2 |                                                                                                                                                                            |
|   237 | N15   | vBC      | Valor da BC do ICMS                                 | E    | N10   | N  | 1-1   | 15 |  2 |                                                                                                                                                                            |
|   238 | N16   | pICMS    | Alíquota do imposto                                 | E    | N10   | N  | 1-1   |  5 |  2 |                                                                                                                                                                            |
|   239 | N17   | vICMS    | Valor do ICMS                                       | E    | N10   | N  | 1-1   | 15 |  2 |                                                                                                                                                                            |
|   240 | N18   | modBCST  | Modalidade de determinação da BC do ICMS ST         | E    | N10   | N  | 1-1   |  1 |    | 0 - Preço tabelado ou máximo sugerido; 1 - Lista Negativa (valor); 2 - Lista Positiva (valor); 3 - Lista Neutra (valor); 4 - Margem Valor Agregado (%); 5 - Pauta (valor); |
|   241 | N19   | pMVAST   | Percentual da margem de valor Adicionado do ICMS ST | E    | N10   | N  | 0-1   |  5 |  2 |                                                                                                                                                                            |
|   242 | N20   | pRedBCST | Percentual da Redução de BC do ICMS ST              | E    | N10   | N  | 0-1   |  5 |  2 |                                                                                                                                                                            |

![Image](assets/image_000005_dc00abc4fd4d9c8f614df600cecec7c57793c9e5d5608c372429c5471073a6cc.png)

|   243 | N21   | vBCST   | Valor da BC do ICMS ST         | E   | N10   | N   | 1-1   |   15 |   2 |                         |
|-------|-------|---------|--------------------------------|-----|-------|-----|-------|------|-----|-------------------------|
|   244 | N22   | pICMSST | Alíquota do imposto do ICMS ST | E   | N10   | N   | 1-1   |    5 |   2 |                         |
|   245 | N23   | vICMSST | Valor do ICMS ST               | E   | N10   | N   | 1-1   |   15 |   2 | Valor do ICMS ST retido |

## leia-se:

|   232 | N10   | ICMS90   | TAG de grupo do CST = 90                            | CG   | N01   |    | 1-1   |    |    | CST - 90 - Outros                                                                                                                                                          |
|-------|-------|----------|-----------------------------------------------------|------|-------|----|-------|----|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   233 | N11   | orig     | Origem da mercadoria                                | E    | N10   | N  | 1-1   |  1 |    | Origem da mercadoria: 0 - Nacional; 1 - Estrangeira - Importação direta; 2 - Estrangeira - Adquirida no mercado interno.                                                   |
|   234 | N12   | CST      | Tributação do ICMS                                  | E    | N10   | N  | 1-1   |  2 |    | Tributação pelo ICMS 90 - Outros                                                                                                                                           |
|   235 | N13   | modBC    | Modalidade de determinação da BC do ICMS            | E    | N10   | N  | 1-1   |  1 |    | 0 - Margem Valor Agregado (%); 1 - Pauta (Valor); 2 - Preço Tabelado Máx. (valor); 3 - valor da operação.                                                                  |
|   236 | N15   | vBC      | Valor da BC do ICMS                                 | E    | N10   | N  | 1-1   | 15 |  2 |                                                                                                                                                                            |
|   237 | N14   | pRedBC   | Percentual da Redução de BC                         | E    | N10   | N  | 0-1   |  5 |  2 |                                                                                                                                                                            |
|   238 | N16   | pICMS    | Alíquota do imposto                                 | E    | N10   | N  | 1-1   |  5 |  2 |                                                                                                                                                                            |
|   239 | N17   | vICMS    | Valor do ICMS                                       | E    | N10   | N  | 1-1   | 15 |  2 |                                                                                                                                                                            |
|   240 | N18   | modBCST  | Modalidade de determinação da BC do ICMS ST         | E    | N10   | N  | 1-1   |  1 |    | 0 - Preço tabelado ou máximo sugerido; 1 - Lista Negativa (valor); 2 - Lista Positiva (valor); 3 - Lista Neutra (valor); 4 - Margem Valor Agregado (%); 5 - Pauta (valor); |
|   241 | N19   | pMVAST   | Percentual da margem de valor Adicionado do ICMS ST | E    | N10   | N  | 0-1   |  5 |  2 |                                                                                                                                                                            |
|   242 | N20   | pRedBCST | Percentual da Redução de BC do ICMS ST              | E    | N10   | N  | 0-1   |  5 |  2 |                                                                                                                                                                            |
|   243 | N21   | vBCST    | Valor da BC do ICMS ST                              | E    | N10   | N  | 1-1   | 15 |  2 |                                                                                                                                                                            |

![Image](assets/image_000006_df7055f4c2d9b14779ff6254afd8dd0118c777def5d78811e51d937d6080c8d0.png)

|   244 | N22   | pICMSST   | Alíquota do imposto do ICMS ST   | E   | N10   | N   | 1-1   |   5 |   2 |                         |
|-------|-------|-----------|----------------------------------|-----|-------|-----|-------|-----|-----|-------------------------|
|   245 | N23   | vICMSST   | Valor do ICMS ST                 | E   | N10   | N   | 1-1   |  15 |   2 | Valor do ICMS ST retido |

As dúvidas e sugestões devem ser encaminhadas através do Canal Fale Conosco da Secretaria da Fazenda de São Paulo (http://www.fazenda.sp.gov.br/email/default2.asp) referente à 'Portaria CAT 104/07'.
## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt2008-002/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt2008-002/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt2008-002.md)
- [Proveniência resumida](../../../../sources/provenance/nt2008-002.json)

## Documentos relacionados
_Nenhum documento relacionado conhecido._
