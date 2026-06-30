---
title: "Projeto Nota Fiscal Eletrônica"
slug: "nt2007-006"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "8e77b15c09a2012a1be4d6e7c8f85b1ffedfcb25d774579dc1c4e29a78cbeea1"
converted_at_utc: "2026-06-25T14:58:07.208738+00:00"
status: "published"
type: "nota_tecnica"
---
![Image](assets/image_000000_c4e6daffbc318bd841fc00aef9f87a94e2b919c94e64e8100d060f4f9064a90b.png)

## Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_0da1381da639ef397828e221580902bae1b5c97acffafc661046eafa6d4fb33c.png)

## Nota Técnica 2007.006

Divulga PL\_006\_Hom\_v.100 - Pacote de Liberação de Schemas 006 - versão de homologação 1.00

![Image](assets/image_000002_be6ddeae8e40afc21587cdc2eafdee2e33cd2ea99d07ba45ac166eeb0684e150.png)

Novembro-2007

![Image](assets/image_000003_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

## 1.  Resumo

Divulga a versão preliminar de homologação do Pacote de Liberação 006 -PL\_006\_Hom\_v1.00, com os Schemas XML compatíveis com os leiautes de arquivos do Manual de Integração do Contribuinte - versão 2.0.3, que foi atualizada com as alterações necessárias  para  a  implementação  do  Sistema  de  Contingência  do  Ambiente  Nacional (SCAN) descritas no Manual de Contingência versão 5.01, sendo altamente recomendada a leitura da NT 2007/005 para conhecimento de todas alterações ocorridas na atualização do Manual de Integração do Contribuinte - versão 2.03.

Este Pacote de liberação destina-se ao uso exclusivo no ambiente de homologação da NF-e e  deverá  ser  substituído  pela  versão  do  ambiente  de  produção  que  será  divulgado oportunamente.

## 2.  Identificação e vigência do PL\_006\_Hom\_v1.00

| Versão do Manual de Integração do Contribuinte   | 2.03                                                   |
|--------------------------------------------------|--------------------------------------------------------|
| Versão do Pacote de liberação de Schemas XML     | PL_006_Hom_v1.00                                       |
| Data de início da vigência                       | 28/02/2008                                             |
| Data de termino da vigência                      | Início da entrada em operação do ambiente de produção. |
| Para utilização no Ambiente                      | Homologação                                            |
| Chave de codificação digital MD5 do pacote       | 415ed95431760ec9e6bb9a42a4aae8bc                       |

![Image](assets/image_000004_5abf66d3122ed6f40dc4d306a044327d0ea37aaaf917e4a3c43d27a105a78657.png)

## 3.  Alterações no leiaute da NF-e

## 3.1 Campo tpEmis

Acréscimo do valor '3' como conteúdo válido do campo tpEmis do leiaute da Nota Fiscal eletrônica, que passa a aceitar a seguinte codificação para identificar a forma de emissão da NF-e:

- 1 Normal - emissão normal com transmissão on-line da NF-e para a SEFAZ de origem;
- 2  Contingência  off-line -  emissão  em  contingência,  com  impressão  do DANFE em formulário de segurança e posterior transmissão da NF-e para a SEFAZ de origem quando sanado os problemas técnicos  que  motivaram  a adoção da contingência;
- 3  Contingência  SCAN -  emissão  em  contingência  no  Sistema  de Contingência do Ambiente Nacional - SCAN;

## 3.2 Campo cNF

Redução do tamanho do campo cNF de 9 para 8 posições para permitir a inclusão do campo tpEmis na chave de acesso da NF-e sem alteração do seu tamanho.

## 3.3 Campo fone do emitente

Aumento do tamanho do campo fone de 10 para 11 posições.

## 3.4  Campo RENAVAM

Alteração  do tipo do campo RENAVAM para tipo caractere.

## 3.5 Campo infAdFisco

Aumento do tamanho do campo infAdFisco de 256 para 2.000 posições.

As alterações acima implicam na alteração da versão do leiaute de da NF-e e de todas as mensagens relacionadas com o seu envio.

![Image](assets/image_000005_da9ca9b2024794c51c631128ce25e0c27a400951387ed1118a5cc175fdb0751f.png)

## Schemas que compõe este Pacote de Liberação

| Schema XML                          | Chave de codificação digital MD5   | alteração (item)   |
|-------------------------------------|------------------------------------|--------------------|
| cancNFe_v1.07.xsd                   | 5ef9a8c4c7384ed5881a214dd3044a90   | -                  |
| consCad_v1.01.xsd                   | 42a0737cfa12808cf7b476264830c61d   | -                  |
| consReciNFe_v1.11.xsd               | dd70950db6f37a34b09cf712bc1df5ee   | (3)                |
| consSitNFe_v1.07.xsd                | 824b5d8553f2f8de4a028602cf740b0f   | -                  |
| consStatServ_v1.07.xsd              | 4487b7952b296be96fb820b0bd486272   | -                  |
| enviNFe_v1.11.xsd                   | 850d79eca94f4ddd5a41f123c4f21559   | (3)                |
| inutNFe_v1.07.xsd                   | dc9d81555c72d3bda568f75ba95f6394   | -                  |
| LeiauteCadastroEmissorDFe_v1.01.xsd | 6844b9aea94081890471bd5c3ee1ae59   | -                  |
| leiauteCancNFe_v1.07.xsd            | 38135642968794f4e676267d49e81925   | -                  |
| leiauteConsSitNFe_v1.07.xsd         | e7e66f9c1972b55ac783a9554a7b7d70   | -                  |
| leiauteConsStatServ_v1.07.xsd       | 40c3e669bc59f4d05b479fd50387593f   | -                  |
| leiauteConsultaCadastro_v1.01.xsd   | 8f11bd07cb8787cf5fa0800b45c87dc5   | -                  |
| leiauteInutNFe_v1.07.xsd            | 9ba5d374e41de076ff0f8af0c697ca37   | -                  |
| leiauteNFe_v1.11.xsd                | da13718d08e52029585874eed96b7813   | (3)                |
| nfe_v1.11.xsd                       | bc63c3321165a83f7cfbaa6de6699d8f   | (3)                |
| procCancNFe_v1.07.xsd               | 38ed231357bad2f90597c7c22a8960a2   | -                  |
| procInutNFe_v1.07.xsd               | 188d14dcdc9d00850d7da423f211ea44   | -                  |
| procNFe_v1.11.xsd                   | 3374983ec4726ff7606d4b65a4bb3ec8   | (3)                |
| retAtuCadEmiDFe_v1.01.xsd           | 50859afb311449b932cfadd4572412d0   | -                  |
| retCancNFe_v1.07.xsd                | 1e0f30629dc577feee64c7efec4771bf   | -                  |
| retConsCad_v1.01.xsd                | 1718b87b9eef60fb9faf7eb4ba339745   | -                  |
| retConsReciNFe_v1.11.xsd            | 5dde4b30c6d041640cb0d8a181054644   | (3)                |
| retConsSitNFe_v1.07.xsd             | db4118969872ca55636f27eab49ca9c0   | -                  |
| retConsStatServ_v1.07.xsd           | 7f7a89bf14d5d8e935101c011b0d123f   | -                  |
| retEnviNFe_v1.11.xsd                | 33e87bdf66f10afcf8b435bf2472c16a   | (3)                |
| retInutNFe_v1.07.xsd                | dad0e2b4c31be1cf6aa2418c25aceaf0   | -                  |
| tiposBasico_v1.02.xsd               | bba1572bc5aa5eb37e873f02fcd4aa43   | -                  |
| xmldsig-core-schema_v1.01.xsd       | 9b6c6b52c5ff71e85b801158e0a5aae2   | -                  |
| atuCadEmiDFe_v1.01.xsd              | bd2a38d378dbb89224e366841a3b7eb8   | -                  |
| cabecMsg_v1.02.xsd                  | 62b29086cce16483e4910af45da0a9c4   | -                  |
| cadEmiDFe_v1.01.xsd                 | 10dc830b745ef32fd2670416cf71bbcd   | -                  |
| leiauteConsRecibo_v1.11.xsd         | 9a19c2b13cabfe9085f5a471d211e3da   | (3)                |

As  dúvidas  e  sugestões  devem  ser  encaminhadas  através  do  Canal  Fale  Conosco  da Secretaria  da  Fazenda  de  São  Paulo  (http://www.fazenda.sp.gov.br/email/default2.asp) referente à 'Portaria CAT 104/07'.
## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt2007-006/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt2007-006/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt2007-006.md)
- [Proveniência resumida](../../../../sources/provenance/nt2007-006.json)

## Documentos relacionados
_Nenhum documento relacionado conhecido._
