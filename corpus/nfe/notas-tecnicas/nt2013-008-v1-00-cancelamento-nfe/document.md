---
title: "Projeto Nota Fiscal Eletrônica"
slug: "nt2013-008-v1-00-cancelamento-nfe"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "a8ea72ccfa5d8266c61f1b2911b88befd1c6a08ed56c0627713af210f624b439"
converted_at_utc: "2026-06-25T15:04:32.157794+00:00"
status: "published"
type: "nota_tecnica"
---
![Image](assets/image_000000_800a4b8a63597a6bb63fdd06a6d16b80b3898d87148b745aa839a7997426426d.png)

## Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_0eaf9468f17660078b2a0ec01cf1f9d13e9b723217a04dcec19809d906df1a45.png)

## Nota Técnica 2013/008

## Evento de Cancelamento da NF-e

![Image](assets/image_000002_f6633e8554c5ba5281a65e6fd9fde4a841e72aa8762badd9357b607ec4d1b5ba.png)

Versão 1.00 Dezembro 2013

![Image](assets/image_000003_f049c5bd76a24ce709c591e0e27ec3493f62665b205d5d3f994c78fa37ac0dd9.png)

## 01. Resumo

O Evento de Cancelamento da NF-e é encaminhado pela  Empresa para a SEFAZ Autorizadora, que verifica as regras vinculadas com a autorização  deste Evento. Com a implementação recente dos  novos  eventos  da  NF-e,  as  regras  que  permitem  ou  impedem  o  cancelamento  devem  ser revistas e é este o objetivo desta Nota Técnica.

De forma geral, segue abaixo o prazo previsto para entrada em vigência das alterações:

- Ambiente de Homologação (ambiente de teste das empresas): 02/01/14;
- Ambiente de Produção : 03/02/14.

![Image](assets/image_000004_89aa962382a550688505aac59aa3bd29ab82c91d39b98e943f6cdfe11420a533.png)

## 02. Evento de Cancelamento

## 02.1 Validação das Regras de Negócio específicas do Evento (item 4.9.8 do MOC, conforme NT 2011/006)

| #    | Regra de validação                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                       |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|--------------------------------------------------------------------------------------|
| GA09 | Acessar ao BD de Eventos para a Chave de Acesso: *Evento Manifestação do Destinatário - Existe evento '210200 - Confirmação da Operação' para a NF-e Exceção : Uma NF-e pode ter mais de uma Manifestação do Destinatário, uma de cada tipo, prevalecendo a últi ma manifestação. Permitir o Cancelamento da NF-e se após o evento de 'Confirmação' existir um dos eventos abai xo: - '210220 - Operação não Realizada'; - '210240 - Desconhecimento da Operação'. | Obrig.   |   221 | Rej.     | Rejeição: Confirmado o recebimento da NF-e pelo des tinatário                        |
| GA10 | *Evento Registro de Passagem NF-e - Existe evento '610500 - Registro Passagem NF-e' para a NF-e Exceção : Uma NF-e pode ter vários Registros de Passagem. Permitir o Cancelamento da NF-e se todos os eventos de 'Registro de Passagem NF-e' tiverem o correspondente evento '610501-Registro Passagem NF-e Cancelado'                                                                                                                                             | Obrig.   |   219 | Rej.     | Rejeição: Circulação da NF-e verificada                                              |
| GA11 | - Falha na consulta do Registro de Passagem (*1)                                                                                                                                                                                                                                                                                                                                                                                                                   | Obrig.   |   642 | Rej.     | Rejeição: Falha na Consulta do Registro de Passagem , tente novamente após 5 minutos |
| GA12 | *Evento Conhecimento de Transporte Autorizado - Existe evento '610600 - CT-e Autorizado' para a NF-e Exceção : Uma NF-e pode participar de diferentes CT-e. Permitir o Cancelamento da NF-e se todos os eventos de 'CT-e Autorizado' tiverem o correspondente evento de '610601 - CT-e Cancelado'.                                                                                                                                                                 | Obrig.   |   690 | Rej.     | Rejeição: Pedido de Cancelamento para NF-e com CT-e ou MDF-e                         |
| GA13 | *Eventos da Suframa - Existe evento '990900 - Vistoria Suframa' ou o evento '990910 - Internalização Suframa' para a NF-e                                                                                                                                                                                                                                                                                                                                          | Obrig.   |   304 | Rej.     | Rejeição: Pedido de Cancelamento para NF-e com even to da Suframa                    |
| GA14 | *Evento Manifesto Eletrônico de Documentos Fiscais (Manifesto de Carga) (*2) - Existe evento '610610 - MDF-e Autorizado' para a NF-e Exceção : Uma NF-e pode participar de diferentes MDF-e. Permitir o Cancelamento da NF-e se todos os eventos de 'MDF-e Autorizado' tiverem o correspondente evento de '610611 - MDF-e Cancelado'.                                                                                                                              | Obrig.   |   690 | Rej.     | Rejeição: Pedido de Cancelamento para NF-e com CT-e ou MDF-e                         |

![Image](assets/image_000005_1b06c9d234a55f368757b60df80759db71bc08cdb15007f6efd5ba7b9ccc86ee.png)

| #    | Regra de validação                                                                                             | Aplic. Msg   |     | Efeito Descrição Erro                        |
|------|----------------------------------------------------------------------------------------------------------------|--------------|-----|----------------------------------------------|
| GA15 | *Evento Registro de Passagem NF-e RFID (*3) - Existe evento '610550 - Registro Passagem NF-e RFID' para a NF-e | Obrig.       | 219 | Rej. Rejeição: Circulação da NF-e verificada |

Nota (*1): Na forma anterior, a verificação da exis tência do Registro de Passagem era feita acessando  uma base de dados nacional que mantinha o registro da passagem da NF-e nos Postos Fiscais existentes. No novo modelo de eventos, o Registro de Passagem é automaticamente distribuído para  o  ambiente  de  cada  SEFAZ,  eliminando  a  necessidade  de  consumo  de Web  Service  do  Ambiente  Nacional.  Portanto,  para  o  Registro  de Passagem, foi eliminada a validação '642 - Rejeição : Falha na Consulta do Registro de Passagem, tente novamente após 5 minutos'.

Nota (*2): Evento da NF-e em processo de implantaçã o.

Nota  (*3):  Evento  da  NF-e  em  processo  de  implantaçã o,  com  a  leitura  da  etiqueta  RFID  (Radio-Frequency  IDentification)  vinculada  ao  Manifesto Eletrônico de Documentos Fiscais e consequente registro de passagem para as NF-e vinculadas a este MDF-e.

## 90. Documentacional

## 91. Tabela de códigos de erros e descrições de mens agens de erros

|   Código | RESULTADO DO PROCESSAMENTO DA SOLICITAÇÃO                                            |
|----------|--------------------------------------------------------------------------------------|
|      219 | Rejeição: Circulação da NF-e verificada                                              |
|      221 | Rejeição: Confirmado o recebimento da NF-e pelo destinatário                         |
|      304 | Rejeição: Pedido de Cancelamento para NF-e com evento da Suframa                     |
|      642 | Rejeição: Falha na Consulta do Registro de Passagem , tente novamente após 5 minutos |
|      690 | Rejeição: Pedido de Cancelamento para NF-e com CT-e ou MDF-e                         |

Obs.: Alterada a descrição da mensagem de erro 690,  já existente, incluindo no final da descrição a re ferência ao 'MDF-e'.
## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt2013-008-v1-00-cancelamento-nfe/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt2013-008-v1-00-cancelamento-nfe/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt2013-008-v1-00-cancelamento-nfe.md)
- [Proveniência resumida](../../../../sources/provenance/nt2013-008-v1-00-cancelamento-nfe.json)

## Documentos relacionados
_Nenhum documento relacionado conhecido._
