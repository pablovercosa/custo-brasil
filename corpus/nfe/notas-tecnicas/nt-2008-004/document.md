---
title: "Projeto Nota Fiscal Eletrônica"
slug: "nt-2008-004"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "ecf7d55133b6c29df329b8f965b105c3e996a3ad037513fd62cfb6b1f68c02bb"
converted_at_utc: "2026-06-25T15:01:34.235671+00:00"
status: "published"
type: "nota_tecnica"
---
![Image](assets/image_000000_fe6be84161521e88755b2fcf6266ac33af92377ba5aa975f460bc794e3ba9dba.png)

## Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_23df8919fce260704a8bc46cec3a6b03e65bf2d92b7a434232ab1120ee9bc7fd.png)

## Nota Técnica 2008/004

## Divulga orientações de preenchimento da NF-e

(emissores do Simples Nacional, faturamento direto de veículos novos, código do município e código do país)

![Image](assets/image_000002_fcdfd12f49ac5b0eaf7228583cf71ad767177b3ec53fbc5d17ada094f0ea74c3.png)

## Maio-2008

![Image](assets/image_000003_03855e49621a60885bf4c39a53011576c07dc6f710dc2994f7e1ba3cb6605fe9.png)

## 1.  Resumo

Divulga orientações para preenchimento da NF-e para as seguintes situações:

- Preenchimento da NF-e emitido por contribuintes do Simples Nacional;
- Preenchimento da NF-e de faturamento direto de veículos novos;
- Código de Município da Tabela do IBGE com dígito verificador inválido;
- Código de País da Tabela do BACEN com dígito verificador inválido;

![Image](assets/image_000004_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

## 2.  Preenchimento de NF-e emitido por contribuintes do Simples Nacional

A NF-e emitida por contribuinte optante pelo Simples Nacional deve observar as normas da Resolução CGSN nº 010, de 28 de junho de 2007 ou alterações posteriores que determina:

- Art.  2º As  ME  e  as  EPP  optantes  pelo  Simples  Nacional  utilizarão,  conforme  as  operações  e prestações  que  realizarem,  os  documentos  fiscais,  inclusive  os  emitidos  por  meio  eletrônico, autorizados pelos entes federativos onde possuírem estabelecimento.
- § 2°  A utilização dos documentos fiscais fica condicionada à inutilização dos campos destinados à base de cálculo e ao imposto destacado, de obrigação própria, sem prejuízo do disposto no art. 11 da Resolução CGSN n°  4, de 30 de maio de 2007, constando, no campo destinado às informações complementares ou, em sua falta, no corpo do documento, por qualquer meio gráfico indelével, as expressões:
- (...)
- I - "DOCUMENTO EMITIDO POR ME OU EPP OPTANTE PELO SIMPLES NACIONAL"; e II - "NÃO GERA DIREITO A CRÉDITO FISCAL DE ICMS, DE ISS E DE IPI".
- § 3°  No caso de documento fiscal emitido por ME ou EPP optante pelo Simples Nacional impedida de recolher o ICMS ou o ISS na forma desse Regime, a expressão a que se refere o inciso II do §2° será a seguinte: "NÃO GERA DIREITO A CRÉDITO FISCAL DE IPI".

As  microempresas  e  empresas  de  pequeno  porte  optantes  pelo  Simples  Nacional  não transferem  créditos  dos  tributos  relativos  a  impostos  ou  contribuições  abrangidos  pelo Simples Nacional, não devendo informar o valor da base de cálculo e nem o valor do tributo próprio no documento fiscal.

Enquanto não existir um CST - Código da Situação Tributária específico para identificar as operações  realizadas  por  contribuinte  do  Simples  Nacional,  sem  prejuízo  dos  demais campos obrigatórios, a NF-e emitida por contribuinte do Simples Nacional deverá obedecer as seguintes recomendações de preenchimento de campos da NF-e:

- a)  campo CST do grupo de tributos de ICMS Normal ou ST - informar o valor '41' (41 - não tributada) para o campo CST nas operações normais

Exemplo de XML de operação normal

<!-- formula-not-decoded -->

- b) campo CST do grupo de tributos de PIS - informar o valor '99' (99- outras operações) para o campo CST;

Exemplo de XML:

&lt;PISOutr&gt; &lt;CST&gt; 99 &lt;/CST&gt; &lt;vBC&gt; 0 &lt;/vBC&gt; &lt;pPIS&gt; 0 &lt;/pPIS&gt; &lt;vPIS&gt; 0 &lt;/vPIS&gt;

![Image](assets/image_000005_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

## &lt;/PISOutr&gt;

- c) campo CST do grupo de tributos de COFINS informar o valor  '99' (99 - outras operações) para o campo CST;

## Exemplo de XML:

&lt;COFINSOutr&gt; &lt;CST&gt; 99 &lt;/CST&gt; &lt;vBC&gt; 0 &lt;/vBC&gt; &lt;pCOFINS&gt; 0 &lt;/pCOFINS&gt; &lt;vCOFINS&gt; 0 &lt;/vCOFINS&gt; &lt;/PISOutr&gt;

## 3.  Preenchimento de NF-e de faturamento direto de veículos novos

A  operação  interestadual  de    faturamento  direto  de  veículos  novos  para  consumidor  é disciplinada pelo Convênio ICMS 51/00, de 15/09/00, que determina a repartição do ICMS devido na operação entre a UF de origem e a UF de destino do veículo. A Base de Cálculo do  ICMS  da  operação  própria  é  obtida  com  a  aplicação  de  um  percentual  no  valor  da operação  em  função  da  UF  de  origem,  UF  destino  e  alíquota  do  IPI  aplicável  para  a operação. O valor do ICMS devido para a UF de destino é a diferença entre o ICMS devido na operação e o ICMS da operação própria.

Importante ressaltar que o ICMS da ST devido na operação não significa um acréscimo no valor  operação, não devendo ser acrescentado ao valor total da NF como ocorre com as demais operações sujeitas ao regime da Substituição Tributária.

Enquanto não existir um CST - Código da Situação Tributária específico para identificar as operações interestaduais de faturamento direto de veículos novos, sem prejuízo dos demais campos obrigatórios,  o preenchimento dos campos da NF-e diretamente relacionados com este tipo de operação devem ser realizado da seguinte forma:

- a)  campo tpOp -  informar o valor '2' (2 - faturamento direto) para o campo tpOp do grupo de detalhamento Específico de Veículos novos;
- b)  campo CST  informar o valor '90' (90 - outros);
- c)  campo modBC - informar com o valor '3' (3 - valor da operação);
- d)  campo vBC - informar o valor obtido com a aplicação de um dos percentuais previstos no parágrafo único da cláusula segunda do Convênio ICMS 51/00 sobre o valor da operação;
- e)  campo vICMS - informar o valor do ICMS calculado de acordo com a legislação aplicável para a operação;
- f) campo modBCST - informar o valor '5' - (5 - pauta);
- g)  campo vBCST - informar o valor da operação;
- h)  campo vICMSST - informar o valor do ICMS ST calculado de acordo com a legislação aplicável para a operação descontado o valor do vICMS (item d) próprio;

![Image](assets/image_000006_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

Exemplo: operação de faturamento direto de fabricante paulista para consumidor mineiro:

Valor Total da NF-e:

38.391,60

Alíquota do ICMS:

12%

Alíquota do IPI:

8%

UF origem:

SP

UF destino:

MG

O percentual de redução BC do ICMS da operação própria aplicável para esta operação é 76,39%, conforme previsto na alínea 'p', item II, parágrafo único da cláusula segunda do Convênio ICMS 51/00.

Assim, temos que:

## ICMS Operação própria:

Valor da Operação (a)

: 38.391,60

Perc.Red. BC do ICMS (b)

: 76,39

Valor da BC do ICMS (c=a x b)  : 29.327,34

Alíquota ICMS (d)

: 12%

Valor do ICMS (e= c x d)

:   3.519,28

## ICMS Substituição Tributária:

Valor da BC do ICMS ST (f=a)

: 38.391,60

Alíquota ICMS  ST (g)

: 12%

Valor do ICMS ST (h = f x g - e) :  1.087,71 (4.606,99 - 3.519,28)

Exemplo de XML:

## &lt;ICMS90&gt;

&lt;/ICMS90&gt;

&lt;orig&gt; 0 &lt;/orig&gt; &lt;CST&gt; 90 &lt;/CST&gt; &lt;modBC&gt; 3 &lt;/modBC&gt; &lt;pRedBC&gt; 76.39 &lt;/pRedBC&gt; &lt;vBC&gt; 29327.34 &lt;/vBC&gt; &lt;pICMS&gt; 12.00 &lt;/pICMS&gt; &lt;vICMS&gt; 3519.28 &lt;/vICMS&gt; &lt;modBCST&gt; 5 &lt;/modBCST&gt; &lt;vBCST&gt; 38391.60 &lt;/vBCST&gt; &lt;pICMSST&gt; 12.00 &lt;/pICMSST&gt; &lt;vICMSST&gt; 1087.71 &lt;/vICMSST&gt;

O  DANFE  deve  ser  impresso  com  as  vias  adicionais  e  as  informações  previstas  na cláusula segunda do Convênio ICMS 51/00.

## 4.  Tratamento de Código de Município do IBGE com DV inválido

![Image](assets/image_000007_cd002d4a3d9b9562448920a96ad92d7bab6ddec6d49d43d6b6ff37829369b32b.png)

O  código  de  Município  do  IBGE  dos  seguintes  Municípios  tem  o  DV  -  dígito  verificador inválido:

- 4305871 - Coronel Barros/RS;
- 2201919 - Bom Princípio do Piauí/PI;
- 2202251 - Canavieira /PI;
- 2201988 - Brejo do Piauí/PI;
- 2611533 - Quixaba/PE;
- 3117836 - Cônego Marinho/MG;
- 3152131 - Ponto Chique/MG;
- 5203939 - Buriti de Goiás/GO;
- 5203962 - Buritinópolis/GO;

As aplicações dos Estados e dos emissores devem utilizar os códigos de município do IBGE sem validação do DV - dígito verificador, da mesma forma como consta da tabela de código de município do IBGE.

## 5.  Tratamento de Código de País do BACEN com DV inválido

O código de País do BACEN dos seguintes países tem o DV - dígito verificador inválido:

- 1504 -GUERNSEY, ILHA DO CANAL (INCLUI ALDERNEY E SARK);
- 1508 -JERSEY, ILHA DO CANAL;
- 4525 -MADEIRA, ILHA DA;
- 3595 -MAN, ILHA DE;
- 4985 -MONTENEGRO;
- 6781 -SAINT KITTS E NEVIS;
- 7370 - SERVIA;

As aplicações dos Estados e dos emissores devem utilizar os códigos de País do BACEN sem validação do DV - dígito verificador, da mesma forma que consta da tabela de código de país do BACEN.
## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt-2008-004/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt-2008-004/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt-2008-004.md)
- [Proveniência resumida](../../../../sources/provenance/nt-2008-004.json)


## Documentos relacionados

- [nota-t-cnica-2008-001-publicada-em-30-11-2010](../nota-t-cnica-2008-001-publicada-em-30-11-2010/document.md)
- [nota-t-cnica-2008-003-publicada-em-30-11-2010](../nota-t-cnica-2008-003-publicada-em-30-11-2010/document.md)
- [nota-t-cnica-2008-005-publicada-em-30-11-2010](../nota-t-cnica-2008-005-publicada-em-30-11-2010/document.md)
- [nt-2008-001](../nt-2008-001/document.md)
- [nt-2008-003](../nt-2008-003/document.md)
- [nt-2008-005](../nt-2008-005/document.md)
- [nt-2008-006](../nt-2008-006/document.md)
- [nt2008-002](../nt2008-002/document.md)
