---
title: "Sistema Nota Fiscal Eletrônica"
slug: "anexo-iv-manual-de-conting-ncia-nfc-e"
category: "manual"
source_family: "portal_nacional_nfe"
original_sha256: "0b5ae1e88ae60b57d4f1d752316289ff55f7e10c7e1d405905325e9de2666b0e"
converted_at_utc: "2026-06-25T16:53:10.362154+00:00"
status: "published"
type: "manual"
---

## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfce/manuais/anexo-iv-manual-de-conting-ncia-nfc-e/source.json)
- [Dados normalizados](../../../../normalized/nfce/manuais/anexo-iv-manual-de-conting-ncia-nfc-e/normalized.json)
- [Changelog](../../../../changelog/nfce/manuais/anexo-iv-manual-de-conting-ncia-nfc-e.md)
- [Proveniência resumida](../../../../sources/provenance/anexo-iv-manual-de-conting-ncia-nfc-e.json)

## Sistema Nota Fiscal Eletrônica

Manual de Orientação do Contribuinte

Anexo IV -Padrões Técnicos de Contingência Off-line NFC-e

Versão 7.00 -Novembro de 2020

![Image](assets/image_000001_f840a3fcbd458b9c45f36ebad777ed19e8c09d1a8224472a68223a04ea4e0f78.png)

![Image](assets/image_000002_313aa0a7b363f616e5a008f04134b9fb09b677fb62ae18d4c4c793e887b78be8.png)

## Nota Fiscal Eletrônica

## Sumário

| Controle de Versões ..................................................................................................................   | Controle de Versões ..................................................................................................................   |   3 |
|------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-----|
| Histórico de Alterações / Cronograma.......................................................................................              | Histórico de Alterações / Cronograma.......................................................................................              |   4 |
| 1.                                                                                                                                       | Introdução............................................................................................................................   |   5 |
| 2.                                                                                                                                       | Conceito e Modelo Operacional da Contingência Off-line para NFC-e .............................                                          |   5 |
| 3.                                                                                                                                       | Detalhes Técnicos NFC-e Emitida em Contingência .........................................................                                |   6 |
| 4.                                                                                                                                       | Modelo Operacional Contingência Off-line NFC-e .............................................................                             |   8 |
| 5.                                                                                                                                       | Exemplo Prático.................................................................................................................         |  11 |

![Image](assets/image_000003_532619d6cc038d15c3f7c9ebc70696a55c2c4975651d4e44b049e8883b164944.png)

## Controle de Versões

|   Versão | Publicação    | Descrição                                                                                                                                                                                                |
|----------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     7.00 | Novembro/2020 | Criação deste manual como documento anexo do MOC 7.00. Corresponde ao Manual de Padrões Técnicos Contingência Off-line da NFC-e, que trata da especificação técnica da emissão em Contingência da NFC-e. |

![Image](assets/image_000004_72e01bcbe9c4a8ceb2d6f1a5af20a30c122d852de5791c31a808cc561e1cab30.png)

## Histórico de Alterações / Cronograma

|   Versão | Histórico de atualizações                                                                           | Implantação Homologação   | Implantação Produção   |
|----------|-----------------------------------------------------------------------------------------------------|---------------------------|------------------------|
|     7.00 | Conversão do Manual de Padrões Técnicos Contingência Off-line da NFC-e para este manual específico. |                           |                        |

![Image](assets/image_000005_72e01bcbe9c4a8ceb2d6f1a5af20a30c122d852de5791c31a808cc561e1cab30.png)

## 1.  Introdução

Este documento é parte integrante do Manual de Orientação  do Contribuinte  (MOC) e por  objetivo a definição do leiaute da NF-e, modelos 55 e 65.

O Manual de Orientação do Contribuinte 7.0 é composto pelos seguintes documentos:

- [MOC - Visão Geral](../../../nfe/manuais/manual-de-orienta-o-ao-contribuinte-moc-vers-o-7-0-nf-e-e-nfc-e/document.md)
- [MOC - Anexo I - Leiaute NF-e/NFC-e e Regras de Validação](../../../nfe/manuais/anexo-i-leiaute-e-regra-de-valida-o-nf-e-e-nfc-e/document.md)
- MOC - Anexo II - Manual de Especificações  Técnicas do DANFE e Código de Barras
- [MOC - Anexo III - Manual de Contingência NF-e](../../../nfe/manuais/anexo-iii-manual-de-conting-ncia-nf-e/document.md)
- [MOC - Anexo IV - Manual de Contingência NFC-e](../../../nfe/manuais/anexo-iii-manual-de-conting-ncia-nf-e/document.md)

As informações do DANFE NFC-e estão publicadas no Manual de Especificações Técnicas do DANFE NFC-e e QR Code, disponível no Portal Nacional da NFC-e

Ao longo deste documento o acrônimo NF-e é utilizado para todas as situações que se aplicam indistintamente  a ambos os modelos de NF-e (55 e 65). Sempre que é necessário  identificar  um dos dois modelos em particular, a diferenciação é feita pela expressão respectiva: NF-e modelo 55 ou NFC-e modelo 65.

## 2.  Conceito e Modelo Operacional da Contingência Off-line para NFC-e

O modelo operacional atual da NFC-e prevê a utilização de 'Contingência Off-line NFC-e'.

Nesta  modalidade,  o  contribuinte  que  estiver  com  problemas  técnicos  para  autorização  da  NFC-e poderá emiti-la em contingência  off-line, imprimir o DANFE NFC-e e depois de superado o problema técnico,  transmitir  o  arquivo  XML  da  NFC-e  para  autorização.  O  prazo  estabelecido  pelo  Fisco, atualmente, é o final do primeiro dia útil subsequente contado a partir de sua emissão.

![Image](assets/image_000006_c092402602b34b0aad7a7d27168d5c87a378bc80518af5a62af168afd0d3fb77.png)

![Image](assets/image_000007_abe570ad3bc3d9c6984dd1c815df0be0889b666813f78909b32f5642fff64c35.png)

SNFeSNFCe MOC 7.0 - Anexo  IV, Padrões Técnicos de Contingência  O ff-line NFC-e A  possibilidade  de  uso  da  contingência  off-line  para  NFC-e  é  um  decisão  exclusiva  da  Unidade Federada, que poderá vir a não autorizar esta modalidade de contingência para todos ou determinados contribuintes  emissores  de NFC-e.  Para  tanto,  foi definida  regra  de validação  específica  no leiaute possibilitando a implementação  desta decisão pela UF.

![Image](assets/image_000008_a6e4336b4e9a0da8d684646103e5aa83a47738891c90cd3f7d5b0030b7be2af2.png)

A legislação nacional da NFC-e prevê a possibilidade, inclusive, que, a critério da Unidade Federada, sejam adotadas outras formas de contingência, ou utilização concomitante, como a emissão de cupom fiscal em papel por ECF, ou a geração de Cupom Fiscal Eletrônico por SAT Fiscal.

A contingência off-line é de uso exclusivo como alternativa de contingência de emissão de NFC-e, não sendo aceita  esta  modalidade  de  contingência,  em  nenhuma  hipótese,  para  a  NF-e.  Para  garantia desta premissa foi também inserida regra de validação específica  para garantir o cumprimento  desta regra.

A decisão pela entrada em contingência,  bem como a escolha da alternativa  de contingência (dentre as aceitas pela UF) é exclusiva do contribuinte,  devendo ser utilizada nas situações em que ocorram problemas  técnicos de comunicação  ou processamento  de informações  que impeçam a autorização da NFC-e em tempo real. Não existe exigência de obtenção, pelo contribuinte,  de autorização  prévia do Fisco para  entrada em contingência,  tampouco  de efetuar  qualquer  termo de início  e término  de contingência no livro modelo 6 - RUDFTO.

Todavia, alertamos que as NFC-e devem ser autorizadas, preferencialmente,  em tempo real, antes da ocorrência  do fato gerador, e que as alternativas  de contingência  somente  devem ser acionadas  em situações extremas, que interfiram de forma significativa na atividade operacional do estabelecimento.

Assim, a emissão de NFC-e em contingência off-line deve ser tratada como exceção , sendo que a regra deve ser a emissão com autorização em tempo real.

O  Fisco  poderá  solicitar  esclarecimentos,  e  até  mesmo  restringir  ao  contribuinte  a  utilização  da modalidade  de  contingência  off-line,  caso  seja  identificado que  o  emissor  da  NFC-e  utiliza  a contingência  em demasia e sem justificativa  aceitável, quando  comparado  a outros contribuintes  em situação similar.

É  importante  ressaltar  ainda  que  a  utilização  de  contingência  off-line  deve  se  restringir  às situações de efetiva impossibilidade de autorização da NFC-e em tempo real , haja vista que pode vir a representar custos e riscos adicionais ao contribuinte, em especial, pelos seguintes aspectos:

- As NFC-e emitidas em contingência off-line deverão ser posteriormente encaminhadas  para autorização, podendo virem a ser rejeitadas, gerando possíveis retrabalhos e problemas junto ao cliente, uma vez que a operação comercial já ocorreu;
- As NFC-e emitidas em contingência off-line estarão disponíveis para consulta pública pelos consumidores no site da SEFAZ ou via consulta QR Code apenas em momento posterior, quando forem autorizadas, havendo risco de reclamações ou denúncias de consumidores por não localizarem a sua NFC-e na consulta realizada imediatamente após a venda;
- Na  utilização de  contingência off-line, o contribuinte assume o  risco de  perda  da  informação das NFC-e emitidas em contingência, até que as mesmas constem da base de dados do Fisco. Na autorização online da NFC-e a informação já está segura na base de dados do Fisco;

O nível de serviço acordado para a NFC-e pelos sistemas dos Estados Autorizadores deve ser inferior a 30 (trinta) segundos, em 85% do tempo.

## 3.  Detalhes Técnicos NFC-e Emitida em Contingência

Ao emitir uma NFC-e em contingência, a primeira decisão é sobre a forma de emissão em contingência dentre as disponíveis para NFC-e (de acordo as alternativas aceitas pela Unidade Federada).

No arquivo eletrônico  XML da NFC-e deverá ser indicada  a forma de emissão em contingência  pelo preenchimento do campo tpEmis (B22) com um dos seguintes conteúdos:

- 1-Emissão normal (não em contingência);
- 4 - Contingência EPEC (Evento Prévio da Emissão em Contingência);
- 9 - Contingência off-line da NFC-e.

Figura 2 - Evento de Emissão em Contingência,  Visão Geral

SNFeSNFCe

![Image](assets/image_000009_abe570ad3bc3d9c6984dd1c815df0be0889b666813f78909b32f5642fff64c35.png)

![Image](assets/image_000010_d9147c61abed28c4ca86aa13b99b94e6e031c9ab7fbb4d3091e8b10c2ad7f0cc.png)

Na  escolha  de  contingência  off-line  da  NFC-e  (tpEmis  =  9)  não  é  necessária  a  adoção  de  série específica  ou  a  utilização  de  papel  especial.Todavia,  deve  ser  observado  o  prazo  de  envio  para autorização da NFC-eaté o final do primeiro dia útil subsequente  contado a partir de sua emissão em contingência..

Qualquer que seja a alternativa de contingência adotada, a informação de operação em contingência deve ser impressa no DANFE NFC-e.

Figura 3 - DANFE de uma NFC-e Emitida em Contingência  Off-Line

![Image](assets/image_000011_64140b77242ac3ac3662615c45ab3d8412506238fda5409d87d2f65c3f25d8cf.png)

Além disso, o QR Code impresso no DANFE daNFC-e emitida em contingência conterá a informação da data e hora de emissão do documento fiscal eletrônico. Isto possibilita que na consulta via QR Code, pelo consumidor, a SEFAZ retorne a informação de que se trata de emissão em contingência e o prazo máximo para o documento fiscal eletrônico constar da base de dados do Fisco.

![Image](assets/image_000012_abe570ad3bc3d9c6984dd1c815df0be0889b666813f78909b32f5642fff64c35.png)

SNFeSNFCe

Nos casos de contingências  4 e 9 o contribuinte  deverá preencher,  obrigatoriamente,  os campos de Data e Hora da entrada em contingência  (dhCont B28) e de Justificativa da entrada em contingência (xJust B29) que, todavia, não serão impressos no DANFE NFC-e.

Outro ponto importante é a recomendação de que se avance um número na sequência da numeração quando  da  entrada  em  contingência  a  fim  de  evitar  que  a  NFC-e  emitida  em  contingência  seja posteriormente rejeitada por duplicidade.

Também  cabe  alertar  que,  superado  o  problema  técnico,  na  transmissão  da  NFC-e  emitida  em contingência, deve-se manter a mesma chave de acesso ,  inclusive com a manutenção  do mesmo código numérico original (campo cNF B03).

Codigo

Descricao

003277

PRODUTO

085273

PRODUTO

807194

PRODUTO

046281

PRODUTO

TributosTotais Incidentes(LeiFederal12.741/2012):RS65.62

![Image](assets/image_000013_298e6f73125abdc2f965da3a9966a5df99c9d3b58c6e8f22b2e05c5f63ed0c72.png)

## 4.  Modelo Operacional Contingência Off-line NFC-e

A  contingência  off-line  para  a  NFC-e  foi  pensada  como  uma  forma  de  garantir  ao  contribuinte  a minimização  de risco de impacto operacional pela implantação e utilização  da NFC-e no varejo, sem acarretar a perda de controle pelo Fisco.

A operação comercial no varejo, como regra, envolve uma situação crítica em que o consumidor está presente no estabelecimento,  escolhe a mercadoria e se dirige ao caixa para pagamento e retirada do produto. Dessa forma, a autorização prévia da NFC-e na frente de caixa exige um tempo de resposta adequado,  da  ordem  de  poucos  segundos,  de  forma  a  evitar  reclamações  dos  consumidores  pela demora no atendimento.

Assim, em uma situação de problemas técnicos, seja nos servidores ou rede de comunicação interna do contribuinte, seja no sistema de autorização da SEFAZ, ou ainda no meio de comunicação Internet, em que o tempo de autorização não se mostre adequado, ou não se consiga a autorização, não podem ocorrer reflexos significativos na operação de frente de caixa.

![Image](assets/image_000014_f6883a60619d6998e5c9d51533dc081548cb478895d30de2677fd61a7ff1eda4.png)

Nessas  situações  é  indicada  a  adoção  da  contingência  off-line,  em  que  as  NFC-e  são  geradas, assinadas  e  os  respectivos  DANFE  NFC-e  são  impressos  sem  a  autorização  prévia  da  SEFAZ. Posteriormente,  superado o problema  técnico, até o final do primeiro  dia útil seguinte  à emissão,  as NFC-e emitidas em contingência deverão ser transmitidas para obtenção da autorização de uso.

A  seguir  detalhamos  o  preenchimento  dos  campos  específicos  da  NFC-e  no  caso  de  emissão  em contingência off-line:

- Mod = 65 (NFC-e);
- dhCont = data e hora de entrada em contingência;
- xJust  = preencher com a justificativa da entrada em contingência;
- idDest = 1 (operação interna);
- tpEmis = 9 (contingência off-line);
- finfe = 1 (finalidade de emissão normal);
- indFinal =1 (indicador de operação com consumidor final);
- indPres =1 (indicador de presença do consumidor no estabelecimento);

No caso de emissão em contingência deverá constar obrigatoriamente no DANFE NFC-e a mensagem 'EMITIDA EM CONTINGÊNCIA'.

O DANFE NFC-e tem por característica não trazer impressas as informações detalhadas dos itens de mercadorias,  que serão apresentadas  no documento  Detalhe da Venda ou no resultado  da consulta pública da NFC-e no portal da Secretaria de Fazenda.

No caso de emissão em contingência off-line ,  é  obrigatória  a impressão  do Detalhe  da Venda  e do DANFE NFC-e, sendo que, nesta hipótese, deverá ser impressa uma segunda via do DANFE NFC-e que deverá  permanecer  a disposição  do Fisco no estabelecimento  até que tenha  sido transmitida  e autorizada a respectiva NFC-e emitida em contingência. Esta obrigação poderá, a critério da Unidade Federada, ser dispensada.

Esta segunda via deverá estar identificada como 'Via do Estabelecimento' conforme modelo constante da figura a seguir. Alternativamente à impressão da segunda via do DANFE NFC-e, quando de emissão em contingência,  o contribuinte  poderá  optar pela  guarda eletrônica,  em local seguro,  do respectivo arquivo  XML  da  NFC-e.  Neste  caso,  o  contribuinte  deverá  possibilitar  a  impressão  do  respectivo DANFE NFC-e para apresentação ao fisco quando solicitado.

## Figura 5 - Contingência Off-Line, Via do Estabelecimento

| Codigo              | Descricao           | Qtde UN   | VI Unit      | VI Total   |
|---------------------|---------------------|-----------|--------------|------------|
| 003277              | PRODUTO             | 1CX       | 27,64        | 27,64      |
| 085273              | PRODUTO             | 3LT       | 22,00        | 66,00      |
| 807194              | PRODUTO             | 1CX       | 15,10        | 15,10      |
| 046281              | PRODUTO             | 1 LT      | 30,00        | 30,00      |
| Qtde.total de itens | Qtde.total de itens |           |              | 6          |
| ValortotalR$        | ValortotalR$        |           |              | 138,74     |
| DescontoR$          | DescontoR$          |           |              | 8,00       |
| FreteRS             | FreteRS             |           |              | 10,00      |
| ValoraPagarR$       | ValoraPagarR$       |           |              | 140,74     |
| FORMAPAGAMENTO      | FORMAPAGAMENTO      |           | VALORPAGO R$ |            |
| Dinheiro            | Dinheiro            |           |              | 150,74     |

Tributos Totais Incidentes (Lei Federal12.741/2012):R$65,62

![Image](assets/image_000015_1983ec2390f05355449ad85660458ecd66acc685d42bb3b95f8e033851b04e8c.png)

Para poder  fazer uso desta opção  de guarda eletrônica  do arquivo  XML emitido  em contingência,  o contribuinte  deverá, previamente,  lavrar termo no livro Registro de Utilização  de Documentos Fiscais e Termos de Ocorrência - modelo 6, ou formalizar declaração de opção segundo disciplina que vier a ser estabelecida por sua Unidade Federada, assumindo total responsabilidade pela guarda do arquivo e declarando  ter ciência  que não poderá, posteriormente,  alegar problemas  técnicos para justificar a eventual  perda desta informação  eletrônica sob sua posse,  assumindo  as consequências  legais por ventura cabíveis.

![Image](assets/image_000016_72e01bcbe9c4a8ceb2d6f1a5af20a30c122d852de5791c31a808cc561e1cab30.png)

SNFeSNFCe

## 5.  Exemplo Prático

Figura 5 - Exemplo Prático de Emissão em Contingência

![Image](assets/image_000017_962c8ea8b31dad323e317399c3c06b2a7236319ebb1012782ecce799d5f86c62.png)

![Image](assets/image_000018_262521a215b073d842c287b818dbc6068758b4eed84e7a17ea3a1e6dee89feec.png)

## Tentativa de transmissão

- Há a tentativa de transmissão de uma NFC-e com numeração 20.
- Há um problema técnico na comunicação ou processamento das informações.
- Não há retorno da SEFAZ.

Observação: É vedada a reutilização, em contingência,  de número de NFC-e transmitida com tipo de emissão 'Normal'.

![Image](assets/image_000019_d00ef4665900161c710be1942232a4c962a14d522542ee0b3b1bcad48c724d4f.png)

## Emissão off-line

A NFC-e é emitida offline com numeração diferente, n° 21 , para evitar a duplicidade da nota.  Deve-se imprimir o DANFE-NFCe, em duas vias ou manter em local seguro o arquivo digital, sendo impresso para apresentar ao fisco quando solicitado

## Observações:

- Caso na tentativa de transmissão (opção 1) o serviço de comunicação seja retomado, e a NFC-e autorizada,o procedimento correto é cancelar a NFC-e n°20.
- Caso não haja tentativa de transmissão, a numeração utilizada na emissão off-line pode ser mantida.

![Image](assets/image_000020_6b2db8255811d05de7aaa4c48f8b0d9df122152c24a851590b70566045f3dd62.png)

## Transmissão

Superado o problema técnico, a NFC-e n°21 é transmitida para obtenção da autorização de uso.

Se vier  a  ser  rejeitada,  gerar  novamente  o  arquivo  com  a  mesma  numeração  e  série,  sanando  a irregularidade e transmitir novamente.

Para aquela que ficou pendente de retorno (a nota n° 20 desse exemplo):

![Image](assets/image_000021_abe570ad3bc3d9c6984dd1c815df0be0889b666813f78909b32f5642fff64c35.png)

SNFeSNFCe

## Nota Fiscal Eletrônica

MOC 7.0 - Anexo  IV, Padrões Técnicos de Contingência  O ff-line NFC-e

- inutilizar a numeração, se não autorizada; ou
- cancelar, se autorizada.

![Image](assets/image_000022_72e01bcbe9c4a8ceb2d6f1a5af20a30c122d852de5791c31a808cc561e1cab30.png)

## Documentos relacionados
_Nenhum documento relacionado conhecido._
