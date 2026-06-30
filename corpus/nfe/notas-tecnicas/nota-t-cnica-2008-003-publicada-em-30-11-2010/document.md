![Image](assets/image_000000_dd2ad4f71d8efb2ebbc167d4a35ac83aefebc704148aab528431cea111f93f29.png)

## Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_23df8919fce260704a8bc46cec3a6b03e65bf2d92b7a434232ab1120ee9bc7fd.png)

## Nota Técnica 2008.003

Divulga alteração na regra de validação da NF-e complementar

![Image](assets/image_000002_2db0526f72795fe9ff9421284d9453a0577cd1d4af4f969ffd71d79f0ceba909.png)

Abril-2008

![Image](assets/image_000003_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

## 1.  Resumo

Divulga  alteração  da  regra  de    validação  da  NF-e  complementar  -  Manual  de Integração do Contribuinte - versão 2.0.2.

## 2.  Contexto

Atualmente  a  emissão  de  NF-e  de  complemento  de  valor  ou  de  imposto  só  é permitida para a complementação de uma NF-e.

Esta restrição impede que os emissores obrigados emitam uma NF-e de complemento  para  complementar  uma  operação  acobertada  por  uma  NF  modelo 1/1A.

## 3.  Solução

Alteração das regras de validação G30 e G31 para aceitar a informação de NF-e ou NF normal como NF referenciada.

## 3.1 Alteração da regra de validação G30, páginas 32

## Aonde se lê:

| G30   | Se finalidade da NF-e = 2 (NF-e complementar): verificar se foi informado uma NF-e referenciada   | Obrig.   | 254   | Rej.   |
|-------|---------------------------------------------------------------------------------------------------|----------|-------|--------|

## leia-se:

| G30   | Se finalidade da NF-e = 2 (NF-e complementar): verificar se foi informado uma NF referenciada   | Obrig.   | 254   | Rej.   |
|-------|-------------------------------------------------------------------------------------------------|----------|-------|--------|

## 3.2 Alteração da regra de validação G31, páginas 33

## Aonde se lê:

| G31   | Se finalidade da NF-e = 2 (NF-e complementar): verificar se foi informada uma NF referenciada (NF normal ou NF-e)   | Obrig.   | 255   | Rej.   |
|-------|---------------------------------------------------------------------------------------------------------------------|----------|-------|--------|

## leia-se:

| G31   | Se finalidade da NF-e = 2 (NF-e complementar): verificar se foi informado mais de uma NF referenciada (NF normal ou NF-e)   | Obrig.   | 255   | Rej.   |
|-------|-----------------------------------------------------------------------------------------------------------------------------|----------|-------|--------|

![Image](assets/image_000004_2cf3aec89793c818f2bf1905551957621d1081334be23b3949ac12fb0a032a13.png)

## 3.3 Alteração de texto das mensagens 254 e 255, página 66

## Aonde se lê:

|   254 | Rejeição: NF-e referenciada não informada para NF-e complementar         |
|-------|--------------------------------------------------------------------------|
|   255 | Rejeição: Informada mais de uma NF-e referenciada para NF-e complementar |

## leia-se:

|   254 | Rejeição: NF-e Complementar não possui NF referenciada         |
|-------|----------------------------------------------------------------|
|   255 | Rejeição: NF-e Complementar possui mais de uma NF referenciada |

## 4.  Prazo de implementação

- dia 16/04/08: implantação no ambiente de homologação das empresas;

- dia 23/04/08: implantação em produção.

## 5.  Fase de Transição

O contribuinte deve emitir a NF-e complementar de NF-e ou NF modelo 1/1A, informando o campo finNFe (B26) com o código 1-NF-e normal e a respectiva NF referenciada (campo refNFe - B13 ou grupo refNF - B14), até que a alteração seja implementada em ambiente de produção.

As  dúvidas  e  sugestões  devem  ser  encaminhadas  através  do  Canal  Fale  Conosco  da Secretaria  da  Fazenda  de  São  Paulo  (http://www.fazenda.sp.gov.br/email/default2.asp) referente à 'Portaria CAT 104/07'.

## Metadados

- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nota-t-cnica-2008-003-publicada-em-30-11-2010/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nota-t-cnica-2008-003-publicada-em-30-11-2010/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nota-t-cnica-2008-003-publicada-em-30-11-2010.md)
- [Proveniência resumida](../../../../sources/provenance/nota-t-cnica-2008-003-publicada-em-30-11-2010.json)


## Documentos relacionados

- [[nota-t-cnica-2007-004-publicada-em-15-09-2011]]
- [[nota-t-cnica-2007-007-publicada-em-30-11-2010]]
- [[nota-t-cnica-2008-001-publicada-em-30-11-2010]]
- [[nota-t-cnica-2008-005-publicada-em-30-11-2010]]
- [[nota-t-cnica-2009-001-publicada-em-29-11-2010]]
- [[nota-t-cnica-2009-002-publicada-em-29-11-2010]]
- [[nota-t-cnica-2009-004-publicada-em-30-11-2010]]
- [[nota-t-cnica-2010-002-publicada-em-29-11-2010]]
