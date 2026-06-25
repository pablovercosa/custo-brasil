![Image](assets/image_000000_29ce088f7b0be9100e51d6f6feab07a958b959809e0cf990dc387b6c7e7f3462.png)

## Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_f8debb48e74944103dedb3fbc8f2a353102d70059391bd1b4df93dbadb4cef73.png)

## Nota Técnica 2013/002

## Distribuição de Documentos com Autorização de Uso pela SEFAZ

(Incentivo ao B2B)

![Image](assets/image_000002_98a3b017108aa610b4014be7e8c8a8e0c87fa5906baedf0fb46232b460c3498c.png)

Versão 1.00b Março 2013

![Image](assets/image_000003_66b9bb4511446a0e5f5a931792552ae5716e6ab57c2cff9a15b6016b8b75a97f.png)

## 01. Resumo

Esta Nota Técnica tem como objetivo orientar as empresas usuárias de processos de Business-toBusiness (B2B) a adotarem uma estrutura de dados padronizada, a partir da definição de regras de  encapsulamento  a  serem  adotadas  para  transmissão  do  adendo  B2B  dentro  da  cadeia  de fornecedores  das  empresas,  de  forma  integrada  com  a  NF-e  e  após  a  autorização  de  uso fornecida pela Sefaz Autorizadora da circunscrição do contribuinte.

Outra  inovação trazida  por  esta  Nota  Técnica é  a  possibilidade da empresa emissora de  NF-e utilizar  o  próprio  adendo  B2B  para  notificar  os  seus  clientes  sobre  a  ocorrência  de  eventos vinculados  à  NF-e,  após  a  sua  autorização  de  uso,  como  cancelamentos,  cartas  de  correção, entre outros.

Esclarecemos que esta Nota Técnica não tem por objetivo a definição de padrões específicos e sim  orientar  a  forma  de  utilização  e  encapsulamento  de padrões  setoriais,  nacionais  ou internacionais, que atendam um maior número de empresas emitentes ou destinatárias de NF-e, diminuindo o custo de customizações específicas e contribuindo para a redução do 'Custo Brasil'.

Ratificamos  que  a  legislação  não  permite  o  uso  do  campo  de  informações  complementares  e adicionais da NF-e para o registro de padrões B2B que não são refletidos no Documento Auxiliar da NF-e (DANFE) e que os adendos B2B não precisam ser enviados para as Sefaz Autorizadoras.

![Image](assets/image_000004_0ff846d0a453db96b9aca5c23b507a465f670f0a8a1fe8fec3c0a3004ecc79c4.png)

## 02. Distribuição dos Documentos com Autorização pela SEFAZ

O  Manual  de  Orientação  do  Contribuinte,  no  capítulo  10,  descreve  a  necessidade  de  envio  do arquivo digital da NF-e para o destinatário, conforme os argumentos descritos.

As  orientações  abaixo  se  propõem  a  complementar  as  informações  existentes,  substituindo  a documentação do MOC (Manual de Orientação do Contribuinte) para os itens correspondentes, e orientando  sobre  a  possibilidade  de  harmonização  de  uso  de  padrões  B2B  a  serem  adotados nacionalmente.

## 10.1 Processo de Distribuição

A modalidade tecnológica de intercâmbio do documento eletrônico entre o emissor e receptor deve ser  acordada  entre  ambos,  respeitando  o  sigilo  fiscal  e  o  padrão  de  conteúdo  de  dados  definido neste  item.  As  formas  mais  comuns  de  troca  de  informações  entre  as  empresas  no  comércio eletrônico (B2B) são:

-  troca de mensagens em sistema específico, baseado em WEB ou rede privativa;
-  troca  de  arquivos  via  EDI  (Intercambio  Eletrônico  de  Dados),  baseado  em  WEB  ou  rede privada, ou outros protocolos de troca de arquivos rastreáveis;
-  troca de mensagens via e-mail;
-  disponibilização  de  informações  em  portais,  com  acesso  sob  demanda  e  autenticação  de acesso.

## 10.2 Distribuição de Documentos Autorizados e Informações de B2B

No próximo item, é definida a forma de compartilhamentos dos documentos autorizados pela SEFAZ (NF-e, Cancelamento e Evento).

É  possível  também  a  distribuição  de  informações  unicamente  em  um  padrão  B2B  mais  amplo, incluindo  informações  relacionadas  com  a  logística  de  entrega,  transporte  e  armazenamento  das mercadorias que estão sendo transitadas entre os diferentes entes. Na adoção deste modelo mais amplo, é aconselhável evitar a definição de padrões específicos de determinada empresa, tentando adotar padrões setoriais, nacionais ou internacionais, que atendam um maior número de empresas emitentes ou destinatárias de NF-e, diminuindo o custo de customizações específicas.

De  uma  forma  geral,  esta  estrutura  de  dados  que  engloba  as  informações  dos  documentos autorizados e as informações de logística da circulação de mercadorias entre as empresas, obedece um padrão, conforme exemplo abaixo:

| #    | Campo       | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Descrição/Observação                                                                      |
|------|-------------|-------|-------|--------|---------|--------|-------------------------------------------------------------------------------------------|
| VR01 | nfeProcB2B  | Raiz  | -     | -      | -       | -      | TAG raiz                                                                                  |
| VR02 | nfeProc     | G     | VR01  | xml    | 1-1     | -      | Estrutura de dados da distribuição                                                        |
| VR03 | NFe         | G     | VR02  | xml    | 1-1     | -      |                                                                                           |
| VR04 | (dados)     | -     | -     | -      | -       | -      | Dados da NF-e, inclusive com os dados da assinatura (Anexo 1).                            |
| VR05 | protNfe     | G     | VR02  | xml    | 1-1     | -      |                                                                                           |
| VR06 | (dados)     | -     | -     | -      | -       | -      | Dados do Protocolo de Autorização de Uso (item 4.2.2)                                     |
| VR07 | NFeB2B      | G     | VR01  | xml    | 0-1     | -      |                                                                                           |
| VR08 | xIntegrador | A     | VR07  | C      | 1-1     | 2-15   | Identificador da organização, empresa ou entidade mantenedora do padrão de interface B2B. |

![Image](assets/image_000005_180d4847eba4e71ae50f6cde16caa868bca9cbddf3314751a040102131c43cf7.png)

|      |         |    |      |    |     |      | Exemplo: 'ANFAVEA', 'GS1', ..., 'XYZ'.                                    |
|------|---------|----|------|----|-----|------|---------------------------------------------------------------------------|
| VR09 | xSetor  | A  | VR07 | C  | 1-1 | 2-15 | Identificador do setor ou área a que se refere o padrão B2B, mantido pelo |
| VR10 | versao  | A  | VR07 | C  | 1-1 | 4-5  | Versão do leiaute desta área/setor de padronização B2B. Exemplo: '1.00'.  |
| VR11 | (dados) | -  | VR07 | -  | -   | -    |                                                                           |

## 10.3 Distribuição de Documentos Autorizados

## 10.3.1 Leiaute da Distribuição: NF-e

Deverá ser disponibilizado para o destinatário o mesmo conteúdo da NF-e enviada para a SEFAZ, complementada com a informação da Autorização de Uso.

## Schema XML: procNFe\_v2.00.xsd

| #    | Campo   | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Dec.   | Descrição/Observação                                          |
|------|---------|-------|-------|--------|---------|--------|--------|---------------------------------------------------------------|
| XR01 | nfeProc | Raiz  | -     | -      | -       | -      | -      | TAG raiz                                                      |
| XR02 | versao  | A     | XR01  | N      | 1-1     | 1-4    | 2      |                                                               |
| XR03 | NFe     | G     | XR01  | xml    | 1-1     | -      | -      |                                                               |
| XR04 | (dados) | -     | -     | -      | -       | -      | -      | Dados da NF-e, inclusive com os dados da assinatura (Anexo I) |
| XR05 | protNfe | G     | XR01  | xml    | 1-1     | -      | -      |                                                               |
| XR06 | (dados) | -     | -     | -      | -       | -      | -      | Dados do Protocolo de Autorização de Uso (item 4.2.2)         |

No caso de troca de arquivo entre as empresas, é sugerida a adoção do nome do arquivo como segue:

&lt;999...999&gt;-procNFe.xml, onde:

- ­ &lt;999...999&gt;: corresponde a Chave de Acesso da NF-e;
- ­ '-procNFe': identifica o processamento do documento autorizado.

## 10.3.2 Leiaute de Distribuição: Cancelamento de NF-e

Deverá ser disponibilizado para o destinatário os dados do pedido do cancelamento enviado para a SEFAZ, acrescentados os dados da homologação deste pedido de cancelamento.

## Schema XML: procCancNFe\_v2.00.xsd

| #    | Campo       | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Dec.   | Descrição/Observação                              |
|------|-------------|-------|-------|--------|---------|--------|--------|---------------------------------------------------|
| YR01 | procCancNFe | Raiz  | -     | -      | -       | -      | -      | TAG raiz                                          |
| YR02 | versao      | A     | YR01  | N      | 1-1     | 1-4    | 2      |                                                   |
| YR03 | cancNFe     | G     | YR01  | xml    | 1-1     | -      | -      |                                                   |
| YR04 | (dados)     | -     | -     | -      | -       | -      | -      | Dados do Pedido de Cancelamento (item 4.3.1)      |
| YR05 | retCancNFe  | G     | YR01  | xml    | 1-1     | -      | -      |                                                   |
| YR06 | (dados)     | -     | -     | -      | -       | -      | -      | Dados da homologação do Cancelamento (item 4.3.2) |

![Image](assets/image_000006_0ff846d0a453db96b9aca5c23b507a465f670f0a8a1fe8fec3c0a3004ecc79c4.png)

No caso de troca de arquivo entre as empresas, é sugerida a adoção do nome do arquivo como segue:

&lt;999...999&gt;-procCancNFe.xml, onde:

- ­ &lt;999...999&gt;: corresponde a Chave de Acesso da NF-e;
- ­ '-procCancNFe': identifica o processamento do documento autorizado;

## 10.3.3 Leiaute de Distribuição: Evento da NF-e

Deverá  ser  disponibilizado  para  o  destinatário  os  dados  do  Evento  enviados  para  a  SEFAZ, acrescentados os dados da homologação deste Evento.

## Schema XML: procEventoNFe\_v2.00.xsd

| #    | Campo         | Ele   | Pai   | Tipo   | Ocor.   | Tam.   | Dec.   | Descrição/Observação           |
|------|---------------|-------|-------|--------|---------|--------|--------|--------------------------------|
| ZR01 | procEventoNFe | Raiz  | -     | -      | -       | -      | -      | TAG raiz                       |
| ZR02 | versao        | A     | ZR01  | N      | 1-1     | 1-4    | 2      |                                |
| ZR03 | evento        | G     | ZR01  | xml    | 1-1     | -      | -      |                                |
| ZR04 | (dados)       | -     | -     | -      | -       | -      | -      | Dados do Evento                |
| ZR05 | retEvento     | G     | ZR01  | xml    | 1-1     | -      | -      |                                |
| ZR06 | (dados)       | -     | -     | -      | -       | -      | -      | Dados da homologação do Evento |

No caso de troca de arquivo entre as empresas, é sugerida a adoção do nome do arquivo como segue:

&lt;999...999&gt;\_&lt;888888&gt;-procEventoNFe.xml, onde:

- ­ &lt;999...999&gt;: corresponde a Chave de Acesso da NF-e;
- ­ &lt;888888&gt;: identifica o tipo de evento (CC-e=110110, Cancelamento=110111, ...)
- ­ '-procEventoNFe': identifica o processamento do documento autorizado.