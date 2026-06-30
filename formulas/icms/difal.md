---
slug: difal-icms
title: DIFAL ICMS — Diferencial de Alíquotas
type: formula
tax: icms
regime: difal
status: published
sources:
  - nt-2015-001-v-1-30
  - nt-2015-003-v194
created_at: 2025-06-26
updated_at: 2025-06-26
---

## Metadados

### Fontes normativas
- [nt-2015-001-v-1-30](corpus/nfe/notas-tecnicas/nt-2015-001-v-1-30/document.md)
- [nt-2015-003-v194](corpus/nfe/notas-tecnicas/nt-2015-003-v194/document.md)

### Fontes normativas
- [nt-2015-001-v-1-30](corpus/nfe/notas-tecnicas/nt-2015-001-v-1-30/document.md)
- [nt-2015-003-v194](corpus/nfe/notas-tecnicas/nt-2015-003-v194/document.md)

# DIFAL ICMS — Diferencial de Alíquotas

## Visão geral

O DIFAL (Diferencial de Alíquotas do ICMS) é aplicado nas operações interestaduais destinadas a **consumidor final não contribuinte do ICMS** (EC 87/2015). O imposto é calculado com base na alíquota interna do estado de destino, e a diferença entre essa alíquota e a interestadual é partilhada entre os estados de origem e destino.

## Base legal

- EC 87/2015
- Lei Kandir (LC 87/1996)
- [NT 2015.001](../../corpus/nfe/notas-tecnicas/nt-2015-001-v-1-30/document.md) — sistemática de cálculo (base de cálculo única)
- [NT 2015.003](../../corpus/nfe/notas-tecnicas/nt-2015-003-v194/document.md) — exemplos e regras de validação

## Variáveis

| Variável | Descrição |
|----------|-----------|
| `vProd` | Valor do produto/mercadoria |
| `vFrete` | Valor do frete |
| `vSeg` | Valor do seguro |
| `vOutro` | Outras despesas acessórias |
| `vIPI` | Valor do IPI |
| `vDesc` | Valor do desconto |
| `pICMS_inter` | Alíquota interestadual (%) |
| `pICMS_int_dest` | Alíquota interna do destino (%) |

## Fórmula

### Base de Cálculo única (BCU)

BCU = vProd + vFrete + vSeg + vOutro + vIPI - vDesc

**Nota:** A BCU não utiliza o cálculo "por dentro" (ICMS não integra a própria base). É o valor da operação sem inclusão do ICMS.

### ICMS total

ICMS_total = BCU × pICMS_int_dest / 100

### ICMS de origem (interestadual)

ICMS_origem = BCU × pICMS_inter / 100

### DIFAL

DIFAL = ICMS_total - ICMS_origem = BCU × (pICMS_int_dest - pICMS_inter) / 100

### Partilha (a partir de 2019)

Parte_origem = DIFAL × 20%

Parte_destino = DIFAL × 80%

## Passo a passo

1. Calcular a base de cálculo única (soma dos componentes, sem ICMS "por dentro")
2. Aplicar alíquota interna do destino para obter ICMS total
3. Aplicar alíquota interestadual para obter ICMS de origem
4. Subtrair para obter o DIFAL
5. Ratear o DIFAL entre origem (20%) e destino (80%)

## Exemplo

**Dados:** SP → BA, consumidor final não contribuinte
vProd = 1.000,00 | vFrete = 50,00 | vSeg = 10,00 | vIPI = 0 | vDesc = 30,00
pICMS_inter = 12% (SP → BA) | pICMS_int_dest = 18% (BA interna)

BCU = 1.000 + 50 + 10 + 0 - 30 = 1.030,00

ICMS_total = 1.030 × 0,18 = 185,40

ICMS_origem = 1.030 × 0,12 = 123,60

DIFAL = 185,40 - 123,60 = 61,80

Parte_origem (SP) = 61,80 × 0,20 = 12,36

Parte_destino (BA) = 61,80 × 0,80 = 49,44

Total recolhido pelo remetente (SP): 123,60 + 12,36 = 135,96

## Quando utilizar

### Perfil do contribuinte

- Qualquer contribuinte de ICMS que venda para consumidor final em outro estado
- Consumidor final **não contribuinte** (pessoa física ou jurídica sem inscrição estadual)

### Tipo de operação

- Venda interestadual para consumidor final não contribuinte
- Operações com bens e mercadorias em geral
- Vendas online (e-commerce) para consumidores em outros estados

### Não utilizar quando

- Consumidor final é contribuinte de ICMS (aplica ICMS normal interestadual, sem DIFAL)
- Operação interna (dentro do mesmo estado — use `icms-proprio`)
- Operação sujeita a ST (use `icms-st`)
- Venda para contribuinte que vai revender (ICMS normal com crédito)

## Observações

- **Faseamento da partilha (2016-2018):** 2016: 40% origem / 60% destino; 2017: 60% / 40%; 2018: 80% / 20%; 2019+: 20% / 80%
- **Base de cálculo única:** Diferentemente do ICMS próprio, o DIFAL não usa cálculo "por dentro" — a BC é o valor da operação
- **FCP no DIFAL:** Quando o estado de destino tem FCP, calcula-se FCP separadamente sobre a BCU para o destino
- **EC 132/2023 (Reforma Tributária):** O DIFAL será substituído pelo IBS (imposto de destino), que já nasce com a regra de destino como padrão
- Consulte `formulas/icms/aliquotas-icms-uf.md` para alíquotas interestaduais e internas por UF
