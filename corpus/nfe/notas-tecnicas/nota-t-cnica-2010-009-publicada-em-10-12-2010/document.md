![Image](assets/image_000000_08b68d3191e0bd1152ffff6b91641bd1818a89e9224becb8d80d9e9070ba40e0.png)

## Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_1dc90563abe33a63498866ca3b8f4dbcdda989a112a454842ffe2a866acc4e32.png)

## Nota Técnica 2010/009

Disciplinar o uso do Ambiente de Autorização da SEFAZ, identificando e dando ciência para as empresas das situações de 'uso indevido' deste ambiente.

![Image](assets/image_000002_36a1715a4b29ae68dbadd1e1fa8e9eaefe4931e5f4b72f70552748571bc81475.png)

Setembro - 2010

![Image](assets/image_000003_92e0a4f6dcbaf7ec5dbff0de00f88da13f060eced50d194d0f2c0df5d7074223.png)

## NOTA FISCAL ELETRÔNICA

## 1.  Resumo

Esta nota técnica tem como objetivo disciplinar o u so do Ambiente de Autorização da SEFAZ,  identificando  e  dando  ciência  para  as  empres as  das  situações  de  'uso indevido' deste ambiente, pelas empresas.

## 2.  Instruções Operacionais

A análise do comportamento atual das aplicações das  empresas ('aplicação cliente') permitiu  identificar  as  situações  de  'uso  indevido'   do  ambiente  de  autorização  de Nota Fiscal Eletrônica, mantidos pelas SEFAZ.

Estas  situações  de  'uso  indevido'  estão  descritas  n o  documento  de  'Consumo Indevido do Ambiente de Autorização', disponível no Portal Nacional (www.nfe.fazenda.gov.br/portal), no menu 'Legislação e Documentos', item 'Documentos Diversos'.

O documento citado, além de identificar as situações de uso indevido, orienta sobre as  melhores  práticas  a  serem  seguidas  pelas  empresa s,  estabelece  metas  e descreve as ações a serem tomadas pela SEFAZ para o  atingimento destas metas.

## 3.  Novas Regras de Validações

A  validação  do  uso  de  namespace  indevido  e  de  carac teres  de  edição  nas mensagens deve ser implementada no bloco de Validação da Área de Dados dos Web Services da versão 2.00 existentes com o acréscimo das seguintes regras de validação:

| #    | Regra de Validação                                                                                                   | Aplic.   |   Msg | Efeito   |
|------|----------------------------------------------------------------------------------------------------------------------|----------|-------|----------|
| D01d | Verifica a existência de qualquer namespace diverso do namespace padrão da NF-e (http://www.portalfiscal.inf.br/nfe) | Facul.   |   587 | Rej.     |
| D01e | Verifica a existência de caracteres de edição no in ício ou fim da mensagem ou entre as tags                         | Facul.   |   588 | Rej.     |

|   # | Descrição da Mensagem                                                                                               |
|-----|---------------------------------------------------------------------------------------------------------------------|
| 587 | Rejeição: Usar somente o namespace padrão da NF-e                                                                   |
| 588 | Rejeição: Não é permitida a presença de caracteres de edição no início/fim da mensagem ou entre as tags da mensagem |

Inicialmente, as regras serão implementadas apenas  no ambiente de homologação dos Web Services da versão 2.00.

![Image](assets/image_000004_92e0a4f6dcbaf7ec5dbff0de00f88da13f060eced50d194d0f2c0df5d7074223.png)

## NOTA FISCAL ELETRÔNICA

4.  Exemplos de Rejeição: 587-Rejeição: Usar somente  o namespace padrão da NF-e

O uso de namespace diverso do namespace padrão da NF-e (xmlns="http://www.portalfiscal.inf.br/nfe") nas mensagens XML  da NF-e é vedado e passará a ser rejeitado com o código " 587-Rejeição: Usar somente o namespace padrão da NF-e ".

Exemplo de mensagem XML que não atende o padrão do  projeto:

&lt;?xml version="1.0" encoding="UTF-8"?&gt;&lt;consStatServ xmlns="h ttp://www.portalfiscal.inf.br/nfe" xmlns:ds=http://www.w3.org /2000/09/xmldsig# xmlns:xsi=http://www.w3.org/2001/XMLSchemainstance xsi:schemaLocation=http://www.portalfiscal.inf.br/nf e:\SF\Schemas\consStatServ\_v2.00.xsd versao="2.00"&gt;&lt;tpAmb&gt;2&lt;/ tpAmb&gt;&lt;cUF&gt;35&lt;/cUF&gt;&lt;xServ&gt;STATUS&lt;/xServ&gt;&lt;/consStatServ&gt;

O XML acima tem os seguintes namespaces na tag consStatServ :

- 1)  xmlns:xsi=http://www.w3.org/2001/XMLSchema-instance xsi:schemaLocation=http://www.portalfiscal.inf.br/nf e:\SF\Schemas\consStatServ\_v2.00.xsd
- 2) xmlns:xsd=http://www.w3.org/2001/XMLSchema
- 3) xmlns=http://www.portalfiscal.inf.br/nfe

A  mensagem  será  rejeitada  pelo  Web  Service  da  SEFAZ   com  motivo: "587Rejeição: Usar somente o namespace padrão da NF-e" .

Para sanear o problema, a mensagem XML deverá ter s omente o namespace do projeto como segue:

&lt;?xml version="1.0" encoding="UTF-8"?&gt;&lt;consStatServ xmlns="h ttp://www.portalfiscal.inf.br/nfe" versao="2.00"&gt;&lt;tpAmb&gt;2&lt;/t pAmb&gt;&lt;cUF&gt;35&lt;/cUF&gt;&lt;xServ&gt;STATUS&lt;/xServ&gt;&lt;/consStatServ&gt;

![Image](assets/image_000005_92e0a4f6dcbaf7ec5dbff0de00f88da13f060eced50d194d0f2c0df5d7074223.png)

5.  Exemplos de Rejeição caracteres de edição no início/fim da mensagem ou entre as tags da mensagem ão : 588 - Rejeição: Não é permitida a presença de caracteres de edição no início/fim da mensagem ou entre as tags da Rejeição: Não é permitida a presença de caracteres de edição no início/fim da mensagem ou entre as tags da

O  Manual  de  Integração  do  Contribuinte  veda  a  inclusão  de  caract eres  no arquivo XML ("line-feed", "carriage return", "tab", caracteres de "espaço" entre as TAGs) (item 3.2.1-c do Manual). ntegração  do  Contribuinte  veda  a  inclusão  de  caract eres  no feed", "carriage return", "tab", caracteres de "espaço" entre as c do Manual). ntegração  do  Contribuinte  veda  a  inclusão  de  caract eres  no feed", "carriage return", "tab", caracteres de "espaço" entre as

Exemplo de mensagem XML que não atende o padrão do  projeto Exemplo de mensagem XML que não atende o padrão do  projeto Exemplo de mensagem XML que não atende o padrão do  projeto:

```
= 8crescimo de linha/espaco no inicio d8 mens8gem <?xml·version="1.0"·encoding="UTF-8"? <consStatServ·xmlns="http://www.portalfiscal.inf.br/nfe "·versao="2.00"> <tpAmb>2</tpAmb = acrescimo de <cR2 entre tags <cUF>35</cUF> <xServ>STATUS</xServ </consStatServ T acrescimo de <TAB2 de identacao 10 =acrescimode linha/espacono fim da mensagem
```

Esta mensagem será  rejeitada pelo Web Service da SEFAZ com motivo: Rejeição: Não é permitida a presença de caracteres  de edição no início/fim da mensagem ou entre as tags da mensagem" rejeitada pelo Web Service da SEFAZ com motivo: Rejeição: Não é permitida a presença de caracteres  de edição no início/fim da mensagem ou entre as tags da mensagem" . rejeitada pelo Web Service da SEFAZ com motivo: "588 Rejeição: Não é permitida a presença de caracteres  de edição no início/fim

Todos os caracteres de ed caracteres de edição devem ser eliminados como segue: ão devem ser eliminados como segue:

&lt;?xml version="1.0" encoding="UTF ttp://www.portalfiscal.inf.br/nfe" versao=" pAmb&gt;&lt;cUF&gt;35&lt;/cUF&gt;&lt;xServ&gt;STATUS&lt;/xServ&gt;&lt;/consStatServ " encoding="UTF-8"?&gt;&lt;consStatServ xmlns="h rtalfiscal.inf.br/nfe" versao="2.00"&gt;&lt;tpAmb&gt;2&lt;/t pAmb&gt;&lt;cUF&gt;35&lt;/cUF&gt;&lt;xServ&gt;STATUS&lt;/xServ&gt;&lt;/consStatServ 8"?&gt;&lt;consStatServ xmlns="h "&gt;&lt;tpAmb&gt;2&lt;/t pAmb&gt;&lt;cUF&gt;35&lt;/cUF&gt;&lt;xServ&gt;STATUS&lt;/xServ&gt;&lt;/consStatServ&gt;

## Metadados

- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nota-t-cnica-2010-009-publicada-em-10-12-2010/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nota-t-cnica-2010-009-publicada-em-10-12-2010/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nota-t-cnica-2010-009-publicada-em-10-12-2010.md)
- [Proveniência resumida](../../../../sources/provenance/nota-t-cnica-2010-009-publicada-em-10-12-2010.json)
