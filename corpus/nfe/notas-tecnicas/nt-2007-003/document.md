---
title: "Projeto Nota Fiscal Eletrônica"
slug: "nt-2007-003"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "0c700a4ecb03e9ddd73544c9c0c5bb1e1645c6c4b3830d9e09806a197c22e8db"
converted_at_utc: "2026-06-25T15:03:39.413591+00:00"
status: "published"
type: "nota_tecnica"
---
![Image](assets/image_000000_dd2ad4f71d8efb2ebbc167d4a35ac83aefebc704148aab528431cea111f93f29.png)

## Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_97910a2ce66ea579edb2095fcc2104258c19c0419a7635c2ecaeed8025a08ccf.png)

## Divulga PL\_005a - Pacote de Liberação de

## Nota Técnica 2007.003 Schemas 005a

![Image](assets/image_000002_92184f8bd39470e2cf03d293f30a766371086dd26fbc979d64245d6a03989d07.png)

Outubro-2007

![Image](assets/image_000003_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

## 1.  Resumo

Divulga a versão definitiva do Pacote de Liberação 005a - PL\_005a, com os Schemas XML compatíveis com os leiautes de arquivos do Manual de Integração do Contribuinte - versão 2.0.2.

- O PL\_005a substitui a versão de homologação do Pacote de Liberação 005a (PL\_005a\_Hom\_v0.02.zip)  divulgada  anteriormente  e  não  exige  qualquer  alteração  nos aplicativos do contribuinte ou da Fazenda.

## 2.  Identificação e vigência do PL\_005a

| Versão do Manual de Integração do Contribuinte   | 2.02                             |
|--------------------------------------------------|----------------------------------|
| Versão do Pacote de liberação de Schemas XML     | PL_005a                          |
| Data de início da vigência                       | 01/11/2007                       |
| Chave de codificação digital MD5 do pacote       | 4b64d637de0a427a3caddc116282d83d |

![Image](assets/image_000004_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

## 3.  Atualizações

## 3.1 Tipo TString para campos alfanuméricos

Foi  identificada  uma  não  conformidade  na  definição  do  tipo TString do  Schema tiposBasico\_v1.02.xsd , utilizado como tipo simples para campos alfanuméricos da NF-e, que impedia a informação de apenas um caractere no campo alfanumérico, que está sendo solucionada com a seguinte alteração na definição do tipo TString :

## Alterado de:

```
<xs:simpleType name="TString"> <xs:annotation> <xs:documentation> Tipo string genérico</xs:documentation> </xs:annotation> <xs:restriction base="xs:string"> <xs:whiteSpace value="preserve"/> <xs:pattern value="[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}"/> </xs:restriction> </xs:simpleType>
```

## para:

```
<xs:simpleType name="TString"> <xs:annotation> <xs:documentation> Tipo string genérico</xs:documentation> </xs:annotation> <xs:restriction base="xs:string"> <xs:whiteSpace value="preserve"/> <xs:pattern value="[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}"/> </xs:restriction> </xs:simpleType>
```

## 3.2 Tipo TAmb para aceitar o valor '1'

Acréscimo do valor '1' (ambiente de produção) na definição do tipo TAmb , para que o pacote de liberação possa ser utilizado no ambiente de produção:

## Alterado de:

```
<xs:simpleType name="TAmb"> <xs:annotation> <xs:documentation>Tipo Ambiente</xs:documentation> </xs:annotation> <xs:restriction base="xs:token">
```

![Image](assets/image_000005_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

## para:

```
<xs:enumeration value="2"/> </xs:restriction> </xs:simpleType> <xs:simpleType name="TAmb"> <xs:annotation> <xs:documentation>Tipo Ambiente</xs:documentation> </xs:annotation> <xs:restriction base="xs:token"> <xs:enumeration value="1"/> <xs:enumeration value="2"/> </xs:restriction> </xs:simpleType>
```

## 3.3 Correção do include do schema retConsStatServ\_v1.07.xsd

Alteração da primeira letra do conteúdo (' LeiauteConsStatServ\_v1.07.xsd' ) do atributo schemaLocation do elemento xs:include para minúscula (' leiauteConsStatServ\_v1.07.xsd' ):

## Alterado de:

## para:

```
<?xml version="1.0" encoding="UTF-8"?> <xs:schema xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns="http://www.portalfiscal.inf.br/nfe" xmlns:xs="http://www.w3.org/2001/XMLSchema" targetNamespace="http://www.portalfiscal.inf.br/nfe" elementFormDefault="qualified" attributeFormDefault="unqualified"> <xs:include schemaLocation="LeiauteConsStatServ_v1.07.xsd"/> <xs:element name="retConsStatServ" type="TRetConsStatServ"> <xs:annotation> <xs:documentation>Schema XML de validação do Resultado da Consulta do Status do Serviço</xs:documentation> </xs:annotation> </xs:element> </xs:schema> <?xml version="1.0" encoding="UTF-8"?> <xs:schema xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns="http://www.portalfiscal.inf.br/nfe" xmlns:xs="http://www.w3.org/2001/XMLSchema"
```

![Image](assets/image_000006_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

```
targetNamespace="http://www.portalfiscal.inf.br/nfe" elementFormDefault="qualified" attributeFormDefault="unqualified"> <xs:include schemaLocation="leiauteConsStatServ_v1.07.xsd"/> <xs:element name="retConsStatServ" type="TRetConsStatServ"> <xs:annotation> <xs:documentation>Schema XML de validação do Resultado da Consulta do Status do Serviço</xs:documentation> </xs:annotation> </xs:element> </xs:schema>
```

## 3.4 Atributo versao do schema cabecMsg

Alteração do tipo do atributo versao do schema cabecMsg de " type xs:decimal " para " type xs:token ".

## Alterado de:

```
<xs:attribute name="versao" use="required" fixed="1.02"> <xs:simpleType> <xs:restriction base="xs:decimal"> <xs:totalDigits value="4"/> <xs:fractionDigits value="2"/> </xs:restriction> </xs:simpleType> </xs:attribute>
```

## para:

```
<xs:attribute name="versao" use="required"> <xs:simpleType> <xs:restriction base="xs:token"> <xs:pattern value="1\.02"/> </xs:restriction> </xs:simpleType> </xs:attribute>
```

## 3.5 Elemento versaoDados do schema cabecMsg

Alteração  do  tipo  do  elemento versaoDados do  schema  cabecMsg  de  " type xs:decimal " para " type xs:token ".

## Alterado de:

![Image](assets/image_000007_03855e49621a60885bf4c39a53011576c07dc6f710dc2994f7e1ba3cb6605fe9.png)

```
<xs:element name="versaoDados"> <xs:annotation> </xs:annotation> <xs:simpleType> <xs:restriction base="xs:decimal"> <xs:pattern value="[1-9]{1}[0-9]{0,1}\.[0-9]{2}"/> </xs:restriction> </xs:simpleType>
```

## para:

```
<xs:element name="versaoDados"> <xs:annotation> </xs:annotation> <xs:simpleType> <xs:restriction base="xs:token"> <xs:pattern value="[1-9]{1}[0-9]{0,1}\.[0-9]{2}"/> </xs:restriction> </xs:simpleType>
```

```
<xs:documentation>Versão da Leiaute XML da área de Dados</xs:documentation> <xs:documentation>Versão da Leiaute XML da área de Dados</xs:documentation>
```

![Image](assets/image_000008_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

## Schemas que compõe este Pacote de Liberação

| Schema XML                          | Chave de codificação digital MD5   | alteração (item)   |
|-------------------------------------|------------------------------------|--------------------|
| cancNFe_v1.07.xsd                   | 5ef9a8c4c7384ed5881a214dd3044a90   | -                  |
| consCad_v1.01.xsd                   | 42a0737cfa12808cf7b476264830c61d   | -                  |
| consReciNFe_v1.10.xsd               | c4256c71425addd717812d01d9e225d4   | -                  |
| consSitNFe_v1.07.xsd                | 824b5d8553f2f8de4a028602cf740b0f   | -                  |
| consStatServ_v1.07.xsd              | 4487b7952b296be96fb820b0bd486272   | -                  |
| enviNFe_v1.10.xsd                   | 9f4801904d64be34ee143c3df7abbc3c   | -                  |
| inutNFe_v1.07.xsd                   | dc9d81555c72d3bda568f75ba95f6394   | -                  |
| LeiauteCadastroEmissorDFe_v1.01.xsd | 6844b9aea94081890471bd5c3ee1ae59   | -                  |
| leiauteCancNFe_v1.07.xsd            | 38135642968794f4e676267d49e81925   | -                  |
| leiauteConsSitNFe_v1.07.xsd         | e7e66f9c1972b55ac783a9554a7b7d70   | -                  |
| leiauteConsStatServ_v1.07.xsd       | 40c3e669bc59f4d05b479fd50387593f   | -                  |
| leiauteConsultaCadastro_v1.01.xsd   | 8f11bd07cb8787cf5fa0800b45c87dc5   | -                  |
| leiauteInutNFe_v1.07.xsd            | 9ba5d374e41de076ff0f8af0c697ca37   | -                  |
| leiauteNFe_v1.10.xsd                | ac5822159e3ea961ab92d2428ef47eb7   | -                  |
| nfe_v1.10.xsd                       | c9ceb68d9d7fa3541e656dd2dddd3411   | -                  |
| procCancNFe_v1.07.xsd               | 38ed231357bad2f90597c7c22a8960a2   | -                  |
| procInutNFe_v1.07.xsd               | 188d14dcdc9d00850d7da423f211ea44   | -                  |
| procNFe_v1.10.xsd                   | 7e2ff42978fb786f7f96a8fb1f904c7f   | -                  |
| retAtuCadEmiDFe_v1.01.xsd           | 50859afb311449b932cfadd4572412d0   | -                  |
| retCancNFe_v1.07.xsd                | 1e0f30629dc577feee64c7efec4771bf   | -                  |
| retConsCad_v1.01.xsd                | 1718b87b9eef60fb9faf7eb4ba339745   | -                  |
| retConsReciNFe_v1.10.xsd            | 485f90ca049796602b3e9a4346f7e0ec   | -                  |
| retConsSitNFe_v1.07.xsd             | db4118969872ca55636f27eab49ca9c0   | -                  |
| retConsStatServ_v1.07.xsd           | 7f7a89bf14d5d8e935101c011b0d123f   | (3.3)              |
| retEnviNFe_v1.10.xsd                | c99485ddaa6aa26384f2360bf3b482f8   | -                  |
| retInutNFe_v1.07.xsd                | dad0e2b4c31be1cf6aa2418c25aceaf0   | -                  |
| tiposBasico_v1.02.xsd               | f539cce64cbc6845ba3f48b9efa37f29   | (3.1/3.2)          |
| xmldsig-core-schema_v1.01.xsd       | 9b6c6b52c5ff71e85b801158e0a5aae2   | -                  |
| atuCadEmiDFe_v1.01.xsd              | bd2a38d378dbb89224e366841a3b7eb8   | -                  |
| cabecMsg_v1.02.xsd                  | 0d7ed0d23ec21732b723f03337ab4cc0   | (3.4/3.5)          |
| cadEmiDFe_v1.01.xsd                 | 10dc830b745ef32fd2670416cf71bbcd   | -                  |

As  dúvidas  e  sugestões  devem  ser  encaminhadas  através  do  Canal  Fale  Conosco  da Secretaria  da  Fazenda  de  São  Paulo  (http://www.fazenda.sp.gov.br/email/default2.asp) referente à 'Portaria CAT 65/06'.
## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt-2007-003/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt-2007-003/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt-2007-003.md)
- [Proveniência resumida](../../../../sources/provenance/nt-2007-003.json)


## Documentos relacionados

- [[nota-t-cnica-2007-004-publicada-em-15-09-2011]]
- [[nota-t-cnica-2007-007-publicada-em-30-11-2010]]
- [[nt-2007-001]]
- [[nt-2007-002]]
- [[nt-2007-004]]
- [[nt-2007-007]]
- [[nt-2007-008]]
- [[nt-2007-009]]
