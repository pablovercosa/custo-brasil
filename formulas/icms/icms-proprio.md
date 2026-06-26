---
slug: icms-proprio
title: ICMS Próprio — Cálculo Básico
type: formula
tax: icms
regime: normal
status: published
sources:
  - nt-2015-003-v194
  - nt2019-001-v1-70-regras-de-valida-o
  - nt-2026-002-v1-00
  - tabela-fcp-uf-2025
created_at: 2025-06-26
updated_at: 2025-06-26
---

# ICMS Próprio — Cálculo Básico

## Visão geral

O ICMS próprio é o imposto devido pelo próprio contribuinte remetente na operação. É calculado "por dentro" (o imposto integra a própria base de cálculo) e incide sobre operações relativas à circulação de mercadorias e serviços de transporte interestadual e intermunicipal.

## Base legal

- LC 87/1996 (Lei Kandir)
- NT 2015.003 — sistemática de cálculo do ICMS interestadual (EC 87/2015)
- NT 2019.001 — regras de validação do ICMS
- NT 2026.002 — alterações para NFC-e e leiaute
- Tabela FCP por UF (tabela-fcp-uf-2025)

## Variáveis

| Variável | Descrição | Fonte |
|----------|-----------|-------|
| `vProd` | Valor do produto/mercadoria | NF-e |
| `vFrete` | Valor do frete | NF-e |
| `vSeg` | Valor do seguro | NF-e |
| `vOutro` | Outras despesas acessórias | NF-e |
| `vIPI` | Valor do IPI (quando integra BC) | NF-e |
| `vDesc` | Valor do desconto condicionado | NF-e |
| `pICMS` | Alíquota do ICMS (%) | Tabela por UF |
| `pRedBC` | Percentual de redução de BC (%) | Legislação UF |

## Fórmula

### Base de Cálculo (BC)

BC = (vProd + vFrete + vSeg + vOutro + vIPI - vDesc) / (1 - pICMS / 100)

### ICMS devido

ICMS = BC × pICMS / 100

### Com redução de base (CST 20)

BC_reduzida = BC × (1 - pRedBC / 100)

ICMS = BC_reduzida × pICMS / 100

### Com FCP (Fundo de Combate à Pobreza)

FCP = BC × pFCP / 100

Total = ICMS + FCP

## Passo a passo

1. Somar valor do produto + frete + seguro + IPI + outras despesas
2. Subtrair descontos condicionados
3. Dividir por (1 - alíquota decimal) para obter a BC
4. Multiplicar BC pela alíquota para obter o ICMS
5. Se houver redução de BC, aplicar o percentual antes do passo 4
6. Se houver FCP, calcular separadamente sobre a mesma BC

## Exemplo

**Dados:** vProd = 1.000,00 | vFrete = 50,00 | vSeg = 10,00 | vIPI = 0 | vDesc = 0 | pICMS = 18%

BC = (1000 + 50 + 10 + 0 - 0) / (1 - 0,18) = 1060 / 0,82 = 1.292,68

ICMS = 1.292,68 × 0,18 = 232,68

**Comprovação:** O valor do ICMS embutido na BC é exatamente o calculado:
BC - ICMS = 1.292,68 - 232,68 = 1.060,00 (valor original sem ICMS)

## Observações

- **CST 00** — ICMS próprio integral (sem redução)
- **CST 20** — ICMS próprio com redução de BC (benefício fiscal)
- **CST 40** — Isento (ICMS = 0)
- **CST 41** — Não tributado (ICMS = 0)
- **CST 51** — Diferimento parcial (recolhimento postecipado)
- **CST 60** — ICMS cobrado anteriormente por ST
- Alíquotas interestaduais: 12% (operações Sul/Sudeste → Sul/Sudeste), 7% (Sul/Sudeste → Norte/Nordeste/CO), 4% (operações com importados)
- IPI integra a BC do ICMS (exceto quando a operação for entre contribuintes e destinada a industrialização/comercialização)
- FCP varia por UF — tabela completa em `corpus/geral/tabelas-federais/tabela-fcp-uf-2025/`
