---
title: "Projeto Nota Fiscal Eletrônica"
slug: "nt-2008-006"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "ff16e2acbc187662c9b69d31bde9920032fc88b08093375e7cbabc6c3e3583fc"
converted_at_utc: "2026-06-25T15:07:47.894623+00:00"
status: "published"
type: "nota_tecnica"
---
![Image](assets/image_000000_dd2ad4f71d8efb2ebbc167d4a35ac83aefebc704148aab528431cea111f93f29.png)

## Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_23df8919fce260704a8bc46cec3a6b03e65bf2d92b7a434232ab1120ee9bc7fd.png)

## Nota Técnica 2008/006

## Divulga PL\_005b com aperfeiçoamento das regras de validação do Schema XML da Nota Fiscal Eletrônica - NF-e

![Image](assets/image_000002_f4de4a5d7647374820f4d5a247fb5be5c26aac502b9675744a51ef6639c3fbbf.png)

Outubro-2008

![Image](assets/image_000003_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

## 1.  Resumo

A disponibilização de novas modalidades de emissão de Nota Fiscal Eletrônica - NF-e em contingência exigiu a alteração do Schema XML da NF-e para identificar as modalidades de emissão da NF-e possíveis:

1. Emissão Normal;
2. Emissão em contingência com impressão do DANFE em Formulário de Segurança;
3. Emissão  em  contingência  no  Sistema  de  Contingência  do  Ambiente  Nacional  SCAN;
4. Emissão  em  contingência  com  envio  da  Declaração  Prévia  de  Emissão  em Contingência - DPEC;
5. Emissão em contingência com impressão do DANFE em Formulário de Segurança para Impressão de Documento Auxiliar de Documento Fiscal Eletrônico (FS-DA).

Com o objetivo de minimizar o impacto nas aplicações dos contribuintes emissores, optouse por adequar o Schema XML da NF-e sem a criação de uma nova versão do leiaute, até porque a adequação não implicou na criação de novos campos no leiaute vigente da NF-e e nem na alteração de tamanho de campos existentes.

Algumas regras de validação dos campos do Schema XML da NF-e foram aperfeiçoadas para  sanear  as  falhas  de  validação  que  possibilitavam  a  informação  de  conteúdo  em desacordo com as regras previstas no leiaute da NF-e.

Em princípio, as alterações não terão qualquer efeito para os contribuintes emissores de NFe que preenchem a NF-e corretamente, contudo, recomendamos a realização de testes no ambiente de homologação para identificar as eventuais desconformidades no preenchimento da NF-e que serão identificadas com o código de rejeição 225 - Rejeição: Falha no Schema XML da NF-e.

Importante destacar que a regra de preenchimento do campo cProdANP foi  alterada para preenchimento  obrigatório,  pois  foi  identificado  que  muitos  contribuintes  do  segmento  de combustíveis  estavam  omitindo  a  informação  nas  situações  em  que  o  campo  deveria  ser informado.

A implementação do pacote de liberação PL\_005b ocorrerá nos seguintes prazos:

- 03/11/2008 -implementação dos novos schemas XML em ambiente de homologação;
- 15/12/2008 - implementação dos novos schemas XML em ambiente de produção.

![Image](assets/image_000004_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

## 2.  Ampliação do domínio do campo tpEmis

O domínio do campo tpEmis (ID=B22) foi alterado para aceitar os seguintes valores:

- 1 - Normal - emissão normal;
- 2 -  Contingência  FS  -  emissão  em  contingência  com  impressão  do  DANFE  em Formulário de Segurança;
- 3 -  Contingência  SCAN - emissão em contingência no Sistema de Contingência do Ambiente Nacional - SCAN;
- 4 - Contingência DPEC - emissão em contingência com envio da Declaração Prévia de Emissão em Contingência - DPEC;
- 5 -  Contingência  FS-DA  -  emissão  em  contingência  com  impressão  do  DANFE  em Formulário  de  Segurança  para  Impressão  de  Documento  Auxiliar  de  Documento Fiscal Eletrônico (FS-DA).

## 3.  Atualizações das regras de Validação Geral do Schema XML

- Aperfeiçoamento  da  validação  dos  campos  caractere  para  impedir  a  aceitação  de caracteres de espaço no início ou no final do campo (elimina a definição do campo de tipo "token");
- Aperfeiçoamento da validação dos campos data para impedir a aceitação de datas inválidas ou anteriores à 01/01/2000.

## 4.  Atualizações das regras de Validação específicas do Schema XML

- Campo cPais (ID = C14), para aceitar apenas o valor 1058;
- Campo xPais (ID = C15), para aceitar apenas a literal 'BRASIL' ou 'Brasil';
- Campo IE do emitente (ID = C17), para aceitar :
- o algarismos  para  destinatários  contribuintes  do  ICMS,  sem  caracteres  de formatação (ponto, barra, hífen, etc.);
- o literal 'ISENTO' para contribuintes do ICMS que são isentos de inscrição no cadastro de contribuintes do ICMS e estejam emitindo NF-e avulsa;
- Campo IE do destinatário (ID = E17), para aceitar apenas:
- o ausência de conteúdo (&lt;IE&gt;&lt;/IE&gt; ou &lt;IE/&gt;) para destinatários não contribuintes do ICMS;
- o algarismos  para  destinatários  contribuintes  do  ICMS,  sem  caracteres  de formatação (ponto, barra, hífen, etc.);
- o literal 'ISENTO' para destinatários contribuintes do ICMS que são isentos de inscrição no cadastro de contribuintes do ICMS;
- o 'PR9999' a 'PR99999999' para destinatários produtores rurais de MG.
- Campo UF do emitente (ID = C12) para aceitar apenas uma sigla de UF válida;
- Campo UF do fisco emitente (ID = D07) para aceitar apenas uma sigla de UF válida;
- Campo UFDesemb (ID = I22) para aceitar apenas uma sigla de UF válida;
- Campo UFCons (ID = L120) para aceitar apenas uma sigla de UF válida;

![Image](assets/image_000005_b0e3b8d1b89d9fa4554cbbdc288c80ee6decdbcbb6e91113f2a4930255a0363b.png)

- Campo CFOP do  produto  (ID  =  I08)  para  aceitar  apenas  os  CFOP  atualmente vigentes;
- Campo cPais (ID  =  E14)  para  aceitar  apenas  os  código  de  paises  existentes  na tabela do BACEN;
- Campo ISUF - inscrição SUFRAMA do destinatário (ID = E18) para aceitar apenas valores compreendidos na faixa 100000000 a 9999999999;
- Campo RENAVAM (ID=J15) - alterado para aceitar conteúdo alfanumérico;
- Os seguintes campos devem ser informados com pelo menos 2 caracteres:
- o Campo xNome do emitente (ID = C03);
- o Campo xLgr do endereço do emitente (ID = C06);
- o Campo xBairro
- do endereço do emitente (ID = C09);
- o Campo xMun do endereço do emitente (ID = C11);
- o Campo xNome do destinatário (ID = E04);
- o Campo xLgr do endereço do destinatário (ID = E06);
- o Campo xMun do endereço do destinatário (ID = E11);
- o Campo xPais do endereço do destinatário (ID = E15);
- o Campo xLgr do local da retirada (ID = F03);
- o Campo xMun do local da retirada (ID = F08);
- o Campo xLgr do local de entrega (ID = G03);
- o Campo xMun do local de entrega (ID = G08);
- Campo cProdANP (ID=L102)  -  alterado  para  preenchimento  obrigatório  quando  o grupo de informações específicas para combustíveis líquidos ( comb ) for informado. Caso  o  produto  não  seja  regulado  pela  ANP  -  Agência  Nacional  de  Petróleo,  o campo deverá ser preenchido com o literal 999999999.

A alteração do Manual de Integração para registro da implementação será realizada quando publicarmos uma nova versão oficial do Manual de Integração.
## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt-2008-006/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt-2008-006/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt-2008-006.md)
- [Proveniência resumida](../../../../sources/provenance/nt-2008-006.json)


## Documentos relacionados

- [[nota-t-cnica-2008-001-publicada-em-30-11-2010]]
- [[nota-t-cnica-2008-003-publicada-em-30-11-2010]]
- [[nota-t-cnica-2008-005-publicada-em-30-11-2010]]
- [[nt-2008-001]]
- [[nt-2008-003]]
- [[nt-2008-004]]
- [[nt-2008-005]]
- [[nt2008-002]]
