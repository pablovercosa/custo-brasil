![Image](assets/image_000000_c4e6daffbc318bd841fc00aef9f87a94e2b919c94e64e8100d060f4f9064a90b.png)

## Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_579898203cd01afe170ce12a96777804f366d3309138443a484ccc830f4320df.png)

Nota Técnica 2009/001

## Divulga novos Schemas da NF-e e do DPEC

![Image](assets/image_000002_ee1b686a18eee0cde4acc88c100eface6294f63408daa6f6fadd0af8e508af08.png)

Janeiro-2009

![Image](assets/image_000003_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

## 1.  Resumo

Esta Nota Técnica divulga os seguintes Pacotes de L iberação:

- a) PL\_005c da  NF-e  com  correção  de  algumas  regras  de  validaçã o  que  não  haviam  sido implementadas corretamente no PL\_005b;
- b) PL\_DPEC\_101a do  DPEC, com alteração no nome da tag DPEC na mens agem de envio e de retorno e aperfeiçoamento da validação do atributo  Id.

![Image](assets/image_000004_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

## 2.  Atualizações das regras de validação específicas do  Schema XML da NF-e

O PL\_005c foi alterado para aceitar a informação da  sigla 'EX' no campo UF de consumo do grupo de detalhamento específico de combustíveis.

O PL\_005c substitui o PL\_005b e será utilizado em a mbiente de produção  a partir do dia 19/01/2009.

## Alterações do PL\_005c:

- Campo cPais (ID = C14) do emitente, para aceitar apenas o valor 1058;

alterado de:

```
<xs:element name="cPais" type="Tpais" minOccurs="0"> <xs:annotation> <xs:documentation>Código do país </xs:documentation> </xs:annotation> para: <xs:documentation>Código do país </xs:documentation>
```

```
<xs:element name="cPais" minOccurs="0"> <xs:annotation> </xs:annotation> <xs:simpleType> <xs:restriction base="TString"> <xs:enumeration value="1058"/> </xs:restriction> </xs:simpleType> </xs:element>
```

- Campo UFCons (ID = L120) para aceitar a sigla 'EX';

```
alterado de: <xs:element name="UFCons" type="TUfEmi">
```

```
para: <xs:element name="UFCons" type="TUf">
```

## 3.  Nova versão dos Schemas XML do DPEC

- Alteração da identificação da tag DPEC para envDPEC no leiaute da Mensagem de Retorno do envio da DPEC ( retDPEC ) - página 20 do manual;

| AR11 envDPEC   | G AR03 xml 1-1 Mensagem de Declaração Prévia de Emissão em   |
|----------------|--------------------------------------------------------------|

![Image](assets/image_000005_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

| Contingência transmitida   |
|----------------------------|

- Alteração da identificação da tag DPEC para retDPEC no leiaute da Mensagem de Retorno da Consulta da DPEC (retConsDPEC) - página 30 do ma nual;
- Aperfeiçoamento da validação do atributo ID da tag infDPEC , para que o atributo Id tenha o formato DPEC99999999999999 (DPEC + CNPJ):
- Aperfeiçoamento  da  validação  do  atributo  ID  da  tag infDPECReg ,  para  que  o  atributo Id tenha o formato RETDPEC99999999999999 (RETDPEC + CNPJ):

| BR07 retDPEC   | G   | BR01   | xml   | 1-1   | DPEC localizada tem a mesma estrutura da   |
|----------------|-----|--------|-------|-------|--------------------------------------------|

```
alterado de: <xs:attribute name="Id" type="xs:ID" use="required"/> para: <xs:attribute name="Id" use="required"> <xs:simpleType> <xs:restriction base="xs:ID"> <xs:pattern value="DPEC[0-9]{14}"/> </xs:restriction> </xs:simpleType> </xs:attribute>
```

## alterado de:

```
<xs:attribute name="Id" type="xs:ID" use="required"/> para: <xs:attribute name="Id" use="required"> <xs:simpleType> <xs:restriction base="xs:ID"> <xs:pattern value="RETDPEC[0-9]{14}"/> </xs:restriction> </xs:simpleType>
```

```
</xs:attribute>
```

- Alteração da versão para 1.01 nos seguintes schema s:
- o
- o
- o
- o
- o

```
consDPEC_v1.00.xsd para consDPEC_v1.01; envDPEC_v1.00.xsd para envDPEC_v1.01; retConsDPEC_v1.00.xsd para retConsDPEC_v1.01.xsd; retDPEC_v1.00.xsd para retDPEC_v1.01.xsd; leiauteDPEC_v1.00 para leiauteDPEC_v1.01.xsd;
```

## Metadados

- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nota-t-cnica-2009-001-publicada-em-29-11-2010/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nota-t-cnica-2009-001-publicada-em-29-11-2010/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nota-t-cnica-2009-001-publicada-em-29-11-2010.md)
- [Proveniência resumida](../../../../sources/provenance/nota-t-cnica-2009-001-publicada-em-29-11-2010.json)


## Documentos relacionados

- [[nota-t-cnica-2007-004-publicada-em-15-09-2011]]
- [[nota-t-cnica-2007-007-publicada-em-30-11-2010]]
- [[nota-t-cnica-2008-001-publicada-em-30-11-2010]]
- [[nota-t-cnica-2008-003-publicada-em-30-11-2010]]
- [[nota-t-cnica-2008-005-publicada-em-30-11-2010]]
- [[nota-t-cnica-2009-002-publicada-em-29-11-2010]]
- [[nota-t-cnica-2009-004-publicada-em-30-11-2010]]
- [[nota-t-cnica-2010-002-publicada-em-29-11-2010]]
