---
title: "Projeto Nota Fiscal Eletrônica"
slug: "nt-2007-008"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "c89a58c59c82a970fa3f2fdfa8873a3a91a5caca53a12de3e96acd02dfb4a087"
converted_at_utc: "2026-06-25T15:29:49.842809+00:00"
status: "published"
type: "nota_tecnica"
---
![Image](assets/image_000000_772887f126e5c274736c852a998f6aaffd031a3fc30b6e90de4b243faeb418d6.png)

## Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_ea0def68806c7538febacde7634326556b8a298a159849de896804dce067802a.png)

## Nota Técnica 2007/008 Divulga Manual de Integração do Contribuinte versão 2.04

![Image](assets/image_000002_92184f8bd39470e2cf03d293f30a766371086dd26fbc979d64245d6a03989d07.png)

Dezembro-2007

![Image](assets/image_000003_fe6be84161521e88755b2fcf6266ac33af92377ba5aa975f460bc794e3ba9dba.png)

## 1.  Resumo

Divulga Manual de Integração do Contribuinte - versão 2.0.4., com seguintes alterações:

- a) Leiaute da NF-e - alterações do tipo e tamanho de alguns campos para atender as necessidades dos contribuintes;
- c) DANFE os modelos de DANFE foram alterados para que o valor do indicador de ENTRADA/SAÍDA do DANFE tenha os mesmos valores informados na NF-e;
- b) Atualização  do  Manual  o  manual  de  integração  foi  atualizado  para  prever  a SEFAZ VIRTUAL;
- d) Correção ou aprimoramento de texto.

As alterações referidas neste documento têm como base o Manual de Orientação versão 2.02.

## 2.  Identificação e vigência do Manual de Integração do Contribuinte

| Versão do Manual de Integração do Contribuinte   | 2.04                             |
|--------------------------------------------------|----------------------------------|
| Chave de codificação digital MD5 do Manual       | dae55a67f5d2daeec9915eeb2a2e5c89 |
| Data de publicação                               | 26/12/2007                       |
| Data prevista para entrada em homologação        | 28/02/2008                       |
| Data prevista para entrada em produção           | 24/03/2008                       |

![Image](assets/image_000004_d662bdabbe94ec5ba3a6388f53b1315aad8ed53c337c5be8f2102169eed198dc.png)

## 3.  Alterações no leiaute da NF-e

## 3.1 Campo tpEmis (página 90)

Acréscimo do valor '3' como conteúdo válido do campo tpEmis do leiaute da Nota Fiscal eletrônica, que passa a aceitar a seguinte codificação para identificar a forma de emissão da NF-e:

- 1 Normal - emissão normal com transmissão da NF-e para a SEFAZ de origem;
- 2 Contingência off-line - emissão em contingência, com impressão do DANFE em formulário de segurança e posterior transmissão  da  NF-e  para  a  SEFAZ  de  origem  quando  sanado  os  problemas  técnicos  que  motivaram  a  adoção  da contingência;
- 3 Contingência SCAN - emissão em contingência no Sistema de Contingência do Ambiente Nacional - SCAN;

## Alterado de:

| 26   | B22   | tpEmis   | Forma de Emissão da NF-e   | E   | B01   | N   | 1-1   | 1   | 1-Normal/ 2-Contingência   |
|------|-------|----------|----------------------------|-----|-------|-----|-------|-----|----------------------------|

## Para:

| 26   | B22   | tpEmis   | Forma de Emissão da NF-e   | E   | B01   | N   | 1-1   | 1   | 1 - Normal - emissão normal com transmissão on-line da NF-e para a SEFAZ de origem; 2 - Contingência off-line - emissão em contingência, com impressão do DANFE em formulário de segurança e posterior transmissão da NF-e para a SEFAZ de origem quando sanados os problemas técnicos que motivaram a adoção da contingência; 3 - Contingência SCAN - emissão em contingência no Sistema de Contingência do Ambiente Nacional -   |
|------|-------|----------|----------------------------|-----|-------|-----|-------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

![Image](assets/image_000005_d662bdabbe94ec5ba3a6388f53b1315aad8ed53c337c5be8f2102169eed198dc.png)

SCAN;

## 3.2 Campo fone (página 92)

Aumento do tamanho do campo fone de 10 para 11 posições

## Alterado de:

45

C16

fone

Telefone

E

C05

N

0-1

1-10

Preencher com Código DDD + número do telefone.

## Para:

45

C16

Fone

Telefone

E

C05

N

0-1

1-11

Preencher com Código DDD + número do telefone.

## 3.3 Campo RENAVAM (página 99)

Alteração tipo do campo RENAVAM para caractere.

## Alterado de:

143

J15

RENAVAM

RENAVAM

E

J01

N

0-1

9

Não informar a TAG na exportação.

## Para:

![Image](assets/image_000006_a7c20ba28c840cbe5288f6f4fc88bfc21861235611fdc8685a4c987f0a3edf95.png)

| 143   | J15   | RENAVAM   | RENAVAM   | E   | J01   | C   | 0-1   | 9   | Não informar a TAG na exportação.   |
|-------|-------|-----------|-----------|-----|-------|-----|-------|-----|-------------------------------------|

## 3.4 Campo infAdFisco (página 121)

Aumento do tamanho do campo infAdFisco de 256 para 2.000 posições

## Alterado de:

| 400   | Z02   | infAdFisco   | Informações Adicionais de Interesse do Fisco   | E   | Z01   | C   | 0-1   | 1-256   |
|-------|-------|--------------|------------------------------------------------|-----|-------|-----|-------|---------|

## Para:

| 400   | Z02   | infAdFisco   | Informações Adicionais de Interesse do Fisco   | E   | Z01   | C   | 0-1   | 1-2000   |
|-------|-------|--------------|------------------------------------------------|-----|-------|-----|-------|----------|

## 3.5 Item 5 do Leiaute da NF-e  (página 129)

O item 5 que trata da chave de acesso da NF-e foi eliminado.

![Image](assets/image_000007_fe6be84161521e88755b2fcf6266ac33af92377ba5aa975f460bc794e3ba9dba.png)

## 4.  Alteração do Manual / SEFAZ Virtual

## 4.1 Inclusão de Texto (página 24)

## '3.6 SEFAZ VIRTUAL

As Secretarias da Fazenda Estadual podem optar por não desenvolver sistemas próprios de autorização da emissão da Nota Fiscal Eletrônica para os Contribuintes da sua jurisdição. Neste caso, os serviços da autorização de emissão da NF-e serão supridos por uma SEFAZ VIRTUAL, através de um Protocolo de cooperação assinado entre as SEFAZ e/ou entre a SEFAZ e a RFB.

Os serviços da SEFAZ VIRTUAL compreendem os Web Services descritos no Modelo Conceitual da Arquitetura de Comunicação, conforme consta no item 3.1 do Manual de Integração com o Contribuinte,

Atualmente estão previstas as operações das SEFAZ VIRTUAL de:

- SEFAZ VIRTUAL - RS
- SEFAZ VIRTUAL - RFB.

Em qualquer um dos casos, a responsabilidade sobre o credenciamento e sobre a autorização para o contribuinte usar os serviços de uma determinada SEFAZ VIRTUAL, é da SEFAZ de circunscrição do contribuinte.

Para os sistemas das Empresas, deve ser totalmente transparente se os serviços estão sendo disponibilizados pela SEFAZ VIRTUAL ou por um sistema de autorização da própria SEFAZ de circunscrição do contribuinte. A única mudança visível é no endereço dos Web Services onde ficam disponibilizados os serviços.'

## 4.2 Alteração de Texto (página 27)

## Alterado de:

| AR08 nRec   | E AR0 7   | N   | 1-1   | 15   | Número do Recibo gerado pelo Portal da Secretaria de Fazenda Estadual, composto por: duas posições com Código da UF onde foi entregue o lote, codificação de UF do IBGE, e treze posições numéricas seqüenciais. (vide item 5.5)   |
|-------------|-----------|-----|-------|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Para:

| AR0 8 nRec   | E AR0 7   | N   | 1-1   | 15   | Número do Recibo gerado pelo Portal da Secretaria de Fazenda Estadual, composto por duas posições com o Código da UF (codificação do IBGE) onde foi entregue o Lote, uma posição para o Tipo de Autorizador e doze posições numéricas seqüenciais   |
|--------------|-----------|-----|-------|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

![Image](assets/image_000008_fe6be84161521e88755b2fcf6266ac33af92377ba5aa975f460bc794e3ba9dba.png)

![Image](assets/image_000009_eb1932a8bea218adc57af58e680b0e13c0bdd65c74688c8b7adb9319bf160f15.png)

## 4.3 Alteração de Texto (página 27)

## Alterado de:

'Deverão ser realizadas as validações e procedimentos que seguem.'

## Para:

'Existe um limite de até 50 NF-e por lote e o agrupamento destas NF-e dentro do lote pode ser feito de qualquer uma das formas que seguem:

- todas as NF-e são do mesmo estabelecimento (mesmo CNPJ do Emitente);
- todas as NF-e são da mesma empresa (mesmo CNPJ-Base do Emitente);
- as NF-e são de diferentes Empresas.

Em qualquer um dos casos acima, por uma restrição operacional e de controle, todos os CNPJ emitentes devem ser da mesma Unidade da Federação.

Deverão ser realizadas as validações e procedimentos que seguem.'

## 4.4 Alteração de Texto (página 29)

## Alterado de:

'Não existindo qualquer problema nas validações acima referidas, o aplicativo deverá gerar um número de recibo composto por: duas posições com Código da UF onde foi entregue o lote (codificação de UF do IBGE) e treze posições numéricas seqüenciais e gravar a mensagem, juntamente com o número do recibo e o CNPJ do transmissor. '

## Para:

'Não existindo qualquer problema nas validações acima referidas, o aplicativo deverá gerar um número de recibo (vide item 5.5) e gravar a mensagem, juntamente com o número do recibo e o CNPJ do transmissor.'

## 4.5 Alteração de Texto (página 33)

## Alterado de:

![Image](assets/image_000010_a939ab80abed98b8b1877888aa76924d74ad1accfd31c3e19d49a06ff93ea213.png)

## Nota Fiscal Eletrônica

| G34   | Se finalidade da NF-e = 2 (NF-e complementar): - Verificar se o CNPJ emitente da NF Referenciada (válido se a NF referenciada for uma NF eletrônica ou não) é diferente do CNPJ do emitente desta NF-e   | Obrig.   | 269   | Rej.   |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|--------|

## Para:

| G34   | Se finalidade da NF-e = 2 (NF-e complementar): - Verificar se o CNPJ emitente da NF Referenciada (válido se a NF referenciada for uma NF eletrônica ou não) é diferente do CNPJ do emitente desta NF-e   | Obrig.   | 269   | Rej.   |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|--------|

'Nota: No caso de envio de lote para a SEFAZ VIRTUAL, todas as NF-e do Lote deverão ser da  mesma  UF.  Para  a  SEFAZ  VIRTUAL,  deverá  ser  verificado  se  todas  as  NF-e  são  da mesma UF da primeira NF-e do Lote. Em caso negativo, rejeitar a NF-e com erro 408-'Lote com NF-e de diferentes UF'.

## 4.6 Alteração de Texto (página 35)

## Alterado de:

| BP04   | nRec   | E   | BP01   | N   | 1-1   | 15   | Número do Recibo Número gerado pelo Portal da Secretaria de Fazenda Estadual, composto por: duas posições com código da UF onde foi entregue o lote, codificação de UF do IBGE, e treze posições numéricas seqüenciais.   |
|--------|--------|-----|--------|-----|-------|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Para:

| BP04 nRec   | E   | BP01   | N   | 1-1   | 15   | Número do Recibo (vide item 5.5)   |
|-------------|-----|--------|-----|-------|------|------------------------------------|

## 4.7 Alteração de Texto (página 35)

## Alterado de:

| BR04a nRec   | E   | BR01   | N   | 1-1   | 15   | Número do Recibo consultado   |
|--------------|-----|--------|-----|-------|------|-------------------------------|

## Para:

| BR04a nRec   | E   | BR01   | N   | 1-1   | 15   | Número do Recibo consultado (vide item 5.5)   |
|--------------|-----|--------|-----|-------|------|-----------------------------------------------|

## 4.8 Alteração de Texto (página 36)

## Alterado de:

| PR09 nProt   | E   | PR03   | N   | 0-1   | 15   | Número do Protocolo da NF-e   |
|--------------|-----|--------|-----|-------|------|-------------------------------|

![Image](assets/image_000011_c4e6daffbc318bd841fc00aef9f87a94e2b919c94e64e8100d060f4f9064a90b.png)

| 1 posição (1 - Secretaria de Fazenda Estadual 2 - Receita Federal); 2 posições para código da UF; 2 posições ano; 10 seqüencial no ano   |
|------------------------------------------------------------------------------------------------------------------------------------------|

## Para:

| PR09 nProt   | E   | PR03   | N   | 0-1   | 15   | Número do Protocolo da NF-e (vide item 5.6)   |
|--------------|-----|--------|-----|-------|------|-----------------------------------------------|

## 4.9 Alteração de Texto (página 40)

## Alterado de:

| CP08 nProt   | E   | CP03   | N   | 1-1   | 15   | Informar o número do Protocolo de Autorização da NF-e a ser Cancelada.   |
|--------------|-----|--------|-----|-------|------|--------------------------------------------------------------------------|

## Para:

| CP08 nProt   | E   | CP03   | N   | 1-1   | 15   | Informar o número do Protocolo de Autorização da NF-e a ser Cancelada.   |
|--------------|-----|--------|-----|-------|------|--------------------------------------------------------------------------|

## 4.10  Alteração de Texto (página 41)

## Alterado de:

| CR11 nProt   | E   | CR03   | N   | 0-1   | Número do Protocolo de Cancelamento 1 posição (1 - Secretaria de Fazenda Estadual 2 - Receita Federal); 2 posições para código da UF; 2 posições ano; 10 seqüencial no ano. O controle de numeração de Protocolo será único para todos os serviços.   |
|--------------|-----|--------|-----|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Para:

| CR11 nProt   | E   | CR03   | N   | 0-1   | 15   | Número do Protocolo de Cancelamento (vide item 5.6). O controle de numeração de Protocolo é único para todos os serviços.   |
|--------------|-----|--------|-----|-------|------|-----------------------------------------------------------------------------------------------------------------------------|

## 4.11  Alteração de Texto (página 47)

## Alterado de:

| DR17 nProt   | E DR03   | N   | 0-1   | 15   | Número do Protocolo de Inutilização   |
|--------------|----------|-----|-------|------|---------------------------------------|

![Image](assets/image_000012_c4e6daffbc318bd841fc00aef9f87a94e2b919c94e64e8100d060f4f9064a90b.png)

| 1 posição (1 - Secretaria de Fazenda Estadual 2 - Receita Federal); 2 posições para código da UF; 2 posições ano; 10 seqüencial no ano. O controle de numeração do Protocolo será único para todos os serviços.   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Para:

| DR17 nProt   | E   | DR03   | N   | 0-1   | 15   | Número do Protocolo de Inutilização (vide item 5.6). O controle de numeração do Protocolo é único para todos os serviços.   |
|--------------|-----|--------|-----|-------|------|-----------------------------------------------------------------------------------------------------------------------------|

## 4.12  Alteração de Texto (página 52)

## Alterado de:

| ER11 nProt   | E   | ER03   | N   | 0-1   | 15   | Número do Protocolo do   |
|--------------|-----|--------|-----|-------|------|--------------------------|

## Para:

| ER11 nProt   | E   | ER03   | N   | 0-1   | 15   | Número do Protocolo do Status atual da NF-e (vide item 5.6).   |
|--------------|-----|--------|-----|-------|------|----------------------------------------------------------------|

## 4.13  Acréscimo  da mensagem 408 (página 68)

| 408   | REJEIÇÃO: Lote com NF-e de diferentes UF   |
|-------|--------------------------------------------|

## 4.14  Alteração de Texto (página 71)

## Alterado de:

O número do Recibo do Lote deve ser gerado pelo Portal da Secretaria de Fazenda Estadual, com a seguinte regra de formação: duas posições com Código da UF onde foi entregue o lote e treze posições numéricas seqüenciais:

| 9            | 9            | 9                         | 9                         | 9                         | 9                         | 9                         | 9                         | 9                         | 9                         | 9                         | 9                         | 9                         | 9                         | 9                         |
|--------------|--------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|
| código da UF | código da UF | seqüencial de 13 posições | seqüencial de 13 posições | seqüencial de 13 posições | seqüencial de 13 posições | seqüencial de 13 posições | seqüencial de 13 posições | seqüencial de 13 posições | seqüencial de 13 posições | seqüencial de 13 posições | seqüencial de 13 posições | seqüencial de 13 posições | seqüencial de 13 posições | seqüencial de 13 posições |

## Para:

![Image](assets/image_000013_fe6be84161521e88755b2fcf6266ac33af92377ba5aa975f460bc794e3ba9dba.png)

O número do Recibo do Lote deve ser gerado pelo Portal da Secretaria de Fazenda Estadual, com a seguinte regra de formação:

- 2 posições com o Código da UF onde foi entregue o lote (codificação do IBGE);
- 1 posição com o Tipo de Autorizador (0 ou 1=SEFAZ normal, 2=Contingência SCAN - RFB, 3=SEFAZ VIRTUAL-RS, 4=SEFAZ VIRTUAL-RFB);
- 12 posições numéricas seqüenciais.

|                          |   Código da UF |   Tipo Autorizador |   seqüencial |
|--------------------------|----------------|--------------------|--------------|
| Quantidade de caracteres |             02 |                 01 |           12 |

## 4.15  Alteração de Texto (página 71)

## Alterado de:

A regra de formação do número do protocolo é:

| 9             | 9            | 9            | 9   | 9   | 9                         | 9                         | 9                         | 9                         | 9                         | 9                         | 9                         | 9                         | 9                         | 9                         |
|---------------|--------------|--------------|-----|-----|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|
| órgão gerador | código da UF | código da UF | ano | ano | seqüencial de 10 posições | seqüencial de 10 posições | seqüencial de 10 posições | seqüencial de 10 posições | seqüencial de 10 posições | seqüencial de 10 posições | seqüencial de 10 posições | seqüencial de 10 posições | seqüencial de 10 posições | seqüencial de 10 posições |

- 1 posição para indicar o órgão (1 - Secretaria de Fazenda Estadual 2 - Receita Federal);
- 2 posições para o código da UF do IBGE;
- 2 posições para ano;
- 10 posições para o seqüencial no ano.

## Para:

A regra de formação do número do protocolo é:

| 9           | 9      | 9      | 9   | 9   | 9                         | 9                         | 9                         | 9                         | 9                         | 9                         | 9                         | 9                         | 9                         | 9                         |
|-------------|--------|--------|-----|-----|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|
| Tipo de     | código | código | ano | ano | seqüencial de 10 posições | seqüencial de 10 posições | seqüencial de 10 posições | seqüencial de 10 posições | seqüencial de 10 posições | seqüencial de 10 posições | seqüencial de 10 posições | seqüencial de 10 posições | seqüencial de 10 posições | seqüencial de 10 posições |
| Autorizador | da UF  |        |     |     |                           |                           |                           |                           |                           |                           |                           |                           |                           |                           |

- 1 posição com o Tipo de Autorizador (1=SEFAZ normal, 2= Contingência SCAN RFB, 3=SEFAZ VIRTUAL-RS, 4=SEFAZ VIRTUAL-RFB);
- 2 posições para o código da UF do IBGE;
- 2 posições para ano;
- 10 posições para o seqüencial no ano.

![Image](assets/image_000014_fe6be84161521e88755b2fcf6266ac33af92377ba5aa975f460bc794e3ba9dba.png)

## Nota Fiscal Eletrônica

## 4.16  Alteração de Texto (página 79)

## Alterado de:

Os pedidos de inutilização de numeração de NF-e serão compartilhados somente com a Receita Federal.

## Para:

Os pedidos de inutilização de numeração de NF-e serão compartilhados somente com a Receita Federal.

Nota: No caso da SEFAZ VIRTUAL, o arquivo digital representando a operação realizada deverá ser distribuído também para a SEFAZ de circunscrição do contribuinte.

## 4.17  Alteração de Texto (página 80)

## Alterado de:

Nota : O Número do Protocolo é composto por: 1 posição (1 - Secretaria de Fazenda Estadual, 2 - Receita Federal) + 2 posições para código da UF no IBGE + 2 posições ano + 10 seqüencial no ano.

## Para:

Nota:

A composição do Número do Protocolo está descrita no item 5.6.

## 4.18  Alteração de Texto (página 138)

## Alterado de:

## São Paulo:

## Ambiente de homologação:

- NfeRecepcao
- https://homologacao.nfe.fazenda.sp.gov.br/nfeWEB/services/NfeRecepcaoSoap
- ·
- NfeRetRecepcao
- https://homologacao.nfe.fazenda.sp.gov.br/nfeWEB/services/NfeRetRecepcaoSoap
- NfeCancelamento

https://homologacao.nfe.fazenda.sp.gov.br/nfeWEB/services/NfeCancelamentoSoap

- NfeInutilizacao https://homologacao.nfe.fazenda.sp.gov.br/nfeWEB/services/NfeInutilizacaoSoap

-

-

-

-

![Image](assets/image_000015_fe6be84161521e88755b2fcf6266ac33af92377ba5aa975f460bc794e3ba9dba.png)

## Nota Fiscal Eletrônica

- NfeConsultaNF

https://homologacao.nfe.fazenda.sp.gov.br/nfeWEB/services/NfeConsultaSoap

- NfeStatusServico
- https://homologacao.nfe.fazenda.sp.gov.br/nfeWEB/services/NfeStatusServicoSoap

## Ambiente de produção:

- NfeRecepcao - https://nfe.fazenda.sp.gov.br/nfeWEB/services/NfeRecepcaoSoap
- ·
- NfeRetRecepcao https://nfe.fazenda.sp.gov.br/nfeWEB/services/NfeRetRecepcaoSoap
- NfeCancelamento https://nfe.fazenda.sp.gov.br/nfeWEB/services/NfeCancelamentoSoap
- NfeInutilizacao - https://nfe.fazenda.sp.gov.br/nfeWEB/services/NfeInutilizacaoSoap
- NfeConsultaNF  - https://nfe.fazenda.sp.gov.br/nfeWEB/services/NfeConsultaSoap
- NfeStatusServico https://nfe.fazenda.sp.gov.br/nfeWEB/services/NfeStatusServicoSoap

-

-

-

-

-

A documentação do WSDL pode ser obtida na internet acessando o endereço do Web Service desejado.

Exemplificando, para obter o WSDL de cada um dos Web Service acione o navegador Web (Internet Explorer, por exemplo) e digite o endereço desejado seguido do literal '?WSDL'.

## Para:

## São Paulo:

## Ambiente de homologação:

| •   | NfeRecepcao https://homologacao.nfe.fazenda.sp.gov.br/nfeWEB/services/NfeRecepcao.asmx           | -   |
|-----|--------------------------------------------------------------------------------------------------|-----|
| •   | NfeRetRecepcao https://homologacao.nfe.fazenda.sp.gov.br/nfeWEB/services/NfeRetRecepcao.asmx     | -   |
| •   | NfeCancelamento https://homologacao.nfe.fazenda.sp.gov.br/nfeWEB/services/NfeCancelamento.asmx   | -   |
| •   | NfeInutilizacao https://homologacao.nfe.fazenda.sp.gov.br/nfeWEB/services/NfeInutilizacao.asmx   | -   |
| •   | NfeConsultaNF https://homologacao.nfe.fazenda.sp.gov.br/nfeWEB/services/NfeConsulta.asmx         | -   |
| •   | NfeStatusServico https://homologacao.nfe.fazenda.sp.gov.br/nfeWEB/services/NfeStatusServico.asmx | -   |

## Ambiente de produção:

- NfeRecepcao - https://nfe.fazenda.sp.gov.br/nfeWEB/services/NfeRecepcao.asmx

-

-

-

-

-

-

![Image](assets/image_000016_a939ab80abed98b8b1877888aa76924d74ad1accfd31c3e19d49a06ff93ea213.png)

|                                                                                                                                                                                                                                                                                                                                                                                                                                             | • NfeRetRecepcao                                                                                                                                                                                                                                                                                                                                                                                                                            | -                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| https://nfe.fazenda.sp.gov.br/nfeWEB/services/NfeRetRecepcao.asmx • NfeCancelamento - https://nfe.fazenda.sp.gov.br/nfeWEB/services/NfeCancelamento.asmx • NfeInutilizacao - https://nfe.fazenda.sp.gov.br/nfeWEB/services/NfeInutilizacao.asmx • NfeConsultaNF - https://nfe.fazenda.sp.gov.br/nfeWEB/services/NfeConsulta.asmx • NfeStatusServico - https://nfe.fazenda.sp.gov.br/nfeWEB/services/NfeStatusServico.asmx SEFAZ VIRTUAL RS: | https://nfe.fazenda.sp.gov.br/nfeWEB/services/NfeRetRecepcao.asmx • NfeCancelamento - https://nfe.fazenda.sp.gov.br/nfeWEB/services/NfeCancelamento.asmx • NfeInutilizacao - https://nfe.fazenda.sp.gov.br/nfeWEB/services/NfeInutilizacao.asmx • NfeConsultaNF - https://nfe.fazenda.sp.gov.br/nfeWEB/services/NfeConsulta.asmx • NfeStatusServico - https://nfe.fazenda.sp.gov.br/nfeWEB/services/NfeStatusServico.asmx SEFAZ VIRTUAL RS: | https://nfe.fazenda.sp.gov.br/nfeWEB/services/NfeRetRecepcao.asmx • NfeCancelamento - https://nfe.fazenda.sp.gov.br/nfeWEB/services/NfeCancelamento.asmx • NfeInutilizacao - https://nfe.fazenda.sp.gov.br/nfeWEB/services/NfeInutilizacao.asmx • NfeConsultaNF - https://nfe.fazenda.sp.gov.br/nfeWEB/services/NfeConsulta.asmx • NfeStatusServico - https://nfe.fazenda.sp.gov.br/nfeWEB/services/NfeStatusServico.asmx SEFAZ VIRTUAL RS: |
| Ambiente •                                                                                                                                                                                                                                                                                                                                                                                                                                  | de homologação: NfeRecepcao                                                                                                                                                                                                                                                                                                                                                                                                                 | -                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             | https://homologacao.nfe.sefazvirtual.rs.gov.br/ws/nferecepcao/NfeRecepcao.asmx NfeRetRecepcao                                                                                                                                                                                                                                                                                                                                               | -                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| •                                                                                                                                                                                                                                                                                                                                                                                                                                           | https://homologacao.nfe.sefazvirtual.rs.gov.br/ws/nferetrecepcao/NfeRetRecepcao.as                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| •                                                                                                                                                                                                                                                                                                                                                                                                                                           | mx NfeCancelamento                                                                                                                                                                                                                                                                                                                                                                                                                          | -                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| • NfeInutilizacao                                                                                                                                                                                                                                                                                                                                                                                                                           | https://homologacao.nfe.sefazvirtual.rs.gov.br/ws/nfeinutilizacao/NfeInutilizacao.asm x                                                                                                                                                                                                                                                                                                                                                     | -                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| •                                                                                                                                                                                                                                                                                                                                                                                                                                           | NfeConsultaNF                                                                                                                                                                                                                                                                                                                                                                                                                               | -                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             | https://homologacao.nfe.sefazvirtual.rs.gov.br/ws/nfeconsulta/NfeConsulta.asmx                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| •                                                                                                                                                                                                                                                                                                                                                                                                                                           | NfeStatusServico https://homologacao.nfe.sefazvirtual.rs.gov.br/ws/nfestatusservico/NfeStatusServico.a                                                                                                                                                                                                                                                                                                                                      | -                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             | smx Ambiente de produção:                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| • •                                                                                                                                                                                                                                                                                                                                                                                                                                         | NfeRecepcao - https://nfe.sefazvirtual.rs.gov.br/ws/nferecepcao/NfeRecepcao.asmx NfeRetRecepcao https://nfe.sefazvirtual.rs.gov.br/ws/nferetrecepcao/NfeRetRecepcao.asmx NfeCancelamento-                                                                                                                                                                                                                                                   | -                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| • •                                                                                                                                                                                                                                                                                                                                                                                                                                         | https://nfe.sefazvirtual.rs.gov.br/ws/nfecancelamento/NfeCancelamento.asmx NfeInutilizacao https://nfe.sefazvirtual.rs.gov.br/ws/nfeinutilizacao/NfeInutilizacao.asmx NfeConsultaNF - https://nfe.sefazvirtual.rs.gov.br/ws/nfeconsulta/NfeConsulta.asmx                                                                                                                                                                                    | -                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| •                                                                                                                                                                                                                                                                                                                                                                                                                                           | NfeStatusServico - https://nfe.sefazvirtual.rs.gov.br/ws/nfestatusservico/NfeStatusServico.asmx                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| •                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             | A relação atualizada das UF e os respectivos endereços dos Web Services                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Nota:                                                                                                                                                                                                                                                                                                                                                                                                                                       | oferecidos estão publicados no Portal Nacional da NF-e.                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## Obtenção do WSDL:

-

-

-

-

-

-

-

-

-

-

-

![Image](assets/image_000017_fe6be84161521e88755b2fcf6266ac33af92377ba5aa975f460bc794e3ba9dba.png)

A documentação do WSDL pode ser obtida na internet acessando o endereço do Web Service desejado.

Exemplificando,  para  obter  o  WSDL  de  cada  um  dos  Web  Service  acione  o navegador  Web  (Internet  Explorer,  por  exemplo)  e  digite  o  endereço  desejado seguido do literal '?WSDL' .

## 5.  Quadro Indicador de ENTRADA/SAÍDA do Modelo de DANFE (página 130)

Os  modelos  de  DANFE  dos  Anexos  II  e  III  foram  alterados  para  que  o  valor  do indicador de ENTRADA/SAÍDA do DANFE tenha os mesmos valores informados na NF-e.

## Anexo II - Modelo de DANFE - retrato

![Image](assets/image_000018_b8de18a3a04d72b36c170af1e03f52a58a9c02be944d81702462c58596e63cd2.png)

Divulga Manual de Integração do Contribuinte - versão 2.04

![Image](assets/image_000019_3f3dd97128c79fccc130e27d9780db80976fe599b8015030829bf8ec58466787.png)

NF-e

DATA CE RECEBIMENTO

CENTIFICAGAO EASSIFATUFA DO RECEBEDOR

N.000.000.000

SERIE 000

## DANFE

CCNTRCLE DO FISCO

Identificacaodoemitente

- [x] Documento Auxiliar da Nota Fiscal Eletronica

Logotipo

(nome ou razao social, endereco,bairro,municipio， UF,telefone/faxe CEP)

- [ ] 0 - ENTRADA 1- SAIDA

N. 000.000.000-FL1/n SERIE000

NATUREZA DA CPERACAO

NSC.ESTADUALDOSLBST.TAIEUTAAIO

CNPJ

CHAVE DEA

00.00.00.00.00.000.000/0000-00-000.000.000-000-000.000.000-0

DESTINATA RIO/REMETENTE

NOME/RAZAO SOCIAL

CNPUCPF

DATA DA EMISSAO

ENDEREQO

BAIRRODISTRITO

CEP

DATA DA ENTRADA

MUNICIPIO

FONE/FAX

LF

HORA DE SAIDA

FATURA

CALCULO DOIMPOSTO

VALOR DO ICMS

BASE CECALCULO DOICMSSUBSTITUIKAO

VALOR DO ICMS SUBSTITUICAO

VALCA TOTAL DOS PRODUTOS

VALCR DO FRETE

VALCR DO SEGLRO

DESCONTO

CUTRAS DESPESAS ACESSORAS

VALOR DO IFI

VALOR TOTAL DA NOTA

TRANSPORTADORVOLUMESTRANSPORTADOS

RAZAO SOCAL

- [ ] FRETE POR CONTA 1 - EWTENTE 2-DESTNATARO

CODIGO ANTT

PLACA DO VEICLLO

UF

CNPJCFF

ENDEREQO

MUNICIPIO

UF

QUANTIDADE

ESFECE

MARCA

NUMERACAO

FESO BRUTO

FESO UCUIDO

## DADOSDOPRODUTO/SERVICOS

COD.FACO,

DESCRICAO CO PRCOUTO/ SERVICCS

NCWSH

CST

CFCP

UNDADE

CUA.NTIDADE

V, UNITARIO

V. TOTAL

BC ICMS

V. ICMS

V.IFI

ALIO.

ALIO.

CMS

IP1

CALCULODOISSQN

NSCRICAO MUNICIPAL

VALOR TOTALDCS SERVICCG

BASE DE CALCULO DO ISSCN

VALOR DO ISSCN

DADOS ADICIONAIS

NFCFMACCES COMPLEMENTAFES

![Image](assets/image_000020_8ff22ba449e62e82b17ddbe4fbc654e3937e39e42df0b5fd5ff23f6bf60532f8.png)

DADOSDOPRODUTO/SERVICOS

| COD.FRCO,   | CESCAICAO DO PRCOUTO/ SERVICCS   | NCM'SH   | CFCP   | UNDACE   | CUANTIDADE   | V,UNITARIO   | V. TOTAL   | BC ICMS   | V. ICMS   | ALIO. ALIO. SNOI IPI   |
|-------------|----------------------------------|----------|--------|----------|--------------|--------------|------------|-----------|-----------|------------------------|

![Image](assets/image_000021_96799c06a94cb1616a320a59195080f39d940fa87c756abd4206d8e17d1ea9f3.png)

## DANFE

CCNTACLE DO FISCO

Identificacaodoemitente

Documento Auxiliar da Nota Fiscal Eletronica

Logotipo

(nome ourazao social, endereco,bairro,municipio, UF,telefone/faxeCEP)

- [ ] 0- ENTRADA 1- SAIDA

N.000.000.000-FLn/n

SERIE000

NATUREZA DA CPERACAO

NSC.ESTADUALDO SLBST.TRIEUTARIO

CNPJ

00.00.00.00.00.000.000/0000-00-000.000.000-000-000.000.000-0

DADOSDOPRODUTO/SERVICOS

COD.FRCC,

DESCRICAO DO PRCOUTO/ SERVICOS

NCWSH

CFCP

UNIDACE

CUA.NTIDADE

V, UNITARIO

V. TOTAL

BC ICMS

V. ICMS

V.IFI

ALIO. ALIO.

ICMS

IPI

![Image](assets/image_000022_d7f4dbc126ac83213c2aa2da8123efaa890db3839def8b92bd29a7e6b0e1347c.png)

![Image](assets/image_000023_8da0e9c2a6240c3ff5c848e40e7111408da9306c271e168101efe6838fe09cfc.png)

## Anexo III - Modelo de DANFE - paisagem

RECEBEMOS

DANFE

CONTROLE DO FISCO

DE

Identificacaodo emitente

Documento Auxiliar da Nota Fiscal Eletronica 0- ENTRADA 1- SAIDA N000.000.000-FL1/n

Logotipo

(nome ou razao social, enderego, bairro, municipio UF, telefone/fax e CEP)

DE(RAZAO

IEHT

SERIE 000

SOCIAL

NAT.DA OPERAGO

D

INSCRICAO ESTADUAL

NSC. EST. DO SUEST. TREBUTAAIO.

CNPJ

WWW.NFE.FAZENDA. GCV.BR 00.0000.00.000.000/0000-00-00-000-000.000.000-000.000.000-0

DO

四

DESTINATARIO/REMETENTE

NOHERAZAO SOCIAL

CNPUCFF

DATA DAEMSSO

DO

TENTE)

AECEIE

ENDEREGO

BAIRAODGTRTO

CEP

DATADE SAICA/ENTRADA

OS

PRODUTOS

MUNCPIO

FONEPAE

INSCRIPAO ESTADUAL

HORA CE SACA

FATURA

CONSTANTESI

CALCULO DOIMPOSTO

SNOI 00 0100T0 30 35V

VALOA TOTAL DOG PROOUTOS

WALOACO FRETE

DESCONTO

CUTRASDESPESASACESSCRIAS

VALORDO IPI

VALOR TOTAL DA HOTA

TRANSPORTADORVOLUMESTRANSPORTADOS

NOTAS

RAZAO SOCAL

- [ ] 1-EMTN 2 -DGSTIAARIO

PRETE POR CONTA

COCIGC ANTT

UF

dO.FdND

ENCERECO

MUNICIPIO

UF

T

FISCALI

CUANTEACE

MARCA

N.MERA CAO

PESO BRUTO

PESO LiouDO

INDICADA

DADOS DO PRODUTO/ SERVIQOS

CCC.PROCUTO

DESCRICAO DOS PROOUTOS/ SERVIQOG

NCHSH

CST

LNICADE

QTO

OIYLINTA

V.TOTAL

BC DO ICM5

V.ICMS

V.1P

ALO.IOWS

ALQIR

AAOLADO

INSCRICAO MUNICIFAL

VALOR TOTAL DOS SERVIPOS

BASE DE CALCULO DO ISOON

VALOR DO ISSGN

DADOS ADICIONAIS

000.000.000

INPOAMAPOES COMPLENENTAAES

RESERAADO AO FISCO

NF-e

![Image](assets/image_000024_d9f98cf12b7309ef8ac611929b6b964bcd82660255fcc5c141b7e8c305e26ac5.png)

![Image](assets/image_000025_6ec8999c74cf6a76fc04f8c5577fdbcf25667fd45ea28c535a9f20657ae586af.png)

## Divulga Manual de Integração do Contribuinte - versão 2.04

![Image](assets/image_000026_5b74e4fe78071ee68d379babf2d82f323edb884f76f0d0cd83617e2542859230.png)

| INSCRIPAOESTADUAL           | INSCRIPAOESTADUAL           | INSC. EST. DO SLIE/ST.TRIEUTARIO.   | INSC. EST. DO SLIE/ST.TRIEUTARIO.   |                             |                             |                             |                             |                             |                             |                             |                             |                             |                             |                             |
|-----------------------------|-----------------------------|-------------------------------------|-------------------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|
| DADOS DO PRODUTO / SERVICOS | DADOS DO PRODUTO / SERVICOS | DADOS DO PRODUTO / SERVICOS         | DADOS DO PRODUTO / SERVICOS         | DADOS DO PRODUTO / SERVICOS | DADOS DO PRODUTO / SERVICOS | DADOS DO PRODUTO / SERVICOS | DADOS DO PRODUTO / SERVICOS | DADOS DO PRODUTO / SERVICOS | DADOS DO PRODUTO / SERVICOS | DADOS DO PRODUTO / SERVICOS | DADOS DO PRODUTO / SERVICOS | DADOS DO PRODUTO / SERVICOS | DADOS DO PRODUTO / SERVICOS | DADOS DO PRODUTO / SERVICOS |
| GO0PROOUTO                  | DESGRIG SERVICOS            | DESGRIG SERVICOS                    | NCMSH                               | OST                         | CPOP                        |                             | QTD                         | V.UNITARIO                  |                             | BG DOICMS                   |                             | AUGICMS                     | AUQIFI                      |                             |
|                             |                             |                                     |                                     |                             |                             | LNCADE                      |                             |                             | V.TOTAL                     | VJOMS                       | V.IP1                       |                             |                             |                             |

![Image](assets/image_000027_a8fbafb0b4e2977d1f6c6b810b6971a72cb8ba6ee4aee247aa62157f8e7b9579.png)

## Divulga Manual de Integração do Contribuinte - versão 2.04

![Image](assets/image_000028_360a9dc78dc384505b6098d1b33f94ef19f9bebc48fe54bbdc4a881c4c00f71b.png)

![Image](assets/image_000029_ad26cc5286de90e8f937dbe735aa4b042e009b1a847f39bc348cedb1609f0e44.png)

## 6.  Alterações diversas para correção ou aperfeiçoamento de texto

- Versões de leiautes do PL\_005a (pg. 3)

```
. linha 'NFe': trocar para 'Lei au te' . linha 'envNFe': trocar para 'env i NFe' . linha 'retEnvNFe' : trocar para 'retEnv i NFe' -Item 2 (pg. 8): trocar para: '... foi atualizado pelo s Ajustes SINIEF ...' -Item 2.3 (pg. 9): . trocar para: '... em papel comum, geralmente em única via, ...' . trocar para '... através do sítio da Secretaria da Fazenda Estadual autorizadora ou Receita Federal.' . trocar de: 'Apesar disto, no primeiro momento de implantação do projeto, o contribuinte .destinatário , não ...' para:  'O contribuinte destinatário não emissor de NF-e poderá ...' -Item 3.2.1-b (pg. 11): . trocar o prefixo de namespace de 'NFe' para ' nfe ', melhorando a documentação (3 ocorrências); . trocar de: 'exemplo para o XML da NF-e e com prefixo ...' para:  'exemplo para o XML da NF-e com prefixo ...' -Item 3.2.1-c (pg. 12): . trocar para: '... caso específico do lote de envio da ...' ' E xemplo 1: campo R01 ...' ' E xemplo 2: Sub g rupo de Informações de .... -Item 3.2.1-d (pg. 13): trocar para '... pela Secretaria da Fazenda Estadual, antes de seu envio.' -Item 3.2.2 (pg. 13): trocar para '... no Portal da Secretaria de Fazenda Estadual ...'
```

![Image](assets/image_000030_ad26cc5286de90e8f937dbe735aa4b042e009b1a847f39bc348cedb1609f0e44.png)

- -Item 3.2.2 (pg. 13): Incluir o texto que segue, antes da linha de 'Segue abaixo um exemplo ...' ' Os  parâmetros  de  chamada  para  os  diferentes  Web  Services  do  Projeto  NF-e  são  do  tipo  'string',  com  os  nomes  de:

## 'nfeCabecMsg' e 'nfeDadosMsg'.

- -Item 3.2.3-b (pg. 14): trocar para: '...entre o servidor do contribuinte e o Portal da ...' -Item 3.2.4 (pg. 15): Schema xmldsig-core-schema . linha XS06, coluna Descrição : trocar para 'Atributo Algorithm de SignatureMethod ' . linha XS07, coluna Descrição: trocar para 'Grupo de Reference ' . linha XS17, coluna Ocor.: trocar para ' 1-1 ' -Item 3.2.4 (pg. 15): trocar para '... para cada NF-e , conforme leiaute ...' -Item 3.4.3 (pg. 22): trocar para '... das mensagens dos Web Services ...' trocar para 'env i NFe\_v1.03.xsd -Item 3.5.1 (pg. 23): tabela do Pacote de Liberação: . trocar para 'tiposBasicoNFe' (2 ocorrências) -Item 4 (pg. 25): eliminar o texto ' a Nota Fiscal Modelo 1/1A ou ' -Item 4.1 (pg. 26): trocar de: 'Transmissão de Lote de NF-e' para: ' Lote de NF-e ' trocar para 'Schema XML: env i NFe\_ ...' trocar para 'Schema XML: retEnv i NFe\_ ...' -Item 4.1.9-d (pg. 31, 32): .'
- . linha G03b, coluna Regra de Validação: trocar para: '... processo de emissão da NF-e pelo aplicativo do contribuinte (procEmi = 0) . linha G12, coluna Regra de Validação:

![Image](assets/image_000031_ad26cc5286de90e8f937dbe735aa4b042e009b1a847f39bc348cedb1609f0e44.png)

- . linha G14, coluna Regra de Validação: incluir o texto:

trocar para '... posterior à data de recebimento da NF-e na SEFAZ '

'O campo de IE ST somente tem sentido na operação interestadual e a validação da IE ST segue as regras de validação da IE da UF de destino.'

'Acesso BD NFE\_Inutilização (Chave: Ano, CNPJ, Modelo, Série, Número da NF-e)'

- . linha G29, coluna Regra de Validação: trocar para:
- -Item 4.2 (pg. 34):

. trocar de 'Consulta Processamento de Lote de NF-e' para: 'Consulta Resultado do Processamento do Lote'

- -Item 4.4.7-d (pg. 49):
- . linha I07, coluna Regra de Validação: trocar para: 'Acesso BD NFE\_Inutilização (Chave: Ano, CNPJ, Modelo, Série, Número da NF-e)'
- -
- Item 4.5.1 (pg. 51): . linha EP01, coluna Campo: trocar para 'con s SitNFe'
- -Item 4.5.8 (pg. 54): trocar para '... com os valores 100 ('Autorizado o Uso da NF-e'), 101 ('Cancelamento de NF-e homologado') ou 110 ('Uso Denegado').'
- -Item 4.6.8 (pg. 58): trocar para '... códigos de situação 107 ('Serviço em Operação'), 108 ('Serviço Paralisado Momentaneamente') e 109 ('Serviço Paralisado sem
- Previsão').
- -Item 5.1 (pg. 65): trocar para 'Web Se r vice existente.'
- -Item 9 (pg. 76): trocar para 'O ambi en te de homologação ...'
- -Item 12 (pg. 81): trocar para '... qualquer erro ou incons is tência ...'

![Image](assets/image_000032_ad26cc5286de90e8f937dbe735aa4b042e009b1a847f39bc348cedb1609f0e44.png)

```
-Item 12.1 (pg. 82): . linha O11b, coluna Descrição: trocar para 'Si tua ção do emissor:' -Item 12.2 (pg. 83): . linha M11b, coluna Descrição: trocar para 'Si tua ção do emissor:' - Anexo I - Leiaute da NF-e (pg. 86): . linha 4, coluna Campo: trocar para 'pk_n I tem' . linha 31a, coluna Observação: trocar para '... as informações do remetente ...' . linha 78, coluna Observação: trocar de 'contribuint o ' para 'contribuin te '  (2 ocorrências) . linha 101, coluna Observação: trocar para 'mercadorias/produto s ' . linha 162i, coluna Campo: trocar para ' IMCSComb ' . linha 278, coluna Ele: trocar para ' CG' . linha 280, coluna Ele: trocar para ' CG' . linha 294, coluna Ele: trocar para ' CG' . linha 299, coluna Ele: trocar para ' CG' . linha 304, coluna Ele: trocar para ' CG' . linha 306, coluna Ele: trocar para ' CG' . linha 355, coluna Observação: trocar para ' infralegais' . linha 367, coluna Tipo: trocar para ' N' . linha 368, coluna Tipo: trocar para ' N' . linha 369, coluna Tipo: trocar para ' N' . linha 370, coluna Tipo: trocar para ' N' . linha 371, coluna Tipo: trocar para ' N' . linha 372, coluna Tipo: trocar para ' N' . linha 382, coluna Tamanho: trocar para ' 1-15' . linha 388, coluna Descrição: trocar para 'Número do Lacre ' . linha 401g, coluna Observação: eliminar a observação atual . linha 401h, coluna Descr / Obs: trocar de 'I n dentificador' para 'Identificador' (2 ocorrências)
```

![Image](assets/image_000033_b466affc7c73971f5e87a1a69ff43d16c9248ab855c749ec85291c5aa2a80da6.png)

- Anexo IV (pg. 137) : documentar o endereço do Web Service de Consulta Cadastro
- Rio Grande do Sul  / Ambiente de homologação:
- CadConsultaCadastro  - https://sef.sefaz.rs.gov.br/ws/cadconsultacadastro/cadconsultacadastro.asmx
- Anexo VI (pg. 140) : trocar para 'Zona Franca de Man au s':

As dúvidas e sugestões devem ser encaminhadas através do Canal Fale Conosco da Secretaria da Fazenda de São Paulo (http://www.fazenda.sp.gov.br/email/default2.asp) referente à 'Portaria CAT 104/07'.
## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt-2007-008/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt-2007-008/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt-2007-008.md)
- [Proveniência resumida](../../../../sources/provenance/nt-2007-008.json)


## Documentos relacionados

- [nota-t-cnica-2007-004-publicada-em-15-09-2011](../nota-t-cnica-2007-004-publicada-em-15-09-2011/document.md)
- [nota-t-cnica-2007-007-publicada-em-30-11-2010](../nota-t-cnica-2007-007-publicada-em-30-11-2010/document.md)
- [nt-2007-001](../nt-2007-001/document.md)
- [nt-2007-002](../nt-2007-002/document.md)
- [nt-2007-003](../nt-2007-003/document.md)
- [nt-2007-004](../nt-2007-004/document.md)
- [nt-2007-007](../nt-2007-007/document.md)
- [nt-2007-009](../nt-2007-009/document.md)
