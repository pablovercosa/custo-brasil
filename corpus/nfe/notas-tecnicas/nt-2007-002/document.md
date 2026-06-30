---
title: "Projeto Nota Fiscal Eletrônica"
slug: "nt-2007-002"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "d1126132df780e25ba77d9838897aadc2f07aa88bef5ef67dc989b5735c0de01"
converted_at_utc: "2026-06-25T15:01:13.982268+00:00"
status: "published"
type: "nota_tecnica"
---
![Image](assets/image_000000_c4e6daffbc318bd841fc00aef9f87a94e2b919c94e64e8100d060f4f9064a90b.png)

## Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_fc88b2ba2099fccb5268de655eed9d07cf534c8c319fcafeb4152d963eeee414.png)

## Nota Técnica 2007.002

Divulga PL\_005a\_Hom\_v0.02 - Pacote de Liberação de Schemas 005a - Ambiente de Homologação - versão 0.02

![Image](assets/image_000002_245aadd9f41c69d821384747d8934c7eed19b4d04c264df5ad5503dae537983a.png)

Setembro-2007

![Image](assets/image_000003_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

## 1.  Resumo

Divulga o Pacote de Liberação 005a do Ambiente de Homologação - PL\_005a\_Hom\_v0.02, com os Schemas XML compatíveis com os leiautes de arquivos do Manual de Integração do Contribuinte - versão 2.0.2.

O  PL\_005b\_Hom\_v0.02  substitui  a  versão  preliminar  do  Pacote  de  Liberação  005a (PL\_005a\_Hom\_v0.01.zip)  divulgada  anteriormente  e  não  exige  qualquer  alteração  nos aplicativos do contribuinte ou da Fazenda.

Este Pacote de liberação destina-se ao uso exclusivo no ambiente de homologação da NF-e e deverá ser substituído pela versão definitiva do ambiente de produção que será divulgado oportunamente.

## 2.  Identificação e vigência do PL\_005a\_hom\_v0.02

| Versão do Manual de Integração do Contribuinte   | 2.02                             |
|--------------------------------------------------|----------------------------------|
| Versão do Pacote de liberação de Schemas XML     | PL_005a_Hom_v0.02                |
| Data de início da vigência                       | 14/09/2007                       |
| Data de termino da vigência                      | 31/09/2007                       |
| Para utilização no Ambiente                      | Homologação                      |
| Chave de codificação digital MD5 do pacote       | a3bba28f3d252215ba7b1500897949c1 |

![Image](assets/image_000004_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

## 3.  Atualizações ocorridas

## 3.1 Validação da versão dos Schemas

Alteração do tipo do atributo versao dos Schemas de " type xs:decimal "  para " type xs:token " para solucionar a situação em que o conteúdo do atributo versao é gerado sem o zero não significativo pela aplicação do contribuinte.

Ex.:  Em  algumas  situações  o  processo  de  geração  automática  de  XML  do contribuinte  transforma  o  valor  "1.10"  para  "1.1"  no  conteúdo  do  atributo versao , eliminando os zeros não significativos, causando erro na validação do Schema  XML que espera o conteúdo "1.10".

A solução proposta pela Equipe Técnica é a modificação do tipo campo de numérico ( type  xs:decimal )  para  alfanumérico  ( type  xs:token) ,  cabendo  ressaltar  que  esta solução  não  exige  nenhuma  alteração  nos  aplicativos  do  contribuinte  ou  da Fazenda .

A  implementação  da  solução  proposta  foi  realizada  com  a  criação  dos  seguintes tipos simples ( simple Type ) para cada um dos leiautes de Web Services existentes:

- TVerCadEmi -  para  uso  nos  Schemas  relacionados  com  os  leiautes  do cadastro de emitentes de DF;
- TVerCancNFe -  para  uso  nos  Schemas  relacionados  com  os  leiautes  de Cancelamento da NF-e;
- TVerConsSitNFe -  para  uso  nos Schemas relacionados com os leiuates de Consulta Situação de NF-e;
- TVerConsStatServ - para uso nos Schemas relacionados com os leiuates de Consulta Situação do Serviço;
- TVerConsCad  Schemas -  para  uso  nos  Schemas  relacionados  com  os leiuates de Consulta Cadastro;
- TVerInutNFe -  para  uso  nos  Schemas  relacionados  com  os  leiuates  de Inutilização de numeração de NF-e;
- TVerNFe - para uso nos Schemas relacionados com os leiuates da NF-e;

## Exemplo de alteração:

## Alterado de:

&lt;xs:attribute name="versao" use="required" fixed="1.10"&gt; &lt;xs:simpleType&gt;

&lt;xs:restriction base="xs:decimal"&gt;

&lt;xs:totalDigits value="4"/&gt;

&lt;xs:fractionDigits value="2"/&gt;

&lt;/xs:restriction&gt;

&lt;/xs:simpleType&gt;

![Image](assets/image_000005_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

## Nota Fiscal Eletrônica

&lt;/xs:attribute&gt;/&gt;

## para:

&lt;xs:attribute name="versao" type="TVerNFe" use="required"/&gt;

## onde, o tipo TVerNFe tem a seguinte definição:

```
<xs:simpleType name="TVerNFe"> <xs:annotation> <xs:documentation> Tipo Versão da NF-e - 1.10</xs:documentation> </xs:annotation> <xs:restriction base="xs:token"> <xs:pattern value="1\.10"/> </xs:restriction> </xs:simpleType>
```

## 3.2 Correção do Schema atuCadEmiDFe\_v1.01.xsd

## 3.2.1  referência do "include"

Correção do erro de referência existente no " include " do Schema cadEmiDFe\_v1.01.xsd.

## Alterado de:

- &lt; xs:include schemaLocation =" LeiauteCadastroEmissorNFe\_v1.01.xsd " /&gt; para:

&lt; xs:include schemaLocation =" LeiauteCadastroEmissorDFe\_v1.01.xsd " /&gt;

## 3.2.2  elemento "atuCadEmiNFe"

Correção no " type " e no " name " do elemento atuCadEmiNFe  do  Schema cadEmiDFe\_v1.01.xsd.

## Alterado de:

&lt; xs:element name ="atuCadEmiNFe" type ="TAtuCadEmiNFe"&gt;

![Image](assets/image_000006_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

## para:

&lt; xs:element name ="atuCadEmiDFe" type ="TAtuCadEmiDFe"&gt;

## 4.  Schemas que compõe este Pacote de Liberação

| Schema XML                          | Chave de codificação digital MD5   | alteração (item)   |
|-------------------------------------|------------------------------------|--------------------|
| cancNFe_v1.07.xsd                   | 5ef9a8c4c7384ed5881a214dd3044a90   | -                  |
| consCad_v1.01.xsd                   | 42a0737cfa12808cf7b476264830c61d   | -                  |
| consReciNFe_v1.10.xsd               | c4256c71425addd717812d01d9e225d4   | -                  |
| consSitNFe_v1.07.xsd                | 824b5d8553f2f8de4a028602cf740b0f   | -                  |
| consStatServ_v1.07.xsd              | 4487b7952b296be96fb820b0bd486272   | -                  |
| enviNFe_v1.10.xsd                   | 9f4801904d64be34ee143c3df7abbc3c   | -                  |
| inutNFe_v1.07.xsd                   | dc9d81555c72d3bda568f75ba95f6394   | -                  |
| LeiauteCadastroEmissorDFe_v1.01.xsd | 6844b9aea94081890471bd5c3ee1ae59   | (3.1)              |
| leiauteCancNFe_v1.07.xsd            | 38135642968794f4e676267d49e81925   | (3.1)              |
| leiauteConsSitNFe_v1.07.xsd         | e7e66f9c1972b55ac783a9554a7b7d70   | (3.1)              |
| leiauteConsStatServ_v1.07.xsd       | 40c3e669bc59f4d05b479fd50387593f   | (3.1)              |
| leiauteConsultaCadastro_v1.01.xsd   | 8f11bd07cb8787cf5fa0800b45c87dc5   | (3.1)              |
| leiauteInutNFe_v1.07.xsd            | 9ba5d374e41de076ff0f8af0c697ca37   | (3.1)              |
| leiauteNFe_v1.10.xsd                | ac5822159e3ea961ab92d2428ef47eb7   | (3.1)              |
| nfe_v1.10.xsd                       | c9ceb68d9d7fa3541e656dd2dddd3411   | -                  |
| procCancNFe_v1.07.xsd               | 38ed231357bad2f90597c7c22a8960a2   | -                  |
| procInutNFe_v1.07.xsd               | 188d14dcdc9d00850d7da423f211ea44   | -                  |
| procNFe_v1.10.xsd                   | 7e2ff42978fb786f7f96a8fb1f904c7f   | -                  |
| retAtuCadEmiDFe_v1.01.xsd           | 50859afb311449b932cfadd4572412d0   | -                  |
| retCancNFe_v1.07.xsd                | 1e0f30629dc577feee64c7efec4771bf   | -                  |
| retConsCad_v1.01.xsd                | 1718b87b9eef60fb9faf7eb4ba339745   | -                  |
| retConsReciNFe_v1.10.xsd            | 485f90ca049796602b3e9a4346f7e0ec   | -                  |
| retConsSitNFe_v1.07.xsd             | db4118969872ca55636f27eab49ca9c0   | -                  |
| retConsStatServ_v1.07.xsd           | 30126cdf8c05017a4f2a9aebcd2c53bb   | -                  |
| retEnviNFe_v1.10.xsd                | c99485ddaa6aa26384f2360bf3b482f8   | -                  |
| retInutNFe_v1.07.xsd                | dad0e2b4c31be1cf6aa2418c25aceaf0   | -                  |
| tiposBasico_v1.02.xsd               | 42712e56c023a760b318a0a823524143   | -                  |
| xmldsig-core-schema_v1.01.xsd       | 9b6c6b52c5ff71e85b801158e0a5aae2   | -                  |
| atuCadEmiDFe_v1.01.xsd              | bd2a38d378dbb89224e366841a3b7eb8   | (3.2)              |
| cabecMsg_v1.02.xsd                  | 62b29086cce16483e4910af45da0a9c4   | -                  |
| cadEmiDFe_v1.01.xsd                 | 10dc830b745ef32fd2670416cf71bbcd   | -                  |

As  dúvidas  e  sugestões  devem  ser  encaminhadas  através  do  Canal  Fale  Conosco  da Secretaria  da  Fazenda  de  São  Paulo  (http://www.fazenda.sp.gov.br/email/default2.asp) referente à 'Portaria CAT 65/06'.
## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt-2007-002/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt-2007-002/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt-2007-002.md)
- [Proveniência resumida](../../../../sources/provenance/nt-2007-002.json)


## Documentos relacionados

- [[nota-t-cnica-2007-004-publicada-em-15-09-2011]]
- [[nota-t-cnica-2007-007-publicada-em-30-11-2010]]
- [[nt-2007-001]]
- [[nt-2007-003]]
- [[nt-2007-004]]
- [[nt-2007-007]]
- [[nt-2007-008]]
- [[nt-2007-009]]
