---
slug: icms-monofasico
title: ICMS Monofásico — Combustíveis
type: formula
tax: icms
regime: monofasico
status: published
sources:
  - nt2023-001v1-60-tributa-o-monof-sica-dos-combust-veis
  - nt-2023-01-perguntas-e-respostas
  - tabela-combustiveis-monofasica
created_at: 2025-06-26
updated_at: 2025-06-26
---

## Metadados

### Fontes normativas
- [nt2023-001v1-60-tributa-o-monof-sica-dos-combust-veis](corpus/combustiveis/notas-tecnicas/nt2023-001v1-60-tributa-o-monof-sica-dos-combust-veis/document.md)
- [nt-2023-01-perguntas-e-respostas](corpus/combustiveis/notas-tecnicas/nt-2023-01-perguntas-e-respostas/document.md)
- tabela-combustiveis-monofasica

### Fontes normativas
- [nt2023-001v1-60-tributa-o-monof-sica-dos-combust-veis](corpus/combustiveis/notas-tecnicas/nt2023-001v1-60-tributa-o-monof-sica-dos-combust-veis/document.md)
- [nt-2023-01-perguntas-e-respostas](corpus/combustiveis/notas-tecnicas/nt-2023-01-perguntas-e-respostas/document.md)
- tabela-combustiveis-monofasica

# ICMS Monofásico — Combustíveis

## Visão geral

O ICMS monofásico sobre combustíveis (também chamado ICMS Mono) concentra a tributação em uma única etapa da cadeia (produção ou importação), com alíquota **ad rem** (valor fixo por unidade, R$/litro, R$/kg). O regime foi instituído pela Lei Complementar 192/2022 e unifica a tributação do ICMS sobre combustíveis em todo o território nacional, com alíquotas uniformes por tipo de combustível definidas pelo CONFAZ.

## Base legal

- LC 192/2022 — ICMS monofásico sobre combustíveis
- Convênio ICMS 199/2022 — alíquotas ad rem
- [NT 2023.001](../../corpus/combustiveis/notas-tecnicas/nt2023-001v1-60-tributa-o-monof-sica-dos-combust-veis/document.md) — tributaçao monofásica dos combustíveis (leiaute)
- NT 2023.01 — perguntas e respostas com exemplos de cálculo
- Tabela de combustíveis monofásica (`corpus/geral/tabelas-federais/tabela-combustiveis-monofasica/`)

## Variáveis

| Variável | Descrição |
|----------|-----------|
| `qtd` | Quantidade tributada (litros, kg) |
| `adRem` | Alíquota ad rem (R$/unidade) |
| `pDif` | Percentual de diferimento (%) |
| `qtdRet` | Quantidade sujeita à retenção |
| `adRemICMSRet` | Alíquota ad rem para retenção (ajustada) |

## Fórmulas por CST

### CST 02 — Tributação monofásica própria

O contribuinte fabricante/importador recolhe o ICMS monofásico integralmente.

vICMSMono = qtd × adRem

### CST 15 — Tributação monofásica própria + retida anteriormente

O contribuinte recolhe o ICMS monofásico próprio e também declara o valor retido anteriormente (quando adquire de outro contribuinte monofásico).

vICMSMono = qtd × adRem

vICMSMonoRet = qtdRet × adRemICMSRet

### CST 53 — Tributação monofásica com diferimento

O contribuinte difere parte do ICMS monofásico para a etapa seguinte (ex: distribuidor que difere para o revendedor). O percentual de diferimento é de 33,33% (pDif = 33,33).

vICMSMonoOp = qtd × adRem

vICMSMonoDif = qtd × adRem × pDif / 100

vICMSMono = vICMSMonoOp - vICMSMonoDif = qtd × adRem × (1 - pDif / 100)

### CST 61 — Tributação monofásica com retenção

O contribuinte retém o ICMS monofásico na aquisição (ex: distribuidor que adquire com retenção do biodiesel). A alíquota da retenção pode ser ajustada.

vICMSMonoRet = qtdRet × adRemICMSRet

Para biodiesel B100: adRemICMSRet = adRem × 0,6667

vICMSMono = 0 (já retido anteriormente)

## Exemplos (NT 2023.01)

### Exemplo 1 — Diesel, CST 15
**Dados:** 8.800 litros, 12% B100, adRem = R$ 0,9456/L

| Passo | Descrição | Cálculo | Valor |
|-------|-----------|---------|------|
| 1 | Quantidade de diesel | 8.800 × 0,88 | 7.744 L |
| 2 | ICMS Mono próprio | 7.744 × 0,9456 | 7.322,73 |
| 3 | ICMS Mono retido (B100) | 1.056 × (0,9456 × 0,6667) | 665,56 |
| 4 | Total | 7.322,73 + 665,56 | 7.988,29 |

### Exemplo 2 — GLP, CST 02
**Dados:** 10.000 kg, adRem = R$ 1,2571/kg

vICMSMono = 10.000 × 1,2571 = 12.571,00

### Exemplo 3 — Gasolina, CST 15 com diferimento
**Dados:** 7.300 litros, 27% EAC (etanol), adRem = R$ 1,22/L, pDif = 33,33%

| Passo | Descrição | Cálculo | Valor |
|-------|-----------|---------|------|
| 1 | Quantidade de gasolina | 7.300 × 0,73 | 5.329 L |
| 2 | ICMS Mono operação | 5.329 × 1,22 | 6.501,38 |
| 3 | ICMS Mono diferido | 5.329 × 1,22 × 0,3333 | 2.166,97 |
| 4 | ICMS Mono devido | 6.501,38 - 2.166,97 | 4.334,41 |
| 5 | ICMS Mono retido (etanol) | 1.971 × (1,22 × 0,6667) | 1.602,87 |
| 6 | Total | 4.334,41 + 1.602,87 | 5.937,28 |

## Quando utilizar

### CST aplicáveis

| CST | Descrição | Perfil |
|-----|-----------|--------|
| 02 | Tributação monofásica própria | Fabricante/importador |
| 15 | Própria + retida anteriormente | Distribuidor que adquire com retenção |
| 53 | Com diferimento | Distribuidor difere para revenda |
| 61 | Com retenção | Distribuidor que retém na aquisição |

### Perfil do contribuinte

- Fabricante de combustível (produtor/refinaria)
- Importador de combustível
- Distribuidor de combustível (adquire com retenção ou difere)
- Revendedor (não recolhe ICMS mono — já retido anteriormente)

### Produtos sujeitos

Conforme tabela em `corpus/geral/tabelas-federais/tabela-combustiveis-monofasica/`:

- Diesel e biodiesel (B100)
- Gasolina e etanol anidro (EAC)
- GLP (gás liquefeito de petróleo)
- Querosene de aviação
- Outros combustíveis listados em convênio

### Não utilizar quando

- Combustível não listado na tabela monofásica
- Operação interestadual com contribuinte final (não monofásico)
- Revendedor varejista (já retido anteriormente, usar CST 60)
- Substituição tributária convencional (ICMS-ST)

## Observações

- As alíquotas ad rem são definidas pelo CONFAZ e válidas em todo território nacional (diferentemente do ICMS normal, que varia por UF)
- O percentual de diferimento padrão para combustíveis é 33,33%
- Para o biodiesel B100, a alíquota de retenção é `adRem × 0,6667` (2/3 da alíquota cheia)
- A tabela de combustíveis monofásicos inclui alíquotas ad rem por UF e tipo de combustível
- O ICMS monofásico substituiu o ICMS-ST para combustíveis a partir da LC 192/2022
- A Nota Técnica 2023.01 contém exemplos detalhados de preenchimento de todos os campos da NF-e para cada CST
