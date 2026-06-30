![Image](assets/image_000000_181538cba8008b7211d15e5cd978d6d0c2bf11226028da3c4f63e632b4682dd6.png)

## Projeto Nota Fiscal Eletrônica Projeto Nota Fiscal Eletrônica Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_62f467db8e75df3b69c42e4a25108c482fc63f7d81b04501ff221245ca84a411.png)

## Nota Técnica 2011 Nota Técnica 2011 /007

Prazo do Cancelamento da Nota Fiscal Eletrônica Prazo do Cancelamento da Nota Fiscal Eletrônica

![Image](assets/image_000002_7b9f322dedb8058e2d54cc8c7037b5f9b708adff65cbbc352ad555ba5d302527.png)

Versão 1.00 Dezembro 2011

![Image](assets/image_000003_3a66fc30b576bfac27b6b482a1fed6f23193ea1f2f4b163bb34e2f3fed6e5e9c.png)

## 01. Resumo

Esta edição documenta a alteração no prazo de cance lamento da NF-e pelo emitente, que passa a ser não superior a 24 horas (1 dia), contado do m omento em que foi concedida a respectiva Autorização  de  Uso  da  NF-e  e  outras  condições,  conf orme  Ato  Cotepe  ICMS  35  de  24  de novembro de 2010.

O  novo  prazo  de  cancelamento  deverá  entrar  em  vigor até  o  dia  02/01/2012,  considerando  o feriado do primeiro do ano.

![Image](assets/image_000004_331fe630ffd23ee160f43c343be41cf0b9ce5523c38c29f0785599868c7fbd94.png)

## Nota Fiscal eletrônica

## 2. Alteração de Regra de Validação existente

Alterado Web Service de cancelamento, no item 4.3.7-d do Manual de Integração - Contribuinte.

| #   | Regra de Validação                                                                                                                   | Aplic.   |   Msg | Efeito   |
|-----|--------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|
| H10 | Verificar NF-e autorizada a mais de 1 dia (24 horas), considerando também a exceção de prazo definida em legislação estadual. Obrig. |          |   220 | Rej.     |

## 03. Mensagens alteradas

Alterada  tabela  de  Códigos  de  Erros  e  Descrições  de   Mensagens  de  Erro,  no  item  5.1.1  do Manual de Integração - Contribuinte.

|   Código | RESULTADO DO PROCESSAMENTO DA SOLICITAÇÃO                           |
|----------|---------------------------------------------------------------------|
|      220 | Rejeição: Prazo de Cancelamento Superior ao Pre visto na Legislação |

## Metadados

- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nota-t-cnica-2011-007-publicada-em-26-12-2011/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nota-t-cnica-2011-007-publicada-em-26-12-2011/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nota-t-cnica-2011-007-publicada-em-26-12-2011.md)
- [Proveniência resumida](../../../../sources/provenance/nota-t-cnica-2011-007-publicada-em-26-12-2011.json)
