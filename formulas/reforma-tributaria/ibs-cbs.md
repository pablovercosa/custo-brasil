---
slug: ibs-cbs
title: IBS e CBS — Reforma Tributária
type: formula
tax: reforma-tributaria
regime: ibs-cbs
status: published
sources:
  - nt-2025-002-v1-50-rtc-nf-e-ibs-cbs-is
  - aliquotas-cbs-2026
  - cclass-trib-2026
  - it-2026-002-v-1-00-tabela-de-aliquotas-da-cbs
  - it-2026-001-v-1-00-tabelas-de-meios-de-pagamento-para-vincula-o-com-o-split
  - ccredpres-2025
created_at: 2025-06-26
updated_at: 2025-06-26
---

# IBS e CBS — Reforma Tributária

## Visão geral

A Reforma Tributária (EC 132/2023) institui o IBS (Imposto sobre Bens e Serviços — estadual/municipal) e a CBS (Contribuição sobre Bens e Serviços — federal), que substituirão respectivamente ICMS/ISS e PIS/COFINS/IPI. O modelo é de IVA dual não cumulativo, com crédito financeiro (não cumulativo amplo) e split payment como mecanismo de arrecadação.

## Base legal

- EC 132/2023
- NT 2025.002 — RTC NF-e IBS/CBS/IS (leiaute e regras)
- IT 2025.002 — tabelas de classificação tributária do IBS e da CBS
- IT 2026.002 — tabela de alíquotas da CBS
- IT 2026.001 — meios de pagamento vinculados ao split
- Tabela de alíquotas CBS 2026 (`aliquotas-cbs-2026`)
- Tabela cClassTrib 2026 (`cclass-trib-2026`)

## Variáveis

| Variável | Descrição | Fonte NT 2025.002 |
|----------|-----------|-------------------|
| `vProd` | Valor do produto | NF-e |
| `vServ` | Valor do serviço | NF-e |
| `vFrete` | Valor do frete | NF-e |
| `vSeg` | Valor do seguro | NF-e |
| `vOutro` | Outras despesas | NF-e |
| `vII` | Valor do Imposto de Importação | NF-e |
| `vDesc` | Valor do desconto condicionado | NF-e |
| `vPIS` | Valor do PIS (excluído da BC) | NF-e |
| `vCOFINS` | Valor da COFINS (excluído da BC) | NF-e |
| `vICMS` | Valor do ICMS (excluído da BC) | NF-e |
| `pIBS` | Alíquota do IBS | Tabela |
| `pCBS` | Alíquota da CBS | Tabela |

## Fórmula

### Base de Cálculo do IBS/CBS (conforme NT 2025.002)

BC_IBS_CBS = vProd + vServ + vFrete + vSeg + vOutro + vII - vDesc - vPIS - vCOFINS - vICMS

**Atenção:** PIS-ST e COFINS-ST não são excluídos quando compõem o valor total da NF-e.

### IBS devido

IBS = BC_IBS_CBS × pIBS / 100

### CBS devido

CBS = BC_IBS_CBS × pCBS / 100

### Total

Total_IBS_CBS = IBS + CBS

## Passo a passo

1. **Calcular a base comum:** partindo do valor total da operação, somar produto, serviço, frete, seguro, outras despesas e II
2. **Excluir da base:** descontos incondicionais, PIS, COFINS e ICMS
3. **Aplicar alíquotas:** multiplicar a BC pelas alíquotas de IBS e CBS
4. **Apurar créditos:** o contribuinte pode creditar o IBS e a CBS pagos nas aquisições
5. **Split payment:** no pagamento, o valor do IBS+CBS é segregado e recolhido diretamente ao fisco

## Exemplo

**Dados:**

| Componente | Valor |
|------------|-------|
| vProd | 1.000,00 |
| vFrete | 50,00 |
| vSeg | 10,00 |
| vOutro | 20,00 |
| vII | 0,00 |
| vDesc | 30,00 |
| vPIS | 16,50 |
| vCOFINS | 76,00 |
| vICMS | 180,00 |

Alíquotas (valores hipotéticos): pIBS = 26,5%, pCBS = 9,0%

### BC

BC = 1000 + 50 + 10 + 20 + 0 - 30 - 16,50 - 76,00 - 180,00 = 777,50

### IBS e CBS

IBS = 777,50 × 0,265 = 206,04

CBS = 777,50 × 0,090 = 69,98

Total = 276,02

### Split payment

O pagador deve segregar os 276,02 do valor total para recolhimento ao fisco.
O fornecedor recebe o valor líquido da operação na forma definida pela IT 2026.001.

## Crédito financeiro (não cumulativo amplo)

Diferentemente do PIS/COFINS não cumulativo atual, o IBS e a CBS permitem crédito sobre **todas as aquisições** de bens e serviços, exceto aquisições para uso ou consumo pessoal.

Credito_IBS = vAquisicao × pIBS / 100

Credito_CBS = vAquisicao × pCBS / 100

### Apropriação

- Crédito apropriado mensalmente
- Sem vedação setorial (todos os contribuintes)
- Crédito financeiro (não vinculado à saída tributada)
- Estornos para aquisições de bens do ativo imobilizado (rateio em 48 meses)

## Split payment

O split payment é o mecanismo de pagamento em que o valor do tributo é separado no momento da transação financeira e recolhido diretamente ao fisco, sem passar pelo caixa do fornecedor.

### Fluxo (IT 2026.001)

1. Comprador efetua o pagamento
2. Instituição financeira split:
   a. Parte líquida → conta do fornecedor
   b. IBS + CBS → conta do fisco
3. Meios de pagamento vinculados conforme tabela IT 2026.001

### Implicações

- O fornecedor não recebe o valor do tributo — elimina a inadimplência fiscal
- O comprador tem o débito liquidado no ato do pagamento
- O split é obrigatório para meios de pagamento eletrônicos vinculados

## Classificação Tributária (cClassTrib)

A classificação tributária do IBS e da CBS é definida pela tabela cClassTrib (2026), que atribui CST de IBS e CBS a cada NCM:

| Campo | Descrição |
|-------|-----------|
| `cClassTrib` | Código de classificação tributária |
| `cstIBS` | CST do IBS |
| `cstCBS` | CST da CBS |
| `credPres` | Crédito presumido aplicável |

Consulte `corpus/geral/tabelas-federais/cclass-trib-2026/` para a tabela completa (1.157 registros).

## Observações

- **Alíquotas de referência:** IBS — entre 25% e 27% (estimado); CBS — entre 8% e 10% (IT 2026.002)
- **Seletividade:** Bens e serviços podem ter alíquotas reduzidas (regimes específicos)
- **Cesta básica:** alíquota zero ou reduzida para itens selecionados
- **Zona Franca de Manaus:** mantém diferencial competitivo (crédito presumido)
- **Serviços financeiros, seguros, planos de saúde:** regimes específicos
- **IS (Imposto Seletivo):** tributo extra sobre bens prejudiciais à saúde/meio ambiente
- A NT 2025.002 define que o PIS-ST e COFINS-ST **não** são excluídos da BC quando compõem o valor total
- O split payment não se aplica a pagamentos em espécie ou não vinculados
- O ICMS integra a BC do IBS/CBS (não é excluído por ser imposto não cumulativo)
