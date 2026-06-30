---
slug: imposto-seletivo
title: Imposto Seletivo (IS)
type: formula
tax: reforma-tributaria
regime: is
status: published
sources:
  - nt-2025-002-v1-40-rtc-nf-e-ibs-cbs-is-final
  - nt-2025-002-v1-50-rtc-nf-e-ibs-cbs-is
created_at: 2025-06-26
updated_at: 2025-06-26
---

## Metadados

### Fontes normativas
- [nt-2025-002-v1-40-rtc-nf-e-ibs-cbs-is-final](corpus/reforma-tributaria/notas-tecnicas/nt-2025-002-v1-40-rtc-nf-e-ibs-cbs-is-final/document.md)
- [nt-2025-002-v1-50-rtc-nf-e-ibs-cbs-is](corpus/reforma-tributaria/notas-tecnicas/nt-2025-002-v1-50-rtc-nf-e-ibs-cbs-is/document.md)

### Fontes normativas
- [nt-2025-002-v1-40-rtc-nf-e-ibs-cbs-is-final](corpus/reforma-tributaria/notas-tecnicas/nt-2025-002-v1-40-rtc-nf-e-ibs-cbs-is-final/document.md)
- [nt-2025-002-v1-50-rtc-nf-e-ibs-cbs-is](corpus/reforma-tributaria/notas-tecnicas/nt-2025-002-v1-50-rtc-nf-e-ibs-cbs-is/document.md)

# Imposto Seletivo (IS)

## Visão geral

O Imposto Seletivo (IS) é um tributo federal instituído pela Reforma Tributária (EC 132/2023) que incidirá sobre bens e serviços prejudiciais à saúde ou ao meio ambiente. É um imposto extrafiscal, não cumulativo, que será apurado na NF-e/NFC-e a partir da implementação da Reforma.

## Base legal

- EC 132/2023
- [NT 2025.002](../../corpus/reforma-tributaria/notas-tecnicas/nt-2025-002-v1-36-rtc-nf-e-ibs-cbs-is/document.md) — leiaute do IS na NF-e/NFC-e

## Variáveis

| Variável | Descrição |
|----------|-----------|
| `vBC` | Base de cálculo do IS |
| `pIS` | Alíquota percentual do IS (%) |
| `qtd` | Quantidade tributada |
| `pISEspec` | Alíquota específica (R$/unidade) |

## Fórmula

### Alíquota percentual

vIS = vBC × pIS / 100

### Alíquota percentual + específica (combinada)

vIS = vBC × pIS / 100 + qtd × pISEspec / 100

## Passo a passo

1. Identificar se o produto/serviço está sujeito ao IS (tabaco, bebidas alcoólicas, etc.)
2. Determinar a base de cálculo (valor da operação)
3. Se aplicável, determinar a quantidade para alíquota específica
4. Aplicar a(s) alíquota(s) para obter o valor do IS

## Exemplo

**Dados:** vBC = 1.000,00 | pIS = 10% | qtd = 100 | pISEspec = 0,50

vIS = 1.000 × 0,10 + 100 × 0,50 / 100 = 100,00 + 0,50 = 100,50

**Apenas percentual:** vIS = 1.000 × 0,10 = 100,00

## Quando utilizar

### Produtos/serviços sujeitos

- Tabaco e derivados
- Bebidas alcoólicas
- Produtos prejudiciais à saúde (lista a definir em lei complementar)
- Produtos prejudiciais ao meio ambiente (lista a definir)
- **Não** incidirá sobre: exportações, bens da cesta básica, energia elétrica, telecomunicações (definido na EC 132)

### Perfil do contribuinte

- Fabricante, importador ou distribuidor dos bens sujeitos
- Apuração na NF-e/NFC-e junto com IBS e CBS

### Não utilizar quando

- Bem/serviço não listado na legislação do IS
- Exportação (imune)
- IBS, CBS, ICMS, IPI — tributos distintos, com BC e cálculos próprios

## Observações

- O IS substituirá o IPI sobre produtos industrializados selecionados (tabaco, bebidas)
- O IS **não é cumulativo**: creditamento nas aquisições (a definir em regulamentação)
- A alíquota máxima será definida por lei complementar (estimativa: até 20% para produtos selecionados)
- O IS incide mesmo sobre produtos sujeitos a IBS e CBS — são cumulativos
- A arrecadação do IS será federal (não partilhada com estados/municípios)
- O IS integra a BC do IBS e da CBS na forma definida pela [NT 2025.002](../../corpus/reforma-tributaria/notas-tecnicas/nt-2025-002-v1-36-rtc-nf-e-ibs-cbs-is/document.md)
- **Período de transição:** o IS começa a valer integralmente com o novo regime (2027-2033)
