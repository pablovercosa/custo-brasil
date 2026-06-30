---
title: "Projeto Nota Fiscal Eletrônica"
slug: "nt2013-004-v1-00-resol-13"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "34e61327a81b610242fd2a84b4d4b326d4296b51ebe16f7cabc4d451f27f8c6f"
converted_at_utc: "2026-06-25T15:02:32.731192+00:00"
status: "published"
type: "nota_tecnica"
---
![Image](assets/image_000000_03ca96dd47c3c944f1e1f5e8116e5ec97276920c675b8587f83e37ae1cc6fe3d.png)

## Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_7eea3ade68ab7b2ee4b661cbcba30b7c5727c48c66dfc2f0e2a0dc16fdffdca6.png)

## Nota Técnica 2013/004

Operação Interestadual com Bens e Mercadorias Importados do Exterior

![Image](assets/image_000002_a45770cb4195731552b1c4fa4268aac911afb2f871a503ad8503670bd960e716.png)

Versão 1.00 Maio 2013

![Image](assets/image_000003_e63d153f4044bbd2e0101d9137a654d625b5e415bf65076f5fd9b88408e44d37.png)

## 01. Resumo

A  Resolução  13/2012  do  Senado  Federal  teve  sua  impl ementação  regulamentada  pelo  Ajuste SINIEF 19/2012 e pelo Ajuste SINIEF 20/2012. editados pelo CONFAZ - Conselho Nacional de Política  Fazendária.  A  repercussão  destas  legislaçõ es  sobre  a  NF-e  foram  tratadas  na  NT 2012.005.

Esta NT documenta algumas adaptações necessárias na implementação da regra de validação GN16, com:

- Incluída nova exceção no controle de alíquota: não se aplica a regra para o CFOP 6.929 (Lançamento relativo a operação registrada em Cupom  Fiscal);
- Eliminado o controle da Data de Emissão para a exc eção nas operações de Devolução / Retorno;

Prazo previsto para entrada em vigência das alteraç ões:

- Ambiente de Homologação (ambiente de teste das empresas): 13/05/13;
- Ambiente de Produção : 20/05/13.

NT 2013.004

![Image](assets/image_000004_e12c07bee3c98e054942b7c2cc4d27d82a3892ff452284edc593c4b885bc3593.png)

## 03. Regras de Validação da NF-e (item 4.1.9.4 do Ma nual)

## 03.1 Operação interestadual com bens e mercadorias  importados

Incluída nova regra de validação, conforme segue:

| #    | Campo   | Regra de validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                                         |
|------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|------------------------------------------------------------------------------------------------------------------------|
| GN16 | N16     | CFOP de operação de saída para outra UF (inicia por 6) e - IE do destinatário difere de 'ISENTO' ou nulo - Origem da mercadoria = 1, 2 ou 3 - CST de ICMS = 00, 10, 20, 70 ou 90 - Data de Emissão igual ou superior a 01/01/2013 - Valor alíquota do ICMS maior do que '4.00' (4 por cento) Exceção 1 : A regra acima não se aplica para as operações de Retorno / Devolução, com os CFOP: 6201, 6202, 6208, 6209, 6210, 6410, 6411, 6412, 6413, 6503, 6553, 6555, 6556, 6660, 6661, 6662, 6664, 6665, 6902, 6903, 6906, 6907, 6909, 6913, 6916, 6918, 6919, 6921, 6925 Exceção 2: A regra de validação acima não se aplica para operação com gás natural importado (cProdANP= 220101003, 220101004, 220101002, 220101001, 220101005 ou 220101006).' Exceção 3: A regra de validação acima não se aplica n a venda de veículos novos (grupo 'veicProd'), para a Venda direta para grandes consumidores (tpOp=3), ou para Faturamento direto para consumidor final (tpOp=2). Exceção 4: Mesmo que informada a IE do destinatário, a regra de validação acima não se aplica para as operações com os CFOP 6107, 6108 (Não Contribuinte). Exceção 5: A regra de validação acima não se aplica para a NF Complementar (finNFe=2) quando: - se referenciada uma NF-e, a NF-e referenciada tem a Data de Emissão anterior a 01/01/13; - se referenciada uma NF modelo 1, a Data de | Facult.  |   663 | Rej.     | Rejeição: Alíquota do ICMS com valor superior a 4 por cento na operação de saída interestadual com produtos importados |

![Image](assets/image_000005_37a85a931684e7b49826067588c5d5e0798b77c8c4f5fc5a1aee142c3ee228f5.png)

| Nota Fiscal eletrônica   |
|--------------------------|

| #   | Campo   | Regra de validação                                                                                                                                                                                                                        | Aplic.   | Msg   | Efeito Descrição Erro   |
|-----|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|-------------------------|
|     |         | Emissão é anterior a 1301 (tag refNF/AAMM). Exceção 6 : Mesmo que informada a IE do destinatário, a regra de validação acima não se aplica para as operações com o CFOP 6.929 (Lançamento relativo a operação registrada em Cupom Fiscal) |          |       |                         |
## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt2013-004-v1-00-resol-13/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt2013-004-v1-00-resol-13/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt2013-004-v1-00-resol-13.md)
- [Proveniência resumida](../../../../sources/provenance/nt2013-004-v1-00-resol-13.json)


## Documentos relacionados

- [nt2013-006-v1-00-resol-13-fci](../nt2013-006-v1-00-resol-13-fci/document.md)
