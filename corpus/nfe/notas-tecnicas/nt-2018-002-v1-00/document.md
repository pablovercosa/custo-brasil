---
title: "Projeto Nota Fiscal Eletrônica"
slug: "nt-2018-002-v1-00"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "33bccb4e33729acc5af60778b6f764dc6aa4e0ab7ec0b63293b4b9963b146a5e"
converted_at_utc: "2026-06-25T15:27:41.624740+00:00"
status: "published"
type: "nota_tecnica"
---
![Image](assets/image_000000_33bc90e3d0b38c2d35755a3212489879b66d1b89881673a0582970b00df7fd1c.png)

## Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_5e74d9ab48b86a9a9fe463146f204e471f0d5715d9601340c2b294e5409d5360.png)

## Nota Técnica 2018/002 Consumo Indevido

![Image](assets/image_000002_2246e6788dcb019b464f6a5b7c7871540cdf9e6b2df40a158b9b6668e75d392f.png)

Versão 1.00

Abril de 2018

![Image](assets/image_000003_43cc4335ce6aa7915d881f3e43b952fc6a2fb23957bd9f52d893d5bee88d9b24.png)

## 1 Resumo

Atualmente, várias UF autorizadoras de documentos fiscais eletrônicos estão tendo seus serviços utilizados de forma indevida por alguns contribuintes. Esse uso indevido pode comprometer a estabilidade dos Web Services e resultar na saturação dos recursos, deixando o ambiente autorizador inoperante, podendo também ser interpretadas como ataques aos recursos de processamento, rede e armazenamento.

Portanto, para preservar os sistemas autorizadores, observado um comportamento indevido da aplicação de alguma empresa no consumo dos diversos Web Services, a SEFAZ autorizadora, a seu critério, poderá implantar as regras de validação de Consumo Indevido.

O contribuinte que estiver utilizando indevidamente os sistemas poderá sofrer as penalidades definidas na legislação de cada UF.

Os prazos previstos para a implementação das mudanças são:

- o Ambiente de Homologação (ambiente de teste das empresas): 02/05/2018
- o Ambiente de Produção : 16/05/2018

## 2 Regras de Validação Consumo Indevido (RV)

A critério da SEFAZ Autorizadora, as requisições enviadas em ' looping ' e/ou com erro poderão ser rejeitadas com o erro '656-Rejeição: Consumo indevido', independentemente de outras medidas saneadoras do erro detectado.

## 2.1 Web Service de Autorização

| Campo- Seq   | Modelo   | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                                            |
|--------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|---------------------------------------------------------------------------------------------------------------------------|
|              | 55/65    | NF-e/NFC-e* enviada com mais de 30* rejeições iguais: - Contribuinte ficará com o WS de autorização recebendo a rejeição 656 por até 1 (uma)* hora para todas as requisições. Observação 1:Caso após o tempo de 1 (uma)* hora o contribuinte envie novamente a mesma NF-e/NFC-e* e tenha a mesma rejeição, ele poderá voltar a receber a rejeição 656 por até 1 (uma)* hora, e isso se repetirá até ele parar de enviar a NF-e com a mesma rejeição. Observação 2: A verificação do contribuinte para receber a rejeição 656 poderá ser feita em tempo de conexão pela identificação do CNPJ do certificado digital de transmissão mais | Facult.  |   656 | Rej.     | Rejeição: Consumo indevido pelo aplicativo da empresa [det: Quantidade de rejeições encontradas: XXX, NF-e: CHAVE_ACESSO] |

![Image](assets/image_000004_33bc90e3d0b38c2d35755a3212489879b66d1b89881673a0582970b00df7fd1c.png)

| Campo- Seq   | Modelo   | Regra de Validação                                                                                                                                                                                                                                                                                                    | Aplic.   | Msg Efeito   | Descrição Erro   |
|--------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|--------------|------------------|
|              |          | o endereço IP (CNPJ + IP) ou pela identificação do CNPJ do emitente (emit/CNPJ). Observação 3: A critério da UF, após 50* bloqueios o contribuinte poderá receber a rejeição 656 permanentemente, até entrar em contato com a UF autorizadora. (*) Critérios preferenciais, parametrizáveis por ambiente autorizador. |          |              |                  |

## 2.2 Web Service de Eventos

| Campo- Seq   | Modelo   | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                                         |
|--------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|------------------------------------------------------------------------------------------------------------------------|
|              | 55/65    | Evento enviado com mais de 20 * rejeições iguais: - Contribuinte ficará com o WS de Eventos recebendo a rejeição 656 por até 1 (uma)* hora para todas as requisições. Observação 1: Caso após o tempo de 1 (uma)* hora o contribuinte envie novamente o mesmo Evento e tenha a mesma rejeição, ele poderá voltar a receber a rejeição 656 por até 1 (uma)* hora, e isso se repetirá até ele parar de enviar o Evento com a mesma rejeição. Observação 2: A verificação do contribuinte para receber a rejeição 656 poderá ser feita em tempo de conexão pela identificação do CNPJ do certificado digital de transmissão mais o endereço IP (CNPJ + IP) ou pela identificação do CNPJ do emitente (emit/CNPJ). Observação 3: A critério da UF, após 50* bloqueios o contribuinte poderá receber a rejeição 656 permanentemente, até entrar em contato com a UF autorizadora. (*) Critérios preferenciais, parametrizáveis por ambiente | Facult.  |   656 | Rej.     | Rejeição: Consumo indevido pelo aplicativo da empresa [det: Quantidade de rejeições encontradas: XXX, NF-e: ID_EVENTO] |

![Image](assets/image_000005_43cc4335ce6aa7915d881f3e43b952fc6a2fb23957bd9f52d893d5bee88d9b24.png)

## 2.3 Web Service de Inutilização

| Campo- Seq   | Modelo   | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                                               |
|--------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|------------------------------------------------------------------------------------------------------------------------------|
|              | 55/65    | Inutilização enviada com mais de 20* rejeições iguais: - Contribuinte (CNPJ + IP) ficará com o WS de Inutilização recebendo a rejeição 656 por até 1 (uma)* hora para todas as requisições. Observação 1: Caso após o tempo de 1 (uma)* hora o contribuinte envie novamente a mesma Inutilização e tenha a mesma rejeição, ele poderá voltar a receber a rejeição 656 por até 1 (uma)* hora, e isso se repetirá até ele parar de enviar a Inutilização com a mesma rejeição. Observação 2: A verificação do contribuinte para receber a rejeição 656 poderá ser feita em tempo de conexão pela identificação do CNPJ do certificado digital de transmissão mais o endereço IP (CNPJ + IP) ou pela identificação do CNPJ do emitente (emit/CNPJ). Observação 3: A critério da UF, após 50* bloqueios o contribuinte poderá receber a rejeição 656 permanentemente, até entrar em contato com a UF autorizadora. (*) Critérios preferenciais, parametrizáveis por ambiente autorizador. | Facult.  |   656 | Rej.     | Rejeição: Consumo indevido pelo aplicativo da empresa [det: Quantidade de rejeições encontradas: XXX, Inutilização: ID_INUT] |

## 2.4 Web Service de Consulta Protocolo

| Campo- Seq   | Modelo   | Regra de Validação                                                                                                                                                                                                                                                                                               | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                                                  |
|--------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|---------------------------------------------------------------------------------------------------------------------------------|
|              | 55/65    | NF-e consultada mais de 10* vezes em 1 (uma)* hora: - Contribuinte ficará com o WSde Consulta Protocolo recebendo a rejeição 656 por até 1 (uma)* hora para todas as requisições. Observação 1: Após o tempo de 1 (uma)* hora o contribuinte poderá fazer novamente mais 10* consultas da mesma chave de acesso. | Facult.  |   656 | Rej.     | Rejeição: Consumo indevido pelo aplicativo da empresa [det: Número máximo de consultas excedido (10) para a NF-e: CHAVE_ACESSO] |

![Image](assets/image_000006_33bc90e3d0b38c2d35755a3212489879b66d1b89881673a0582970b00df7fd1c.png)

| Campo- Seq   | Regra de Validação                                                                                                                                                                                                                                                                                                                         | Aplic.   | Msg Efeito   | Descrição Erro   |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|--------------|------------------|
|              | Observação 2: A verificação do contribuinte para receber a rejeição 656 poderá ser feita em tempo de conexão pela identificação do CNPJ do certificado digital de transmissão mais o endereço IP (CNPJ + IP) ou pela identificação do CNPJ do emitente (emit/CNPJ). (*) Critérios preferenciais, parametrizáveis por ambiente autorizador. |          |              |                  |

## 2.5 Web Service de Consulta Lote

| Campo- Seq   | Modelo   | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                                                  |
|--------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|---------------------------------------------------------------------------------------------------------------------------------|
|              | 55/65    | Recibo consultado mais de 40* vezes em 1 (uma)* hora: - Contribuinte ficará com o WS de Consulta Lote recebendo a rejeição 656 por até 1 (uma)* hora para todas as requisições. Observação 1: Após o tempo de 1 (uma)* hora o contribuinte poderá fazer novamente mais 40* consultas do número do lote. Observação 2: A verificação do contribuinte para receber a rejeição 656 será feita em tempo de conexão pela identificação do CNPJ do certificado digital de transmissão mais o endereço IP (CNPJ + IP) ou pela identificação do CNPJ do emitente (emit/CNPJ). (*) Critérios preferenciais, parametrizáveis por ambiente autorizador. | Facult.  |   656 | Rej.     | Rejeição: Consumo indevido pelo aplicativo da empresa [det: Número máximo de consultas excedido (40) para o recibo: NUM_RECIBO] |

## 2.6 Outros Serviços

| Campo- Seq   | Modelo   | Regra de Validação                                                                                                                                 | Aplic.   | Msg Efeito   | Descrição Erro                                                          |
|--------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------|----------|--------------|-------------------------------------------------------------------------|
|              | 55/65    | Se for verificado algum tipo de envio em looping (mais de 40* envios repetidos) em outro Web Service que gere erro ou onere o sistema autorizador: | Facult.  | 656 Rej.     | Rejeição: Consumo indevido pelo aplicativo da empresa [det: DESC_ERRO ] |

![Image](assets/image_000007_33bc90e3d0b38c2d35755a3212489879b66d1b89881673a0582970b00df7fd1c.png)

| Campo- Seq   | Modelo   | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                                                          | Aplic.   | Msg Efeito   | Descrição Erro   |
|--------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|--------------|------------------|
|              |          | - Contribuinte ficará com o WebService recebendo a rejeição 656 por até 1 (uma)* hora para todas as requisições. Observação 1: A verificação do contribuinte para receber a rejeição 656 poderá ser feita em tempo de conexão pela identificação do CNPJ do certificado digital de transmissão mais o endereço IP (CNPJ + IP) ou pela identificação do CNPJ do emitente (emit/CNPJ). (*) Critérios preferenciais, parametrizáveis por ambiente autorizador. |          |              |                  |

![Image](assets/image_000008_43cc4335ce6aa7915d881f3e43b952fc6a2fb23957bd9f52d893d5bee88d9b24.png)

## ANEXO I - ERROS E PROBLEMAS COMUNS

O erro e problema mais comum encontrado pelas UFs é o envio repetido (em looping) de requisições para os Web Services dos sistemas autorizadores de documentos fiscais eletrônicos. Normalmente isso ocorre devido algum erro na aplicação do emissor de documentos fiscais eletrônicos ou má utilização do usuário.

Após o envio de uma requisição para o sistema autorizador, essa requisição pode ser autorizada ou rejeitada. Caso ela seja rejeitada, o usuário do sistema deverá verificar o motivo da rejeição e corrigi-la, se assim desejar, ou caso a rejeição seja indevida (o sistema autorizador rejeitou de forma equivocada) deverá entrar em contato com a SEFAZ autorizadora.

Seguem alguns exemplos de 'Consumo Indevido' dos Web Services existentes:

| Web Services                                    | Aplicação com erro/problema                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Envio de Lote de NF-e.                          |  Aplicação da empresa em 'looping' enviando o mesmo Lote de NF-e rejeitado por erro de Schema, ou em 'loop' com NF e rejeitada por um erro específico.  Usuário do sistema fica enviando manualmente a mesma NF-e (efeito pica-pau).                                                                                                                                                                                                                                    |
| Consulta Resultado do Lote.                     |  Aplicação da empresa efetua 'looping' consultando os números de Recibo de Lote em sequência, mesmo para Número de Recibo que não foram gerados para sua empresa.  Usuário do sistema fica enviando manualmente a mesma consulta (efeito pica-pau).                                                                                                                                                                                                                     |
| Evento da NF-e.                                 |  Aplicação da empresa em 'looping' enviando o mesmo Pedido de Cancelamento ou Evento, que sempre é rejeitado.  Usuário do sistema fica enviando manualmente o mesmo cancelamento ou evento (efeito pica-pau).                                                                                                                                                                                                                                                           |
| Inutilização de Numeração.                      |  Aplicação da empresa em 'looping' enviando o mesmo pedido de inutilização, que sempre é rejeitado  Usuário do sistema fica enviando manualmente o mesmo pedido de Inutilização (efeito pica-pau).                                                                                                                                                                                                                                                                      |
| Consulta Situação da NF-e (Consulta Protocolo). |  Algumas empresas utilizam esta consulta para verificar a disponibilidade dos serviços da SEFAZ Autorizadora, consultando a mesma Chave de Acesso, em 'looping'.  Algumas empresas mantêm em 'looping' uma consulta as Chaves de Acesso de NF-e destinadas para sua empresa. Em alguns casos, fica sendo consultada uma Chave de Acesso inexistente durante meses.  Usuário do sistema fica enviando manualmente o mesmo pedido de consulta da NF-e (efeito pica-pau). |
| Consulta Status Serviço                         |  Aplicação em 'loop' consumindo o Web service em uma frequência maior do que a prevista.                                                                                                                                                                                                                                                                                                                                                                                 |

NT 2018.002
## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt-2018-002-v1-00/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt-2018-002-v1-00/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt-2018-002-v1-00.md)
- [Proveniência resumida](../../../../sources/provenance/nt-2018-002-v1-00.json)


## Documentos relacionados

- [[manual-de-boas-pr-ticas-nfc-e-bp-2018-001-vers-o-1-0]]
- [[nota-t-cnica-2016-001-v-1-40-publicada-em-16-07-2018]]
- [[nt-2018-003-v1-01-tabela-de-pa-ses]]
- [[nt-2018-004-cancelamento-por-substitui-o-da-nfc-e]]
- [[nt2018-001-v1-10-emitente-cpf]]
- [[nt2018-005-v1-52-alteracaodeleiautenf-enfc]]
