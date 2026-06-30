---
title: "Validações cBenef Rio Grande do Sul"
slug: "validacoes-cbenef-rs"
category: "cbenef"
source_family: "portal_nacional_nfe"
original_sha256: "8ea7808360bac24468f3e907721324c3fa3dcb0bd01bb6e2c0eed21f504c25a0"
converted_at_utc: "2026-06-26T15:51:43.123370+00:00"
status: "published"
type: "tax_benefit_table"
---
## Validações cBenef

## 

## Regras de validação:

As regras de validação dos campos relacionados com código de benefício fiscal, valor desonerado e diferimento foram divulgadas na NT2019.001.

As regras de validação vigentes no Estado do Rio Grande do Sul, para os modelos 55 (NF-e) e 65 (NFC-e), são:

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   **Validação**  **Código de rejeição**                                                                          **Quando esse erro ocorre:**                                                                                                                                                   **Data de implementação**
  --------------- ----------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------
      N12-85      **930:** CST com benefício fiscal e não informado o código de benefício fiscal \[nItem: nnn\]   Quando informado um CST que está associado a algum código de benefício fiscal, conforme tabela publicada pelo RS, sem o preenchimento do campo cBenef.                           01/02/2023 (mod.55)\
                                                                                                                                                                                                                                                                                                    01/06/2023 (mod.65)

      N12-86      **928:** Informado código de benefício fiscal para CST sem benefício fiscal \[nItem: nnn\]      Quando informado um CST que não está associado a algum código de benefício fiscal, conforme tabela publicada pelo RS, e há o preenchimento do campo cBenef.                           01/10/2019

      N12-94      **931:** Informado código de benefício fiscal incompatível com CST e UF \[nItem: nnn\]          Quando informado um CST que não possui correspondência com o tipo de código de benefício fiscal associado, conforme tabela de código de benefício fiscal publicada pelo RS.      01/02/2023 (mod.55)\
                                                                                                                                                                                                                                                                                                    01/06/2023 (mod.65)

      N12-98      **946:** Informado código de benefício fiscal incorreto ou inexistente na UF \[nItem: nnn\]     Quando o código de benefício fiscal informado não existe ou não está vigente, conforme tabela de código de benefício fiscal publicada pelo RS.                                        10/05/2020
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 

## Códigos de benefícios válidos para cada CST:

**00 - Tributada integralmente:**

\- Não preencher o campo cBenef.

**10 - Tributada e com cobrança do ICMS por substituição tributária:**

\- SEM CBENEF;

\- RS052901 - LIVRO II, ART. 12 - DECISÕES JUDICIAIS;

\- RS052999 - Anexo V.B -- OUTRAS.

**20 - Com redução de base de cálculo:**

\- Códigos de redução da base cálculo;

\- Códigos de diferimento parcial;

\- RS05**1**901 - LIVRO II, ART. 12 - DECISÕES JUDICIAIS;

\- RS05**2**901 - LIVRO II, ART. 12 - DECISÕES JUDICIAIS.

**30 - Isenta ou não-tributada e com cobrança do ICMS por substituição tributária:**

\- SEM CBENEF;

\- Códigos de isenção;

\- Códigos de não-incidência de ICMS;

\- RS05**1**901 - LIVRO II, ART. 12 - DECISÕES JUDICIAIS.

**40 -- Isenta:**

\- SEM CBENEF;

\- Códigos de isenção;

\- Códigos de não-incidência de ICMS;

\- RS05**1**901 - LIVRO II, ART. 12 - DECISÕES JUDICIAIS.

**41 - Não-tributada:**

\- SEM CBENEF;

\- Códigos de isenção;

\- Códigos de não-incidência de ICMS;

\- RS05**1**901 - LIVRO II, ART. 12 - DECISÕES JUDICIAIS;

\- RS051902 - LIVRO I,ART.38-A,§4º,E - RDA GORJETA;

\- RS051904 - L.I,ART.19,IV -- DEMANDA CONTRATADA NÃO UTILIZADA.

**50 -- Suspensão:**

\- SEM CBENEF;

\- Códigos de suspensão;

\- RS05**2**901 - LIVRO II, ART. 12 - DECISÕES JUDICIAIS;

\- RS05**2**999 - Anexo V.B -- OUTRAS.

**51 -- Diferimento:**

\- SEM CBENEF;

\- Códigos de redução da base cálculo;

\- Códigos de diferimento;

\- Códigos de diferimento parcial;

\- RS05**2**901 - LIVRO II, ART. 12 - DECISÕES JUDICIAIS;

\- RS05**2**999 - Anexo V.B -- OUTRAS.

**60 - ICMS cobrado anteriormente por substituição tributária:**

\- SEM CBENEF;

\- Códigos de ICMS já recolhido por ST;

\- RS05**2**901 - LIVRO II, ART. 12 - DECISÕES JUDICIAIS;

\- RS05**2**999 - Anexo V.B -- OUTRAS.

**70 - Com redução de base de cálculo e cobrança do ICMS por substituição tributária:**

\- Códigos de redução da base cálculo;

\- RS05**1**901 - LIVRO II, ART. 12 - DECISÕES JUDICIAIS;

\- Códigos de diferimento parcial;

\- RS05**2**901 - LIVRO II, ART. 12 - DECISÕES JUDICIAIS;

**90 -- Outras:**

\- SEM CBENEF;

\- RS05**2**901 - LIVRO II, ART. 12 - DECISÕES JUDICIAIS;

\- RS05**2**902 - IN45 - T.I - CAP. XXVIII - 2.2 - OPERAÇÕES ESPECÍFICAS DA PETROBRAS;

\- RS05**2**904 - AJUSTE SINIEF 13-2017 - OPERAÇÕES ESPECÍFICAS DA PETROBRAS E TRANSPETRO;

\- RS05**2**999 - Anexo V.B -- OUTRAS.

## 

## SEM CBENEF

Ao preencher o campo cBenef com a informação "SEM CBENEF" o contribuinte estará declarando ao Fisco que a operação não é tributada, sem indicar o código específico que desonera esta operação. Nestas situações o Fisco admitirá a operação, mas poderá solicitar informações adicionais ao contribuinte.

## Simples Nacional

O preenchimento do campo cBenef não se aplica para contribuintes do Simples Nacional.

## Operações de devolução

No Rio Grande do Sul, não será exigido o preenchimento dos campos nas operações de devolução quando tratar-se de operação interestadual ou para o exterior.

Nas operações de devolução internas, o campo referente ao cBenef deverá ser preenchido e será o mesmo cBenef da operação de origem.

## Operações de ajuste

No Rio Grande do Sul, não será aplicada validação nas notas fiscais emitidas com finalidade de ajuste.

## 

## Operações de entrada

No Rio Grande do Sul, não será aplicada validação nas notas fiscais emitidas com finalidade de entrada.

## Tabela de códigos 

A tabela de códigos utilizada para validação dos campos encontra-se disponível em nfe.fazenda.gov.br, opção, no menu, "Documentos", "Diversos".

## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/Estado de RS/validacoes-cbenef-rs/source.json)
- [Dados normalizados](../../../../normalized/nfe/Estado de RS/validacoes-cbenef-rs/normalized.json)
- [Changelog](../../../../changelog/nfe/Estado de RS/validacoes-cbenef-rs.md)
- [Proveniência resumida](../../../../sources/provenance/validacoes-cbenef-rs.json)
