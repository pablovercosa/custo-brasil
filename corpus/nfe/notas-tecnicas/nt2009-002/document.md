---
title: "Projeto Nota Fiscal Eletrônica"
slug: "nt2009-002"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "de7589d9978331c31bc81049939ca29c7066db485b6dee35b1bcf3c950eb0390"
converted_at_utc: "2026-06-25T14:51:44.950298+00:00"
status: "published"
type: "nota_tecnica"
---
![Image](assets/image_000000_c4e6daffbc318bd841fc00aef9f87a94e2b919c94e64e8100d060f4f9064a90b.png)

## Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_8c6d67dae777e125552d20592f9f269bfabb4d6a473bc3f8d79bed7b961d132d.png)

## Nota Técnica 2009/002

## Divulga PL\_005d com novos Schemas XML da NF-e

![Image](assets/image_000002_71e682ad71c8bdf6631a003ebf38027126a50b04515f6a03dfbbc58f99bb3dbc.png)

Agosto-2009

![Image](assets/image_000003_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

## 1.  Resumo

Esta  Nota  Técnica  divulga  o  Pacote  de  Liberação  de  Schemas  XML PL\_005d da  NF-e  que contempla os novos CFOPs criados pelo Ajuste SINIEF 05/2009 e a nova tabela de código de País do BACEN.

A  regra  de  validação  da  Inscrição  SUFRAMA  foi  aperf eiçoada  para  aceitar  números  com  8  ou  9 dígitos.

A validação do conteúdo do atributo Id da tag infNFe foi acrescentada como validação de Schema XML para complementar a regra de validação G04, com  esta alteração a informação de caracteres inválidos neste atributo irá gerar uma falha de Sch ema XML.

As  alterações  de  Schema  realizadas  neste  PL  deve  af etar  apenas  os  emissores  que  informam indevidamente  a  literal  'NFE'  ao  invés  da  literal  ' NFe'  no  atributo Id da  tag infNFe nas  UF  que aplicavam a regra de validação G04 de forma incompl eta.

As  Secretarias  de  Fazenda  devem  adotar  o  novo  Pacote  de  Liberação  em  seus  ambientes  de produção até o dia 17/08/2009.

![Image](assets/image_000004_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

## 2. Alteração do leiauteNFe\_v1.10.xsd

- a)  Inclusão dos novos CFOP criados pelo Ajuste SINI EF 05/2009 na tabela de CFOP:
- 5667 -  Venda de combustível ou lubrificante a consumido r ou usuário final estabelecido em outra unidade da Federação
- 7667 - Venda de combustível ou lubrificante a consumido r ou usuário final.
- 6667 -  Venda de combustível ou lubrificante a consumido r ou usuário final estabelecido em outra unidade da Federação diferente da que ocor rer o consumo
- b)  Aperfeiçoamento da validação do atributo Id da t ag infNFe para aceitar conteúdo com o seguinte padrão:

NFe99999999999999999999999999999999999999999999

- c)  Aperfeiçoamento da validação da Inscrição SUFRAM A para aceitar inscrições com 8 ou 9 dígitos.

## 3. Schema tiposBasico\_v1.2.xsd

- a)  Atualização da tabela de países do BCB, disponív el para download em http://www.bcb.gov.br/Rex/TabPaises/Ftp/paises.txt
- Exclusão de código:
3. o 4235 - LEBUAN, ILHAS
- Inclusão de novos códigos:
5. o 7200 - SAO TOME E PRINCIPE, ILHAS
6. o 8958 - ZONA DO CANAL DO PANAMA
7. o 9903 - PROVISAO DE NAVIOS E AERONAVES
8. o 9946 - A DESIGNAR
9. o 9950 - BANCOS CENTRAIS
10. o 9970 - ORGANIZACOES INTERNACIONAIS
## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt2009-002/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt2009-002/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt2009-002.md)
- [Proveniência resumida](../../../../sources/provenance/nt2009-002.json)

## Documentos relacionados
_Nenhum documento relacionado conhecido._
