---
slug: icms-st
title: ICMS Substituição Tributária
type: formula
tax: icms
regime: substituicao-tributaria
status: published
sources:
  - nt2020-005-v1-21-regras-de-valida-o
  - nt-2016-002-v1-61
  - nt2018-005-v1-52-alteracaodeleiautenf-enfc
  - cbenef-pr-html
  - tabela-fcp-uf-2025
created_at: 2025-06-26
updated_at: 2025-06-26
---

## Metadados

### Fontes normativas
- [nt2020-005-v1-21-regras-de-valida-o](corpus/nfe/notas-tecnicas/nt2020-005-v1-21-regras-de-valida-o/document.md)
- [nt-2016-002-v1-61](corpus/nfe/notas-tecnicas/nt-2016-002-v1-61/document.md)
- [nt2018-005-v1-52-alteracaodeleiautenf-enfc](corpus/nfe/notas-tecnicas/nt2018-005-v1-52-alteracaodeleiautenf-enfc/document.md)
- [cbenef-pr-html](corpus/nfe/Estado de PR/cbenef-pr-html/document.md)
- tabela-fcp-uf-2025

### Fontes normativas
- [nt2020-005-v1-21-regras-de-valida-o](corpus/nfe/notas-tecnicas/nt2020-005-v1-21-regras-de-valida-o/document.md)
- [nt-2016-002-v1-61](corpus/nfe/notas-tecnicas/nt-2016-002-v1-61/document.md)
- [nt2018-005-v1-52-alteracaodeleiautenf-enfc](corpus/nfe/notas-tecnicas/nt2018-005-v1-52-alteracaodeleiautenf-enfc/document.md)
- [cbenef-pr-html](corpus/nfe/Estado de PR/cbenef-pr-html/document.md)
- tabela-fcp-uf-2025

# ICMS Substituição Tributária

## Visão geral

O ICMS-ST é o regime pelo qual a responsabilidade pelo recolhimento do imposto é atribuída a um contribuinte substituto (geralmente o fabricante, importador ou atacadista), que recolhe o ICMS de toda a cadeia até o consumo final. O cálculo envolve a Margem de Valor Agregado (MVA/IVA), a alíquota interna do destino e a dedução do ICMS próprio.

## Base legal

- Convênios ICMS de ST por setor (PE-13, etc.)
- [NT 2020.005](../../corpus/nfe/notas-tecnicas/nt2020-005-v1-21-regras-de-valida-o/document.md) — nova modalidade de BC do ICMS-ST (CST 70 e 90)
- [NT 2016.002](../../corpus/nfe/notas-tecnicas/nt-2016-002-v1-61/document.md) — alterações de leiaute para ST
- [NT 2018.005](../../corpus/nfe/notas-tecnicas/nt2018-005-v1-52-alteracaodeleiautenf-enfc/document.md) — campo pST (alíquota suportada pelo consumidor final)
- Benefícios fiscais por UF (cbenef-PR, SP, RS, etc.)
- Tabela FCP por UF

## Variáveis

| Variável | Descrição | Fonte |
|----------|-----------|-------|
| `vProd` | Valor do produto/mercadoria | NF-e |
| `vFrete` | Valor do frete | NF-e |
| `vSeg` | Valor do seguro | NF-e |
| `vOutro` | Outras despesas acessórias | NF-e |
| `vIPI` | Valor do IPI | NF-e |
| `vDesc` | Valor do desconto | NF-e |
| `pICMS_inter` | Alíquota interestadual (%) | Tabela |
| `pICMS_int` | Alíquota interna no destino (%) | Tabela |
| `pMVA` | Margem de Valor Agregado / IVA (%) | Convênio |
| `pRedBC` | Redução de BC do ICMS próprio (%) | Legislação UF |
| `pRedBCST` | Redução de BC do ICMS-ST (%) | Legislação UF |
| `pFCP` | Alíquota do FCP (%) | Tabela UF |

## Fórmula

### 1. Base de Cálculo do ICMS próprio

BC_propria = (vProd + vFrete + vSeg + vOutro + vIPI - vDesc) / (1 - pICMS_inter / 100)

### 2. ICMS próprio

ICMS_proprio = BC_propria × pICMS_inter / 100

### 3. Base de Cálculo do ICMS-ST

**Com MVA original:**

BC_ST = (vProd + vFrete + vSeg + vOutro + vIPI - vDesc) × (1 + pMVA / 100)

**Com MVA ajustado (IVA_Ajustado):**

IVA_Ajustado = (1 + pMVA / 100) × (1 - pICMS_inter / 100) / (1 - pICMS_int / 100) - 1

BC_ST = (vProd + vFrete + vSeg + vOutro + vIPI - vDesc) × (1 + IVA_Ajustado)

### 4. ICMS-ST total

ICMS_ST_total = BC_ST × pICMS_int / 100

### 5. ICMS-ST a recolher

ICMS_ST_a_recolher = ICMS_ST_total - ICMS_proprio

### 6. FCP na ST

FCP_ST = BC_ST × pFCP / 100

Total_a_recolher = ICMS_ST_a_recolher + FCP_ST

### Com redução de BC (CST 70)

Com redução de base de cálculo, aplicam-se percentuais distintos sobre a BC própria e a BC da ST conforme [NT 2020.005](../../corpus/nfe/notas-tecnicas/nt2020-005-v1-21-regras-de-valida-o/document.md):

BC_propria_reduzida = BC_propria × (1 - pRedBC / 100)

BC_ST_reduzida = BC_ST × (1 - pRedBCST / 100)

## Passo a passo

1. Calcular o ICMS próprio (mesmo que seja diferido/reduzido)
2. Identificar a MVA/IVA aplicável ao produto (por convênio/protocolo)
3. Ajustar a MVA se aplicável (IVA_Ajustado)
4. Calcular a BC da ST aplicando a MVA sobre o valor total da operação
5. Aplicar a alíquota interna do destino para obter o ICMS-ST total
6. Subtrair o ICMS próprio para obter o valor a recolher
7. Calcular o FCP separadamente sobre a BC_ST

## Exemplo

**Dados:** vProd = 1.000,00 | vFrete = 50,00 | vSeg = 0 | vIPI = 100,00 | vDesc = 0
pICMS_inter = 12% | pICMS_int = 18% | pMVA = 40% | pFCP = 2%

### Passo 1 — ICMS próprio

BC_propria = (1000 + 50 + 0 + 0 + 100 - 0) / (1 - 0,12) = 1150 / 0,88 = 1.306,82

ICMS_proprio = 1.306,82 × 0,12 = 156,82

### Passo 2 — MVA ajustado

IVA_Ajustado = (1 + 0,40) × (1 - 0,12) / (1 - 0,18) - 1
= 1,40 × 0,88 / 0,82 - 1
= 1,5024 - 1
= 0,5024 (50,24%)

### Passo 3 — BC da ST

BC_ST = 1150 × (1 + 0,5024) = 1150 × 1,5024 = 1.727,76

### Passo 4 — ICMS-ST total

ICMS_ST_total = 1.727,76 × 0,18 = 311,00

### Passo 5 — ICMS-ST a recolher

ICMS_ST_a_recolher = 311,00 - 156,82 = 154,18

### Passo 6 — FCP na ST

FCP_ST = 1.727,76 × 0,02 = 34,55

Total = 154,18 + 34,55 = 188,73

## Quando utilizar

### CST aplicáveis

- **CST 10** — ICMS próprio + ST (substituto calcula ambos os tributos)
- **CST 30** — Isento ou não tributado + ST (ICMS próprio = 0, apenas ST)
- **CST 70** — ICMS próprio com redução de BC + ST (percentuais de redução distintos)
- **CST 90** — Outras (ST com modalidade de BC específica por legislação)
- **CST 60** — ICMS cobrado anteriormente por ST (quem recebe a mercadoria já com ST recolhida)

### Perfil do contribuinte

**Substituto (responsável pelo recolhimento):**
- Fabricante, importador, atacadista ou distribuidor
- Definido por convênio/protocolo ICMS para cada setor
- Obrigado a reter o ICMS-ST na saída

**Substituído (contribuinte que recebe):**
- Comerciante varejista ou atacadista que adquire mercadoria já com ST
- Não recolhe ICMS próprio na revenda (já foi retido pelo substituto)
- Deve usar CST 60 na saída

### Tipo de operação

- Operações internas e interestaduais com produtos sujeitos a ST
- Setores típicos: autopeças, medicamentos, perfumaria, bebidas, cigarros, materiais de construção, lubrificantes, pneus
- A lista de produtos e MVAs é definida por convênio ICMS (ex: Convênio 142/2018, PE-13, etc.)

### Não utilizar quando

- Produto não listado em convênio/protocolo ST (operação normal, sem ST)
- Substituído revendendo mercadoria (já recolhido pelo substituto — usar CST 60)
- Simples Nacional (alguns regimes de ST têm regras específicas)
- ICMS próprio sem ST — use `icms-proprio`

## Observações

- **CST 10** — ICMS próprio + ST (operação regular com ST)
- **CST 30** — Isento ou não tributado + ST
- **CST 70** — ICMS próprio com redução de BC + ST
- **CST 90** — Outras (ST com modalidade de BC específica)
- CST 60 — ICMS cobrado anteriormente por ST (quem recebe a mercadoria já com ST recolhida)
- O MVA/IVA original é definido em convênios ICMS por setor
- O IVA Ajustado é usado em operações interestaduais para equilibrar a tributação entre estados
- Diferimento parcial: ICMS próprio reduzido, ST calculado integralmente (ex: cbenef-PR)
- **Tabela de alíquotas por UF** em `formulas/icms/aliquotas-icms-uf.md`
- CST 70 e 90 com nova modalidade de BC ([NT 2020.005](../../corpus/nfe/notas-tecnicas/nt2020-005-v1-21-regras-de-valida-o/document.md)): percentuais de redução distintos
