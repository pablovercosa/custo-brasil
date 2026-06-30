---
title: "Sistema Nota Fiscal Eletrônica"
slug: "nt2024-002-v1-00-econf"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "8ca5bff382332103108f0e6ea52eb8be0f9a61030774077f09289391ba03b7e7"
converted_at_utc: "2026-06-25T16:28:02.165522+00:00"
status: "published"
type: "nota_tecnica"
---
![Image](assets/image_000000_b99ce6ecd4c1d044f602fecc97027f67c2f6c0878f6ceb8c7b5be4212d027840.png)

![Image](assets/image_000001_55843cdb6e86ec03a0e8303faaa9c88b0581d763d1c0e592d943e0d68c25d2fa.png)

## Sistema Nota Fiscal Eletrônica

Nota Técnica 2024.002

Evento de Conciliação Financeira - ECONF

Versão 1.00 - Maio 2024

![Image](assets/image_000002_5e39dc17f37a536669b7b641067843ce12cd3b73aba4292900224ca21e8786c8.png)

![Image](assets/image_000003_f45a268df27afc36d690415e03e1c8481c93cb35c3981a3c506888c255f3714c.png)

NT 2024.002 - Evento de Conciliação Financeira - ECONF.

## Sumário

| Controle de   | Versões ...................................................................................................................................................................................................... 3            |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Histórico de  | Alterações / Cronograma............................................................................................................................................................................ 3                       |
| 1.            | Resumo................................................................................................................................................................................................................... 4 |
| 2.            | Visão Geral.............................................................................................................................................................................................................. 4 |
| 2.1.          | Webservice de Evento....................................................................................................................................................................................... 4               |
| 3.            | Evento 'Conciliação Financeira - ECONF'.............................................................................................................................................................. 4                     |
| 3.1.          | Leiaute Mensagem de Entrada........................................................................................................................................................................... 4                    |
| 3.2.          | Leiaute Mensagem de Retorno........................................................................................................................................................................... 7                    |
| 3.3.          | Processo de Recepção de Evento...................................................................................................................................................................... 8                      |
| 3.4.          | Validação do Certificado de Transmissão - Geral............................................................................................................................................... 8                            |
| 3.5.          | Validação Inicial da Mensagem no Web Service - Geral .................................................................................................................................... 8                                 |
| 3.6.          | Validação da área de Dados - Geral.................................................................................................................................................................. 9                      |
| 3.7.          | Validação das Regras de Negócio.................................................................................................................................................................... 10                      |
| 3.8.          | Final do Processamento do Lote....................................................................................................................................................................... 11                    |
| 4. Evento     | 'Cancelamento Conciliação Financeira - ECONF'.................................................................................................................................... 12                                        |
| 4.1.          | Leiaute Mensagem de Entrada......................................................................................................................................................................... 12                     |
| 4.2.          | Leiaute Mensagem de Retorno......................................................................................................................................................................... 13                     |
| 4.3.          | Processo de Recepção de Evento.................................................................................................................................................................... 14                       |
| 4.4.          | Validação do Certificado de Transmissão - Geral ........................................................................................................................................... 14                              |
| 4.5.          | Validação Inicial da Mensagem no Web Service - Geral................................................................................................................................. 14                                    |
| 4.6.          | Validação da área de Dados - Geral................................................................................................................................................................ 14                       |
| 4.7.          | Validação das Regras de Negócio................................................................................................................................................................... 14                       |
| 4.8.          | Final do Processamento do Lote....................................................................................................................................................................... 16                    |

![Image](assets/image_000004_1224b2dfc1de7af666a46f761bb0ec0b59e52287035e89826eb9ad6d96a49e01.png)

## Controle de Versões

|   Versão | Publicação   | Descrição        |
|----------|--------------|------------------|
|     1.00 | Maio/2024    | Publicação da NT |

## Histórico de Alterações / Cronograma

|   Versão | Histórico de atualizações   | Implantação Teste   | Implantação Produção   |
|----------|-----------------------------|---------------------|------------------------|
|     1.00 | Publicação da NT            | Até 01/07/2024      | 02/09/2024             |

![Image](assets/image_000005_6b90574bd841205e76d82e373f6e14d369184d061245c4d6d7725ab0095483fb.png)

## 1. Resumo

Esta nota técnica tem o objetivo de prover aos atores envolvidos nos processos da NF-e/NFC-e a possibilidade de anotar no documento fiscal eletrônico as transações financeiras relacionadas a operação, facilitando a vinculação entre documentos fiscais e recursos financeiros recebidos.

Busca-se encontrar uma solução para pagamentos que ocorrem distantes da data do fato gerador e da emissão do documento fiscal. Portanto, para que seja possível às empresas informarem que o recebimento de recurso está relacionado a determinado documento fiscal, está sendo criado o Evento de Conciliação Financeira - ECONF. Os Ajustes SINIEF nº 3/2023 e 10/2023 prevêem este evento.

A utilização do Evento de Conciliação Financeira - ECONF é facultativa e tem o objetivo de auxiliar as empresas que buscam demonstrar a existência de conformidade fiscal entre as informações financeiras e de meios de pagamentos e os documentos fiscais emitidos.

## 2. Visão Geral

## 2.1.  Webservice de Evento

Para o modelo 55 (NF-e), a Sefaz Virtual do Rio Grande do Sul (SVRS) disponibiliza o WebService de eventos que será utilizado por contribuintes de todas as unidades federadas para autorização do ECONF, no endereço do Webservice de Eventos da SVRS: https://nfe.svrs.rs.gov.br/ws/recepcaoevento/recepcaoevento4.asmx.

Para o modelo 65 (NFC-e), os Contribuintes deverão usar o Webservice de Eventos próprio da UF (mesma URL utilizada para o Evento de Cancelamento).

## 3. Evento 'Conciliação Financeira - ECONF'

## 3.1.  Leiaute Mensagem de Entrada

O Web Service de Registro de Evento possui uma interface genérica complementada por uma área específica para cada tipo de evento. Segue o leiaute da mensagem de entrada.

## Schema XML: envEventoNFe\_v9.99.xsd

## Schema XML - parte específica: leiauteEventoConciliacaoFinanceira\_v1.00.xsd

| #   | Campo     | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Descrição/Observação                                                                                                                                                                        |
|-----|-----------|-------|-------|--------|---------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| P01 | envEvento | Raiz  | -     | -      | -       | -      | TAGraiz                                                                                                                                                                                     |
| P02 | versao    | A     | P01   | N      | 1-1     | 2v2    | Versão do leiaute                                                                                                                                                                           |
| P03 | idLote    | E     | P01   | N      | 1-1     | 1-15   | Identificador de controle do Lote de envio do Evento. Númerosequencial único para identificação do Lote, de uso exclusivo do autor do evento.O Web Service não faz uso deste identificador. |

![Image](assets/image_000006_2a0fdef6f813e8d8af75ea308556fcb4a3b56dc022062b6e3e02687e191e47e4.png)

![Image](assets/image_000007_6b90574bd841205e76d82e373f6e14d369184d061245c4d6d7725ab0095483fb.png)

| #   | Campo         | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Descrição/Observação                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----|---------------|-------|-------|--------|---------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| P04 | evento        | G     | P01   | xml    | 1-20    | -      | Evento, umlote pode conter até 20 eventos                                                                                                                                                                                                                                                                                                                                                                                                  |
| P05 | versao        | A     | P04   | N      | 1-1     | 2v2    | Versão do leiaute do evento                                                                                                                                                                                                                                                                                                                                                                                                                |
| P06 | infEvento     | G     | P04   | -      | 1-1     | -      | Grupo de informações do registro do Evento                                                                                                                                                                                                                                                                                                                                                                                                 |
| P07 | Id            | ID    | P06   | C      | 1-1     | 54     | Identificador daTAGaser assinada, formado por: 'ID' + tpEvento + Chave da NF -e + nSeqEvento                                                                                                                                                                                                                                                                                                                                               |
| P08 | cOrgao        | E     | P06   | N      | 1-1     | 2      | Código do órgão de recepção do Evento, conforme Tabela do IBGE. Para a NF-e (modelo 55): Informar o código 92-SVRS, utilizando a URL do WSde Eventos da SVRS para este modelo de Documento Fiscal. Para a NFC-e (modelo 65): Se UF participante da SVRS, informar o código 92-SVRS, utilizando a URL do WSde Eventos da SVRS; se não participante, informar o Código da UF do Emitente, para as SEFAZ com ambiente de autorização próprio. |
| P09 | tpAmb         | E     | P06   | N      | 1-1     | 1      | Identificação do Ambiente: 1=Produção; 2=Homologação                                                                                                                                                                                                                                                                                                                                                                                       |
| P10 | CNPJ          | CE    | P06   | N      | 1-1     | 14     | Informar o CNPJ/CPF do autor do Evento.                                                                                                                                                                                                                                                                                                                                                                                                    |
| P11 | CPF           | CE    | P06   | N      | 1-1     | 11     |                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| P12 | chNFe         | E     | P06   | N      | 1-1     | 44     | Chave de Acesso da NF-e que o evento será vinculado.                                                                                                                                                                                                                                                                                                                                                                                       |
| P13 | dhEvento      | E     | P06   | D      | 1-1     | -      | Data e hora do evento. Formato AAAA-MM-DDThh:mm:ss TZD (UTC)                                                                                                                                                                                                                                                                                                                                                                               |
| P14 | tpEvento      | E     | P06   | N      | 1-1     | 6      | Código do evento: 110750 - ' ECONF '                                                                                                                                                                                                                                                                                                                                                                                                       |
| P15 | nSeqEvento    | E     | P06   | N      | 1-1     | 1-2    | Sequencial do evento para o mesmotipo de evento. Valores de 1 a 99.                                                                                                                                                                                                                                                                                                                                                                        |
| P16 | verEvento     | E     | P06   | N      | 1-1     | 2v2    | Versão do grupo de detalhe do evento.                                                                                                                                                                                                                                                                                                                                                                                                      |
| P17 | detEvento     | G     | P06   |        | 1-1     | -      | Detalhes do evento                                                                                                                                                                                                                                                                                                                                                                                                                         |
| P18 | versao        | A     | P17   | N      | 1-1     | 2v2    | Informaro mesmovalorda tag 'verEvento' (P16)                                                                                                                                                                                                                                                                                                                                                                                               |
| P19 | descEvento    | E     | P17   | C      | 1-1     | 5-60   | ' ECONF '                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| P20 | verAplic      | E     | P17   | C      | 1-1     | 1-20   | Versão do aplicativo do Autor do Evento.                                                                                                                                                                                                                                                                                                                                                                                                   |
| P21 | detPag        | G     | P17   | -      | 1-100   |        | Grupo de detalhamento do pagamento.                                                                                                                                                                                                                                                                                                                                                                                                        |
| P22 | indPag        | E     | P21   | N      | 0-1     | 1      | 0= Pagamento à Vista 1= Pagamento à Prazo.                                                                                                                                                                                                                                                                                                                                                                                                 |
| P23 | tPag          | E     | P21   | N      | 1-1     | 2      | Meio de Pagamento - Utilizar a Tabela de códigos dos meios de pagamentos publicada no Portal Nacional da Nota Fiscal Eletrônica                                                                                                                                                                                                                                                                                                            |
| P24 | xPag          | E     | P21   | C      | 0-1     | 2-60   | Descrição do meio de pagamento. Preencher informando o meio de pagamento utilizado quando o código do meio de pagamento for informado como 99-outros.                                                                                                                                                                                                                                                                                      |
| P25 | vPag          | E     | P21   | N      | 1-1     | 13v2   | Valor do Pagamento                                                                                                                                                                                                                                                                                                                                                                                                                         |
| P26 | dPag          | E     | P21   | D      | 1-1     | -      | Data do Pagamento no formato AAAA-MM-DD. Em caso de pagamentos agendados, informar a data da efetivação.                                                                                                                                                                                                                                                                                                                                   |
| P27 | Sequência XML | G     | P21   |        | 0-1     |        |                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| P28 | CNPJPag       | E     | P27   | N      | 1-1     | 14     | Preencher informando o CNPJ do estabelecimento onde o pagamento foi processado/transacionado/recebido quando a emissão do documento fiscal ocorrer em estabelecimento distinto.                                                                                                                                                                                                                                                            |
| P29 | UFPag         | E     | P27   | C      | 1-1     | 2      | UF do CNPJ do estabelecimento onde o pagamento foi processado/transacionado/recebido.                                                                                                                                                                                                                                                                                                                                                      |
| P30 | CNPJIF        | E     | P21   | N      | 0-1     | 14     | CNPJ da instituição financeira, de pagamento, adquirente ou subadquirente.                                                                                                                                                                                                                                                                                                                                                                 |

NT 2024.002 - Evento de Conciliação Financeira - ECONF.

![Image](assets/image_000008_6b90574bd841205e76d82e373f6e14d369184d061245c4d6d7725ab0095483fb.png)

| #   | Campo         | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Descrição/Observação                                                                                                                 |
|-----|---------------|-------|-------|--------|---------|--------|--------------------------------------------------------------------------------------------------------------------------------------|
| P31 | tBand         | E     | P21   | N      | 0-1     | 2      | Utilizar a Tabela de Códigos das Operadoras de cartão de crédito e/ou débito publicada no Portal Nacional da Nota Fiscal Eletrônica. |
| P32 | cAut          | E     | P21   | C      | 0-1     | 1-128  | Identifica o número da autorização da transação da operação                                                                          |
| P33 | Sequência XML | G     | P21   |        | 0-1     |        |                                                                                                                                      |
| P34 | CNPJReceb     | E     | P33   | N      | 1-1     | 14     | Informar o CNPJ do estabelecimento beneficiário do pagamento                                                                         |
| P35 | UFReceb       | E     | P33   | C      | 1-1     | 2      | UF do CNPJ do estabelecimento beneficiário do pagamento.                                                                             |
| P91 | Signature     | G     | P04   | XML    | 1-1     | -      | Assinatura Digital do documento XML, a assinatura deverá ser aplicada no elemento infEvento.                                         |

## 3.2.  Leiaute Mensagem de Retorno

O Web Service de Registro de Evento possui uma interface genérica complementada por uma área específica para cada tipo de evento. Segue o leiaute da mensagem de retorno (resposta).

## Schema XML: retEnvEventoNFe\_v1.0.xsd

| #   | Campo        | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Descrição/Observação                                                                                                                                                                          |
|-----|--------------|-------|-------|--------|---------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R01 | retEnvEvento | Raiz  | -     | -      | -       | -      | TAGraiz damensagem de retorno                                                                                                                                                                 |
| R02 | versao       | A     | R01   | N      | 1-1     | 2v2    | Versão do leiaute                                                                                                                                                                             |
| R03 | idLote       | E     | R01   | N      | 1-1     | 1-15   | Idem a mensagem de entrada.                                                                                                                                                                   |
| R04 | tpAmb        | E     | R01   | N      | 1-1     | 1      | Idem a mensagem de entrada.                                                                                                                                                                   |
| R05 | verAplic     | E     | R01   | C      | 1-1     | 1-20   | Versão da aplicação que processouo evento.                                                                                                                                                    |
| R06 | cOrgao       | E     | R01   | N      | 1-1     | 2      | Órgão de recepção do Evento, idem a mensagem de entrada.                                                                                                                                      |
| R07 | cStat        | E     | R01   | N      | 1-1     | 3      | Código do status da resposta para o Lote de Eventos. Se não tiver erro, será retornado: '128 - Lote de Evento Processado'                                                                     |
| R08 | xMotivo      | E     | R01   | C      | 1-1     | 1-255  | Descrição do status da resposta                                                                                                                                                               |
| R09 | retEvento    | G     | R01   | -      | 0-20    | -      | Grupo do resultado do processamento do para cada Evento                                                                                                                                       |
| R10 | versao       | A     | R09   | N      | 1-1     | 2v2    | Versão do leiaute                                                                                                                                                                             |
| R11 | infEvento    | G     | R09   |        | 1-1     | -      | Grupo de informações do registro do Evento                                                                                                                                                    |
| R12 | Id           | ID    | R11   | C      | 0-1     | 17     | Identificador da TAG a ser assinada, somente deve ser informado seo órgão deregistro assinar a resposta. No caso de assinatura, preencher comonúmerodoprotocolo, precedido pela literal 'ID'. |
| R13 | tpAmb        | E     | R11   | N      | 1-1     | 1      | Idem a mensagem de entrada.                                                                                                                                                                   |
| R14 | verAplic     | E     | R11   | C      | 1-1     | 1-20   | Versão da aplicação que registrou o Evento, utilizar literal que permita a identificação do órgão, como a sigla da UF ou do órgão.                                                            |
| R15 | cOrgao       | E     | R11   | N      | 1-1     | 2      | Idem a mensagem de entrada.                                                                                                                                                                   |
| R16 | cStat        | E     | R11   | N      | 1-1     | 3      | Código do status da resposta.                                                                                                                                                                 |
| R17 | xMotivo      | E     | R11   | C      | 1-1     | 1-255  | Descrição do status da resposta.                                                                                                                                                              |
| R18 | chNFe        | E     | R11   | N      | 0-1     | 44     | Idem a mensagem de entrada.                                                                                                                                                                   |
| R19 | tpEvento     | E     | R11   | N      | 0-1     | 6      | Idem a mensagem de entrada.                                                                                                                                                                   |
| R20 | xEvento      | E     | R11   | C      | 0-1     | 5-60   | Idem a mensagem de entrada.                                                                                                                                                                   |
| R21 | nSeqEvento   | E     | R11   | N      | 0-1     | 1-2    | Idem a mensagem de entrada.                                                                                                                                                                   |
| R50 | dhRegEvento  | E     | R11   | D      | 1-1     | -      | Data e hora de registro do evento no formato AAAA-MM-DDTHH:MM:SSTZD(formatoUTC). Seo evento for rejeitado informar a data e hora de recebimento do evento.                                    |

![Image](assets/image_000009_2a0fdef6f813e8d8af75ea308556fcb4a3b56dc022062b6e3e02687e191e47e4.png)

![Image](assets/image_000010_2a0fdef6f813e8d8af75ea308556fcb4a3b56dc022062b6e3e02687e191e47e4.png)

| #   | Campo     | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Descrição/Observação                                                                                                                                                                   |
|-----|-----------|-------|-------|--------|---------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R51 | nProt     | E     | R11   | N      | 0-1     | 15     | Número Protocolo do Evento 1 posição (1- Secretaria da Fazenda Estadual, 2-RFB, 3-SVRS), 2 posições para o código da UF, 2 posições para o ano e 10 posições para o sequencial no ano. |
| R91 | Signature | G     | R09   | XML    | 0-1     | -      | Assinatura Digital do documento XML, a assinatura deverá ser aplicada no elemento infEvento. Adecisão de assinar a mensagem fica a critério da UF.                                     |

Nota: No caso de evento registrado com sucesso, os campos opcionais serão retornados.

## 3.3.  Processo de Recepção de Evento

O Web Service de Evento é acionado pelo interessado, que deve enviar mensagem com o pedido de autorização do evento da NF-e. O processo de Registro de Eventos recebe eventos em uma estrutura de lotes no qual pode conter de 1 a 20 eventos.

## 3.4.  Validação do Certificado de Transmissão - Geral

Regras de validação idênticas aos demais Web Services, podendo gerar os erros:

- 280: 'Rejeição: Certificado Transmissor inválido'

•

- 281: 'Rejeição: Certificado Transmissor Data Validade'

- 283: 'Rejeição: Certificado Transmissor - erro Cadeia de Certificação'

- 286: 'Rejeição: Certificado Transmissor erro no acesso a LCR'

- 284: 'Rejeição: Certificado Transmissor revogado'

- 285: 'Rejeição: Certificado Transmissor difere ICP-Brasil'

- 282: 'Rejeição: Certificado Transmissor sem CNPJ/CPF'

## 3.5.  Validação Inicial da Mensagem no Web Service - Geral

Regras de validação idênticas aos demais Web Services, podendo gerar os erros:

- 214: 'Rejeição: Tamanho da mensagem excedeu o limite estabelecido'

- 108: 'Serviço Paralisado Momentaneamente (curto prazo)'

- 109: 'Serviço Paralisado sem Previsão'

- 410: 'Rejeição: UF informada no campo cOrgão não é atendida pelo WebService'

- 239: 'Rejeição: Versão do arquivo XML não suportada'

## 3.6.  Validação da área de Dados - Geral

## b) Validação de forma da área de dados

Regras de validação idênticas aos demais Web Services, podendo gerar os erros:

- 516: 'Rejeição: Falha Schema XML, inexiste a tag raiz esperada para a mensagem'
- 517: 'Rejeição: Falha Schema XML, inexiste atributo versão na tag raiz da mensagem'
- 215: 'Rejeição: Falha Schema XML'
- 587: 'Rejeição: Usar somente o namespace padrão da NF-e'
- 588: 'Rejeição: Não é permitida a presença de caracteres de edição no início/fim da  mensagem ou entre as tags da mensagem'
- 404: 'Rejeição: Uso de prefixo de namespace não permitido'
- 402: 'Rejeição: XML da área de dados com codificação diferente de UTF-8'

## c) Extração dos eventos do lote e validação do Schema XML do evento

Regras de validação idênticas aos demais Eventos, podendo gerar os erros:

- 491: 'Rejeição: O tpEvento informado invalido'
- 492: 'Rejeição: O verEvento informado invalido'
- 493: 'Rejeição: Evento não atende o Schema XML específico'

## d) Validação do Certificado Digital de Assinatura

Regras de validação idênticas aos demais Web Services, podendo gerar os erros:

- 290: 'Rejeição: Certificado Assinatura inválido'
- 291: 'Rejeição: Certificado Assinatura Data Validade'
- 292: 'Rejeição: Certificado Assinatura sem CNPJ/CPF'
- 293: 'Rejeição: Certificado Assinatura - erro Cadeia de Certificação'
- 296: 'Rejeição: Certificado Assinatura erro no acesso a LCR'
- 294: 'Rejeição: Certificado Assinatura revogado'
- 295: 'Rejeição: Certificado Assinatura difere ICP-Brasil'

## e) Validação da Assinatura Digital

Regras de validação idênticas aos demais Web Services, podendo gerar os erros:

- 298: 'Rejeição: Assinatura difere do padrão do Sistema'
- 297: 'Rejeição: Assinatura difere do calculado'
- 213: 'Rejeição: CNPJ-Base do Autor difere do CNPJ-Base do Certificado Digital'
- 227: 'Rejeição: CPF do Emitente difere do CPF do Certificado Digital'

![Image](assets/image_000011_1224b2dfc1de7af666a46f761bb0ec0b59e52287035e89826eb9ad6d96a49e01.png)

## 3.7.  Validação das Regras de Negócio

| #      | Regra de Validação                                                                                                                                                            | Aplic.   |   Msg | Descrição Erro                                                                                                  |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|-----------------------------------------------------------------------------------------------------------------|
| P07-10 | Atributo 'Id' nãocorrespondeàconcatenação dos campos do evento ('ID' + tpEvento + chNFe + nSeqEvento) (*1)                                                                    | Obrig.   |   572 | Rejeição: Erro AtributoIDdo evento não corresponde a concatenação dos campos ('Id' +tpEvento+chNFe+ nSeqEvento) |
| P08-10 | Código do órgão de recepção do Evento diverge do definido para este evento (*1)                                                                                               | Obrig.   |   250 | Rejeição:UFdivergedaUF autorizadora                                                                             |
| P09-10 | Tipo do ambiente difere do ambientedo WebService (*1)                                                                                                                         | Obrig.   |   252 | Rejeição:Ambienteinformado diverge do Ambiente de recebimento                                                   |
| P10-10 | Se informado CNPJ do Autor do Evento: - CNPJ inválido (zeros, nuloouDV inválido) (*1)                                                                                         | Obrig.   |   489 | Rejeição:CNPJinformado inválido (DV ou zeros)                                                                   |
| P11-10 | Se informado o CPF do Autor do evento: - CPF inválido (zeros, nulo ou DVinválido) (*1)                                                                                        | Obrig.   |   490 | Rejeição:CPFinformado inválido (DV ou zeros)                                                                    |
| P12-10 | Validação da Chave de Acesso da NF-e (tag: chNFe): - Dígito verificador inválido (*1)                                                                                         | Obrig.   |   236 | Rejeição: Chave de Acesso comdígitoverificador inválido                                                         |
| P12-14 | - Código UFinválido (*1)                                                                                                                                                      | Obrig.   |   614 | Rejeição: Chave de Acesso inválida (Código UFinválido)                                                          |
| P12-18 | - Ano < 06 ou Ano maior que Ano corrente (*1)                                                                                                                                 | Obrig.   |   615 | Rejeição: Chave de Acesso inválida (Ano < 06 ou Ano maior que Ano corrente)                                     |
| P12-22 | - Mês = 0 ou Mês > 12 (*1)                                                                                                                                                    | Obrig.   |   616 | Rejeição: Chave de Acesso inválida(Mês<1ouMês> 12)                                                              |
| P12-26 | - CNPJ/CPF zerado oudígito inválido (*1) Nota: Considerar a Série para determinar se CNPJ/CPF na Chave de Acesso. CNPJ: Série=[0-909], CPF: Série<>[0-909]                    | Obrig.   |   617 | Rejeição: Chave de Acesso inválida (CNPJ/CPF zerado ou dígito inválido)                                         |
| P12-28 | - Modelodivergede55/65                                                                                                                                                        | Obrig.   |   618 | Rejeição: Chave de Acesso inválida (Modelo diferente de 55/65)                                                  |
| P12-34 | - Número NF = 0 (*1)                                                                                                                                                          | Obrig.   |   619 | Rejeição:ChavedeAcesso inválida (número NF = 0)                                                                 |
| P12-40 | - UF da Chave de Acesso diverge da UF Autorizadora                                                                                                                            | Obrig.   |   249 | Rejeição:UFdaChave de AcessodivergedaUF autorizadora                                                            |
| P12-44 | - CNPJ/CPF do Autor diverge do CNPJ/CPF da Chave de Acesso Nota: Considerar a Série para determinar se CNPJ/CPF na Chave de Acesso. CNPJ: Série=[0- 909], CPF: Série<>[0-909] | Obrig.   |   574 | Rejeição: Autor do evento divergedoemissordaNF-e                                                                |
| P13-10 | Data do evento maior que a data de processamento (aceitar tolerância de até 5 minutos) (*1)                                                                                   | Obrig.   |   578 | Rejeição: A data do evento não pode ser maior que a data do processamento                                       |
| P26-10 | Data de Pagamento maior que a data de processamento                                                                                                                           | Obrig.   |   657 | Rejeição: Data de Pagamento inválida [nOcor:999]                                                                |

![Image](assets/image_000012_2a0fdef6f813e8d8af75ea308556fcb4a3b56dc022062b6e3e02687e191e47e4.png)

![Image](assets/image_000013_2a0fdef6f813e8d8af75ea308556fcb4a3b56dc022062b6e3e02687e191e47e4.png)

| #      | Regra de Validação                                                                                                                        | Aplic.   |   Msg | Descrição Erro                                                   |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|------------------------------------------------------------------|
| P28-10 | Se informado CNPJ do estabelecimento onde o pagamento foi processado/transacionado/recebido: - CNPJ inválido (zeros, nulo ou DV inválido) | Obrig.   |   961 | Rejeição: CNPJ transacional do pagamento inválido [nOcor:999)    |
| P30-10 | Se informado CNPJ da instituição financeira de pagamento, adquirente ou subadquirente: - CNPJ inválido (zeros, nulo ou DV inválido)       | Obrig.   |   437 | Rejeição: CNPJ da instituição de pagamento inválido) [nOcor:999) |
| P34-10 | Se informado CNPJ do beneficiário de pagamento: - CNPJ inválido (zeros, nulo ou DV inválido)                                              | Obrig.   |   208 | Rejeição:CNPJinformado inválido (DV ou zeros) [nOcor:999)        |

| #                            | Regra de Validação                                                                                                                                                                                                            | Aplic.                       | Msg                          | Descrição Erro                                                                |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|------------------------------|-------------------------------------------------------------------------------|
| *** Banco de Dados: Emitente | *** Banco de Dados: Emitente                                                                                                                                                                                                  | *** Banco de Dados: Emitente | *** Banco de Dados: Emitente | *** Banco de Dados: Emitente                                                  |
| 1P10-20                      | Acesso ao Cadastro de Contribuintes (Chave: CNPJ/CPF do Autor do Evento): - Verificar situação fiscal do emitente                                                                                                             | Obrig.                       | 240                          | Rejeição: Irregularidade fiscal do emitente                                   |
| *** Banco de Dados: NF-e     | *** Banco de Dados: NF-e                                                                                                                                                                                                      | *** Banco de Dados: NF-e     | *** Banco de Dados: NF-e     | *** Banco de Dados: NF-e                                                      |
| 2P12-10                      | Acesso BD NFE (Chave: Chave de Acesso): - Chave Acesso inexistente para o tpEvento que exige a existência da NF-e (*1)                                                                                                        | Obrig.                       | 494                          | Rejeição:ChavedeAcesso Inexistente                                            |
| 2P12-22                      | - Verificar se NF-e está denegada ou cancelada                                                                                                                                                                                | Obrig.                       | 580                          | Rejeição:Eventoexigeuma NF-e autorizada                                       |
| 2P13-10                      | - Data do evento menor que a Data de Emissão da NF-e (*1)                                                                                                                                                                     | Obrig.                       | 577                          | Rejeição: A data do evento nãopodesermenorquea data de emissão da NF-e        |
| 2P13-14                      | - Data do evento menor que a Data de Autorização da NF-e não emitida em contingência (tpEmis=1) Nota : Tolerância de 5 minutos, devido ao sincronismo de horário entre o servidor da Empresaeoservidor da SEFAZ Autorizadora. | Obrig.                       | 579                          | Rejeição: A data do evento não pode ser menor que a datade autorização daNF-e |

| #                          | Regra de Validação                                                                            | Aplic.                     | Msg                        | Descrição Erro                |
|----------------------------|-----------------------------------------------------------------------------------------------|----------------------------|----------------------------|-------------------------------|
| *** Banco de Dados: Evento | *** Banco de Dados: Evento                                                                    | *** Banco de Dados: Evento | *** Banco de Dados: Evento | *** Banco de Dados: Evento    |
| 3P15-10                    | Acesso BDdeEventos (Chave: Chave de Acesso, tpEvento, nSeqEvento): - Evento já existente (*1) | Obrig.                     | 573                        | Rejeição:Duplicidadede Evento |

## 3.8.  Final do Processamento do Lote

O processamento do lote pode resultar em:

- Rejeição do Lote: por algum problema que comprometa o processamento do lote;
- Processamento do Lote: o lote foi processado (cStat='128 - Lote de Evento Processado'), e a validação de cada evento do lote poderá resultar em:

- Rejeição: o Evento será rejeitado, retornando do código do status do motivo da rejeição;
- Evento Autorizado, com vinculação à respectiva NF-e : Encontrada a NF-e no banco de dados. Retornar cStat='135-Evento registrado e vinculado a NF-e';
- Evento Autorizado, sem vinculação à respectiva NF-e: Não encontrada a NF-e no banco de dados. Retornar cStat='136-Evento registrado, mas não vinculado a NF-e';

## 4. Evento 'Cancelamento Conciliação Financeira - ECONF'

## 4.1.  Leiaute Mensagem de Entrada

O Web Service de Registro de Evento possui uma interface genérica, complementada por uma área específica para cada tipo de evento. Segue o leiaute da mensagem de entrada deste evento.

## Schema XML - parte específica: leiauteEventoCancelamentoConciliacaoFinanceira\_v1.00.xsd

| #   | Campo      | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Descrição/Observação                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----|------------|-------|-------|--------|---------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| P01 | envEvento  | Raiz  | -     | -      | -       | -      | TAGraiz                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| P02 | versao     | A     | P01   | N      | 1-1     | 2v2    | Versão do leiaute                                                                                                                                                                                                                                                                                                                                                                                                                          |
| P03 | idLote     | E     | P01   | N      | 1-1     | 1-15   | Identificador de controle do Lote de envio do Evento. Númerosequencial único para identificação do Lote, de uso exclusivo do autor do evento.O Web Service não faz uso deste identificador.                                                                                                                                                                                                                                                |
| P04 | evento     | G     | P01   | xml    | 1-20    | -      | Evento, umlote pode conter até 20 eventos                                                                                                                                                                                                                                                                                                                                                                                                  |
| P05 | versao     | A     | P04   | N      | 1-1     | 2v2    | Versão do leiaute do evento                                                                                                                                                                                                                                                                                                                                                                                                                |
| P06 | infEvento  | G     | P04   | -      | 1-1     | -      | Grupode informações do registro do Evento                                                                                                                                                                                                                                                                                                                                                                                                  |
| P07 | Id         | ID    | P06   | C      | 1-1     | 54     | Identificador daTAGaser assinada, formado por: 'ID' + tpEvento + Chave da NF -e + nSeqEvento                                                                                                                                                                                                                                                                                                                                               |
| P08 | cOrgao     | E     | P06   | N      | 1-1     | 2      | Código do órgão de recepção do Evento, conforme Tabela do IBGE. Para a NF-e (modelo 55): Informar o código 92-SVRS, utilizando a URL do WSde Eventos da SVRS para este modelo de Documento Fiscal. Para a NFC-e (modelo 65): Se UF participante da SVRS, informar o código 92-SVRS, utilizando a URL do WSde Eventos da SVRS; se não participante, informar o Código da UF do Emitente, para as SEFAZ com ambiente de autorização próprio. |
| P09 | tpAmb      | E     | P06   | N      | 1-1     | 1      | Identificação do Ambiente: 1=Produção; 2=Homologação                                                                                                                                                                                                                                                                                                                                                                                       |
| P10 | CNPJ       | CE    | P06   | N      | 1-1     | 14     | Informar o CNPJ/CPF do autor do Evento.                                                                                                                                                                                                                                                                                                                                                                                                    |
| P11 | CPF        | CE    | P06   | N      | 1-1     | 11     |                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| P12 | chNFe      | E     | P06   | N      | 1-1     | 44     | Chave de Acesso da NF-e que o evento será vinculado.                                                                                                                                                                                                                                                                                                                                                                                       |
| P13 | dhEvento   | E     | P06   | D      | 1-1     | -      | Data e hora do evento. Formato AAAA-MM-DDThh:mm:ss TZD (UTC)                                                                                                                                                                                                                                                                                                                                                                               |
| P14 | tpEvento   | E     | P06   | N      | 1-1     | 6      | Código do evento: 110751 - ' Cancelamento Conciliação Financeira '                                                                                                                                                                                                                                                                                                                                                                         |
| P15 | nSeqEvento | E     | P06   | N      | 1-1     | 1-2    | Sequencial do evento para o mesmo tipo de evento. O autor do evento deve numerar de forma sequencial os eventos deste tipo, com os valores de 1 a 99.                                                                                                                                                                                                                                                                                      |
| P16 | verEvento  | E     | P06   | N      | 1-1     | 2v2    | Versão do grupo de detalhe do evento.                                                                                                                                                                                                                                                                                                                                                                                                      |

![Image](assets/image_000014_f0738f27c9e4e9ebd496e8bf35f9cb9a8c4cad3a5ac67a52bc723ba87e727473.png)

![Image](assets/image_000015_2a0fdef6f813e8d8af75ea308556fcb4a3b56dc022062b6e3e02687e191e47e4.png)

| P16a   | verAplic    | E   | P06   | C   | 1-1   | 1-20   | Versão do aplicativo do Autor do Evento.                                                          |
|--------|-------------|-----|-------|-----|-------|--------|---------------------------------------------------------------------------------------------------|
| P17    | detEvento   | G   | P06   |     | 1-1   | -      | Detalhes do evento                                                                                |
| P18    | versao      | A   | P17   | N   | 1-1   | 2v2    | Informaro mesmovalorda tag 'verEvento' (P16)                                                      |
| P19    | descEvento  | E   | P17   | C   | 1-1   | 5-60   | Veja a descrição do evento, junto com o Tipo de Evento documentado anteriormente                  |
| P22    | verAplic    | E   | P17   | C   | 1-1   | 1-20   | Versão do aplicativo do Autor do Evento.                                                          |
| P23    | nProtEvento | E   | P17   | N   | 1-1   | 15     | Informar o número do Protocolo de Autorização do Evento da NF-e a que se refere este cancelamento |
| P91    | Signature   | G   | P04   | XML | 1-1   | -      | Assinatura Digital do documento XML, a assinatura deverá ser aplicada no elemento infEvento.      |

## 4.2.  Leiaute Mensagem de Retorno

O Web Service de Registro de Evento possui uma interface genérica, complementada por uma área específica para cada tipo de evento. Segue o leiaute da mensagem de retorno (resposta).

## Schema XML: retEnvEventoNFe\_v1.0.xsd

| #   | Campo        | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Descrição/Observação                                                                                                                                                                          |
|-----|--------------|-------|-------|--------|---------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R01 | retEnvEvento | Raiz  | -     | -      | -       | -      | TAGraiz damensagem de retorno                                                                                                                                                                 |
| R02 | versao       | A     | R01   | N      | 1-1     | 2v2    | Versão do leiaute                                                                                                                                                                             |
| R03 | idLote       | E     | R01   | N      | 1-1     | 1-15   | Idem a mensagem de entrada.                                                                                                                                                                   |
| R04 | tpAmb        | E     | R01   | N      | 1-1     | 1      | Idem a mensagem de entrada.                                                                                                                                                                   |
| R05 | verAplic     | E     | R01   | C      | 1-1     | 1-20   | Versão da aplicação que processouo evento.                                                                                                                                                    |
| R06 | cOrgao       | E     | R01   | N      | 1-1     | 2      | Órgão de recepção do Evento, idem a mensagem de entrada.                                                                                                                                      |
| R07 | cStat        | E     | R01   | N      | 1-1     | 3      | Código do status da resposta para o Lote de Eventos. Se não tiver erro, será retornado: '128 - Lote de Evento Processado'                                                                     |
| R08 | xMotivo      | E     | R01   | C      | 1-1     | 1-255  | Descrição do status da resposta                                                                                                                                                               |
| R09 | retEvento    | G     | R01   | -      | 0-20    | -      | Grupo do resultado do processamento do para cada Evento                                                                                                                                       |
| R10 | versao       | A     | R09   | N      | 1-1     | 2v2    | Versão do leiaute                                                                                                                                                                             |
| R11 | infEvento    | G     | R09   |        | 1-1     | -      | Grupo de informações do registro do Evento                                                                                                                                                    |
| R12 | Id           | ID    | R11   | C      | 0-1     | 17     | Identificador da TAG a ser assinada, somente deve ser informado seo órgão deregistro assinar a resposta. No caso de assinatura, preencher comonúmerodoprotocolo, precedido pela literal 'ID'. |
| R13 | tpAmb        | E     | R11   | N      | 1-1     | 1      | Idem a mensagem de entrada.                                                                                                                                                                   |
| R14 | verAplic     | E     | R11   | C      | 1-1     | 1-20   | Versão da aplicação que registrou o Evento, utilizar literal que permita a identificação do órgão, como a sigla da UF ou do órgão.                                                            |
| R15 | cOrgao       | E     | R11   | N      | 1-1     | 2      | Idem a mensagem de entrada.                                                                                                                                                                   |
| R16 | cStat        | E     | R11   | N      | 1-1     | 3      | Código do status da resposta.                                                                                                                                                                 |
| R17 | xMotivo      | E     | R11   | C      | 1-1     | 1-255  | Descrição do status da resposta.                                                                                                                                                              |
| R18 | chNFe        | E     | R11   | N      | 0-1     | 44     | Idem a mensagem de entrada.                                                                                                                                                                   |
| R19 | tpEvento     | E     | R11   | N      | 0-1     | 6      | Idem a mensagem de entrada.                                                                                                                                                                   |

![Image](assets/image_000016_2a0fdef6f813e8d8af75ea308556fcb4a3b56dc022062b6e3e02687e191e47e4.png)

| R20   | xEvento     | E   | R11   | C   | 0-1   | 5-60   | Idem a mensagem de entrada.                                                                                                                                                            |
|-------|-------------|-----|-------|-----|-------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R21   | nSeqEvento  | E   | R11   | N   | 0-1   | 1-2    | Idem a mensagem de entrada.                                                                                                                                                            |
| R50   | dhRegEvento | E   | R11   | D   | 1-1   | -      | Data e hora de registro do evento no formato AAAA-MM-DDTHH:MM:SSTZD(formatoUTC). Seo evento for rejeitado informar a data e hora de recebimento do evento.                             |
| R51   | nProt       | E   | R11   | N   | 0-1   | 15     | Número Protocolo do Evento 1 posição (1- Secretaria da Fazenda Estadual, 2-RFB, 3-SVRS), 2 posições para o código da UF, 2 posições para o ano e 10 posições para o sequencial no ano. |
| R91   | Signature   | G   | R09   | XML | 0-1   | -      | Assinatura Digital do documento XML, a assinatura deverá ser aplicada no elemento infEvento. Adecisão de assinar a mensagem fica a critério da UF.                                     |

Nota: No caso de evento registrado com sucesso, os campos opcionais serão retornados.

## 4.3.  Processo de Recepção de Evento

Idem ao item 3.3.

## 4.4.  Validação do Certificado de Transmissão - Geral

Igual às regras previstas no item 03.4

## 4.5.  Validação Inicial da Mensagem no Web Service - Geral

Igual às regras previstas no item 03.5

## 4.6.  Validação da área de Dados - Geral

Igual às regras previstas no item 03.6

## 4.7.  Validação das Regras de Negócio

| #      | Regra de Validação                                                                                       | Aplic.   |   Msg | Descrição Erro                                                                                                  |
|--------|----------------------------------------------------------------------------------------------------------|----------|-------|-----------------------------------------------------------------------------------------------------------------|
| P07-10 | Atributo 'Id' nãocorrespondeàconcatenação dos campos do evento ('ID' + tpEvento + chNFe nSeqEvento) (*1) | Obrig.   |   572 | Rejeição: Erro AtributoIDdo evento não corresponde a concatenação dos campos ('Id' +tpEvento+chNFe+ nSeqEvento) |
| P08-10 | Código do órgão de recepção do Evento diverge do definido para este evento (*1)                          | Obrig.   |   250 | Rejeição:UFdivergedaUF autorizadora                                                                             |
| P09-10 | Tipo do ambiente difere do ambientedo WebService (*1)                                                    | Obrig.   |   252 | Rejeição:Ambienteinformado diverge do Ambiente de recebimento                                                   |
| P10-10 | Se informado CNPJ do Autor do Evento: - CNPJ inválido (zeros, nuloouDV inválido) (*1)                    | Obrig.   |   489 | Rejeição:CNPJinformado inválido (DV ou zeros)                                                                   |
| P11-10 | Se informado o CPF do Autor do evento: - CPF inválido (zeros, nulo ou DVinválido) (*1)                   | Obrig.   |   490 | Rejeição:CPFinformado inválido (DV ou zeros)                                                                    |

![Image](assets/image_000017_6b90574bd841205e76d82e373f6e14d369184d061245c4d6d7725ab0095483fb.png)

| #                            | Regra de Validação                                                                                                                                                                                                            | Aplic.                       | Msg                          | Descrição Erro                                                                |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|------------------------------|-------------------------------------------------------------------------------|
| P12-10                       | Validação da Chave de Acesso da NF-e (tag: chNFe): - Dígito verificador inválido (*1)                                                                                                                                         | Obrig.                       | 236                          | Rejeição: Chave de Acesso comdígitoverificador inválido                       |
| P12-14                       | - Código UFinválido (*1)                                                                                                                                                                                                      | Obrig.                       | 614                          | Rejeição: Chave de Acesso inválida (Código UFinválido)                        |
| P12-18                       | - Ano < 06 ou Ano maior que Ano corrente (*1)                                                                                                                                                                                 | Obrig.                       | 615                          | Rejeição: Chave de Acesso inválida (Ano < 06 ou Ano maior que Ano corrente)   |
| P12-22                       | - Mês = 0 ou Mês > 12 (*1)                                                                                                                                                                                                    | Obrig.                       | 616                          | Rejeição: Chave de Acesso inválida(Mês<1ouMês> 12)                            |
| P12-26                       | - CNPJ/CPF zerado oudígito inválido (*1) Nota: Considerar a Série para determinar se CNPJ/CPF na Chave de Acesso. CNPJ: Série=[0-909], CPF: Série<>[0-909]                                                                    | Obrig.                       | 617                          | Rejeição: Chave de Acesso inválida (CNPJ/CPF zerado ou dígito inválido)       |
| P12-28                       | - Modelodivergede55/65                                                                                                                                                                                                        | Obrig.                       | 618                          | Rejeição: Chave de Acesso inválida (Modelo diferente de 55/65)                |
| P12-34                       | - Número NF = 0 (*1)                                                                                                                                                                                                          | Obrig.                       | 619                          | Rejeição:ChavedeAcesso inválida (número NF = 0)                               |
| P12-40                       | - UF da Chave de Acesso diverge da UF Autorizadora                                                                                                                                                                            | Obrig.                       | 249                          | Rejeição:UFdaChave de AcessodivergedaUF autorizadora                          |
| P12-44                       | - CNPJ/CPF do Autor diverge do CNPJ/CPF da Chave de Acesso Nota: Considerar a Série para determinar se CNPJ/CPF na Chave de Acesso. CNPJ: Série=[0-909], CPF: Série<>[0-909]                                                  | Obrig.                       | 574                          | Rejeição: Autor do evento divergedoemissordaNF-e                              |
| P13-10                       | Data do evento maior que a data de processamento (aceitar tolerância de até 5 minutos) (*1)                                                                                                                                   | Obrig.                       | 578                          | Rejeição: A data do evento não pode ser maior que a data do processamento     |
| *** Banco de Dados: Emitente | *** Banco de Dados: Emitente                                                                                                                                                                                                  | *** Banco de Dados: Emitente | *** Banco de Dados: Emitente | *** Banco de Dados: Emitente                                                  |
| 1P10-20                      | Acesso ao Cadastro de Contribuintes (Chave: CNPJ/CPF do Autor do Evento): - Verificar situação fiscal do emitente                                                                                                             | Obrig.                       | 240                          | Rejeição: Irregularidade fiscal do emitente                                   |
| *** Banco de Dados: NF-e     | *** Banco de Dados: NF-e                                                                                                                                                                                                      | *** Banco de Dados: NF-e     | *** Banco de Dados: NF-e     | *** Banco de Dados: NF-e                                                      |
| 2P12-10                      | Acesso BD NFE (Chave: Chave de Acesso): - Chave Acesso inexistente para o tpEvento que exige a existência da NF-e (*1)                                                                                                        | Obrig.                       | 494                          | Rejeição:ChavedeAcesso Inexistente                                            |
| 2P12-22                      | - Verificar se NF-e está denegada ou cancelada                                                                                                                                                                                | Obrig.                       | 580                          | Rejeição:Eventoexigeuma NF-e autorizada                                       |
| 2P13-10                      | - Data do evento menor que a Data de Emissão da NF-e (*1)                                                                                                                                                                     | Obrig.                       | 577                          | Rejeição: A data do evento nãopodesermenorquea data de emissão da NF-e        |
| 2P13-14                      | - Data do evento menor que a Data de Autorização da NF-e não emitida em contingência (tpEmis=1) Nota : Tolerância de 5 minutos, devido ao sincronismo de horário entre o servidor da Empresaeoservidor da SEFAZ Autorizadora. | Obrig.                       | 579                          | Rejeição: A data do evento não pode ser menor que a datade autorização daNF-e |
| *** Banco de Dados: Evento   | *** Banco de Dados: Evento                                                                                                                                                                                                    | *** Banco de Dados: Evento   | *** Banco de Dados: Evento   | *** Banco de Dados: Evento                                                    |

NT 2024.002 - Evento de Conciliação Financeira - ECONF.

![Image](assets/image_000018_2a0fdef6f813e8d8af75ea308556fcb4a3b56dc022062b6e3e02687e191e47e4.png)

| #                            | Regra de Validação                                                                               | Aplic.                       | Msg                          | Descrição Erro                                     |
|------------------------------|--------------------------------------------------------------------------------------------------|------------------------------|------------------------------|----------------------------------------------------|
| 3P15-10                      | Acesso BDdeEventos (Chave: Chave de Acesso, tpEvento, nSeqEvento): - Evento já existente (*1)    | Obrig.                       | 573                          | Rejeição: Duplicidadede Evento                     |
| *** Banco de Dados: Evento 2 | *** Banco de Dados: Evento 2                                                                     | *** Banco de Dados: Evento 2 | *** Banco de Dados: Evento 2 | *** Banco de Dados: Evento 2                       |
| 4P15-10                      | Acesso BD de Eventos (Chave: Chave de Acesso, tpEvento=110750, nSeqEvento): - Evento inexistente | Obrig.                       | 459                          | Rejeição: Cancelamento de Evento inexistente       |
| 4P23-10                      | - Número do Protocolo não encontrado                                                             | Obrig.                       | 460                          | Rejeição: Protocolo do Evento difere do cadastrado |

(*1) Validações genéricas do Registro de Evento.

## 4.8.  Final do Processamento do Lote

O processamento do lote pode resultar em:

- Rejeição do Lote: por algum problema que comprometa o processamento do lote;
- Processamento do Lote: o lote foi processado (cStat='128 - Lote de Evento Processado'), e a validação de cada evento do lote poderá resultar em:
- Rejeição: o Evento será rejeitado, retornando do código do status do motivo da rejeição;
- Evento Autorizado, com vinculação à respectiva NF-e : Encontrada a NF-e no banco de dados. Retornar cStat='135-Evento registrado e vinculado a NF-e';
- Evento Autorizado, sem vinculação à respectiva NF-e: Não encontrada a NF-e no banco de dados. Retornar cStat='136-Evento registrado, mas não vinculado a NF-e';
## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt2024-002-v1-00-econf/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt2024-002-v1-00-econf/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt2024-002-v1-00-econf.md)
- [Proveniência resumida](../../../../sources/provenance/nt2024-002-v1-00-econf.json)

## Documentos relacionados
_Nenhum documento relacionado conhecido._
