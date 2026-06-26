# Fórmulas — Custo Brasil

Fórmulas para cálculo tributário referenciadas aos documentos normativos do corpus.

## Estrutura

```
formulas/
├── icms/               # ICMS próprio, ST, DIFAL, FCP
├── pis-cofins/         # PIS/COFINS cumulativo e não cumulativo
├── reforma-tributaria/ # IBS, CBS, split payment
├── ipi/                # IPI (reservado)
└── iss/                # ISS (reservado)
```

## Convenções

Cada fórmula segue o padrão:

- **Front matter** com slug, tipo (`type: formula`), imposto (`tax`), regime (`regime`), fontes (`sources`) referenciando slugs do corpus
- **Visão geral** — contexto e finalidade do cálculo
- **Base legal** — referências aos documentos do corpus que fundamentam a fórmula
- **Variáveis** — definição de cada entrada
- **Fórmula** — expressão matemática literal
- **Passo a passo** — sequência didática do cálculo
- **Exemplo** — aplicação numérica com valores hipotéticos
- **Observações** — diferenças por UF, CST, regime ou caso concreto

## Relação com o corpus

As fórmulas são **derivadas** dos documentos normativos em `corpus/`. A procedência de cada regra é indicada pelo campo `sources` no front matter, que referencia slugs de documentos do corpus. Consulte o corpus para o texto original das normas.

## Regimes especiais

Cada imposto pode ter regimes distintos (normal, ST, monofásico, cumulativo, não cumulativo, etc.). As fórmulas indicam claramente a qual regime se aplicam.

> **Aviso**: Fórmulas são referência didática. Consulte a legislação vigente e profissional habilitado para cálculos reais. Alíquotas variam por UF, produto e regime.
