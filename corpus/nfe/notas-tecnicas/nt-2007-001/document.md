---
title: "Projeto Nota Fiscal Eletrônica"
slug: "nt-2007-001"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "4a5311f7303ad509a7897fca97cb66e416d13cd7462cb210753ff3bbb30ded90"
converted_at_utc: "2026-06-25T14:55:03.434282+00:00"
status: "published"
type: "nota_tecnica"
---

## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt-2007-001/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt-2007-001/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt-2007-001.md)
- [Proveniência resumida](../../../../sources/provenance/nt-2007-001.json)

## Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_97910a2ce66ea579edb2095fcc2104258c19c0419a7635c2ecaeed8025a08ccf.png)

## Nota Técnica 2007.001

Divulga PL\_005a\_hom\_v0.01 - Pacote de Liberação de Schemas 005a - Ambiente de Homologação - versão 0.01

![Image](assets/image_000002_245aadd9f41c69d821384747d8934c7eed19b4d04c264df5ad5503dae537983a.png)

Agosto-2007

![Image](assets/image_000003_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

## 1.  Resumo

Divulga o Pacote de Liberação 005a do Ambiente de Homologação - PL\_005a\_Hom\_v0.01, com os Schemas XML compatíveis com os leiautes de arquivos do Manual de Integração do Contribuinte - versão 2.0.2.

O  PL\_005b\_Hom\_v0.01  substitui  a  versão  preliminar  do  Pacote  de  Liberação  005a (PL\_005a\_draft\_v0.02.zip) divulgada anteriormente.

Este Pacote de liberação destina-se ao uso exclusivo no ambiente de homologação da NF-e e deverá ser substituído pela versão defintiva do ambiente de produção que será divulgado oportunamente.

## 2.  Identificação e vigência do PL\_005a\_hom\_v0.01

| Versão do Manual de Integração do Contribuinte   | 2.02              |
|--------------------------------------------------|-------------------|
| Versão do Pacote de liberação de Schemas XML     | PL_005a_Hom_v0.01 |
| Data de início da vigência                       | 01/09/2007        |
| Data de termino da vigência                      | 31/09/2007        |
| Para utilização no Ambiente                      | Homologação       |

![Image](assets/image_000004_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

## 3.  Atualizações ocorridas

## 3.1 Correção da expressão regular

## 3.1.1  TDec\_0804

## Alterado de:

&lt; xs:pattern value ="0|0\.[0-9]{3}|[1-9]{1}[0-9]{0,7}(\.[0-9]{4})?" /&gt;

## para:

```
< xs:pattern value ="0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,7}(\.[0-9]{4})?" />
```

## 3.1.2  TDec\_1204

## Alterado de:

&lt; xs:pattern value ="0|0\.[0-9]{3}|[1-9]{1}[0-9]{0,7}(\.[0-9]{4})?" /&gt; para: &lt; xs:pattern value ="0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,11}(\.[0-9]{4})?" /&gt;

## 3.2 Otimização da expressão regular

## 3.2.1  TDec\_0302Opc

## Alterado de:

```
< xs:pattern value ="0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[1-9]{1}|0\.[19]{1}[0-9]{1}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?" />
```

## para:

```
< xs:pattern value ="0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[09]{0,2}(\.[0-9]{2})?" />
```

## 3.2.1  TDec\_1302Opc

## Alterado de:

```
< xs:pattern value ="0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[1-9]{1}|0\.[1-9]{1}[09]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?" />
```

## para:

![Image](assets/image_000005_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

<!-- formula-not-decoded -->

## 3.3 Validação de datas

Adoção  da  expressão  regular  "\d{4}-\d{2}-\d{2}"  para  impedir  a  possibilidade  de informar o TIME ZONE nos campos data, que aceitava como datas válidas: "200708-13-03:00", "2007-08-13+03:00","2007-8013-Z", etc.

## 3.4 Correção do Schema cadEmiDFe\_v1.01.xsd

Correção do erro de referência no " include " existente no Schema cadEmiDFe\_v1.01.xsd.

## Alterado de:

- &lt; xs:include schemaLocation =" LeiauteCadastroEmissorNFe\_v1.01.xsd " /&gt;

## para:

- &lt; xs:include schemaLocation =" LeiauteCadastroEmissorDFe\_v1.01.xsd " /&gt;

As  dúvidas  e  sugestões  devem  ser  encaminhadas  através  do  Canal  Fale  Conosco  da Secretaria  da  Fazenda  de  São  Paulo  (http://www.fazenda.sp.gov.br/email/default2.asp) referente à 'Nota Fiscal eletrônica'.

## Documentos relacionados
_Nenhum documento relacionado conhecido._
