---
title: "Sistema Nota Fiscal Eletrônica"
slug: "nt2022-004-v1-10-regras-de-valida-o-issqn"
category: "nota_tecnica"
source_family: "portal_nacional_nfe"
original_sha256: "58c4bfdbb0878a8240024317f376df57da595aa6cf726ef175ee4f4a097ea05d"
converted_at_utc: "2026-06-25T15:33:57.727441+00:00"
status: "published"
type: "nota_tecnica"
---

## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/notas-tecnicas/nt2022-004-v1-10-regras-de-valida-o-issqn/source.json)
- [Dados normalizados](../../../../normalized/nfe/notas-tecnicas/nt2022-004-v1-10-regras-de-valida-o-issqn/normalized.json)
- [Changelog](../../../../changelog/nfe/notas-tecnicas/nt2022-004-v1-10-regras-de-valida-o-issqn.md)
- [Proveniência resumida](../../../../sources/provenance/nt2022-004-v1-10-regras-de-valida-o-issqn.json)

## Sistema Nota Fiscal Eletrônica

Nota Técnica 2022.004

Aperfeiçoamento de Regra de Validação de ISSQN

Versão 1.10 -Fevereiro de 2023

![Image](assets/image_000002_4f156f2c8dd28b38a94591806b062ef98645ee5a37b3e3d835ff1d2302be224e.png)

## Nota Fiscal Eletrônica

Nota Técnica 2022.004 v1.10 - Aperfeiçoamento de Regra de Validação de ISSQN

## Sumário

| Controle de Versões ............................................................................................................................3   | Controle de Versões ............................................................................................................................3    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Histórico de Alterações / Cronograma..................................................................................................4             | Histórico de Alterações / Cronograma..................................................................................................4              |
| 1                                                                                                                                                   | Resumo...........................................................................................................................................5   |
| 1.1                                                                                                                                                 | Alterações introduzidas na versão 1.10....................................................................................5                          |
| 2                                                                                                                                                   | Objetivo...........................................................................................................................................6 |
| 3                                                                                                                                                   | Regra de Validação.........................................................................................................................7         |
| 3.1                                                                                                                                                 | Verificar se a NF-e/NFC-e tem pelo menos um item sujeito ao ICMS........................................7                                            |

![Image](assets/image_000003_daff8b9eb665010935ea69799779bce55373064cdab97b881aedc0e90967f801.png)

Nota Técnica 2022.004 v1.10 - Aperfeiçoamento de Regra de Validação de ISSQN

## Controle de Versões

|   Versão | Publicação     | Descrição         |
|----------|----------------|-------------------|
|     1.10 | Fevereiro/2023 | Alteração da NT   |
|     1.00 | Dezembro/2022  | Publicação da NT. |

![Image](assets/image_000004_29181af27e9578ffb24e50a04e34d03811a5afe846e44a511a6ea99316b8d646.png)

## Nota Fiscal Eletrônica

Nota Técnica 2022.004 v1.10 - Aperfeiçoamento de Regra de Validação de ISSQN

## Histórico de Alterações / Cronograma

|   Versão | Histórico de atualizações                                            | Implantação Teste   | Implantação Produção                       |
|----------|----------------------------------------------------------------------|---------------------|--------------------------------------------|
|     1.10 | • Alteração da data de ativação em produção para DF, da regra U01-20 | 15/02/2023          | 28/02/2023                                 |
|     1.00 | • Aperfeiçoamento de regra de validação relativas ao ISSQN           | Até 28/12/2022      | 02/01/2023 Conforme, calendário da cada UF |

![Image](assets/image_000005_13b16160b02ccb658834d362d1424ee70940acd5d1e3a3d85b2447c34c1ecf51.png)

## Nota Fiscal Eletrônica

Nota Técnica 2022.004 v1.10 - Aperfeiçoamento de Regra de Validação de ISSQN

## 1    Resumo

Esta Nota Técnica - NT divulga o aperfeiçoamento da regra de validação do campo de ISSQN.

## 1.1   Alterações introduzidas na versão 1.10

A versão 1.10 visa alterar a data de ativação em produção para DF, da regra U01-20.

![Image](assets/image_000006_daff8b9eb665010935ea69799779bce55373064cdab97b881aedc0e90967f801.png)

Nota Técnica 2022.004 v1.10 - Aperfeiçoamento de Regra de Validação de ISSQN

## 2 Objetivo

Essa NT tem o objetivo de aperfeiçoar a regra de validação do campo de ISSQN, permitindo que as UF possam parametrizar com precisão a aceitação, ou não, da autorização de NF-e/NFC-e com a Tag de item de Serviço.

Visando  dar  transparência  na  identificação  da  parametrização  adotada  pela  UF,  poderá  ser realizada  consulta  na  Tabela  publicada  no  link  &lt;http://nfce.encat.org/&gt;,  aba  'Desenvolvedor', opção 'Regras de Validação'.

Essa NT não gera grandes impactos de desenvolvimento para os contribuintes, permitindo que o prazo de implantação em homologação e produção sejam reduzidos e vem da necessidade de o Distrito  Federal  adequar  a  emissão  das  notas  fiscais  eletrônicas,  modelo  55  e  65,  dos  seus contribuintes em virtude da publicação de legislação interna para implementação, no âmbito do DF, da Nota Fiscal Eletrônica de Serviço - NFS-e para itens sujeitos ao Imposto Sobre Serviços de Qualquer Natureza - ISS.

![Image](assets/image_000007_036a5fd1e563f35614e21bd34847a71048bd08a8bf0d20540504e4332a5eb899.png)

## 3 Regra de Validação

## 3.1  Verificar se a NF-e/NFC-e tem pelo menos um item sujeito ao ICMS

| Campo-Seq Modelo   | Regra de Validação                                                                                                                                                                                                                                                                                                                                                                                                        | Aplic.   | Msg Efeito   | Descrição Erro                                                           |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|--------------|--------------------------------------------------------------------------|
| U01-20 55/65       | Informado grupo de tributação do ISSQN (id:U01) sem informar nenhum grupo de ICMS (id:N01) Exceção: A critério da UF poderá ser autorizada/vedada a emissão de NF-e/NFC-e que só tenham itens sujeitos ao ISSQN. ([NT 2010/010](../nt2010-010/document.md)); Parametrizações possíveis: - 0 =Não aceita item de Serviço; - 1 =Aceita item de Serviço; - 2 =Aceita item de Serviço somente na NF-e/NFC-e conjugada (que contenha também itens de ICMS). | Facul.   | 592 Rej.     | Rejeição: A NF-e deve ter pelo menos um item de produto sujeito ao ICMS. |

![Image](assets/image_000008_6cba6ea60d678d8b48b6098c14418cea2618e407b71128547241906d30a6da96.png)

## Documentos relacionados
_Nenhum documento relacionado conhecido._
