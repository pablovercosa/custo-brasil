---
slug: pis-cofins-nao-cumulativo
title: PIS/COFINS — Regime Não Cumulativo
type: formula
tax: pis-cofins
regime: nao-cumulativo
status: published
sources:
  - nt2010-005
  - nt2011-004
  - nt-2026-002-v1-00
  - nt2009-004
  - mc-nfag-anexo-i-leiaute-e-regras-de-valida-o-v1-00k
created_at: 2025-06-26
updated_at: 2025-06-26
---

# PIS/COFINS — Regime Não Cumulativo

## Visão geral

No regime não cumulativo, o contribuinte apura débitos sobre receitas e créditos sobre aquisições de bens e serviços. O saldo a recolher é a diferença entre débitos e créditos. As alíquotas básicas são 1,65% para PIS e 7,6% para COFINS (total 9,25%).

## Base legal

- Lei 10.637/2002 (PIS não cumulativo)
- Lei 10.833/2003 (COFINS não cumulativo)
- IN RFB 1.009/2010 — CST do PIS/COFINS
- NT 2010.005 — novos CFOP e CST do PIS/COFINS
- NT 2009.004 — grupos de tributos PIS e COFINS no leiaute
- NT 2011.004 — PIS-ST e COFINS-ST (grupos R e T)
- NT 2026.002 — restrições de PIS-ST e COFINS-ST na NFC-e

## Variáveis

| Variável | Descrição |
|----------|-----------|
| `vRec` | Valor da receita bruta (faturamento) |
| `vAqu` | Valor das aquisições de bens/serviços (crédito) |
| `pPIS` | Alíquota do PIS (1,65% básica) |
| `pCOFINS` | Alíquota da COFINS (7,6% básica) |

## Fórmula

### Débitos

Debito_PIS = vRec × pPIS / 100

Debito_COFINS = vRec × pCOFINS / 100

### Créditos (aquisições de bens para revenda/industrialização e serviços utilizados como insumo)

Credito_PIS = vAqu × pPIS / 100

Credito_COFINS = vAqu × pCOFINS / 100

### Saldo a recolher

PIS_a_recolher = max(Debito_PIS - Credito_PIS, 0)

COFINS_a_recolher = max(Debito_COFINS - Credito_COFINS, 0)

## Passo a passo

1. Identificar receitas tributáveis no período
2. Aplicar alíquotas de PIS e COFINS para calcular débitos
3. Identificar aquisições geradoras de crédito (bens para revenda, insumos, energia elétrica, aluguéis, etc.)
4. Aplicar as mesmas alíquotas para calcular créditos
5. Subtrair créditos de débitos por tributo
6. Recolher o saldo positivo; saldo negativo transfere para períodos seguintes

## Exemplo

**Dados:**

Receita do mês: 100.000,00
Aquisições com direito a crédito: 40.000,00
Alíquotas: PIS = 1,65%, COFINS = 7,6%

### Débitos

Debito_PIS = 100.000 × 0,0165 = 1.650,00

Debito_COFINS = 100.000 × 0,076 = 7.600,00

Total débitos = 9.250,00

### Créditos

Credito_PIS = 40.000 × 0,0165 = 660,00

Credito_COFINS = 40.000 × 0,076 = 3.040,00

Total créditos = 3.700,00

### Saldo a recolher

PIS = 1.650 - 660 = 990,00

COFINS = 7.600 - 3.040 = 4.560,00

Total = 5.550,00

## Quando utilizar

### CST aplicáveis

| CST | Descrição | Aplica esta fórmula? |
|-----|-----------|:--------------------:|
| 01 | Operação tributável (alíquota básica) | Sim |
| 02 | Tributável com alíquota diferenciada | Sim* |
| 03 | Tributável com alíquota por unidade | Não (cálculo por unidade) |
| 04 | Tributável com ST | Não (use PIS-ST) |
| 05 | Tributável com ST (alíquota zero) | Não |
| 06 | Tributável com alíquota zero | Sim (débito = 0) |
| 07 | Isenta | Sim (débito = 0) |
| 08 | Sem incidência | Sim (débito = 0) |
| 09 | Suspensão | Sim (débito = 0) |
| 49, 99 | Outras operações | Sim (débito = 0) |
| 50-55, 98 | ST, diferimento, suspensão | Não (operação ST) |

_\* CST 02: alíquota específica por produto (ex: medicamentos — 2,1% PIS / 9,9% COFINS)_

### Perfil do contribuinte

- Pessoa jurídica tributada pelo **Lucro Real** (obrigatório para não cumulativo)
- Empresas de todos os setores (comercial, industrial, serviços)
- Opção pelo não cumulativo é obrigatória para IRPJ Lucro Real

### Tipo de operação

- Receitas operacionais (venda de mercadorias, serviços, receitas financeiras)
- Aquisições de bens e serviços que geram crédito
- Operações no mercado interno e externo (exportação mantém crédito)

### Não utilizar quando

- **Lucro Presumido** — use o regime cumulativo (PIS 0,65%, COFINS 3,0%)
- **Simples Nacional** — recolhimento unificado, não por fórmula separada
- **PIS-ST e COFINS-ST** — uso de MVA, sistemática similar ao ICMS-ST
- **Exportação** — receita de exportação é imune, mas mantém crédito das aquisições
- **Produto monofásico** — alíquota concentrada no fabricante/importador (ex: combustíveis, medicamentos)

## Observações

### CST do PIS/COFINS (NT 2010.005)

| CST | Descrição |
|-----|-----------|
| 01 | Operação tributável (alíquota básica) |
| 02 | Tributável com alíquota diferenciada |
| 03 | Tributável com alíquota por unidade |
| 04 | Tributável com ST |
| 05 | Tributável com ST (alíquota zero) |
| 06 | Tributável com alíquota zero |
| 07 | Isenta |
| 08 | Sem incidência |
| 09 | Suspensão |
| 49 | Outras operações |
| 50 | Diferimento |
| 51 | Diferimento (ST) |
| 52 | Alíquota zero (ST) |
| 53 | Isenta (ST) |
| 54 | Sem incidência (ST) |
| 55 | Suspensão (ST) |
| 98 | Outras operações (ST) |
| 99 | Outras operações |

### Créditos permitidos (não cumulativo)

- Bens para revenda
- Insumos (matérias-primas, embalagens, etc.)
- Energia elétrica e térmica
- Aluguéis de prédios/máquinas
- Máquinas e equipamentos (depreciação)
- Edificações (depreciação)
- Armazenagem e frete na operação de venda
- Devoluções de vendas

### Regime cumulativo

No regime cumulativo (Lucro Presumido para algumas receitas), não há crédito:

PIS = Receita × 0,65%

COFINS = Receita × 3,0%

### PIS-ST e COFINS-ST (NT 2011.004)

PIS e COFINS também podem ser recolhidos por substituição tributária, com CST = 05 nos grupos R (PIS) e T (COFINS). A sistemática é similar ao ICMS-ST, com MVA e dedução do PIS/COFINS próprio.

### Exclusões da NBC do IBS/CBS

A partir da Reforma Tributária (NT 2025.002), o PIS e a COFINS são excluídos da base de cálculo do IBS e da CBS: "Não subtrair o valor do PIS por Substituição Tributária quando compor o valor total da NF-e."
