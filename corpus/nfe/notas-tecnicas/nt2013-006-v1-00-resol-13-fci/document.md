---
title: "Projeto Nota Fiscal Eletrônica"
slug: "nt2013-006-v1-00-resol-13-fci"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "04f5a42d407e2d57c0849cb415bd2c7bd4b7924c3d6bbb45eddcd7025dd40603"
converted_at_utc: "2026-06-25T15:05:00.372583+00:00"
status: "published"
type: "nota_tecnica"
---
![Image](assets/image_000000_03ca96dd47c3c944f1e1f5e8116e5ec97276920c675b8587f83e37ae1cc6fe3d.png)

## Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_df37584501db1e2d572aa7cd124869e13d49c06f95b799842321a9653c09fd5d.png)

## Nota Técnica 2013/006

Operação Interestadual com Bens e Mercadorias Importados do Exterior FCI - Ficha de Conteúdo de Importação

![Image](assets/image_000002_7aa553379f4b5a52e53c90bb7d9a85dbce18ed1b0edabb151134cd45445e6c7a.png)

Versão 1.00 Agosto 2013

![Image](assets/image_000003_e63d153f4044bbd2e0101d9137a654d625b5e415bf65076f5fd9b88408e44d37.png)

## 01. Resumo

A  Resolução  13/2012  do  Senado  Federal  teve  sua  impl ementação  regulamentada  inicialmente pelo Ajuste SINIEF 19/2012 e pelo Ajuste SINIEF 20/2012, editados pelo CONFAZ - Conselho Nacional de Política Fazendária. O Ajuste 19/2012 f oi revogado e a regulamentação sobre este assunto passou a constar no Convênio ICMS 38/2013.  Tratam deste assunto também o Ajuste SINIEF 15/2013 e o Convênio ICMS 88/2013, recém pub licados.

A repercussão destas legislações sobre a NF-e foram tratadas inicialmente nas NT 2012.005 e NT 2013.004.

Esta NT documenta as adaptações no leiaute necessár ias para registrar a informação do Número da FCI, conforme previsto na legislação e outras mu danças.

Prazo previsto para entrada em vigência das alteraç ões:

- Ambiente de Homologação (ambiente de teste das empresas): 06/08/13;
- Ambiente de Produção : 12/08/13.

NT 2013.006

![Image](assets/image_000004_2d8ba4a4bb35b0b9587e2692787836c05885f28cee691cee5bc2795c0ee9bde7.png)

## 02. Leiaute da NF-e (Anexo I do Manual do Contribuinte)

## 02.1 Informação da FCI

Incluído campo de controle relacionado com a Resolu ção 13 do Senado Federal, Convênio ICMS 38/2013 e s uas alterações. A informação do Número da  FCI  passará  a  ser  obrigatória  nas  operações  interestaduais,  conforme  a  Origem  da  Mercadoria  (3,  5  ou  8),  a  partir  de  01/10/2013,  conforme legislação atual.

| #    | ID   | Campo   | Descrição                                                   | Ele   | Pai   | Tipo   | Ocor.   |   Tam. | Observação                                                                                                                                                                                 |
|------|------|---------|-------------------------------------------------------------|-------|-------|--------|---------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 128p | I70  | nFCI    | Número de controle da FCI - Ficha de Conteúdo de Importação | E     | I01   | C      | 0-1     |     36 | Informação relacionada com a Resoluç ão 13/2012 do Senado Federal. Formato: Algarismos, letras maiúscu las de "A" a "F" e o caractere hífen. Exemplo: B01F70AF-10BF-4B1F-848C-65FF57F616FE |

## Observação sobre o Número da FCI:

O número de controle da FCI é gerado por uma função  padrão de geração de números aleatórios e únicos ( veja padrão técnico relacionado com "GUID - Globally Unique IDentifier"). Este padrão a caba gerando uma sequência de 36 caracteres, conten do algarismos, letras maiúsculas de "A" a "F" e o caractere de hífen. Os exemplos abaixo repr esentam códigos de FCI possíveis:

B01F70AF-10BF-4B1F-848C-65FF57F616FE

335905D3-83B2-4DD6-9EA9-6CEF3DF894FA

Para o campo do número de controle da FCI, o Schema  XML irá verificar a formatação do campo (presença dos "hifens" nos locais indicados) e aceitar unicamente os caracteres citados.

## 02.2 Campo Origem da Mercadoria

Os diferentes grupos de tributação do ICMS contém a informação de "Origem" da mercadoria. Com a edição  do Ajuste SINIEF 02/2013, as origens 6 e 7, passam agora a considerar também o gás natural i mportado. Com a edição do Ajuste SINIEF 15/2013, as  origens 0 e 3 sofreram alterações, além da inclusão da origem 8.

O detalhamento abaixo descreve a mudança dos valores do campo 'orig' para o grupo de tributação 'ICMS0 0', mas a mesma mudança ocorre para os demais grupos de tributação do ICMS.

![Image](assets/image_000005_cd4dff1897f5a321a1d368ca044fdaaa5d43bd98ae640c3b10f7875e702e956b.png)

|   # | ID   | Campo   | Descrição            | Ele   | Pai   | Tipo   | Ocor.   |   Tam. | Dec. Observação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----|------|---------|----------------------|-------|-------|--------|---------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 166 | N11  | orig    | Origem da mercadoria | E     | N02   | N      | 1-1     |      1 | Origem da mercadoria: 0 - Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8; 1 - Estrangeira - Importação direta, exceto a indicada no código 6; 2 - Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7; 3 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70%; 4 - Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam as legislações citadas nos Ajustes; 5 - Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40%; 6 - Estrangeira - Importação direta, sem similar nacional, constante em lista da CAMEX e gás natural; 7 - Estrangeira - Adquirida no mercado interno, sem similar nacional, constante em lista da CAMEX e gás natural. 8 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70%; |

![Image](assets/image_000006_2d8ba4a4bb35b0b9587e2692787836c05885f28cee691cee5bc2795c0ee9bde7.png)

## 03. Regras de Validação da NF-e (item 4.1.9.4 do Ma nual do Contribuinte)

## 03.1 Informação da FCI

| #     | Campo   | Regra de validação                                                                                                               | Aplic.   |   Msg | Efeito   | Descrição Erro                                   |
|-------|---------|----------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|--------------------------------------------------|
| G1I70 | I70     | Se informado o Número de Controle da FCI (tag:nFCI, id:I42): - Acessar Cadastro de FCI (Chave: nFCI) Nota: Implementação futura. | Facult.  |   465 | Rej.     | Rejeição: Número de Controle da FCI inexistent e |

## 03.2 Operação interestadual com bens e mercadorias  importadas

Eliminada a exceção 2 da validação da alíquota máxi ma nas operações interestaduais com produtos import ados. O motivo desta alteração é porque as operações com gás natural importado, agora devem co nstar como uma nova Origem no grupo de tributação d o ICMS.

| #    | Campo   | Regra de validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Aplic.   | Msg Efeito   | Descrição Erro                                                                                                         |
|------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|--------------|------------------------------------------------------------------------------------------------------------------------|
| GN16 | N16     | CFOP de operação de saída para outra UF (inicia por 6) e - IE do destinatário difere de 'ISENTO' ou nulo; - Origem da mercadoria = 1, 2, 3 ou 8; - CST de ICMS = 00, 10, 20, 70 ou 90; - Data de Emissão igual ou superior a 01/01/2013; - Valor alíquota do ICMS maior do que '4.00' (4 por cento). Exceção 1 : A regra acima não se aplica para as operações de Retorno / Devolução, com os CFOP: 6201, 6202, 6208, 6209, 6210, 6410, 6411, 6412, 6413, 6503, 6553, 6555, 6556, 6660, 6661, 6662, 6664, 6665, 6902, 6903, 6906, 6907, 6909, 6913, 6916, 6918, 6919, 6921, 6925 Exceção 2: A regra de validação acima não se aplica para operação com gás natural importado (cProdANP = 220101003, 220101004, 220101002, 220101001, 220101005 ou 220101006).' Exceção 3: A regra de validação acima não se aplica na venda de veículos novos (grupo 'veicProd'), para a Venda direta para grandes consumidores (tpOp=3), ou para Faturamento direto para consumidor final (tpOp=2). | Facult.  | 663 Rej.     | Rejeição: Alíquota do ICMS com valor superior a 4 por cento na operação de saída interestadual com produtos importados |

![Image](assets/image_000007_cd4dff1897f5a321a1d368ca044fdaaa5d43bd98ae640c3b10f7875e702e956b.png)

## Nota Fiscal eletrônica

| #   | Campo   | Regra de validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Aplic.   | Msg   | Efeito   | Descrição Erro   |
|-----|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|------------------|
|     |         | Exceção 4: Mesmo que informada a IE do destinatário, a regra de validação acima não se aplica para as operações com os CFOP 6107, 6108 (Não Contribuinte). Exceção 5: A regra de validação acima não se aplica para a NF Complementar (finNFe=2) quando: - se referenciada uma NF-e, a NF-e referenciada tem a Data de Emissão anterior a 01/01/13; - se referenciada uma NF modelo 1, a Data de Emissão é anterior a 1301 (tag refNF/AAMM). Exceção 6 : Mesmo que informada a IE do destinatário, a regra de validação acima não se aplica para as operações com o CFOP 6.929 (Lançamento relativo a operação registrada em Cupom Fiscal) |          |       |          |                  |
## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt2013-006-v1-00-resol-13-fci/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt2013-006-v1-00-resol-13-fci/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt2013-006-v1-00-resol-13-fci.md)
- [Proveniência resumida](../../../../sources/provenance/nt2013-006-v1-00-resol-13-fci.json)


## Documentos relacionados

- [[nt2013-004-v1-00-resol-13]]
