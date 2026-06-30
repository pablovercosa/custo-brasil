---
title: "Projeto Nota Fiscal Eletrônica"
slug: "nt2009-004"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "92defecc026b9588f2ec9a482df4d29e5affe1b0e15a63a345945f37688b8b67"
converted_at_utc: "2026-06-25T14:54:25.066514+00:00"
status: "published"
type: "nota_tecnica"
---
![Image](assets/image_000000_57e90876e2337423e28bb28b063080ec75418bab531376f105e9d8a9c42913af.png)

## Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_88c88e94f3f0352c5a0b1a51658cadf8dcb0b765fe215340975da80f6c6450e7.png)

## Nota Técnica 2009/004

Divulga orientações de preenchimento da NF-e (emissores do Simples Nacional) e revoga item 2 da Nota Técnica 2008/004

![Image](assets/image_000002_b2aa8fb73770d8e1890ec927f4b378491bf373e9ab553b55b903a94fa891fc65.png)

Setembro-2009

![Image](assets/image_000003_23b9e09488e621b5bfccc5364d7de95e29e220f6b0cb0acc29d0c4d4d7e6eb00.png)

## Preenchimento de NF-e emitido por contribuinte do Simples Nacional

A NF-e emitida por Microempresa (ME) ou Empresa de Pequeno Porte (EPP) optante pelo Simples Nacional deve observar as disposições da Re solução CGSN nº 10, de 28 de junho de 2007, e alterações posteriores.

Enquanto  não  forem  implementados  códigos  específicos  para  identificar  as  operações realizadas por contribuinte optante pelo Simples Nacional, sem prejuízo dos demais campos obrigatórios,  a  emissão  da  NF-e  por  estabelecimento   de  ME/EPP  optante  pelo  referido regime  deverá  observar,  para  o  preenchimento  dos  ca mpos  do  documento  fiscal,  as recomendações desta Nota Técnica.

Fica revogado o item 2 da Nota Técnica nº 2008/004,  de maio/2008.

![Image](assets/image_000004_a1b06f8c4e41f03c0f4bfa3ebb8cb74c93f6299b1d4e90e27acaf28ff8725c9f.png)

## Recomendações para o preenchimento da NF-e por ME/E PP optante pelo Simples Nacional

## 1) Grupo de tributos de PIS

```
Informar o valor '99' ('outras operações') no campo  CST. Exemplo de XML: <PISOutr> <CST>99</CST> <qBCProd>0.0000</qBCProd> <vAliqProd>0.0000</vAliqProd> <vPIS>0.00</vPIS> </PISOutr>
```

## 2) Grupo de tributos de COFINS

Informar o valor '99' ('outras operações') no campo  CST.

```
Exemplo de XML: <COFINSOutr> <CST>99</CST> <qBCProd>0.0000</qBCProd> <vAliqProd>0.0000</vAliqProd> <vCOFINS>0.00</vCOFINS> </COFINSOutr>
```

- 3) Grupo de tributos de ICMS (Normal ou ST)
2. 3.1) Operações normais
3. 3.1.1) Emissão de NF-e em operação tributada normal mente pelo Simples Nacional e com permissão de crédito de ICMS (art. 2º-A da Resolução CGSN nº 10/2007):

```
3.1.1.1) Informar o valor '41' ('não tributada') no  campo CST. Exemplo de XML de operação normal:
```

```
<ICMS40> <orig>?</orig> (? = informar a origem da mercadoria: 0, 1 ou 2) <CST>41</CST>
```

&lt;/ICMS40&gt;

3.1.1.2) Indicar, no campo de Informações Complemen tares, as expressões:

"DOCUMENTO EMITIDO POR ME OU EPP OPTANTE PELO SIMPLES NACIONAL"; 'NÃO GERA DIREITO A CRÉDITO FISCAL DE IPI.'.

Obs.: Na NF-e relativa à operação não enquadrada em  qualquer das hipóteses previstas no art.  2º-B  da  Resolução  CGSN  nº  10/2007,  além  das  expressões  anteriores  deverá  ser indicada também a expressão: 'PERMITE O APROVEITAMENTO DO CRÉDITO DE ICMS NO VALOR DE R$...; CORRESPONDENTE À ALÍQUOTA DE ...%, NOS TERMOS DO ART. 23 DA LC 123/2006" (devem ser indicados, nos respectivos espaços, o valor do ICMS e a alíquota utilizada no cálculo).

![Image](assets/image_000005_83fd7e68237587cfc868ccbcab27e3a50ce51edd81685653e5b265a99ab5ac67.png)

## 3.1.2) Emissão de NF-e em operação tributada normal mente pelo Simples Nacional e sem permissão de crédito de ICMS (art. 2º-B da Resolução CGSN nº 10/2007):

3.1.2.1) Informar o valor '41' ('não tributada') no  campo CST.

Exemplo de XML de operação normal:

```
<ICMS40>
```

&lt;orig&gt;?&lt;/orig&gt; (? = informar a origem da mercadoria: 0, 1 ou 2) &lt;CST&gt;41&lt;/CST&gt; &lt;/ICMS40&gt; 3.1.2.2) Indicar, no campo de Informações Complemen tares, as expressões: 'DOCUMENTO EMITIDO POR ME OU EPP OPTANTE PELO SIMPLES NACIONAL"; 'NÃO GERA DIREITO A CRÉDITO FISCAL DE IPI.';

## 3.2) Operações com substituição tributária

## 3.2.1) NF-e emitida por contribuinte na condição de  substituto tributário (art. 2º, § 4º, da Resolução CGSN nº 10/2007):

3.2.1.1)  Informar  o  valor  '30'  ('isenta  ou  não  trib utada  e  com  cobrança  do  ICMS  por substituição tributária') no campo CST.

Exemplo de XML de operação com substituição tributária:

```
<ICMS30> <orig>?</orig> (? = informar a origem da mercadoria: 0, 1 ou 2) <CST>30</CST> <modBCST> '?' </modBCST> (? = informar a modalidade) <vBCST>'?' </vBCST> (? = informar o valor) <pICMSST>'?' </pICMSST> (? = informar a alíquota ) <vICMSST>'?' </vICMSST> (? = informar o valor)
```

## &lt;/ICMS30&gt;

3.2.1.2) Indicar, no campo de Informações Complemen tares, as expressões:

"DOCUMENTO EMITIDO POR ME OU EPP OPTANTE PELO SIMPLES NACIONAL"; 'NÃO GERA DIREITO A CRÉDITO FISCAL DE IPI.'.

Obs.: Na NF-e relativa à operação não enquadrada em  qualquer das hipóteses previstas no art.  2º-B  da  Resolução  CGSN  nº  10/2007,  além  das  expressões  anteriores,  deverá  ser indicada também a expressão: 'PERMITE O APROVEITAMENTO DO CRÉDITO DE ICMS NO VALOR DE R$...; CORRESPONDENTE À ALÍQUOTA DE ...%, NOS TERMOS DO ART. 23 DA LC 123/2006" (devem ser indicados, nos respectivos espaços, o valor do ICMS e a alíquota utilizada no cálculo).

## 3.2.2) NF-e emitida por contribuinte substituído ou  nas operações em que o imposto já tenha sido retido anteriormente

- 3.2.2.1) Informar o valor '60' ('ICMS cobrado anteriormente por substituição tributária') no campo CST.

Exemplo de XML de operação com substituição tributária:

```
<ICMS60> <orig>?</orig> (? = informar a origem da mercadoria: 0, 1 ou 2) <CST>60</CST> <vBCST>'?'</vBCST> (? = informar o valor) <vICMSST>'''?'</vICMSST> (? = informar o valor) </ICMS60>
```

![Image](assets/image_000006_5e6493c5a0eb3c00456d5811e8e093c4fa3db3744771f01cb285925a5cac84bf.png)

3.2.2.2) Indicar, no campo de Informações Complemen tares, as expressões: "DOCUMENTO EMITIDO POR ME OU EPP OPTANTE PELO SIMPLES NACIONAL";

'NÃO GERA DIREITO A CRÉDITO FISCAL DE IPI.';

## 3.3) Emissão de NF-e na devolução de mercadorias pa ra contribuinte não optante pelo Simples Nacional (art. 2º, § 5º, da Resolução CGSN nº 10/2007):

3.3.1) Informar o valor '41' ('não tributada') no c ampo CST.

Exemplo de XML de operação normal:

&lt;ICMS40&gt;

&lt;orig&gt;?&lt;/orig&gt; (? = informar a origem da mercadoria: 0, 1 ou 2)

&lt;CST&gt;41&lt;/CST&gt;

&lt;/ICMS40&gt;

3.3.2)  indicar,  no  campo  de  Informações  Complementa res,  a  base  de  cálculo,  o  imposto destacado e o número da Nota Fiscal referente à aqu isição da mercadoria devolvida, além das mensagens:

"DOCUMENTO EMITIDO POR ME OU EPP OPTANTE PELO SIMPLES NACIONAL"; 'NÃO GERA DIREITO A CRÉDITO FISCAL DE IPI.';

## 3.4)  Emissão  de  NF-e  por  estabelecimento  impedido  d e  recolher  o  ICMS  por ultrapassagem do sublimite estadual de receita  (art. 2º, § 2º-A, da Resolução CGSN nº 10/2007):

- 3.4.1) os campos de CST deverão ser preenchidos com o se o emitente não fosse optante pelo Simples Nacional, isto é, com os códigos aplic áveis à operação (00, 10, 20, 30, 40, 41, 50, 51, 60, 70 ou 90, conforme o caso) e o preenchimento dos demais campos pertinentes; 3.4.2) Indicar, no campo de Informações Complementa res, as expressões:
- 'DOCUMENTO EMITIDO POR ME OU EPP OPTANTE PELO SIMPLES NACIONAL";
- "ESTABELECIMENTO IMPEDIDO DE RECOLHER O ICMS/ISS PELO SIMPLES NACIONAL, NOS TERMOS DO § 1º DO ART. 20 DA LC 123/2006";

"NÃO GERA DIREITO A CRÉDITO FISCAL DE IPI".
## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt2009-004/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt2009-004/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt2009-004.md)
- [Proveniência resumida](../../../../sources/provenance/nt2009-004.json)
