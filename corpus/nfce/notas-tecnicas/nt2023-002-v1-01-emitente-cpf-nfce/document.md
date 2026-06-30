---
title: "Projeto Nota Fiscal Eletrônica"
slug: "nt2023-002-v1-01-emitente-cpf-nfce"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "b0cb9528bfaa6e0b5ac2986c879898eebcbb9457e97fcf0af985a00659649031"
converted_at_utc: "2026-06-25T15:44:38.995556+00:00"
status: "published"
type: "nota_tecnica"
---

## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfce/notas-tecnicas/nt2023-002-v1-01-emitente-cpf-nfce/source.json)
- [Dados normalizados](../../../../normalized/nfce/notas-tecnicas/nt2023-002-v1-01-emitente-cpf-nfce/normalized.json)
- [Changelog](../../../../changelog/nfce/notas-tecnicas/nt2023-002-v1-01-emitente-cpf-nfce.md)
- [Proveniência resumida](../../../../sources/provenance/nt2023-002-v1-01-emitente-cpf-nfce.json)

## Projeto Nota Fiscal Eletrônica

Nota Técnica 2023.002

Emitente Pessoa Física (CPF) com Inscrição Estadual -NFC-e

Versão 1.01 - Novembro 2025

![Image](assets/image_000002_827e2e8447eabae3e3f14de38f9e408565080e3ced72863bf1184097a8cef8ac.png)

![Image](assets/image_000003_243546661a15ca96911c9a4629b5a8b39243e0d3643215d5dd11f86950effd6f.png)

## Sumário

| Controle de Versões.............................................................................................................                                                                                                                                                                    | Controle de Versões.............................................................................................................                                                                                                                                                                    | Controle de Versões.............................................................................................................                                                                                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Histórico de Alterações / Cronograma.................................................................................. 4                                                                                                                                                                            | Histórico de Alterações / Cronograma.................................................................................. 4                                                                                                                                                                            | Histórico de Alterações / Cronograma.................................................................................. 4                                                                                                                                                                            |
| 1.                                                                                                                                                                                                                                                                                                  | Resumo.......................................................................................................................... 5                                                                                                                                                                  | Resumo.......................................................................................................................... 5                                                                                                                                                                  |
| 2.                                                                                                                                                                                                                                                                                                  | Visão Geral .................................................................................................................... 6                                                                                                                                                                  | Visão Geral .................................................................................................................... 6                                                                                                                                                                  |
| 2.1                                                                                                                                                                                                                                                                                                 | 2.1                                                                                                                                                                                                                                                                                                 | Sobre a Chave de Acesso da NFC-e.....................................................................................6                                                                                                                                                                              |
| 2.2                                                                                                                                                                                                                                                                                                 | 2.2                                                                                                                                                                                                                                                                                                 | Alteração de Schema para evitar caracteres inválidos ..........................................................6                                                                                                                                                                                    |
| 2.3                                                                                                                                                                                                                                                                                                 | 2.3                                                                                                                                                                                                                                                                                                 | Alteração das Regras de Validação B26-30 e B26-50...........................................................6                                                                                                                                                                                       |
| 3.                                                                                                                                                                                                                                                                                                  | Grupo D: Validação da Área de Dados.......................................................................... 7                                                                                                                                                                                     | Grupo D: Validação da Área de Dados.......................................................................... 7                                                                                                                                                                                     |
| 3.1 DA. Autorização - Área de dados do lote de                                                                                                                                                                                                                                                      | 3.1 DA. Autorização - Área de dados do lote de                                                                                                                                                                                                                                                      | NF-e................................................................7                                                                                                                                                                                                                               |
| 4.                                                                                                                                                                                                                                                                                                  | Serviço: Autorização de Uso da Nota Fiscal (item 4.1 do MOC).................................... 7                                                                                                                                                                                                  | Serviço: Autorização de Uso da Nota Fiscal (item 4.1 do MOC).................................... 7                                                                                                                                                                                                  |
| 4.1 Leiaute                                                                                                                                                                                                                                                                                         | 4.1 Leiaute                                                                                                                                                                                                                                                                                         | da Nota Fiscal Eletrônica (Anexo I do MOC).............................................................7                                                                                                                                                                                            |
| 4.2                                                                                                                                                                                                                                                                                                 | 4.2                                                                                                                                                                                                                                                                                                 | Alteração em Regras de Validação - RV (Anexo II do MOC)................................................8                                                                                                                                                                                            |
| B. Identificação da Nota Fiscal ............................................................................................................... 8 C. Identificação do Emitente................................................................................................................... 8 | B. Identificação da Nota Fiscal ............................................................................................................... 8 C. Identificação do Emitente................................................................................................................... 8 | B. Identificação da Nota Fiscal ............................................................................................................... 8 C. Identificação do Emitente................................................................................................................... 8 |
| 5.                                                                                                                                                                                                                                                                                                  | Serviço: Evento de Cancelamento (Item 4.3 do MOC)................................................... 9                                                                                                                                                                                              | Serviço: Evento de Cancelamento (Item 4.3 do MOC)................................................... 9                                                                                                                                                                                              |
| 5.1 Alteração em Regras de Validação (Item 4.3.7-e e 4.3.8 do MOC) .......................................9                                                                                                                                                                                         | 5.1 Alteração em Regras de Validação (Item 4.3.7-e e 4.3.8 do MOC) .......................................9                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                     |
| 6.                                                                                                                                                                                                                                                                                                  | Fim da Denegação na NFC-e ...................................................................................... 10                                                                                                                                                                                 | Fim da Denegação na NFC-e ...................................................................................... 10                                                                                                                                                                                 |

![Image](assets/image_000004_2278f3eb709603570ded3091ecf32a2ede75d227135761dc1476200ed409ba50.png)

![Image](assets/image_000005_46d0b38d4276e3bcce9f0962b90d9d83c755850ba5ebc3c5a18b32e8f735a01b.png)

## Controle de Versões

|   Versão | Publicação    | Descrição                                                                     |
|----------|---------------|-------------------------------------------------------------------------------|
|     1.00 | Maio/ 2023    | Publicação da NT para permitir a emissão de NFC-e por CPF para produtor rural |
|     1.01 | Novembro/2025 | Possibilitar emissão de NFC-e pela nota avulsa para a UF SC                   |

![Image](assets/image_000006_a2cedd90c01b62c5fd29f35c0ad71b2562376aad3ee6d6133c06909f050d5fe3.png)

![Image](assets/image_000007_8fd1d7da834e8c7ee9a7696789a7183ae08f026b09636de3a01e9ef07927cce3.png)

## Histórico de Alterações / Cronograma

|   Versão | Histórico de atualizações                                                    | Implantação Teste   | Implantação Produção   |
|----------|------------------------------------------------------------------------------|---------------------|------------------------|
|     1.00 | Emissão de NFC-e para Produtor Rural Pessoa Física e Eliminação da Denegação | 24/07/2023          | Até 04/09/2023         |
|          | Elimina Lote para a NFC-e                                                    | 24/07/2023          | 04/09/2023             |
|     1.01 | Possibilitar emissão de NFC-e pela nota avulsa para a UF SC                  | Até 19/01/2026      | Até 02/02/2026         |

![Image](assets/image_000008_a2cedd90c01b62c5fd29f35c0ad71b2562376aad3ee6d6133c06909f050d5fe3.png)

## 1. Resumo

Foi alterada a legislação nacional (Ajuste SINIEF 54/2022), permitindo a emissão da NFC-e para emitente produtor rural, em substituição a Nota Fiscal, modelo 04. Esta decisão atende produtores rurais, que possuem uma Inscrição Estadual vinculada ao seu CPF, a realizar vendas utilizando a NFC-e.

Com esta mudança, o contribuinte Produtor Rural com CPF poderá emitir a NFC-e na venda para consumidor final. Também será possível utilizar o aplicativo da Nota Fiscal Fácil - NFF para emitir a NFC-e na venda para consumidor final, facultando a identificação do destinatário na venda, facilitando a emissão.

Portanto, deverá ser possível a emissão de NFC-e para produtor rural utilizando o aplicativo NFF ou do próprio contribuinte.

Para a UF SC poderá ser possível também a emissão de NFC-e utilizando aplicativo de Nota Fiscal Avulsa.

Esta especificação documenta as mudanças necessárias no serviço de autorização de NFC-e disponibilizado pelas SEFAZ.

Esta NT também faz referências as alterações necessárias para a eliminação da denegação na NFC-e, prevista pelo Ajuste SINIEF 10/2023.

A NFC-e também terá a eliminação de envio por lote com mais de 1 NFC-e.

![Image](assets/image_000009_0592f8c02b18091e6d8e5fc4ebbded63a95c5699266e213f5635010617c5bf89.png)

## 2. Visão Geral

No leiaute atual da NF-e já consta a possibilidade do emitente ser uma pessoa física, identificada pelo  seu  CPF.  Esta  possibilidade  foi  implementada  pela  Nota  Técnica  2018.001.  Portanto, também será permitido a emissão por CPF para NFC-e.

## 2.1 Sobre a Chave de Acesso da NFC-e

Na Chave de Acesso da NFC-e consta o CNPJ da empresa emitente da NFC-e. Esta realidade terá que ser alterada, permitindo a identificação na Chave de Acesso do emitente produtor rural (CPF).

Também terá que ser alterado o processo de assinatura da NFC-e, que neste caso poderá ser utilizado um e-CPF quando utilizar software próprio.

No caso de emissão com software próprio:

- O CPF deverá constar na Chave de Acesso, precedido por zeros, completando 14 posições;
- Deverá utilizar a série reservada [920-969]
- A NFC-e deverá ser assinada com o Certificado Digital do Emitente, do tipo 'e-CPF'.

No caso de emissão com aplicativo NFF:

- O CPF deverá constar na Chave de Acesso, precedido por zeros, completando 14 posições;
- Não terá série reservada, mas identifica se o emitente é CPF por outro campo na chave de acesso ([NT 2021.002](../../../nfe/notas-tecnicas/nt2021-002-v1-12-nota-fiscal-f-cil/document.md));
- A NFC-e deverá ser assinada com o Certificado Digital do Emitente da Sefaz Virtual do Rio Grande do Sul (SVRS).

## 2.2 Alteração de Schema para evitar caracteres inválidos

Foi identificado algumas NF-e e Eventos sendo emitidos com caracteres inválidos, o que pode gerar  problema  na  assinatura digital,  ou na extração  do  XML. Para  impedir  esses  caracteres inválidos o SCHEMA estará sendo alterado com as correções.

## 2.3 Alteração das Regras de Validação B26-30 e B26-50

Alteração  das  Regras  de  Validação  B26-30  e  B26-50  para  possibilitar  a  emissão  de  NFC-e utilizando aplicativo de Nota Fiscal Avulsa para a UF SC.

![Image](assets/image_000010_76eb5635d6f9db83e5e5f920247d63dd4cec4997a1ae8ae6ac464b9789d174f0.png)

## 3. Grupo D: Validação da Área de Dados

## 3.1 DA. Autorização - Área de dados do lote de NF-e

Para a NFC-e será eliminada a requisição assíncrona, portanto o Lote de NFC-e somente poderá ser informado com 1 NFC-e.

| Campo-Seq Modelo   | Regra de Validação               | Aplic. Msg Efeito Descrição Erro                           |
|--------------------|----------------------------------|------------------------------------------------------------|
| GAP03a-4 65        | Enviado Lote com mais de 1 NFC-e | Obrig. 126 Rej. Rejeição: Enviado lote com mais de 1 NFC-e |

## 4. Serviço: Autorização de Uso da Nota Fiscal (item 4.1 do MOC)

## 4.1 Leiaute da Nota Fiscal Eletrônica (Anexo I do MOC)

Esta Nota Técnica não altera o leiaute da NFC-e, mas para efeito de documentação, são destacadas as séries que serão utilizadas para emissão de NFC-e com sistema próprio. Deverá ser utilizada a mesma série reservada [920-969] da NF-e, conforme documentado na [NT 2018.001](../../../nfe/notas-tecnicas/nt2018-001-v1-10-emitente-cpf/document.md)

## B. Identificação da NF-e (Não altera leiaute)

|   # | ID   | Campo   | Descrição                 | El e   | Pai   | Tip o   | Oco r.   | Tam.   | Observação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-----|------|---------|---------------------------|--------|-------|---------|----------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  11 | B07  | serie   | Série do Documento Fiscal | E      | B01   | N       | 1-1      | 1-3    | Série do Documento Fiscal, preencher com zeros na hipótese de a NF-e não possuir série. Série na faixa - [000-889]: Aplicativo do Contribuinte; Emitente=CNPJ; Assinatura pelo e-CNPJ do contribuinte (procEmi<>1,2); - [890-899]: Emissão no site do Fisco (NFA-e - Avulsa); Emitente= CNPJ / CPF; Assinatura pelo e- CNPJ da SEFAZ (procEmi=1); - [900-909]: Emissão no site do Fisco (NFA-e); Emitente= CNPJ; Assinatura pelo e-CNPJ da SEFAZ (procEmi=1), ou Assinatura pelo e-CNPJ do contribuinte (procEmi=2); - [910-919]: Emissão no site do Fisco (NFA-e); Emitente= CPF; Assinatura pelo e-CNPJ da SEFAZ (procEmi=1), ou Assinatura pelo e-CPF do contribuinte (procEmi=2); |

![Image](assets/image_000011_57f33372fcf6eb4009dc8f4995013d84847d470048e51b8faaa23eb1a9078dd8.png)

![Image](assets/image_000012_5c52a44bfa4d8cf78712fd91b20e22274c87a364934844b309bf8cf1a41ccae0.png)

| - [920-969]: Aplicativo do Contribuinte; Emitente=CPF; Assinatura pelo e-CPF do contribuinte (procEmi<>1,2);   |
|----------------------------------------------------------------------------------------------------------------|

## 4.2 Alteração em Regras de Validação - RV (Anexo II do MOC)

Nesta NT, são melhor documentadas algumas regras de validação já existentes e alteradas regras de validação considerando que o Emitente da NF-e pode ser um CPF. Seguem as alterações em regras de validação:

## B. Identificação da Nota Fiscal

| Campo-Seq   | Modelo   | Regra de Validação                                                                                                                                                                                                                                                                                    | Aplic.   |   Msg | Efeito   | Descrição Erro                                                        |
|-------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|-----------------------------------------------------------------------|
| B26-30      | 55/65    | Se Processo de Emissão pelo Fisco (procEmi=1 ou 2): - Tipo de Emissão difere de 1-Emissão Normal ou Emissão na SVC (tpEmis<>1, 6 e 7) ([NT 2018.001](../../../nfe/notas-tecnicas/nt2018-001-v1-10-emitente-cpf/document.md)/ [NT 2015.002](../../../nfe/notas-tecnicas/nt-2015-002-v141-23-08-2016/document.md)) Exceção 1: Para a UF SC, aceitar Tipo de Emissão igual a 9=Contingência off-line da NFC-e.                                           | Obrig.   |   370 | Rej.     | Rejeição: Processo de emissão pelo Fisco com Tipo de Emissão inválido |
| B26-50      | 65       | Se Tipo de Emissão da NFC-e diferente de Regime Especial NFF (tpEmis<>3): - Processo de Emissão pelo Contribuinte diferente de '0=Emissão de NF-e com aplicativo do contribuinte' (procEmi<>0) Exceção 1: Para a UF SC, a regra não se aplica se Processo de Emissão é pelo Fisco (procEmi = 1 ou 2). | Obrig.   |   957 | Rej.     | Rejeição: Tipo de emissão incompatível com o Processo de Emissão      |

## C. Identificação do Emitente

![Image](assets/image_000013_63d7e434d194075feff964a3e15924128fa13e6d93aabc0a91ce7c731803b665.png)

| Campo-Seq   | Modelo   | Regra de Validação                                                                                                                                     | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                |
|-------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|-----------------------------------------------------------------------------------------------|
| C02a-10     | 55/65    | Se informado CPF do emitente e tpEmis <> 3-NFF ([NT 2021.002](../../../nfe/notas-tecnicas/nt2021-002-v1-12-nota-fiscal-f-cil/document.md)): - Série difere da faixa para emitente CPF: 890-899 e 910-969 ([NT 2018.001](../../../nfe/notas-tecnicas/nt2018-001-v1-10-emitente-cpf/document.md) / [NT 2015.002](../../../nfe/notas-tecnicas/nt-2015-002-v141-23-08-2016/document.md)) | Obrig.   |   495 | Rej.     | Rejeição: CPF do Emitente com Série incompatível                                              |
| C02a-20     | 55/65    | Se informado CPF do emitente: - CPF com zeros, nulo, 111..., 222..., ..., ou DV inválido ([NT 2012/003](../../../nfe/notas-tecnicas/nt2012-003d/document.md))                                                 | Obrig.   |   401 | Rej.     | Rejeição: CPF do emitente inválido                                                            |
| C02a-30     | 55/65    | Se informado CPF do emitente: - CPF do Emitente difere do CPF da primeira NF-e do Lote recebido                                                        | Facult.  |   560 | Rej.     | Rejeição: CNPJ Base/CPF do emitente difere do CNPJ Base/CPF da primeira NF-e do lote recebido |

## 5. Serviço: Evento de Cancelamento (Item 4.3 do MOC)

## 5.1 Alteração em Regras de Validação (Item 4.3.7-e e 4.3.8 do MOC)

| #    | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                      | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                              |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|---------------------------------------------------------------------------------------------|
| G04e | Modelo 55/65 Chave de Acesso inválida: - Série = [0-909] e CNPJ zerado ou dígito inválido, ou - Série = [920-969] e CPF zerado ou dígito inválido                                                                                                                                                                                                                                       | Obrig.   |   617 | Rej.     | Rejeição: Chave de Acesso inválida (CNPJ/CPF zerado ou dígito inválido)                     |
| G06  | 55/65 Acesso BD NFE (Chave: CNPJ/CPF Emitente, Modelo, Série e Número): - Chave Acesso inexistente para o tpEvento que exige a existência da NF-e Observação: Se existir no banco de dados uma Chave de Acesso divergente, concatenar na mensagem de erro a Chave de Acesso já existente, caso o CNPJ/CPF do Autor do evento seja o mesmo CNPJ/CPF da Chave de Acesso (opcional). 55/65 | Obrig.   |   494 | Rej.     | Rejeição: Chave de Acesso inexistente [chNFe:99999999999999999999999999999999 999999999999] |
| G08  | Se evento do emissor verificar se CNPJ/CPF do Autor diferente do CNPJ/CPF da Chave de Acesso da NF-e                                                                                                                                                                                                                                                                                    | Obrig.   |   574 | Rej.     | Rejeição: O autor do evento diverge do emissor da NF-e                                      |

![Image](assets/image_000014_8702429d557b971b5753934f67216900e4ec7b1bf8f8f561497d41bd9007440a.png)

## 6. Fim da Denegação na NFC-e

O  Ajuste  SINIEF  10/2023  publicou  a  alteração  no  qual  exclui  a  denegação  na  NFC-e,  portanto,  a  NFC-e  não  será  mais  denegada  por irregularidade fiscal do emitente, e passará a ser rejeitada.

| Campo-Seq Modelo   | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                    | Aplic.   |   Msg | Efeito   | Descrição Erro                                  |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|-------------------------------------------------|
| 1C17-40 55/65      | - Emitente em situação irregular perante o Fisco Observação: o aplicativo emissor de NFF garante que a solicitação de emissão da NF-e é realizada somente para contribuintes ativos; entretanto, como é possível que ocorra um atraso no envio do XML para o ambiente de autorização, nessa situação, de forma excepcional e transitória, poderá acontecer a autorização de uso de uma NF-e para um contribuinte que já não está mais ativo na UF (NT | Obrig.   |   301 | Den.     | Uso Denegado: Irregularidade fiscal do emitente |

Quando o emissor tiver em situação irregular deverá ter a rejeição '781 - Rejeição: Emissor não habilitado para emissão da NFC-e', da regra 1C17-38.

| Campo-Seq Modelo   | Regra de Validação                                                           | Aplic. Msg   | Efeito   | Descrição Erro                                         |
|--------------------|------------------------------------------------------------------------------|--------------|----------|--------------------------------------------------------|
| 1C17-38            | 65 - Emitente não autorizado para emissão de NFC-e irregular perante o Fisco | Obrig. 781   | Rej.     | Rejeição: Emissor não habilitado para emissão da NFC-e |

![Image](assets/image_000015_8702429d557b971b5753934f67216900e4ec7b1bf8f8f561497d41bd9007440a.png)

## 7. Tabela de códigos e descrições de mensagens de erro

|   CÓDIGO | MOTIVO DE NÃO ATENDIMENTO DA SOLICITAÇÃO                                                      |
|----------|-----------------------------------------------------------------------------------------------|
|      126 | Rejeição: Enviado lote com mais de 1 NFC-e                                                    |
|      401 | Rejeição: CPF do emitente inválido                                                            |
|      494 | Rejeição: Chave de Acesso inexistente [chNFe:99999999999999999999999999999999999999999999]    |
|      560 | Rejeição: CNPJ base/CPF do emitente difere do CNPJ base/CPF da primeira NF-e do lote recebido |
|      574 | Rejeição: O autor do evento diverge do emissor da NF-e                                        |
|      617 | Rejeição: Chave de Acesso inválida (CNPJ/CPF zerado ou dígito inválido)                       |
|      781 | Rejeição: Emissor não habilitado para emissão da NFC-e                                        |
|      957 | Rejeição: Tipo de emissão incompatível com o Processo de Emissão                              |
|      961 | Rejeição: Enviado lote com mais de 1 NFC-e                                                    |

![Image](assets/image_000016_8702429d557b971b5753934f67216900e4ec7b1bf8f8f561497d41bd9007440a.png)

## Documentos relacionados
_Nenhum documento relacionado conhecido._
