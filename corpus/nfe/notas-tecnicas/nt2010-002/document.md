---
title: "Projeto Nota Fiscal Eletrônica"
slug: "nt2010-002"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "03b253b56ad95ca676ba04ae2e483447349c7e60ac325ab14d89f51c99742549"
converted_at_utc: "2026-06-25T14:51:28.690644+00:00"
status: "published"
type: "nota_tecnica"
---
![Image](assets/image_000000_83c23eb121948b933e255e5cfa5405d567f44d6beae3a199330cc2dcb5a97816.png)

## Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_7fd0300fa36c9f9d96d8d3df53c89b391b53dd48444f37764066102e244f5bc6.png)

## Nota Técnica 2010/002

Divulga PL\_006e

![Image](assets/image_000002_1e593f5cdf2d8747c2470959c4f4df850e440696b858183ead845d8cfd085557.png)

Março-2010

![Image](assets/image_000003_fe32b332ed048f2f15dd582cb0dd5eb7616bda526ad7ce5da40d9a794ed5c66c.png)

## 1.  Resumo

Divulgar PL\_006e com aperfeiçoamento da validação d a tag dhCont .

![Image](assets/image_000004_a686540752ec752543eb3ae688688e8f750fc9dba99cac0e0523a4e36ecbd4ba.png)

## 2. Aperfeiçoamento da validação da tag dhCont

A tag dhCont foi acrescentada na versão 2.0 do leiaute da NF-e  para receber a informação da data e hora de início da contingência.

A tag foi definida como tipo dateTime no Schema XML, contudo o tipo dateTime aceita o preenchimento da tag dhCont com data e hora em formato diverso da definição do  leiaute (AAAA-MM-DDTHH:MM:SS), assim a definição do campo e stá sendo alterada de:

```
<xs:element name="dhCont"> <xs:annotation> <xs:documentation>Informar a data e hora de entrada em contingência c ontingência no formato AAAA-MMDDTHH:MM:SS (v.2.0).</xs:documentation> </xs:annotation> <xs:simpleType> <xs:restriction base="xs:dateTime"/> </xs:simpleType> </xs:element> para: <xs:element name="dhCont"> <xs:annotation> <xs:documentation>Informar a data e hora de entrada em contingência c ontingência no formato AAAA-MMDDTHH:MM:SS (v.2.0).</xs:documentation> </xs:annotation> <xs:simpleType> <xs:restriction base="xs:string"> <xs:whiteSpace value="preserve"/> <xs:pattern value="(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[19])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d"/> </xs:restriction> </xs:simpleType> </xs:element>
```
## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt2010-002/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt2010-002/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt2010-002.md)
- [Proveniência resumida](../../../../sources/provenance/nt2010-002.json)
