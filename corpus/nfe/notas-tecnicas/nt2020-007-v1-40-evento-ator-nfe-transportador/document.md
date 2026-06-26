---
title: "Sistema Nota Fiscal Eletrônica"
slug: "nt2020-007-v1-40-evento-ator-nfe-transportador"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "9394c3d8cef55c1a2e6e05b7811bc05cc1f4e66f5190308a1bc6f9c92792bf1f"
converted_at_utc: "2026-06-25T15:51:50.790636+00:00"
status: "published"
type: "nota_tecnica"
---
![Image](assets/image_000000_4f9898c530d8bf82e36dfb5fd14a054dff0ddfd8c9cdd867d989d833a12c8c33.png)

## Sistema Nota Fiscal Eletrônica

Nota Técnica 2020.007

Evento Ator Interessado na NF-e

- Transportador

Versão 1.40 - Agosto 2024

![Image](assets/image_000001_02f41df4d0ce1ff1bed1bc18aa1834a39e4865846ca093b3dacb4ef8bd6365ce.png)

![Image](assets/image_000002_e0f2f4964fc42098f2b3b3a7c6789828e196b197bf1dd605814b2f070478c82a.png)

## Sumário

| Controle de Versões ........................................................................................................................... 3                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Histórico de Alterações / Cronograma................................................................................................. 3                                                                                                                                            |
| 01. Resumo ........................................................................................................................................ 4                                                                                                                              |
| 02. Definições Gerais........................................................................................................................... 4                                                                                                                                 |
| 02.1 Webservice de Evento............................................................................................................. 4                                                                                                                                           |
| 02.2 Prazo da versão em homologação .......................................................................................... 4                                                                                                                                                   |
| 03. Evento 'Ator Interessado na NF-e - Transportador' ...................................................................... 5                                                                                                                                                     |
| 03.1 Leiaute Mensagem de Entrada................................................................................................ 5                                                                                                                                                 |
| 03.2 Leiaute Mensagem de Retorno................................................................................................ 7                                                                                                                                                 |
| 03.3 Processo de Recepção de Evento........................................................................................... 8                                                                                                                                                   |
| 03.4 Validação do Certificado de Transmissão - Geral ................................................................... 8                                                                                                                                                         |
| 03.5 Validação Inicial da Mensagem no Web Service - Geral......................................................... 8                                                                                                                                                               |
| 03.6 Validação da área de Dados - Geral....................................................................................... 8                                                                                                                                                   |
| 03.7 Validação da parte geral do evento ......................................................................................... 9                                                                                                                                                |
| 03.8 Validação da parte específica do evento ................................................................................10                                                                                                                                                    |
| 03.9 Final do Processamento do Lote ............................................................................................12                                                                                                                                                 |
| 90. Mensagens de Erro......................................................................................................................13 90.1 Novos Códigos de Rejeição....................................................................................................13 |

![Image](assets/image_000003_aaeadac0df762b9a31a9ceacc4084091384c0af9a170209927fe044459f3acb5.png)

## Controle de Versões

| Versão   | Publicação     | Descrição                                                            |
|----------|----------------|----------------------------------------------------------------------|
| 1.00     | Setembro/2020  | Publicação da NT em definitivo, após realização de consulta pública. |
| 1.00a    | Novembro/2020  | Correção em regra de validação                                       |
| 1.10     | Fevereiro/2021 | Alteração no prazo de implantação Melhorias na documentação          |
| 1.20     | Outubro/2021   | Alteração no prazo de implantação Melhorias na documentação          |
| 1.21     | Fevereiro/2022 | Alteração no prazo de implantação                                    |
| 1.22     | Outubro/2022   | Alteração no prazo de implantação                                    |
| 1.23     | Fevereiro/2023 | Alteração no prazo de implantação                                    |
| 1.30     | Junho/2023     | Alteração no prazo de implantação Melhorias na documentação          |
| 1.40     | Agosto/2024    | Alteração na RV 4P24-10                                              |

## Histórico de Alterações / Cronograma

| Versão   | Histórico de atualizações                                                                    | Implantação Teste   | Implantação Produção   |
|----------|----------------------------------------------------------------------------------------------|---------------------|------------------------|
| 1.00     | Evento gerado pelo Emitente ou Destinatário informando o Transportador interessado pela NF-e | 01/02/2021          | 05/04/2021             |
| 1.00a    | Correção em regra de validação                                                               | -                   | -                      |
| 1.10     | Alteração no prazo de implantação                                                            | 01/11/2021          | 30/11/2021             |
|          | Melhorias na documentação                                                                    |                     |                        |
| 1.20     | Alteração no prazo de implantação                                                            | 01/03/2022          | 04/04/2022             |
|          | Melhorias na documentação                                                                    |                     |                        |
| 1.21     | Alteração no prazo de implantação                                                            | 07/11/2022          | 05/12/2022             |
| 1.22     | Alteração no prazo de implantação                                                            | 06/03/2023          | 15/05/2023             |
| 1.23     | Alteração no prazo de implantação                                                            | 10/07/2023          | 21/08/2023             |
| 1.30     | Alteração no prazo de implantação Melhorias na documentação                                  | 29/04/2024          | 03/06/2024             |
| 1.40     | Alteração na RV 4P24-10                                                                      | 25/07/2024          | 01/08/2024             |

![Image](assets/image_000004_38634ee29cb5757427c04a1b82d3a078055468a4f3c809e099a1f3b829b90ab3.png)

NT 2020.007 - Evento Ator Interessado na NF-e - Transportador

## 01. Resumo

Um dos grandes desafios do projeto Nota Fiscal Eletrônica é prover para os atores envolvidos nos processos da NF-e informações de seu interesse de forma eficiente e confiável.

No momento da emissão da NF-e, muitas vezes o emitente ainda não definiu o Transportador que ficará responsável pela entrega da mercadoria, impedindo, portanto, que essa informação conste em campo específico da NF-e (tag: CNPJ/CPF, id: X04/X05), ou mesmo no grupo de pessoas autorizadas  a  acessar  o  XML  da  NF-e  (tag:  autXML,  Id:  GA01).  Em  vários  outros  casos,  o responsável pelo transporte é o destinatário e, nesses casos, o Emitente não tem condições de informar o Transportador no XML da NF-e.

O objetivo desta Nota Técnica é permitir que o Emitente informe a identificação do Transportador a qualquer momento, como uma das pessoas autorizadas a acessar o XML da NF-e.

No caso em que o transporte não é de responsabilidade do Emitente, o Destinatário poderá gerar o evento, com o mesmo objetivo de autorizar que o Transportador fique autorizado a acessar o XML da NF-e.

Nos casos de Redespacho ou Subcontratação, definido o transportador contratado, este poderá também autorizar outro transportador participante da mesma operação de transporte a acessar o XML da NF-e.

O Transportador precisa dos dados da NF-e para instrumentalizar seus processos de transporte e, a partir da geração deste evento, possibilita o transportador em buscar o XML da NF-e no Ambiente Nacional, por meio do 'Web Service de Distribuição de DF-e de Interesse dos Atores da NF-e', conforme documentado na NT2014.002.

Este evento somente pode ser gerado no prazo de 6 meses após a data de autorização da NF-e.

## 02. Definições Gerais

## 02.1 Webservice de Evento

O Ambiente Nacional disponibiliza um WebService geral de eventos que é utilizado para manifestação do destinatário e outros tipos de eventos.

Este evento de 'Ator Interessado na NF-e' será implementado unicamente no WebService de eventos do Ambiente Nacional na URL:

https://www.nfe.fazenda.gov.br/NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx

## 02.2 Prazo da versão em homologação

Sobre a liberação de versões, o combinado com as empresas é projetar um prazo de 2 meses entre a implantação da versão em homologação, antes da sua implantação em produção.

No presente caso, a implementação prevista na NT é facultativa, portanto as empresas interessadas nesse assunto podem praticar o prazo que julgarem conveniente em relação à implantação em homologação e a posterior implantação em produção.

![Image](assets/image_000005_6a23b2443cca8ab45c972d8593b1f1c00a2bbf58da65ff83e075f9c83e5ebcd7.png)

![Image](assets/image_000006_38634ee29cb5757427c04a1b82d3a078055468a4f3c809e099a1f3b829b90ab3.png)

## 03. Evento 'Ator Interessado na NF-e - Transportador'

## 03.1 Leiaute Mensagem de Entrada

O Web Service de Registro de Evento possui uma interface genérica, complementada por uma área específica para cada tipo de evento. Segue o leiaute da mensagem de entrada.

Schema XML: envEventoNFe\_v9.99.xsd Schema XML - parte específica: leiauteEventoAtorInteressado\_v1.00.xsd

| #   | Campo         | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Descrição/Observação                                                                                                                                                                                                                         |
|-----|---------------|-------|-------|--------|---------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| P01 | envEvento     | Raiz  | -     | -      | -       | -      | TAG raiz                                                                                                                                                                                                                                     |
| P02 | versao        | A     | P01   | N      | 1-1     | 2v2    | Versão do leiaute                                                                                                                                                                                                                            |
| P03 | idLote        | E     | P01   | N      | 1-1     | 1-15   | Identificador de controle do Lote de envio do Evento. Número sequencial único para identificação do Lote, de uso exclusivo do autor do evento. O Web Service não faz uso deste identificador.                                                |
| P04 | evento        | G     | P01   | xml    | 1-20    | -      | Evento, um lote pode conter até 20 eventos                                                                                                                                                                                                   |
| P05 | versao        | A     | P04   | N      | 1-1     | 2v2    | Versão do leiaute do evento                                                                                                                                                                                                                  |
| P06 | infEvento     | G     | P04   | -      | 1-1     | -      | Grupo de informações do registro do Evento                                                                                                                                                                                                   |
| P07 | Id            | ID    | P06   | C      | 1-1     | 54     | Identificador da TAG a ser assinada, formado por: 'ID' + tpEvento + Chave da NF-e + nSeqEvento                                                                                                                                               |
| P08 | cOrgao        | E     | P06   | N      | 1-1     | 2      | Código do órgão de recepção do Evento, conforme Tabela do IBGE. Código da UF do Emitente, ou: 91 - Ambiente Nacional                                                                                                                         |
| P09 | tpAmb         | E     | P06   | N      | 1-1     | 1      | Identificação do Ambiente: 1=Produção; 2=Homologação                                                                                                                                                                                         |
| P10 | CNPJ          | CE    | P06   | N      | 1-1     | 14     | Informar o CNPJ/CPF do autor do Evento.                                                                                                                                                                                                      |
| P11 | CPF           | CE    | P06   | N      | 1-1     | 11     |                                                                                                                                                                                                                                              |
| P12 | chNFe         | E     | P06   | N      | 1-1     | 44     | Chave de Acesso da NF-e que o evento será vinculado.                                                                                                                                                                                         |
| P13 | dhEvento      | E     | P06   | D      | 1-1     | -      | Data e hora do evento. Formato AAAA-MM-DDThh:mm:ss TZD (UTC)                                                                                                                                                                                 |
| P14 | tpEvento      | E     | P06   | N      | 1-1     | 6      | Código do evento: 110150 - 'Ator interessado na NF-e'                                                                                                                                                                                        |
| P15 | nSeqEvento    | E     | P06   | N      | 1-1     | 1-2    | Sequencial do evento para o mesmo tipo de evento. Valores de 1 a 20.                                                                                                                                                                         |
| P16 | verEvento     | E     | P06   | N      | 1-1     | 2v2    | Versão do grupo de detalhe do evento.                                                                                                                                                                                                        |
| P17 | detEvento     | G     | P06   |        | 1-1     | -      | Detalhes do evento                                                                                                                                                                                                                           |
| P18 | versao        | A     | P17   | N      | 1-1     | 2v2    | Informar o mesmo valor da tag 'verEvento' (P16)                                                                                                                                                                                              |
| P19 | descEvento    | E     | P17   | C      | 1-1     | 5-60   | Descrição do Evento, conforme documentado junto com o Código do Evento (Id: P14).                                                                                                                                                            |
| P20 | cOrgaoAutor   | E     | P17   | N      | 1-1     | 2      | Código da UF do emitente do Evento.                                                                                                                                                                                                          |
| P21 | tpAutor       | E     | P17   | N      | 1-1     | 1      | Informar uma das opções abaixo: 1=Geração do Evento pelo Emitente; 2=Geração do Evento pelo Destinatário; 3=Geração do Evento pelo Transportador Contratado; Valores : 1=Empresa Emitente, 2=Empresa Destinatária; 3=Empresa Transportadora. |
| P22 | verAplic      | E     | P17   | C      | 1-1     | 1-20   | Versão do aplicativo do Autor do Evento.                                                                                                                                                                                                     |
| P23 | autXML        | G     | P17   | -      | 1-1     | -      | Pessoas autorizadas a acessar o XML da NF-e                                                                                                                                                                                                  |
| P24 | CNPJ          | CE    | P23   | N      | 1-1     | 3-14   | CNPJ autorizado                                                                                                                                                                                                                              |
| P25 | CPF           | CE    | P23   | N      | 1-1     | 3-11   | CPF autorizado                                                                                                                                                                                                                               |
| P26 | tpAutorizacao | E     | P17   | N      | 0-1     | 1      | 0 - Não permite; 1 - Permite o transportador autorizado pelo emitente ou destinatário autorizar outros transportadores para ter acesso ao download da NF-e                                                                                   |

## Sistema Nota Fiscal Eletrônica

NT 2020.007 - Evento Ator Interessado na NF-e - Transportador

![Image](assets/image_000007_38634ee29cb5757427c04a1b82d3a078055468a4f3c809e099a1f3b829b90ab3.png)

| #   | Campo     | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Descrição/Observação                                                                                                                                                                                                                                                              |
|-----|-----------|-------|-------|--------|---------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| P27 | xCondUso  | E     | P17   | C      | 0-1     | -      | Condição de uso do tipo de autorização para o transportador: 'O emitente ou destinatário da NF-e, declara que permite o transportador declarado no campo CNPJ/CPF deste evento a autorizar os transportadores subcontratados ou redespachados a terem acesso ao download da NF-e' |
| P91 | Signature | G     | P04   | XML    | 1-1     | -      | Assinatura Digital do documento XML, a assinatura deverá ser aplicada no elemento infEvento.                                                                                                                                                                                      |

## 03.2 Leiaute Mensagem de Retorno

O Web Service de Registro de Evento possui uma interface genérica, complementada por uma área específica para cada tipo de evento. Segue o leiaute da mensagem de retorno (resposta).

Schema XML: retEnvEventoNFe\_v1.0.xsd

| #   | Campo        | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Descrição/Observação                                                                                                                                                                                |
|-----|--------------|-------|-------|--------|---------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R01 | retEnvEvento | Raiz  | -     | -      | -       | -      | TAG raiz da mensagem de retorno                                                                                                                                                                     |
| R02 | versao       | A     | R01   | N      | 1-1     | 2v2    | Versão do leiaute                                                                                                                                                                                   |
| R03 | idLote       | E     | R01   | N      | 1-1     | 1-15   | Idem a mensagem de entrada.                                                                                                                                                                         |
| R04 | tpAmb        | E     | R01   | N      | 1-1     | 1      | Idem a mensagem de entrada.                                                                                                                                                                         |
| R05 | verAplic     | E     | R01   | C      | 1-1     | 1-20   | Versão da aplicação que processou o evento.                                                                                                                                                         |
| R06 | cOrgao       | E     | R01   | N      | 1-1     | 2      | Órgão de recepção do Evento, idem a mensagem de entrada.                                                                                                                                            |
| R07 | cStat        | E     | R01   | N      | 1-1     | 3      | Código do status da resposta para o Lote de Eventos. Se não tiver erro, será retornado: '128- Lote de Evento Processado'                                                                            |
| R08 | xMotivo      | E     | R01   | C      | 1-1     | 1-255  | Descrição do status da resposta                                                                                                                                                                     |
| R09 | retEvento    | G     | R01   | -      | 0-20    | -      | Grupo do resultado do processamento do para cada Evento                                                                                                                                             |
| R10 | versao       | A     | R09   | N      | 1-1     | 2v2    | Versão do leiaute                                                                                                                                                                                   |
| R11 | infEvento    | G     | R09   |        | 1-1     | -      | Grupo de informações do registro do Evento                                                                                                                                                          |
| R12 | Id           | ID    | R11   | C      | 0-1     | 17     | Identificador da TAG a ser assinada, somente deve ser informado se o órgão de registro assinar a resposta. No caso de assinatura, preencher com o número do protocolo, precedido pela literal 'ID'. |
| R13 | tpAmb        | E     | R11   | N      | 1-1     | 1      | Idem a mensagem de entrada.                                                                                                                                                                         |
| R14 | verAplic     | E     | R11   | C      | 1-1     | 1-20   | Versão da aplicação que registrou o Evento, utilizar literal que permita a identificação do órgão, como a sigla da UF ou do órgão.                                                                  |
| R15 | cOrgao       | E     | R11   | N      | 1-1     | 2      | Idem a mensagem de entrada.                                                                                                                                                                         |
| R16 | cStat        | E     | R11   | N      | 1-1     | 3      | Código do status da resposta.                                                                                                                                                                       |
| R17 | xMotivo      | E     | R11   | C      | 1-1     | 1-255  | Descrição do status da resposta.                                                                                                                                                                    |
| R18 | chNFe        | E     | R11   | N      | 0-1     | 44     | Idem a mensagem de entrada.                                                                                                                                                                         |
| R19 | tpEvento     | E     | R11   | N      | 0-1     | 6      | Idem a mensagem de entrada.                                                                                                                                                                         |
| R20 | xEvento      | E     | R11   | C      | 0-1     | 5-60   | Idem a mensagem de entrada.                                                                                                                                                                         |
| R21 | nSeqEvento   | E     | R11   | N      | 0-1     | 1-2    | Idem a mensagem de entrada.                                                                                                                                                                         |
| R22 | cOrgaoAutor  | E     | R11   | N      | 0-1     | 2      | Idem a mensagem de entrada.                                                                                                                                                                         |
| R50 | dhRegEvento  | E     | R11   | D      | 1-1     | -      | Data e hora de registro do evento no formato AAAA-MM-DDTHH:MM:SS TZD (formato UTC). Se o evento for rejeitado informar a data e hora de recebimento do evento.                                      |
| R51 | nProt        | E     | R11   | N      | 0-1     | 15     | Número Protocolo do Evento 1 posição (1- Secretaria da Fazenda Estadual, 2-RFB), 2 posições para o código da UF, 2 posições para o ano e 10 posições para o sequencial no ano.                      |
| R91 | Signature    | G     | R09   | XML    | 0-1     | -      | Assinatura Digital do documento XML, a assinatura deverá ser aplicada no elemento infEvento. A decisão de assinar a mensagem fica a critério da UF.                                                 |

Nota: No caso de evento registrado com sucesso, os campos opcionais serão retornados.

![Image](assets/image_000008_38634ee29cb5757427c04a1b82d3a078055468a4f3c809e099a1f3b829b90ab3.png)

## 03.3 Processo de Recepção de Evento

O Web Service de Evento é acionado pelo interessado, que deve enviar mensagem com o pedido de autorização do evento da NF-e. O processo de Registro de Eventos recebe eventos em uma estrutura de lotes, que pode conter de 1 a 20 eventos.

## 03.4 Validação do Certificado de Transmissão - Geral

Regras de validação idênticas aos demais Web Services, podendo gerar os erros:

- 280: 'Rejeição: Certificado Transmissor inválido'
- 281: 'Rejeição: Certificado Transmissor Data Validade'
- 283: 'Rejeição: Certificado Transmissor - erro Cadeia de Certificação'
- 286: 'Rejeição: Certificado Transmissor erro no acesso a LCR'
- 284: 'Rejeição: Certificado Transmissor revogado'
- 285: 'Rejeição: Certificado Transmissor difere ICP-Brasil'
- 282: 'Rejeição: Certificado Transmissor sem CNPJ/CPF'

## 03.5 Validação Inicial da Mensagem no Web Service - Geral

Regras de validação idênticas aos demais Web Services, podendo gerar os erros:

- 214: 'Rejeição: Tamanho da mensagem excedeu o limite estabelecido'
- 108: 'Serviço Paralisado Momentaneamente (curto prazo)'
- 109: 'Serviço Paralisado sem Previsão'
- 410: 'Rejeição: UF informada no campo cUF não é atendida pelo WebService'
- 239: 'Rejeição: Versão do arquivo XML não suportada'

## 03.6 Validação da área de Dados - Geral

## a) Validação de forma da área de dados

Regras de validação idênticas aos demais Web Services, podendo gerar os erros:

- 516: 'Rejeição: Falha Schema XML, inexiste a tag raiz esperada para a mensagem'
- 517: 'Rejeição: Falha Schema XML, inexiste atributo versão na tag raiz da mensagem'
- 215: 'Rejeição: Falha Schema XML'
- 587: 'Rejeição: Usar somente o namespace padrão da NF-e'
- 588: 'Rejeição: Não é permitida a presença de caracteres de edição no início/fim da mensagem ou entre as tags da mensagem'
- 404: 'Rejeição: Uso de prefixo de namespace não permitido'
- 402: 'Rejeição: XML da área de dados com codificação diferente de UTF-8'

## b) Extração dos eventos do lote e validação do Schema XML do evento

Regras de validação idênticas aos demais Eventos, podendo gerar os erros:

- 491: 'Rejeição: O tpEvento informado invalido'
- 492: 'Rejeição: O verEvento informado invalido'
- 493: 'Rejeição: Evento não atende o Schema XML específico'

## c) Validação do Certificado Digital de Assinatura

Regras de validação idênticas aos demais Web Services, podendo gerar os erros:

- 290: 'Rejeição: Certificado Assinatura inválido'
- 291: 'Rejeição: Certificado Assinatura Data Validade'
- 292: 'Rejeição: Certificado Assinatura sem CNPJ/CPF'
- 293: 'Rejeição: Certificado Assinatura - erro Cadeia de Certificação'
- 296: 'Rejeição: Certificado Assinatura erro no acesso a LCR'

![Image](assets/image_000009_aaeadac0df762b9a31a9ceacc4084091384c0af9a170209927fe044459f3acb5.png)

- 294: 'Rejeição: Certificado Assinatura revogado'

- 295: 'Rejeição: Certificado Assinatura difere ICP-Brasil'

## d) Validação da Assinatura Digital

Regras de validação idênticas aos demais Web Services, podendo gerar os erros:

- 298: 'Rejeição: Assinatura difere do padrão do Sistema'

- •

- 297: 'Rejeição: Assinatura difere do calculado'

- 213: 'Rejeição: CNPJ-Base do Autor difere do CNPJ-Base do Certificado Digital'

- 227: 'Rejeição: CPF do Emitente difere do CPF do Certificado Digital'

## 03.7 Validação da parte geral do evento

| #       | Regra de Validação                                                                                                                                                               | Aplic.   |   Msg | Descrição Erro                                                                                                        |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|-----------------------------------------------------------------------------------------------------------------------|
| P07-10  | Atributo 'Id' não corresponde à concatenação doscampos do evento ('ID' + tpEvento + chNFe + nSeqEvento) (*1)                                                                     | Obrig.   |   572 | Rejeição: Erro Atributo ID do evento não corresponde a concatenação dos campos ('Id' + tpEvento + chNFe + nSeqEvento) |
| P08-10  | Código do órgão de recepção do Evento diverge dodefinido para este evento (*1)                                                                                                   | Obrig.   |   250 | Rejeição: UF diverge da UF autorizadora                                                                               |
| P09-10  | Tipo do ambiente difere do ambiente do Web Service(*1)                                                                                                                           | Obrig.   |   252 | Rejeição: Ambiente informado diverge do Ambiente de recebimento                                                       |
| P10-10  | Se informado CNPJ do Autor do Evento: - CNPJ inválido (zeros, nulo ou DV inválido) (*1)                                                                                          | Obrig.   |   489 | Rejeição: CNPJ informado inválido (DV ou zeros)                                                                       |
| P11-10  | Se informado o CPF do Autor do evento: - CPF inválido (zeros, nulo ou DV inválido) (*1)                                                                                          | Obrig.   |   490 | Rejeição: CPF informado inválido (DV ou zeros)                                                                        |
| P12-10  | Validação da Chave de Acesso da NF-e (tag:chNFe): - Dígito verificador inválido (*1)                                                                                             | Obrig.   |   236 | Rejeição: Chave de Acesso com dígito verificador inválido                                                             |
| P12-14  | - Código UF inválido (*1)                                                                                                                                                        | Obrig.   |   614 | Rejeição: Chave de Acesso inválida (Código UF inválido)                                                               |
| P12-18  | - Ano < 06 ou Ano maior que Ano corrente (*1)                                                                                                                                    | Obrig.   |   615 | Rejeição: Chave de Acesso inválida (Ano < 06 ou Ano maior que Ano corrente)                                           |
| P12-22  | - Mês = 0 ou Mês > 12 (*1)                                                                                                                                                       | Obrig.   |   616 | Rejeição: Chave de Acesso inválida (Mês < 1 ou Mês > 12)                                                              |
| P12-26  | - CNPJ/CPF zerado ou dígito inválido (*1) Nota: Considerar a Série para determinar se CNPJ/CPF na Chave de Acesso. CNPJ: Série=[0-909], CPF: Série<>[0-909]                      | Obrig.   |   617 | Rejeição: Chave de Acesso inválida (CNPJ/CPF zerado ou dígito inválido)                                               |
| P12-30A | - Eventos somente da NF-e: - Modelo diferente de 55                                                                                                                              | Obrig.   |   450 | Rejeição: Modelo da NF-e diferente de 55                                                                              |
| J02f    | Chave de Acesso inválida (modelo diferente de 55 e 65) (NT 2013.005)                                                                                                             | Obrig.   |   618 | Rejeição: Chave de Acesso inválida (modelo diferente de 55 e 65)                                                      |
| P12-34  | - Número NF = 0 (*1)                                                                                                                                                             | Obrig.   |   619 | Rejeição: Chave de Acesso inválida (número NF = 0)                                                                    |
| P12-40  | Se tpAutor=1-Empresa Emitente: - UF da Chave de Acesso diverge da UFAutorizadora                                                                                                 | Obrig.   |   249 | Rejeição: UF da Chave de Acesso diverge da UF autorizadora                                                            |
| P12-44  | - CNPJ/CPF do Autor diverge do CNPJ/CPF daChave de Acesso (*1) Nota: Considerar a Série para determinar seCNPJ/CPF na Chave de Acesso. CNPJ: Série=[0-909], CPF: Série<>[0- 909] | Obrig.   |   574 | Rejeição: Autor do evento diverge do emissor da NF-e                                                                  |

![Image](assets/image_000010_38634ee29cb5757427c04a1b82d3a078055468a4f3c809e099a1f3b829b90ab3.png)

![Image](assets/image_000011_aaeadac0df762b9a31a9ceacc4084091384c0af9a170209927fe044459f3acb5.png)

| P13-10                       | Data do evento maior que a data de processamento(aceitar tolerância de até 5 minutos) (*2)   | Obrig.                       | 578                          | Rejeição: A data do evento não pode ser maior que a data do processamento   |
|------------------------------|----------------------------------------------------------------------------------------------|------------------------------|------------------------------|-----------------------------------------------------------------------------|
| *** Banco de Dados: Emitente | *** Banco de Dados: Emitente                                                                 | *** Banco de Dados: Emitente | *** Banco de Dados: Emitente | *** Banco de Dados: Emitente                                                |

## (*1) Essa regra somente deve ser aplicada se tpAutor=1

(*2) Validações genéricas do Registro de Evento.

## 03.8 Validação da parte específica do evento

| #      | Regra de Validação                                                                                                                        | Aplic.   | Msg   | Descrição Erro                                                            |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|---------------------------------------------------------------------------|
| P15-10 | Número de sequência do Evento maior que 20                                                                                                | Obrig.   | 594   | Rejeição: Número de sequência do evento informado é maior que o permitido |
| P20-10 | Se tpAutor=1-Empresa Emitente: - UF do Autor (cOrgaoAutor) diverge da UF da Chave de Acesso                                               | Obrig.   | 455   | Rejeição: Órgão Autor do evento difere da UF da Chave de Acesso           |
| P21-10 | Tipo do Autor difere de '1=Empresa Emitente', '2=Empresa destinatária' ou '3=Empresa Transportador Contratado.                            | Obrig.   | 466   | Rejeição: Evento com Tipo de Autor incompatível                           |
| P24-10 | Se informado CNPJ autorizado: - CNPJ com zeros ou dígito inválido                                                                         | Obrig.   | 323   | Rejeição: CNPJ autorizado para download inválido                          |
| P25-10 | Se informado CPF autorizado: - CPF com zeros ou dígito inválido                                                                           | Obrig.   | 325   | Rejeição: CPF autorizado para download inválido                           |
| P26-10 | Se autor do evento for o emitente ou destinatário da NF-e: - Obrigatório o preenchimento do campo tpAutorizacao                           | Obrig    | 827   | Rejeição: Obrigatório informar o tipo de autorização                      |
| P26-20 | Se autor do evento não for o emitente ou destinatário da NF-e: - Preenchimento do campo tpAutorizacao não é permitido                     | Obrig    | 828   | Rejeição: Não permitido informar o campo tipo de autorização              |
| P27-10 | Se informado tpAutorizacao igual 1: - Obrigatório informar o campo xCondUso, declarando que está ciente da permissão para o transportador | Obrig.   | 829   | Rejeição: Condição de uso não informado para o tipo de autorização de uso |
| P27-20 | Se informado tpAutorizacao diferente de 1: Preenchimento do campo xCondUso não é permitido                                                | Obrig    | 830 R | Rejeição: Não permitido preencher o campo Condição de Uso                 |

| H03     | Verificar prazo de recepção do evento, em relação a data da autorização da NF-e Obs: 6 meses                 | Obrig.   |   596 | Rejeição: Evento apresentado fora do prazo: [prazo vigente]   |
|---------|--------------------------------------------------------------------------------------------------------------|----------|-------|---------------------------------------------------------------|
| 2P21-10 | - Se tpAutor=2-Empresa Destinatário: - CNPJ/CPF do Autor diverge do CNPJ/CPF do Destinatário da NF-e         | Obrig.   |   575 | Rejeição: Autor do evento diverge do destinatário da NF-e     |
| 2P21-14 | - Se tpAutor=2-Empresa Destinatário: - Modalidade de Frete não é por conta do Destinatário (modFrete<>1 e 4) | Obrig.   |   449 | Rejeição: Modalidade de Frete não é por conta do Destinatário |
| 2P24-10 | - CNPJ/CPF autorizado neste evento idêntico ao CNPJ/CPF do Emitente                                          | Obrig.   |   421 | Rejeição: Informado o CNPJ/CPF do Emitente                    |
| P24-14  | - CNPJ/CPF autorizado neste evento idêntico ao CNPJ/CPF do Destinatário                                      | Obrig.   |   422 | Rejeição: Informado o CNPJ/CPF do Destinatário                |

![Image](assets/image_000012_aaeadac0df762b9a31a9ceacc4084091384c0af9a170209927fe044459f3acb5.png)

| *** Banco de Dados: NF-e Acesso                            | *** Banco de Dados: NF-e Acesso                                                                                                                                                                                                                                                                   | *** Banco de Dados: NF-e Acesso                            | *** Banco de Dados: NF-e Acesso                            | *** Banco de Dados: NF-e Acesso                                                    |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------------------------------|
| 2P12-10                                                    | BD NFE (Chave: Chave de Acesso): - Chave Acesso inexistente para o tpEvento que exige a existência da NF-e (*1)                                                                                                                                                                                   | Obrig.                                                     | 494                                                        | Rejeição: Chave de Acesso Inexistente                                              |
| 2P12-22                                                    | - Verificar se NF-e está denegada ou cancelada                                                                                                                                                                                                                                                    | Obrig.                                                     | 580                                                        | Rejeição: Evento exige uma NF-e autorizada                                         |
| 2P13-10                                                    | - Data do evento menor que a Data de Emissão da NF-e (*1)                                                                                                                                                                                                                                         | Obrig.                                                     | 577                                                        | Rejeição: A data do evento não pode ser menor que a data de emissão da NF-e        |
| 2P13-14                                                    | - Data do evento menor que a Data de Autorização da NF-e não emitida em contingência (tpEmis=1) Nota : Tolerância de 5 minutos, devido ao sincronismo de horário entre o servidor da Empresa e o servidor da SEFAZ Autorizadora.                                                                  | Obrig.                                                     | 579                                                        | Rejeição: A data do evento não pode ser menor que a data de autorização da NF-e    |
| #                                                          | #                                                                                                                                                                                                                                                                                                 | #                                                          | #                                                          | #                                                                                  |
|                                                            | Regra de Validação                                                                                                                                                                                                                                                                                | Aplic.                                                     | Msg                                                        | Descrição Erro                                                                     |
| P24-18                                                     | - CNPJ/CPF autorizado neste evento já está autorizado a acessar o XML da NF-e (leiaute NF- e, tag: autXML, Id:GA01)                                                                                                                                                                               | Obrig.                                                     | 423                                                        | Rejeição: CNPJ/CPF já está autorizado a acessar o XML da NF-e                      |
| *** Banco de Dados: Evento                                 | *** Banco de Dados: Evento                                                                                                                                                                                                                                                                        | *** Banco de Dados: Evento                                 | *** Banco de Dados: Evento                                 | *** Banco de Dados: Evento                                                         |
| 3P15-10                                                    | Acesso BD de Eventos (Chave: Chave de Acesso, tpEvento, nSeqEvento, cOrgaoAutor): - Evento já existente (*1)                                                                                                                                                                                      | Obrig.                                                     | 573                                                        | Rejeição: Duplicidade de Evento                                                    |
| *** Banco de Dados: Evento 2                               | *** Banco de Dados: Evento 2                                                                                                                                                                                                                                                                      | *** Banco de Dados: Evento 2                               | *** Banco de Dados: Evento 2                               | *** Banco de Dados: Evento 2                                                       |
| 3P15-10                                                    | Acesso BD de Eventos (Chave: Chave de Acesso, tpEvento=110150): - CNPJ/CPF autorizado neste evento já está autorizado a acessar o XML da NF-e                                                                                                                                                     | Obrig.                                                     | 423                                                        | Rejeição: CNPJ/CPF já está autorizado a acessar o XML da NF-e                      |
| 3P15-20                                                    | - Evento do BD possui tpAutorizacao=0 para CPF/CNPJ autorizado igual ao CPF/CNPJ autorizado do autor do evento atual.                                                                                                                                                                             | Obrig.                                                     | 831                                                        | Rejeição: Transportador Contratado não autorizado a a liberar acesso a NF-e        |
| 3P15-21                                                    | Se tpAutor=3-Transportador Contratado - Acesso ao BD de Eventos (Chave: Chave de Acesso, tpEvento=110150): Se não Existe CNPJ/CPF autorizado = CNPJ do Autor do evento atual com tpAutorizacao = 1? - Se não existe evento no banco de dados para o autor do evento atual e para a chave indicada | Obrig.                                                     | 585                                                        | Rejeição: Transportador não autorizado a emitir evento para esse documento fiscal. |
| *** Banco de Dados: Cadastro Centralizado de Contribuintes | *** Banco de Dados: Cadastro Centralizado de Contribuintes                                                                                                                                                                                                                                        | *** Banco de Dados: Cadastro Centralizado de Contribuintes | *** Banco de Dados: Cadastro Centralizado de Contribuintes | *** Banco de Dados: Cadastro Centralizado de Contribuintes                         |
| 4P21-10                                                    | Se tpAutor=3-Transportador Contratado: -Acesso Cadastro Centralizado de Contribuintes (Chave: cOrgaoAutor, CNPJ/CPF Autor): - CNPJ/CPF Autor do evento não é emitente de CT-e (nenhum Modal), ou não está ativo para a UF                                                                         | Obrig.                                                     | 448                                                        | Rejeição: CNPJ/CPF Autor não é emitente de CT-e                                    |
| 4P24-10                                                    | Acesso CCC-Cadastro Centralizado de Contribuintes (Chave: cOrgaoAutor , CNPJ/CPF Autorizado): - CNPJ/CPF autorizado neste evento não é emitente de CT-e (nenhum Modal), ou não está ativo para a UF                                                                                               | Obrig.                                                     | 371                                                        | Rejeição: CNPJ/CPF Autorizado não é emitente de CT-e                               |

## 03.9 Final do Processamento do Lote

O processamento do lote pode resultar em:

- Rejeição do Lote: por algum problema que comprometa o processamento do lote;
- Processamento do Lote: o lote foi processado (cStat='128 - Lote de Evento Processado'), e a validação de cada evento do lote poderá resultar em:
- Rejeição: o Evento será rejeitado, retornando do código do status do motivo da rejeição;
- Evento Autorizado, com vinculação à respectiva NF-e :  Encontrada a NF-e no banco de dados. Retornar cStat='135-Evento registrado e vinculado a NF-e';
- Evento Autorizado, sem vinculação à respectiva NF-e: Não encontrada a NF-e no banco de dados. Retornar cStat='136-Evento registrado, mas não vinculado a NF-e';

![Image](assets/image_000013_aaeadac0df762b9a31a9ceacc4084091384c0af9a170209927fe044459f3acb5.png)

## 90. Mensagens de Erro

## 90.1 Novos Códigos de Rejeição

|   Código | Descrição                                                                          |
|----------|------------------------------------------------------------------------------------|
|      371 | Rejeição: CNPJ/CPF Autorizado não é emitente de CT-e                               |
|      421 | Rejeição: Informado o CNPJ/CPF do Emitente                                         |
|      422 | Rejeição: Informado o CNPJ/CPF do Destinatário                                     |
|      423 | Rejeição: CNPJ/CPF já está autorizado a acessar o XML da NF-e                      |
|      448 | Rejeição: CNPJ/CPF Autor não é emitente de CT-e                                    |
|      449 | Rejeição: Modalidade de Frete não é por conta do Destinatário                      |
|      585 | Rejeição: Transportador não autorizado a emitir evento para esse documento fiscal. |
|      827 | Rejeição: Obrigatório informar o tipo de autorização                               |
|      828 | Rejeição: Não permitido informar o campo tipo de autorização                       |
|      829 | Rejeição: Condição de uso não informado para o tipo de autorização de uso          |
|      830 | Rejeição: Não permitido preencher o campo Condição de Uso                          |
|      831 | Rejeição: Transportador Contratado não autorizado a a liberar acesso a NF-e        |

![Image](assets/image_000014_38634ee29cb5757427c04a1b82d3a078055468a4f3c809e099a1f3b829b90ab3.png)