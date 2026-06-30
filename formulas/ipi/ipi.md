---
slug: ipi
title: IPI — Cálculo Básico
type: formula
tax: ipi
regime: normal
status: published
sources:
  - nt2020-002v-1-01-espec-fica-para-ipi
created_at: 2025-06-26
updated_at: 2025-06-26
---

## Metadados

### Fontes normativas
- [nt2020-002v-1-01-espec-fica-para-ipi](corpus/nfe/notas-tecnicas/nt2020-002v-1-01-espec-fica-para-ipi/document.md)

### Fontes normativas
- [nt2020-002v-1-01-espec-fica-para-ipi](corpus/nfe/notas-tecnicas/nt2020-002v-1-01-espec-fica-para-ipi/document.md)

# IPI — Cálculo Básico

## Visão geral

O IPI (Imposto sobre Produtos Industrializados) é um imposto federal não cumulativo que incide sobre produtos industrializados. O cálculo pode ser por **alíquota percentual** (sobre o valor do produto) ou por **valor fixo por unidade** (ad rem).

## Base legal

- Decreto 7.212/2010 (RIPI)
- [NT 2020.002](../../corpus/nfe/notas-tecnicas/nt2020-002v-1-01-espec-fica-para-ipi/document.md) — especificações para IPI
- Tabela de Incidência do IPI (TIPI)

## Variáveis

| Variável | Descrição |
|----------|-----------|
| `vBC` | Base de cálculo (valor do produto + encargos) |
| `pIPI` | Alíquota percentual (%) |
| `qtd` | Quantidade de produto |
| `vIPI_und` | Valor do IPI por unidade |

## Fórmula

### Por alíquota percentual

IPI = vBC × pIPI / 100

### Por valor por unidade (ad rem)

IPI = qtd × vIPI_und

## Quando utilizar

### CST aplicáveis

| CST | Descrição | Aplica? |
|-----|-----------|:-------:|
| 00 | Entrada tributada | Sim |
| 01 | Entrada tributada alíq. zero | Sim (IPI = 0) |
| 02 | Entrada isenta | Sim (IPI = 0) |
| 03 | Entrada não tributada | Sim (IPI = 0) |
| 04 | Entrada imune | Sim (IPI = 0) |
| 05 | Entrada com suspensão | Sim (IPI = 0) |
| 49 | Outras entradas | Sim (IPI = 0) |
| 50 | Saída tributada | Sim |
| 51 | Saída tributada alíq. zero | Sim (IPI = 0) |
| 52 | Saída isenta | Sim (IPI = 0) |
| 53 | Saída não tributada | Sim (IPI = 0) |
| 54 | Saída imune | Sim (IPI = 0) |
| 55 | Saída com suspensão | Sim (IPI = 0) |

### Perfil do contribuinte

- Estabelecimento industrial
- Equiparado a industrial (importador, atacadista em alguns casos)
- Não contribuinte não calcula IPI

### Não utilizar quando

- Produto não industrializado (comércio, serviço puro)
- Importação (contribuinte equiparado, mas cálculo com II incluso na BC)
- Regime monofásico (combustíveis — use `icms-monofasico`)

## Observações

- O IPI é não cumulativo: o contribuinte credita o IPI das aquisições e debita o IPI das saídas
- A BC do IPI inclui: valor do produto + frete + seguro + despesas acessórias + II (se importado)
- O IPI **não** integra a própria BC (diferentemente do ICMS)
- A TIPI segue a Nomenclatura do Mercosul (NCM) com alíquotas variando de 0% a 300%+
- Produtos com alíquota zero: alimentos básicos, medicamentos, livros
- Produtos com alíquota elevada: bebidas alcoólicas, cigarros, perfumes
- O IPI será substituído pela CBS no novo regime tributário (Reforma Tributária)
