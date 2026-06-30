---
title: "Projeto Nota Fiscal Eletrônica"
slug: "nt-2007-009"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "13ef43d5771044ef0cac87fa1bd4d1580fa39ebdb191071121b5a252a019956f"
converted_at_utc: "2026-06-25T14:57:38.997257+00:00"
status: "published"
type: "nota_tecnica"
---
![Image](assets/image_000000_c4e6daffbc318bd841fc00aef9f87a94e2b919c94e64e8100d060f4f9064a90b.png)

## Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_0da1381da639ef397828e221580902bae1b5c97acffafc661046eafa6d4fb33c.png)

## Nota Técnica 2007.009

Divulga PL\_007\_Hom\_v.100 - Pacote de Liberação de Schemas 007 - versão de homologação 1.00

![Image](assets/image_000002_be6ddeae8e40afc21587cdc2eafdee2e33cd2ea99d07ba45ac166eeb0684e150.png)

Novembro-2007

![Image](assets/image_000003_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

## 1.  Resumo

Divulga a versão preliminar de homologação do Pacote de Liberação 007 -PL\_007\_Hom\_v1.00, com os Schemas XML compatíveis com os leiautes de arquivos do Manual de Integração do Contribuinte - versão 2.0.4, que foi atualizada com as alterações necessárias  para  a  implementação  do  Sistema  de  Contingência  do  Ambiente  Nacional (SCAN) descritas no Manual de Contingência versão 6.00, sendo altamente recomendada a leitura da NT 2007/008 para conhecimento de todas alterações ocorridas na atualização do Manual de Integração do Contribuinte - versão 2.0.4.

Este Pacote de liberação destina-se ao uso exclusivo no ambiente de homologação da NF-e e  deverá  ser  substituído  pela  versão  do  ambiente  de  produção  que  será  divulgado oportunamente.

## 2.  Identificação e vigência do PL\_007\_Hom\_v1.00

| Versão do Manual de Integração do Contribuinte   | 2.04                                                   |
|--------------------------------------------------|--------------------------------------------------------|
| Versão do Pacote de liberação de Schemas XML     | PL_007_Hom_v1.00                                       |
| Data de início da vigência                       | 28/02/2008                                             |
| Data de termino da vigência                      | Início da entrada em operação do ambiente de produção. |
| Para utilização no Ambiente                      | Homologação                                            |
| Chave de codificação digital MD5 do pacote       | f94251eab10d4e39cf58e7bb4b1379a9                       |

![Image](assets/image_000004_bd6067dbc95a3a571c718b70c3b84dcf5378170f16b6c8867a4a06df1bcee3e4.png)

## 3.  Alterações no leiaute da NF-e

## 3.1 Campo tpEmis

Acréscimo do valor '3' como conteúdo válido do campo tpEmis do leiaute da Nota Fiscal eletrônica, que passa a aceitar a seguinte codificação para identificar a forma de emissão da NF-e:

- 1 Normal - emissão normal com transmissão on-line da NF-e para a SEFAZ de origem;
- 2  Contingência  off-line -  emissão  em  contingência,  com  impressão  do DANFE em formulário de segurança e posterior transmissão da NF-e para a SEFAZ de origem quando sanado os problemas técnicos  que  motivaram  a adoção da contingência;
- 3  Contingência  SCAN -  emissão  em  contingência  no  Sistema  de Contingência do Ambiente Nacional - SCAN;

## 3.2 Campo fone do emitente

Aumento do tamanho do campo fone de 10 para 11 posições.

## 3.3  Campo RENAVAM

Alteração do tipo do campo RENAVAM para tipo caractere.

## 3.4 Campo infAdFisco

Aumento do tamanho do campo infAdFisco de 256 para 2.000 posições.

As alterações acima implicam na alteração da versão do leiaute de da NF-e e de todas as mensagens relacionadas com o seu envio.

![Image](assets/image_000005_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

## Schemas que compõe este Pacote de Liberação

| Schema XML                          | Chave de codificação digital MD5   | alteração (item)   |
|-------------------------------------|------------------------------------|--------------------|
| cancNFe_v1.07.xsd                   | 5ef9a8c4c7384ed5881a214dd3044a90   | -                  |
| consCad_v1.01.xsd                   | 42a0737cfa12808cf7b476264830c61d   | -                  |
| consReciNFe_v1.11.xsd               | dd70950db6f37a34b09cf712bc1df5ee   | -                  |
| consSitNFe_v1.07.xsd                | 824b5d8553f2f8de4a028602cf740b0f   | -                  |
| consStatServ_v1.07.xsd              | 4487b7952b296be96fb820b0bd486272   | -                  |
| enviNFe_v1.12.xsd                   | 20c67b0829fd1e1f192527eea1c13578   | (3)                |
| inutNFe_v1.07.xsd                   | dc9d81555c72d3bda568f75ba95f6394   | -                  |
| LeiauteCadastroEmissorDFe_v1.01.xsd | 6844b9aea94081890471bd5c3ee1ae59   | -                  |
| leiauteCancNFe_v1.07.xsd            | 38135642968794f4e676267d49e81925   | -                  |
| leiauteConsSitNFe_v1.07.xsd         | e7e66f9c1972b55ac783a9554a7b7d70   | -                  |
| leiauteConsStatServ_v1.07.xsd       | 40c3e669bc59f4d05b479fd50387593f   | -                  |
| leiauteConsultaCadastro_v1.01.xsd   | 8f11bd07cb8787cf5fa0800b45c87dc5   | -                  |
| leiauteInutNFe_v1.07.xsd            | 9ba5d374e41de076ff0f8af0c697ca37   | -                  |
| leiauteNFe_v1.12.xsd                | 1a5268171bf5a2349382c67800e129d7   | (3)                |
| nfe_v1.12.xsd                       | d5a47e8e84214506b6c30af05b215da0   | (3)                |
| procCancNFe_v1.07.xsd               | 38ed231357bad2f90597c7c22a8960a2   | -                  |
| procInutNFe_v1.07.xsd               | 188d14dcdc9d00850d7da423f211ea44   | -                  |
| procNFe_v1.12.xsd                   | 2b7a13bffb8c6fb6a857575befdd6dd6   | (3)                |
| retAtuCadEmiDFe_v1.01.xsd           | 50859afb311449b932cfadd4572412d0   | -                  |
| retCancNFe_v1.07.xsd                | 1e0f30629dc577feee64c7efec4771bf   | -                  |
| retConsCad_v1.01.xsd                | 1718b87b9eef60fb9faf7eb4ba339745   | -                  |
| retConsReciNFe_v1.11.xsd            | 5dde4b30c6d041640cb0d8a181054644   | -                  |
| retConsSitNFe_v1.07.xsd             | db4118969872ca55636f27eab49ca9c0   | -                  |
| retConsStatServ_v1.07.xsd           | 7f7a89bf14d5d8e935101c011b0d123f   | -                  |
| retEnviNFe_v1.12.xsd                | 253aeed072d343e011bf8c8e621a0a98   | (3)                |
| retInutNFe_v1.07.xsd                | dad0e2b4c31be1cf6aa2418c25aceaf0   | -                  |
| tiposBasico_v1.02.xsd               | bba1572bc5aa5eb37e873f02fcd4aa43   | -                  |
| xmldsig-core-schema_v1.01.xsd       | 9b6c6b52c5ff71e85b801158e0a5aae2   | -                  |
| atuCadEmiDFe_v1.01.xsd              | bd2a38d378dbb89224e366841a3b7eb8   | -                  |
| cabecMsg_v1.02.xsd                  | 62b29086cce16483e4910af45da0a9c4   | -                  |
| cadEmiDFe_v1.01.xsd                 | 10dc830b745ef32fd2670416cf71bbcd   | -                  |
| leiauteConsRecibo_v1.11.xsd         | 9a19c2b13cabfe9085f5a471d211e3da   | -                  |

As  dúvidas  e  sugestões  devem  ser  encaminhadas  através  do  Canal  Fale  Conosco  da Secretaria  da  Fazenda  de  São  Paulo  (http://www.fazenda.sp.gov.br/email/default2.asp) referente à 'Portaria CAT 104/07'.
## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt-2007-009/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt-2007-009/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt-2007-009.md)
- [Proveniência resumida](../../../../sources/provenance/nt-2007-009.json)
