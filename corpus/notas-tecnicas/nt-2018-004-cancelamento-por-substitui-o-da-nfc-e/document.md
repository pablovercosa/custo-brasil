![Image](assets/image_000000_87068efaacdcfba37c009d21d2142f80bf18f025f314e97058cd11f62feb52d0.png)

![Image](assets/image_000001_3ebe18e7d44788c92d727014eb2f6f20d633408aa48e34420ad14e0f9a1cbed8.png)

## Projeto Nota Fiscal Eletrônica

## Nota Técnica 2018.004

Evento de cancelamento por substituição da NFC-e

Versão 1.00 - Dezembro 2018

![Image](assets/image_000002_5d5226da8b3fb32d24e78b0efdd7f4358f9a95538443f1554ff2f68472d5a2a5.png)

## Controle de Versões

|   Versão | Publicação     | Descrição         |
|----------|----------------|-------------------|
|     1.00 | Dezembro/ 2018 | Publicação da NT. |

## Histórico de Alterações / Cronograma

|   Versão | Histórico de atualizações                                                            | Implantação Teste   | Implantação Produção   |
|----------|--------------------------------------------------------------------------------------|---------------------|------------------------|
|     1.00 | Implantação do evento de Cancelamento por substituição para a NFC-e seção 2 desta NT | Até 25/02/2019      | 29/04/2019             |

![Image](assets/image_000003_4ce977c4f1caa54baf2b9892e4dc47d44a8ec6a59a895a0cf0ef17b0d1c086a3.png)

## 1  Resumo

Esta Nota Técnica apresenta a especificação técnica necessária para a implementação do evento de 'Cancelamento por Substituição' (tpEvento=110112). Conforme a legislação atual, este evento será  implementado  inicialmente  para  a  NFC-e  (Modelo  65),  aguardando  possível  alteração  da legislação em relação a NF-e (Modelo 55).

Este  evento  é  muito  semelhante  ao  evento  de  cancelamento  normal  e,  para  clareza  na documentação, incluímos nesta especificação o leiaute e regras de validação do atual evento de Cancelamento (tpEvento=110111). O evento de cancelamento normal não teve nenhuma mudança na especificação.

## 2 Cancelamento por Substituição

O Ajuste SINIEF 07/18, que alterou o ajuste 19/16, trouxe a seguinte redação: ' Cláusula décima quinta-A Na hipótese prevista no inciso I da cláusula décima segunda, o emitente poderá solicitar o cancelamento da NFC-e, desde que tenha sido emitida uma outra NFC-e em contingência para acobertar a mesma operação, em prazo não superior a 168 horas, podendo ser reduzido a critério de cada unidade federada, contado do momento em que foi concedida a Autorização de Uso da NFC-e, de que trata o inciso I da cláusula oitava.'.

Sendo assim, a partir dessa Nota Técnica será possível um contribuinte cancelar uma NFC-e que foi emitida em duplicidade. Esse tipo de situação pode acontecer quando um contribuinte emite uma NFC-e (NFC-e 1), porém, por algum motivo, não obtém resposta, ficando pendente de retorno, e em seguida emite outra NFC-e (NFC-2), normalmente em contingência, para acobertar a operação. Depois é verificado que a 'NFC-e 1' também foi autorizada, e sendo assim temos duas NFC-e acobertando a mesma operação. Acontecendo isso, o contribuinte poderá solicitar o cancelamento, no  prazo  não  superior  a  168  horas,  da  NFC-e  emitida  em  duplicidade  e  que  não  acobertou  a operação (NFC-e 1), tendo que referenciar a NFC-e que substituiu (NFC-2) aquela que está sendo cancelada.

![Image](assets/image_000004_7960d33f2b154f941221050690ae870cb6f1c389263b12926bbfcde80ed5f207.png)

## 2.1. Leiaute Mensagem de Entrada

O Web Service de Registro de Evento possui uma interface genérica, complementada por uma área específica para cada tipo de evento. Segue o leiaute da mensagem de entrada deste evento.

Schema XML:

envEventoCancNFe\_v9.99.xsd (tpEvento=110111) envEventoCancSubst\_v1.0.xsd (tpEvento=110112)

| #   | Campo       | Ele   | Pai   | Tipo   | Ocor   | Tam   | Descrição/Observação                                                                                                                                                                                      |
|-----|-------------|-------|-------|--------|--------|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| P01 | envEvento   | Raiz  | -     | -      | -      | -     | TAG raiz                                                                                                                                                                                                  |
| P02 | versao      | A     | P01   | N      | 1-1    | 2v2   | Versão do leiaute                                                                                                                                                                                         |
| P03 | idLote      | E     | P01   | N      | 1-1    | 1-15  | Identificador de controle do Lote de envio do Evento. Número sequencial único para identificação do Lote, de uso exclusivo do autor do evento.OWeb Service não faz qualquer uso deste identificador.      |
| P04 | evento      | G     | P01   | xml    | 1-20   | -     | Evento, um lote pode conter até 20 eventos                                                                                                                                                                |
| P05 | versao      | A     | P04   | N      | 1-1    | 2v2   | Versão do leiaute do evento                                                                                                                                                                               |
| P06 | infEvento   | G     | P04   | -      | 1-1    | -     | Grupo de informações do registro do Evento                                                                                                                                                                |
| P07 | Id          | ID    | P06   | C      | 1-1    | 54    | Identificador da TAG a ser assinada, formado por: 'ID' + tpEvento + Chave da NF-e + nSeqEvento                                                                                                            |
| P08 | cOrgao      | E     | P06   | N      | 1-1    | 2     | Código do órgão de recepção do Evento, conforme Tabela do IBGE ou: 91 - Ambiente Nacional Informar o código da UF para este evento.                                                                       |
| P09 | tpAmb       | E     | P06   | N      | 1-1    | 1     | Identificação do Ambiente: 1=Produção; 2=Homologação                                                                                                                                                      |
| P10 | CNPJ        | CE    | P06   | N      | 1-1    | 14    | Informar o CNPJ/CPF do autor do Evento.                                                                                                                                                                   |
| P11 | CPF         | CE    | P06   | N      | 1-1    | 11    |                                                                                                                                                                                                           |
| P12 | chNFe       | E     | P06   | N      | 1-1    | 44    | Chave de Acesso da NF-e à qual o evento será vinculado                                                                                                                                                    |
| P13 | dhEvento    | E     | P06   | D      | 1-1    | -     | Data e hora do evento no formato AAAA- MMDDThh:mm:ssTZD (UTC - Universal Coordinated Time)                                                                                                                |
| P14 | tpEvento    | E     | P06   | N      | 1-1    | 6     | Código do evento: - 110111 - 'Cancelamento' - 110112 - 'Cancelamento por substituição'                                                                                                                    |
| P15 | nSeqEvento  | E     | P06   | N      | 1-1    | 1-2   | Sequencial do evento para o mesmo tipo de evento. Informar o valor '1' para este evento.                                                                                                                  |
| P16 | verEvento   | E     | P06   | N      | 1-1    | 2v2   | Versão do grupo de detalhe do evento.                                                                                                                                                                     |
| P17 | detEvento   | G     | P06   |        | 1-1    | -     | Detalhes do evento                                                                                                                                                                                        |
| P18 | versao      | A     | P17   | N      | 1-1    | 2v2   | Informar o mesmo valor da tag 'verEvento' (P16)                                                                                                                                                           |
| P19 | descEvento  | E     | P17   | C      | 1-1    | 5-60  | Veja a descrição do evento, junto com o Tipo de Evento documentado anteriormente.                                                                                                                         |
| P20 | cOrgaoAutor | E     | P17   | N      | 1-1    | 2     | Código do Órgão Autor do Evento. Informar o Código da UF para este Evento. Nota : Campo exclusivo do Evento '110112 - Cancelamento por substituição'.                                                     |
| P21 | tpAutor     | E     | P17   | N      | 1-1    | 1     | Informar 1=Empresa Emitente. Valores : 1=Empresa Emitente, 2=Empresa destinatária; 3=Empresa; 5=Fisco; 6=RFB; 9=Outros Órgãos; Nota : Campo exclusivo do Evento '110112 - Cancelamento por substituição'. |
| P22 | verAplic    | E     | P17   | C      | 1-1    | 1-20  | Versão do aplicativo do Autor do Evento. Nota : Campo exclusivo do Evento '110112 - Cancelamento por substituição'.                                                                                       |
| P23 | nProt       | E     | P17   | N      | 1-1    | 15    | Informar o número do Protocolo de Autorização da NF-e a ser cancelada.                                                                                                                                    |

![Image](assets/image_000005_7960d33f2b154f941221050690ae870cb6f1c389263b12926bbfcde80ed5f207.png)

![Image](assets/image_000006_a20eb4127a92e4e96aa17396e899af8e65868f6845cc40d1918d9691b0b89ec9.png)

![Image](assets/image_000007_6302b6a89c8cf0826c2aa405deecce27637e4701d1b6d67f5e7193241a406406.png)

| #   | Campo     | Ele   | Pai   | Tipo   | Ocor   | Tam     | Descrição/Observação                                                                                                                             |
|-----|-----------|-------|-------|--------|--------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| P30 | xJust     | E     | P17   | C      | 1-1    | 15- 255 | Informar a justificativa do cancelamento                                                                                                         |
| P31 | chNFeRef  | E     | P17   | N      | 1-1    | 44      | Informa a chave de acesso da NF-e substituta da NF-e a ser cancelada. Nota : Campo exclusivo do Evento '110112 - Cancelamento por substituição'. |
| P91 | Signature | G     | P04   | XML    | 1-1    | -       | Assinatura Digital do documento XML, a assinatura deverá ser aplicada no elemento infEvento                                                      |

## 2.2. Leiaute Mensagem de Retorno

O Web Service de Registro de Evento possui uma interface genérica, complementada por uma área específica para cada tipo de evento. Segue o leiaute da mensagem de retorno (resposta) deste evento.

Schema XML: retEnvEventoCancNFe\_v1.0.xsd (tpEvento=110111) retEventoCancSubst\_v1.0.xsd (tpEvento=110112)

| #   | Campo        | Ele   | Pai   | Tipo   | Ocorr   | Tam   | Descrição/Observação                                                                                                                                                                               |
|-----|--------------|-------|-------|--------|---------|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R01 | retEnvEvento | Raiz  | -     | -      | -       | -     | TAG raiz da mensagem de retorno                                                                                                                                                                    |
| R02 | versao       | A     | R01   | N      | 1-1     | 2v2   | Versão do leiaute                                                                                                                                                                                  |
| R03 | idLote       | E     | R01   | N      | 1-1     | 1-15  | Idem a mensagem de entrada.                                                                                                                                                                        |
| R04 | tpAmb        | E     | R01   | N      | 1-1     | 1     | Idem a mensagem de entrada.                                                                                                                                                                        |
| R05 | verAplic     | E     | R01   | C      | 1-1     | 1-20  | Versão da aplicação que processou o evento.                                                                                                                                                        |
| R06 | cOrgao       | E     | R01   | N      | 1-1     | 2     | Órgão de recepção do Evento, idem a mensagem de entrada.                                                                                                                                           |
| R07 | cStat        | E     | R01   | N      | 1-1     | 3     | Código do status da resposta                                                                                                                                                                       |
| R08 | xMotivo      | E     | R01   | C      | 1-1     | 1-255 | Descrição do status da resposta                                                                                                                                                                    |
| R09 | retEvento    | G     | R01   | -      | 0-20    | -     | Grupo do resultado do processamento do Evento                                                                                                                                                      |
| R10 | versao       | A     | R09   | N      | 1-1     | 2v2   | Versão do leiaute                                                                                                                                                                                  |
| R11 | infEvento    | G     | R09   |        | 1-1     | -     | Grupo de informações do registro do Evento                                                                                                                                                         |
| R12 | Id           | ID    | R11   | C      | 0-1     | 17    | Identificador da TAG a ser assinada, somente deve ser informado se o órgão de registro assinar a resposta. No caso de assinatura, preencher com o número do protocolo, precedido pela literal 'ID' |
| R13 | tpAmb        | E     | R11   | N      | 1-1     | 1     | Idem a mensagem de entrada.                                                                                                                                                                        |
| R14 | verAplic     | E     | R11   | C      | 1-1     | 1-20  | Versão da aplicação que registrou o Evento, utilizar literal que permita a identificação do órgão, como a sigla da UF ou do órgão.                                                                 |
| R15 | cOrgao       | E     | R11   | N      | 1-1     | 2     | Idem a mensagem de entrada.                                                                                                                                                                        |
| R16 | cStat        | E     | R11   | N      | 1-1     | 3     | Código do status da resposta.                                                                                                                                                                      |
| R17 | xMotivo      | E     | R11   | C      | 1-1     | 1-255 | Descrição do status da resposta.                                                                                                                                                                   |
| R18 | chNFe        | E     | R11   | N      | 0-1     | 44    | Idem a mensagem de entrada.                                                                                                                                                                        |
| R19 | tpEvento     | E     | R11   | N      | 0-1     | 6     | Idem a mensagem de entrada.                                                                                                                                                                        |
| R20 | xEvento      | E     | R11   | C      | 0-1     | 5-60  | Idem a mensagem de entrada.                                                                                                                                                                        |
| R21 | nSeqEvento   | E     | R11   | N      | 0-1     | 1-2   | Idem a mensagem de entrada.                                                                                                                                                                        |
| R22 | cOrgaoAutor  | E     | R11   | N      | 0-1     | 2     | Idem a mensagem de entrada. Nota : Campo exclusivo do Evento '110112 - Cancelamento por substituição'.                                                                                             |
| R23 | CNPJDest     | CE    | R11   | N      | 0-1     | 14    | Informar o CNPJ / CPF do destinatário da NF-e.                                                                                                                                                     |
| R24 | CPFDest      | CE    | R11   | N      | 0-1     | 11    | Nota : Campo exclusivo do Evento '110111 - Cancelamento'.                                                                                                                                          |
| R25 | emailDest    | E     | R11   | C      | 0-1     | 1-60  | E-mail do destinatário informado na NF-e. Nota : Campo exclusivo do Evento '110111 - Cancelamento'.                                                                                                |
| R30 | dhRegEvento  | E     | R11   | D      | 1-1     | -     | Data e hora de registro do evento no formato AAAA-MMDDTHH:MM:SSTZD (formato UTC).                                                                                                                  |

![Image](assets/image_000008_6735045370dbd12018e9a12008d4626738fa428a6c4320465cec91407c4509f7.png)

![Image](assets/image_000009_6302b6a89c8cf0826c2aa405deecce27637e4701d1b6d67f5e7193241a406406.png)

| #   | Campo     | Ele   | Pai   | Tipo   | Ocorr   | Tam   | Descrição/Observação                                                                                                                                                              |
|-----|-----------|-------|-------|--------|---------|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R31 | nProt     | E     | R11   | N      | 0-1     | 15    | Número do Protocolo do Evento 1 posição (1- Secretaria da Fazenda Estadual, 2-RFB), 2 posições para o código da UF, 2 posições para o ano e 10 posições para o sequencial no ano. |
| R91 | Signature | G     | R09   | XML    | 0-1     | -     | Assinatura Digital do documento XML, a assinatura deverá ser aplicada no elemento infEvento. A decisão de assinar a mensagem fica a critério da UF.                               |

Nota: No caso de evento registrado com sucesso, os campos opcionais serão retornados.

## 2.3. Descrição do Processo de Recepção de Evento

O  Web  Service  de  Evento  é  acionado  pelo  interessado,  emissor  de  NF-e,  que  deve  enviar mensagem com o pedido de cancelamento da NF-e.

O processo de Registro de Eventos recebe eventos em uma estrutura de lotes, que pode conter de 1 a 20 eventos.

## 2.4. Validação do Certificado de Transmissão

As validações de A01, A02, A03, A04 e A05 são realizadas pelo protocolo TLS e não precisam ser implementadas. A validação A06 também pode ser realizada pelo protocolo TLS, mas pode falhar se existirem outros certificados digitais de Autoridade Certificadora Raiz que não sejam 'ICP-Brasil' no repositório de certificados digitais do servidor de Web Service da SEFAZ.

Regras de validação idênticas aos demais Web Services, podendo gerar os erros:

-  280: 'Rejeição: Certificado Transmissor inválido'
-  281: 'Rejeição: Certificado Transmissor Data Validade'
-  283: 'Rejeição: Certificado Transmissor - erro Cadeia de Certificação'
-  286: 'Rejeição: Certificado Transmissor erro no acesso a LCR'
-  284: 'Rejeição: Certificado Transmissor revogado'
-  285: 'Rejeição: Certificado Transmissor difere ICP-Brasil'
-  282: 'Rejeição: Certificado Transmissor sem CNPJ/CPF'

## 2.5. Validação Inicial da Mensagem no Web Service

Regras de validação idênticas aos demais Web Services, podendo gerar os erros:

-  214: 'Rejeição: Tamanho da mensagem excedeu o limite estabelecido'
-  108: 'Serviço Paralisado Momentaneamente (curto prazo)'
-  109: 'Serviço Paralisado sem Previsão'
-  410: 'Rejeição: UF informada no campo cUF não é atendida pelo WebService'
-  239: 'Rejeição: Versão do arquivo XML não suportada'

## 2.6. Validação da área de Dados

## a) Validação de forma da área de dados

Regras de validação idênticas aos demais Web Services, podendo gerar os erros:

-  516: 'Rejeição: Falha Schema XML, inexiste a tag raiz esperada para a mensagem'
-  517: 'Rejeição: Falha Schema XML, inexiste atributo versão na tag raiz da mensagem'
-  215: 'Rejeição: Falha Schema XML'
-  587: 'Rejeição: Usar somente o namespace padrão da NF-e'
-  588: 'Rejeição: Não é permitida a presença de caracteres de edição no início/fim da mensagem ou entre as tags da mensagem'
-  404: 'Rejeição: Uso de prefixo de namespace não permitido'
-  402: 'Rejeição: XML da área de dados com codificação diferente de UTF-8'

## b) Extração dos eventos do lote e validação do Schema XML do evento

Regras de validação idênticas aos demais Eventos, podendo gerar os erros:

-  491: 'Rejeição: O tpEvento informado invalido'
-  492: 'Rejeição: O verEvento informado invalido'
-  493: 'Rejeição: Evento não atende o Schema XML específico'

## c) Validação do Certificado Digital de Assinatura

Regras de validação idênticas aos demais Web Services, podendo gerar os erros:

-  290: 'Rejeição: Certificado Assinatura inválido'
-  291: 'Rejeição: Certificado Assinatura Data Validade'
-  292: 'Rejeição: Certificado Assinatura sem CNPJ/CPF'
-  293: 'Rejeição: Certificado Assinatura - erro Cadeia de Certificação'
-  296: 'Rejeição: Certificado Assinatura erro no acesso a LCR'
-  294: 'Rejeição: Certificado Assinatura revogado'
-  295: 'Rejeição: Certificado Assinatura difere ICP-Brasil'

## d) Validação da Assinatura Digital

Regras de validação idênticas aos demais Web Services, podendo gerar os erros:

-  298: 'Rejeição: Assinatura difere do padrão do Sistema'
-  297: 'Rejeição: Assinatura difere do calculado'
-  213: 'Rejeição: CNPJ-Base do Autor difere do CNPJ-Base do Certificado Digital'
-  227: 'Rejeição: 'CPF do Autor difere do CPF do Certificado Digital'

![Image](assets/image_000010_4ce977c4f1caa54baf2b9892e4dc47d44a8ec6a59a895a0cf0ef17b0d1c086a3.png)

## 2.7. Validação das Regras de Negócio

| #      | Regra de Validação                                                                                                                                                            | Aplic.   |   Msg | Descrição Erro                                                                                                        |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|-----------------------------------------------------------------------------------------------------------------------|
| P07-10 | Atributo 'Id' não corresponde à concatenação dos campos do evento ('ID' + tpEvento + chNFe + nSeqEvento) (*1)                                                                 | Obrig.   |   572 | Rejeição: Erro Atributo ID do evento não corresponde a concatenação dos campos ('ID' + tpEvento + chNFe + nSeqEvento) |
| P08-10 | Código do órgão de recepção do Evento diverge do definido para este evento (*1)                                                                                               | Obrig.   |   250 | Rejeição: UF diverge da UF autorizadora                                                                               |
| P09-10 | Tipo do ambiente difere do ambiente do Web Service (*1)                                                                                                                       | Obrig.   |   252 | Rejeição: Ambiente informado diverge do Ambiente de recebimento                                                       |
| P10-10 | Se informado CNPJ do Autor do Evento: - CNPJ inválido (zeros, nulo ou DV inválido) (*1)                                                                                       | Obrig.   |   489 | Rejeição: CNPJ informado inválido (DV ou zeros)                                                                       |
| P11-10 | Se informado o CPF do Autor do evento: - CPF inválido (zeros, nulo ou DV inválido) (*1)                                                                                       | Obrig.   |   490 | Rejeição: CPF informado inválido (DV ou zeros)                                                                        |
| P11-20 | Se informado o CPF do Autor do evento e Modelo da Chave de Acesso = 65: - Evento não disponível para Autor tipo pessoa física (*1)                                            | Obrig.   |   408 | Rejeição: Evento não disponível para Autor pessoa física                                                              |
| P12-10 | Validação da Chave de Acesso (tag:chNFe): - Dígito verificador inválido (*1)                                                                                                  | Obrig.   |   236 | Rejeição: Chave de Acesso com dígito verificador inválido                                                             |
| P12-14 | - Código UF inválido (*1)                                                                                                                                                     | Obrig.   |   614 | Rejeição: Chave de Acesso                                                                                             |
| P12-18 | - Ano < 06 ou Ano maior que Ano corrente (*1)                                                                                                                                 | Obrig.   |   615 | Rejeição: Chave de Acesso inválida (Ano < 06 ou Ano maior que Ano corrente)                                           |
| P12-22 | - Mês = 0 ou Mês > 12 (*1)                                                                                                                                                    | Obrig.   |   616 | Rejeição: Chave de Acesso inválida (Mês < 1 ou Mês > 12)                                                              |
| P12-26 | - CNPJ/CPF zerado ou dígito inválido (*1) Nota : Considerar a Série para determinar se CNPJ/CPF na Chave de Acesso. CNPJ: Série=[0-909], CPF: Série<>[0-909]                  | Obrig.   |   617 | Rejeição: Chave de Acesso inválida (CNPJ/CPF zerado ou dígito inválido)                                               |
| P12-30 | - Modelo diferente de 55 ou 65 (*1)                                                                                                                                           | Obrig.   |   618 | Rejeição: Chave de Acesso inválida (modelo diferente de 55/65)                                                        |
| P12-34 | - Número NF = 0 (*1)                                                                                                                                                          | Obrig.   |   619 | Rejeição: Chave de Acesso inválida (número NF = 0)                                                                    |
| P12-40 | - UF da Chave de Acesso diverge da UF Autorizadora                                                                                                                            | Obrig.   |   249 | Rejeição: UF da Chave de Acesso diverge da UF autorizadora                                                            |
| P12-44 | - CNPJ/CPF do Autor diverge do CNPJ/CPF da Chave de Acesso Nota : Considerar a Série para determinar se CNPJ/CPF na Chave de Acesso. CNPJ: Série=[0-909], CPF: Série<>[0-909] | Obrig.   |   574 | Rejeição: Autor do evento diverge do emissor da NF-e                                                                  |
| P12-48 | - Se tpEvento=110112 e - tpEmis da Chave de Acesso diferente de 1- Normal; - tpEmis da Chave de Acesso substituta (tag: chNFeRef) diferente de 9-Contingência;                | Obrig.   |   920 | Rejeição: Tipo de Emissão inválido no Cancelamento por Substituição                                                   |
| P13-10 | Data do evento maior que a data de processamento (aceitar tolerância de até 5 minutos) (*1)                                                                                   | Obrig.   |   578 | Rejeição: A data do evento não pode ser maior que a data do processamento                                             |
| P15-10 | Número de sequência do evento diferente de 1                                                                                                                                  | Obrig.   |   594 | Rejeição: Número de sequência do evento informado é maior do que o permitido                                          |
| P20-10 | - Se tpEvento=110112 e UF do Autor (cOrgaoAutor) diverge da UF da Chave de Acesso                                                                                             | Obrig.   |   455 | Rejeição: Órgão Autor do evento difere da UF da Chave de Acesso                                                       |
| P31-10 | Se tpEvento=110112, validar a Chave de Acesso substituta (tag:chNFeRef):                                                                                                      | Obrig.   |   910 | Rejeição: Chave de Acesso NF-e Substituta inválida (Dígito)                                                           |

![Image](assets/image_000011_76c1a61ffe4ebb5f21663f77949037bee54d1b79d59f3fbc8bfaf85d0fa2e1c3.png)

![Image](assets/image_000012_19084112d93eed54b704caa664abf0713d83191616a9a986efe2ab9f78f7c16d.png)

![Image](assets/image_000013_0f5b71abf44b0e43d63a0f3dd62c3ed91041135158a4f146ea39bd9c15fdd783.png)

| #                            | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                            | Aplic.                       | Msg                          | Descrição Erro                                                              |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|------------------------------|-----------------------------------------------------------------------------|
| P31-14                       | - Dígito verificador inválido - Código UF inválido                                                                                                                                                                                                                                                                                                                                                            | Obrig.                       | 910                          | Rejeição: Chave de Acesso NF-e Substituta inválida (Código UF)              |
| P31-18                       | - Ano < 06 ou Ano maior que Ano corrente                                                                                                                                                                                                                                                                                                                                                                      | Obrig.                       | 910                          | Rejeição: Chave de Acesso NF-e Substituta inválida (Ano)                    |
| P31-22                       | - Mês = 0 ou Mês > 12                                                                                                                                                                                                                                                                                                                                                                                         | Obrig.                       | 910                          | Rejeição: Chave de Acesso NF-e Substituta inválida (Mês)                    |
| P31-26                       | - CNPJ/CPF zerado ou dígito inválido Nota : Considerar a Série para determinar se CNPJ/CPF na Chave de Acesso. CNPJ: Série=[0-909], CPF: Série<>[0-909]                                                                                                                                                                                                                                                       | Obrig.                       | 910                          | Rejeição: Chave de Acesso NF-e Substituta inválida (CNPJ/CPF)               |
| P31-30                       | - Modelo diferente de 55 ou 65                                                                                                                                                                                                                                                                                                                                                                                | Obrig.                       | 910                          | Rejeição: Chave de Acesso NF-e Substituta inválida (Modelo)                 |
| P31-34                       | - Número NF = 0                                                                                                                                                                                                                                                                                                                                                                                               | Obrig.                       | 910                          | Rejeição: Chave de Acesso NF-e Substituta inválida (Número)                 |
| P31-38                       | - Chave de Acesso da NF-e Substituta igual a Chave de Acesso da NF-e a ser cancelada                                                                                                                                                                                                                                                                                                                          | Obrig.                       | 911                          | Rejeição: Chave de Acesso NF-e Substituta incorreta (mesma Chave de Acesso) |
| P31-42                       | - Chave de Acesso da NF-e Substituta com UF divergente da Chave de Acesso da NF-e a ser cancelada                                                                                                                                                                                                                                                                                                             | Obrig.                       | 911                          | Rejeição: Chave de Acesso NF-e Substituta incorreta (Código da UF)          |
| P31-46                       | - Chave de Acesso da NF-e Substituta com CNPJ/CPF divergente da Chave de Acesso da NF-e a ser cancelada Nota : Considerar a Série para determinar se CNPJ/CPF na Chave de Acesso. CNPJ: Série=[0-909], CPF: Série<>[0-909]                                                                                                                                                                                    | Obrig.                       | 911                          | Rejeição: Chave de Acesso NF-e Substituta incorreta (CNPJ/CPF)              |
| P31-52                       | - Chave de Acesso da NF-e Substituta com Modelo divergente da Chave de Acesso da NF-e a ser cancelada                                                                                                                                                                                                                                                                                                         | Obrig.                       | 911                          | Rejeição: Chave de Acesso NF-e Substituta incorreta (Modelo)                |
| *** Banco de Dados: Emitente | *** Banco de Dados: Emitente                                                                                                                                                                                                                                                                                                                                                                                  | *** Banco de Dados: Emitente | *** Banco de Dados: Emitente | *** Banco de Dados: Emitente                                                |
| 1P10-10                      | Acesso ao Cadastro de Contribuintes (Chave: CNPJ do Autor): - Verificar se Emitente não autorizado a emitir NF- e                                                                                                                                                                                                                                                                                             | Obrig.                       | 203                          | Rejeição: Emissor não habilitado para emissão de NF-e                       |
| 1P10-20                      | - Verificar situação fiscal do emitente                                                                                                                                                                                                                                                                                                                                                                       | Obrig.                       | 240                          | Rejeição: Irregularidade fiscal do emitente                                 |
| *** Banco de Dados: NF-e     | *** Banco de Dados: NF-e                                                                                                                                                                                                                                                                                                                                                                                      | *** Banco de Dados: NF-e     | *** Banco de Dados: NF-e     | *** Banco de Dados: NF-e                                                    |
| 2P12-10                      | Acesso BD NFE (Chave: CNPJ/CPF da Chave de Acesso, Modelo, Série e Número): - Chave Acesso inexistente para o tpEvento que exige a existência da NF-e (*1) Nota : Caso exista no banco de dados uma NF-e com Chave de Acesso divergente, opcionalmente, deverá ser concatenado a Chave de Acesso existente na descrição do erro, caso o CNPJ/CPF do Autor do Evento seja o mesmo CNPJ/CPF da Chave de Acesso. | Obrig.                       | 494                          | Rejeição: Chave de Acesso Inexistente (chNFe:999...999]                     |
| 2P12-14                      | - Se tpEvento=110111 (Cancelamento Normal): - Se modelo=55 (NF-e) e NF autorizada há mais de 24 horas; - Se modelo=65 (NFC-e) e NF autorizada há mais de 30 minutos. Nota: Considera a exceção de prazo definida em legislação estadual                                                                                                                                                                       | Obrig.                       | 501                          | Rejeição: Prazo de cancelamento superior ao previsto na Legislação          |
| 2P12-18                      | - Se tpEvento=110112 (Cancelamento por Substituição): verificar se NF-e autorizada há mais de 7 dias (168 horas). Nota : Considera a exceção de prazo definida em legislação estadual                                                                                                                                                                                                                         | Obrig.                       | 501                          | Rejeição: Prazo de cancelamento superior ao previsto na Legislação          |
| 2P12-22                      | - Verificar se NF-e está denegada ou cancelada                                                                                                                                                                                                                                                                                                                                                                | Obrig.                       | 580                          | Rejeição: Evento exige uma NF- e autorizada                                 |

![Image](assets/image_000014_0f5b71abf44b0e43d63a0f3dd62c3ed91041135158a4f146ea39bd9c15fdd783.png)

| #                            | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Aplic.                       | Msg                          | Descrição Erro                                                                  |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|------------------------------|---------------------------------------------------------------------------------|
| 2P13-10                      | - Data do evento menor que a Data de Emissão da NF-e (*1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Obrig.                       | 577                          | Rejeição: A data do evento não pode ser menor que a data de emissão da NF-e     |
| 2P13-14                      | - Data do evento menor que a Data de Autorização da NF-e não emitida em contingência (tpEmis=1) Nota : Na comparação acima, aceitar uma tolerância de 5 minutos, devido ao sincronismo de horário entre o servidor da Empresa e o servidor da SEFAZ Autorizadora.                                                                                                                                                                                                                                                                                                                        | Obrig.                       | 579                          | Rejeição: A data do evento não pode ser menor que a data de autorização da NF-e |
| 2P23-10                      | - Número do Protocolo informado diverge do número do Protocolo da NF-e                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Obrig.                       | 222                          | Rejeição: Protocolo de Autorização de Uso difere do cadastrado                  |
| *** Banco de Dados: Evento   | *** Banco de Dados: Evento                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | *** Banco de Dados: Evento   | *** Banco de Dados: Evento   | *** Banco de Dados: Evento                                                      |
| 3P15-10                      | Acesso BD de Eventos (Chave: Chave de Acesso, tpEvento, nSeqEvento): - Duplicidade do evento (tpEvento + chNFe + nSeqEvento) (*1)                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Obrig.                       | 573                          | Rejeição: Duplicidade de Evento                                                 |
| *** Banco de Dados: Evento_2 | *** Banco de Dados: Evento_2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | *** Banco de Dados: Evento_2 | *** Banco de Dados: Evento_2 | *** Banco de Dados: Evento_2                                                    |
| 4P15-14                      | Se NF-e (Modelo 55): Acesso ao BD de Eventos (Chave: Chave de Acesso, tag:chNFe): - Existe evento de Manifestação do Destinatário - tpEvento = '210220-Confirmação da Operação' Exceção : A NF-e pode ter mais de um tipo de Manifestação do Destinatário, prevalecendo a última manifestação. Permitir o cancelamento se após o evento de 'Confirmação' existir um dos eventos abaixo: - '210220 - Desconhecimento da Operação' - '210240 - Operação não Realizada'.                                                                                                                    | Obrig.                       | 221                          | Rejeição: Confirmado o recebimento da NF-e pelo destinatário                    |
| 4P15-18                      | - Existe evento de Conhecimento de Transporte ou MDF-e Autorizado, tpEvento: - '610600 - CT-e Autorizado' (Cancelamento: 610601) - '610610 - MDF-e Autorizado' (Cancelamento: 610611) - '610614 - MDF-e Autorizado com CT-e' (Canc: 610615) Exceção : Uma NF-e pode participar de vários CT-e / MDF-e. Permitir o cancelamento se todos os eventos deste tipo tiverem o                                                                                                                                                                                                                  | Obrig.                       | 690                          | Rejeição: Pedido de Cancelamento para NF-e com CT-e / MDF-e                     |
| 4P15-22                      | correspondente evento de cancelamento. - Existe evento de Registro de Passagem, tpEvento: - '610500 - Registro de Passagem NF-e' (Canc: 610501); - '610510 - Registro de Passagem MDF-e' (Canc: 610511) - '610514 - Registro Passagem MDF-e com CT-e' (Canc: 610515) - '610550 - Registro Passagem NF-e BRId' - '610552 - Registro Passagem Automático MDF-e' - '610554 - Registro Passagem Automático MDF-e com CT-e' Exceção : Uma NF-e pode ter vários Registros de Passagem. Permitir o cancelamento se todos os eventos deste tipo tiverem o correspondente evento de cancelamento. | Obrig.                       | 219                          | Rejeição: Circulação da NF-e verificada                                         |
| 4P15-26                      | - Existe evento da Suframa, tpEvento: - '990900 - Vistoria SUFRAMA'; - '9910910 - Internalização SUFRAMA';                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Obrig.                       | 304                          | Rejeição: Pedido de Cancelamento para NF-e com evento da Suframa                |

![Image](assets/image_000015_f6bd9aa3d664942c7e18be09d9e00fc212b97a6c3c45fa6671e212235d1ac0c4.png)

| #                          | Regra de Validação                                                                                                                                                                                                                                    | Aplic.   |   Msg | Descrição Erro                                                                                                              |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|-----------------------------------------------------------------------------------------------------------------------------|
| *** Banco de Dados: NF-e_2 | *** Banco de Dados: NF-e_2                                                                                                                                                                                                                            |          |       |                                                                                                                             |
| 5P31-10                    | Se tpEvento=110112 (Cancelamento por Substituição): Acesso BD NFE (Chave: Chave de Acesso Substituta, tag:chNFeRef): - Chave Acesso Substituta inexistente                                                                                            | Obrig.   |   912 | Rejeição: NF-e Substituta inexistente                                                                                       |
| 5P31-14                    | - Situação da NF-e = Denegada ou Cancelada                                                                                                                                                                                                            | Obrig.   |   913 | Rejeição: NF-e Substituta Denegada ou Cancelada                                                                             |
| 5P31-20                    | - Data de emissão da NF-e substituta (chNFeRef) maior que 2 horas da data de emissão da NF-e a ser cancelada (chNFe)                                                                                                                                  | Obrig.   |   914 | Rejeição: Data de emissão da NF-e Substituta maior que 2 horas da data de emissão da NF-e a ser cancelada                   |
| 5P31-24                    | - Valor total da NF-e substituta (chNFeRef) difere do valor total da NF-e a ser cancelada (chNFe)                                                                                                                                                     | Obrig.   |   915 | Rejeição: Valor total da NF-e Substituta difere do valor da NF-e a ser cancelada                                            |
| 5P31-28                    | - Valor total do ICMS da NF-e substituta (chNFeRef) difere do valor total do ICMS da NF- e a ser cancelada (chNFe)                                                                                                                                    | Obrig.   |   916 | Rejeição: Valor total do ICMS da NF-e Substituta difere do valor da NF-e a ser cancelada                                    |
| 5P31-32                    | - Se foi identificado o destinatário na NF-e original (CNPJ/CPF/ID Estrangeiro): - Identificação do destinatário (CNPJ/CPF/ID Estrangeiro, IE) da NF-e substituta (chNFeRef) difere da identificação do destinatário da NF-e a ser cancelada (chNFe). | Obrig.   |   917 | Rejeição: Identificação do destinatário da NF-e Substituta difere da identificação do destinatário da NF-e a ser cancelada. |
| 5P31-36                    | - Quantidade de Itens da NF-e substituta (chNFeRef) difere da quantidade de itens da NF- e a ser cancelada (chNFe).                                                                                                                                   | Obrig.   |   918 | Rejeição: Quantidade de itens da NF-e Substituta difere da quantidade de itens da NF-e a ser cancelada.                     |
| 5P31-40                    | - Verificar se o item da NF-e substituta (chNFeRef) difere do respectivo item da NF-e a ser cancelada (chNFe). Nota : Verificar divergência para os campos cProd, cEAN, xProd, NCM, CFOP, uCom, qCom, vUnCom, vProd, indTot                           | Obrig.   |   919 | Rejeição: Item da NF-e Substituta difere do mesmo item da NF-e a ser cancelada.                                             |

Nota:  (*1) Validações genéricas do Registro de Evento.

## 2.8. Final do Processamento do Lote

O processamento do lote pode resultar em:

-  Rejeição do Lote - por algum problema que comprometa o processamento do lote;
-  Processamento do Lote - o lote foi processado (cStat=128), a validação de cada evento do lote poderá resultar em:
-  Rejeição - o Evento será descartado, com retorno do código do status do motivo da rejeição;
-  Recebido pelo Sistema de Registro de Eventos, com vinculação do evento na NF-e , o Evento  será  armazenado  no  repositório  do  Sistema  de  Registro  de  Eventos  com  a vinculação do Evento à respectiva NF-e (cStat=135);

Nota: A SEFAZ autorizadora poderá aceitar o cancelamento fora de prazo, mantendo um código de retorno diferente para estes casos. Nestes casos, deverá ser utilizado o Status '155-Cancelamento homologado fora de prazo'.

## 3 Novos códigos de rejeição

|   CÓDIGO | MOTIVO DE NÃO ATENDIMENTO DA SOLICITAÇÃO                                                                                    |
|----------|-----------------------------------------------------------------------------------------------------------------------------|
|      910 | Rejeição: Chave de Acesso NF-e Substituta inválida (<nome do campo>)                                                        |
|      911 | Rejeição: Chave de Acesso NF-e Substituta incorreta (<nome do campo>)                                                       |
|      912 | Rejeição: NF-e Substituta inexistente                                                                                       |
|      913 | Rejeição: NF-e Substituta Denegada ou Cancelada                                                                             |
|      914 | Rejeição: Data de emissão da NF-e Substituta maior que 2 horas da data de emissão da NF- e a ser cancelada                  |
|      915 | Rejeição: Valor total da NF-e Substituta difere do valor da NF-e a ser cancelada                                            |
|      916 | Rejeição: Valor total do ICMS da NF-e Substituta difere do valor da NF-e a ser cancelada                                    |
|      917 | Rejeição: Identificação do destinatário da NF-e Substituta difere da identificação do destinatário da NF-e a ser cancelada. |
|      918 | Rejeição: Quantidade de itens da NF-e Substituta difere da quantidade de itens da NF-e a ser cancelada.                     |
|      919 | Rejeição: Item da NF-e Substituta difere do mesmo item da NF-e a ser cancelada.                                             |
|      920 | Rejeição: Tipo de Emissão inválido no Cancelamento por Substituição                                                         |

![Image](assets/image_000016_7960d33f2b154f941221050690ae870cb6f1c389263b12926bbfcde80ed5f207.png)