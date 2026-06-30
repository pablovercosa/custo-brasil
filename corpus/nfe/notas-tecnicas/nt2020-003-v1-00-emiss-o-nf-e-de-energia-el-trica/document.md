---
title: "Sistema Nota Fiscal Eletrônica"
slug: "nt2020-003-v1-00-emiss-o-nf-e-de-energia-el-trica"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "c68e46cf667adfdfef73c40423beb884ae589016584d780eba83c5d70f71274a"
converted_at_utc: "2026-06-25T15:40:55.811669+00:00"
status: "published"
type: "nota_tecnica"
---

## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt2020-003-v1-00-emiss-o-nf-e-de-energia-el-trica/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt2020-003-v1-00-emiss-o-nf-e-de-energia-el-trica/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt2020-003-v1-00-emiss-o-nf-e-de-energia-el-trica.md)
- [Proveniência resumida](../../../../sources/provenance/nt2020-003-v1-00-emiss-o-nf-e-de-energia-el-trica.json)

## Sistema Nota Fiscal Eletrônica

Nota Técnica 2020.003

Orientações para Emissão de NF-e pelo Transmissor de Energia Elétrica

Versão 1.00 -Junho de 2020

![Image](assets/image_000002_f8e4edf9c58cf40f4e1c632415fa3edf3efd0182504e785ec8077bd3a565db28.png)

## Nota Fiscal Eletrônica

## Sumário

| Controle de Versões ............................................................................................................................3   | Controle de Versões ............................................................................................................................3   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Histórico de Alterações / Cronograma..................................................................................................4             | Histórico de Alterações / Cronograma..................................................................................................4             |
| 1                                                                                                                                                   | Resumo...........................................................................................................................................5  |
| 2                                                                                                                                                   | Detalhamento dos campos a serem preenchidos............................................................................6                            |
| 2.1                                                                                                                                                 | Grupo B. Identificação da Nota Fiscal Eletrônica......................................................................6                             |
| 2.2                                                                                                                                                 | Grupo I. Produtos e Serviços da NF-e......................................................................................6                         |
| 2.3                                                                                                                                                 | Grupo M. Tributos incidentes no Produto ou Serviço................................................................6                                 |
| 2.4                                                                                                                                                 | Grupo N. ICMS Normal ou ST..................................................................................................6                       |
| 2.5                                                                                                                                                 | Grupo Tributação do ICMS = 40, 41, 50...................................................................................6                           |
| 2.6                                                                                                                                                 | Grupo X. Informações do Transporte da NF-e..........................................................................7                               |
| 2.7                                                                                                                                                 | Grupo Z. Informações Adicionais da NF-e................................................................................7                            |
| 2.8                                                                                                                                                 | Orientações de preenchimento dos campos de Tributos Federais ...........................................7                                           |

![Image](assets/image_000003_2c45ff1698c6ac78f79df8c39ecd8d12246d64024bf4edbfae9d60ae499367aa.png)

## Controle de Versões

|   Versão | Publicação   | Descrição         |
|----------|--------------|-------------------|
|     1.00 | Junho/2020   | Publicação da NT. |

![Image](assets/image_000004_fa0702d955869ce14748a0190d1d3dc7d8792f325387ac545cbff7b980d64a87.png)

## Histórico de Alterações / Cronograma

|   Versão | Histórico de atualizações                                                                                                                | Implantação Teste   | Implantação Produção   |
|----------|------------------------------------------------------------------------------------------------------------------------------------------|---------------------|------------------------|
|     1.00 | • Divulgação de orientações para emissão de NF-e pelo Transmissor de energia elétrica, de acordo com o disposto no Ajuste SINIEF 11/2020 |                     |                        |

![Image](assets/image_000005_fa0702d955869ce14748a0190d1d3dc7d8792f325387ac545cbff7b980d64a87.png)

## 1  Resumo

Esta Nota Técnica divulga orientações para emissão de NF-e pelo Transmissor de Energia, com o objetivo de orientar o Transmissor de Energia elétrica a emitir corretamente a NF-e, em atenção ao disposto no disposto no Ajuste SINIEF 11/2020, de 16 de abril de 2020.

Não há criação nem alterações nos campos e nas regras de validação existentes; a presente Nota Técnica  tem  o  objetivo  único  de  esclarecer  o  conteúdo  que  deve  ser  colocado  nos  respectivos campos da NF-e.

![Image](assets/image_000006_2c45ff1698c6ac78f79df8c39ecd8d12246d64024bf4edbfae9d60ae499367aa.png)

## 2  Detalhamento dos Campos a Serem Preenchidos

Ao  emitir  Nota  Fiscal  Eletrônica  Modelo  55  (NF-e),  os  transmissores  de  energia  elétrica deverão observa as orientações constantes na presente Nota Técnica.

## 2.1  Grupo B. Identificação da Nota Fiscal Eletrônica

|   # | ID   | Campo    | Descrição                                                | Instruções de Preenchimento                                                                                                                       |
|-----|------|----------|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
|   8 | B04  | natOp    | Descrição da Natureza da Operação                        | Informar o valor 'Transmissão de energia elétrica - encargo de uso/conexão'                                                                       |
|  10 | B06  | mod      | Código do Modelo do Documento Fiscal                     | Informar o valor '55'=NF -e                                                                                                                       |
|  13 | B09  | dhEmi    | Data e hora de emissão do Documento Fiscal               | A emissão da NF-e deve ser feita até o último dia do mês em que ocorrer a emissão do aviso de crédito pelo ONS ou cobrança do encargo de conexão. |
|  14 | B10  | dhSaiEnt | Data e hora de Saída ou da Entrada da Mercadoria/Produto | Repetir o valor informado no campo Data de emissão (campo B10)                                                                                    |
|  15 | B11  | tpNF     | Tipo de Operação                                         | Informar o valor '1'=Saída                                                                                                                        |

## 2.2  Grupo I. Produtos e Serviços da NF-e

| #    | ID   | Campo   | Descrição                                                                         | Observação                                                                                                                                       |
|------|------|---------|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 102  | I03  | cEAN    | GTIN (Global Trade Item Number) do produto, antigo código EAN ou código de barras | Informar o valor 'SEM GTIN'                                                                                                                      |
| 103  | I04  | xProd   | Descrição do produto ou serviço                                                   | Conforme o caso, informar o valor: • 'Energia Elétrica - Encargo de Uso do Sistema de Transmissão'; ou • 'Energia Elétrica - Encargo de Conexão' |
| 104  | I05  | NCM     | Código NCM com 8 dígitos                                                          | Informar o valor '27160000' =Energia Elétrica                                                                                                    |
| 107  | I08  | CFOP    | Código Fiscal de Operações e Prestações                                           | Informar o valor: • '5949', no caso de operações internas; ou • '6949', no caso de operações interestaduais                                      |
| 108  | I09  | uCom    | Unidade Comercial                                                                 | Informar o valor 'UN'                                                                                                                            |
| 109  | I10  | qCom    | Quantidade Comercial                                                              | Informar o valor '1,00'                                                                                                                          |
| 109a | I10a | vUnCom  | Valor Unitário de Comercialização                                                 | Informar o valor recebido ou a receber, conforme aviso de crédito recebido do ONS                                                                |
| 110  | I11  | vProd   | Valor Total Bruto dos Produtos ou Serviços                                        | Informar o valor recebido ou a receber, conforme aviso de crédito recebido do ONS                                                                |
| 112  | I13  | uTrib   | Unidade Tributável                                                                | Informar o valor 'UN'                                                                                                                            |
| 113  | I14  | qTrib   | Quantidade Tributável                                                             | Informar o valor '1,00'                                                                                                                          |
| 113a | I14a | vUnTrib | Valor Unitário de tributação                                                      | Informar o valor recebido ou a receber, conforme aviso de crédito recebido do ONS                                                                |

## 2.3  Grupo M. Tributos Incidentes no Produto ou Serviço

|   # | ID   | Campo   | Descrição                                 | Observação              |
|-----|------|---------|-------------------------------------------|-------------------------|
| 163 | M01  | imposto | Tributos incidentes no Produto ou Serviço | Informar o Grupo <ICMS> |

## 2.4  Grupo N. ICMS Normal ou ST

|   # | ID   | Campo   | Descrição                                    | Observação                |
|-----|------|---------|----------------------------------------------|---------------------------|
| 164 | N01  | ICMS    | Informações do ICMS da Operação própria e ST | Informar o Grupo <ICMS40> |

## 2.5  Grupo Tributação do ICMS = 40, 41, 50

|   # | ID   | Campo   | Descrição                         | Observação                                                                    |
|-----|------|---------|-----------------------------------|-------------------------------------------------------------------------------|
| 203 | N11  | orig    | Origem da mercadoria              | Informar o valor '0' = Nacional - exceto as indicadas nos códigos 3, 4, 5 e 8 |
| 204 | N12  | CST     | Tributação do ICMS = 40, 41 ou 50 | Informar o valor '41' = Não tributada                                         |

![Image](assets/image_000007_fa0702d955869ce14748a0190d1d3dc7d8792f325387ac545cbff7b980d64a87.png)

## 2.6  Grupo X. Informações do Transporte da NF-e

|   # | ID   | Campo                        | Descrição   | Observação                       |
|-----|------|------------------------------|-------------|----------------------------------|
| 357 | X02  | modFrete Modalidade do frete |             | Informar o valor '9' = Sem frete |

## 2.7  Grupo Z. Informações Adicionais da NF-e

|   # | ID   | Campo   | Descrição                                               | Observação                                                                                                                                                                       |
|-----|------|---------|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 401 | Z03  | infCpl  | Informações Complementares de interesse do Contribuinte | Informar o valor 'Não incidência de ICMS, nos termos da cláusula primeira do Convênio ICMS 117/2004.' Após o texto acima, informar os dados do aviso de crédito emitido pelo NOS |

## 2.8  Orientações de Preenchimento dos Campos de Tributos Federais

Os  campos  relativos  aos  tributos  federais  (PIS,  COFINS  e  IPI)  deverão  ser  informados conforme as respectivas legislações.

![Image](assets/image_000008_fa0702d955869ce14748a0190d1d3dc7d8792f325387ac545cbff7b980d64a87.png)

## Documentos relacionados
_Nenhum documento relacionado conhecido._
