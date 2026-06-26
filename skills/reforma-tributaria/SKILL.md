---
name: reforma-tributaria
description: Consulta especializada sobre IBS/CBS usando os documentos dedicados da Reforma Tributária do Consumo no corpus.
---

# Skill: Reforma Tributária (IBS/CBS)

Use esta skill para consultas sobre o novo sistema tributário do consumo: IBS (Imposto sobre Bens e Serviços), CBS (Contribuição sobre Bens e Serviços), split payment, período de transição, alíquotas e classificações.

## Documentos-base

### Notas Técnicas
Localizadas em `corpus/reforma-tributaria/notas-tecnicas/`:
- `nt-2025-002-v1-36-rtc-nf-e-ibs-cbs-is` — RTC versão inicial
- `nt-2025-002-v1-40-rtc-nf-e-ibs-cbs-is-final` — RTC versão final
- `nt-2025-002-v1-50-rtc-nf-e-ibs-cbs-is` — RTC versão atual

### Informes Técnicos
Localizados em `corpus/reforma-tributaria/informes-tecnicos/`:
- `it-2025-002-v-1-50-tabelas-de-classifica-o-do-ibs-e-da-cbs` — classificação IBS/CBS
- `it-2025-004-v-1-10-tabela-de-ind-ce-de-mistura-de-biocombsut-vel` — índice de mistura
- `it-2026-001-v-1-00-tabelas-de-meios-de-pagamento-para-vincula-o-com-o-split` — split payment
- `it-2026-002-v-1-00-tabela-de-aliquotas-da-cbs` — alíquotas CBS

### Tabelas auxiliares
- `corpus/geral/tabelas-federais/aliquotas-cbs-2026/` — alíquotas da CBS

### Fórmulas de cálculo
- `formulas/reforma-tributaria/ibs-cbs.md` — demonstração do cálculo de IBS e CBS, crédito financeiro, split payment e exclusões da BC

### Schemas
- `corpus/reforma-tributaria/schema/PL_IBS_001/` — schemas XML IBS/CBS

## Passos

1. **Consulte primeiramente a categoria `reforma-tributaria/`** para questões sobre IBS, CBS, split payment, transição e alíquotas.

2. **Diferencie regime anterior do novo regime** — Indique se a resposta se refere ao regime anterior (PIS/COFINS, ICMS/IPI) ou ao novo regime (IBS/CBS). Use as NTs de adequação (`nt-2025-002-v1-*`) para verificar o impacto nos leiautes NF-e/NFC-e.

3. **Consulte o changelog** em `changelog/reforma-tributaria/notas-tecnicas/{slug}.md` para rastrear a evolução dos documentos. A reforma está em andamento — o changelog registra as atualizações.

4. **Não invente cenários de transição** — O corpus documenta regras publicadas. Se o período de transição ou alíquota não estiver documentado, informe que não há evidência no corpus.

## Saída

Resposta objetiva sobre IBS/CBS, slug(s) do(s) documento(s)-fonte, path, vigência documentada e relação com NF-e/NFC-e.

## Procedência

Consulte `agents/CORPUS.md` para navegação. A categoria `reforma-tributaria/` contém exclusivamente documentos do novo regime. Consulte também o agent `especialista-reforma-tributaria` para consultas aprofundadas.
