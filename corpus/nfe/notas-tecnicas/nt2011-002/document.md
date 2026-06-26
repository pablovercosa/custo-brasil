![Image](assets/image_000000_83c23eb121948b933e255e5cfa5405d567f44d6beae3a199330cc2dcb5a97816.png)

## Projeto Nota Fiscal Eletrônica

![Image](assets/image_000001_96dc2e06b312306cac636d35253c15b1c1fb715829aec532575dca6f08e4dab3.png)

## Nota Técnica 2011/002

Divulga novas regras de validação para recepção de NF-e

![Image](assets/image_000002_b0999d8f160de60eb8ac921b1ec8c51b5647a67f293b0c3996af5c5c565b5855.png)

Março-2011

![Image](assets/image_000003_342f208eb1b069e6c3e0cc13d79566c2821e9c48fe68c93fa0351695faeea7a3.png)

## 1.  Resumo

Esta edição divulga as seguintes alterações no proc esso de recepção de NF-e:

## a)  Regra de recepção das NF-e da versão 1.10 após 3 1/03/2011

Implementação de regras para impedir a recepção de notas fiscais  da  versão  1.10 emitidas com data de emissão posterior à 31/03/2011 .

A  NF-e  emitidas  em  ambiente  de  produção  com  data  de   emissão  anterior  à 01/04/2011 serão recepcionadas pelo prazo de 30 dia s conforme previsto na regra GB13 ou outro limite conforme critério definido pel a SEFAZ.

O ambiente de homologação deixará de recepcionar a  NF-e da versão 1.10 a partir do dia 01/04/2011.

O prazo máximo de implementação das alterações em a mbiente de produção é 31/03/2011.

## b)  Regra de recepção de NF-e da versão 2.00 em ambi ente de homologação

Para facilitar a identificação das notas fiscais em itidas em ambiente de homologação, as informações  do  destinatário/remetente  das  notas  fis cais  deverão  ser  preenchidas  da seguinte forma:

| Campo              | tag         | Conteúdo                                                                         |
|--------------------|-------------|----------------------------------------------------------------------------------|
| CNPJ               | CNPJ (E02)  | conteúdo vazio - operação com o exterior; 99.999.999/0001-91 - demais operações. |
| Razão Social/Nome  | xNome (E04) | NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL                       |
| Inscrição Estadual | IE (E17)    | conteúdo vazio                                                                   |

As  demais  informações  do  destinatário/remetente  pod erão  ser  preenchidas  com  as informações que o emissor desejar.

Exemplo de preenchimento para operação interna

```
<dest> <CNPJ> 00000000000191 </CNPJ> <xNome> NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL </xNome> <enderDest> (...) </enderDest> <IE></IE> </dest>
```

Exemplo de preenchimento para operação com exterior

```
<dest> <CNPJ></CNPJ> <xNome> NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL </xNome> <enderDest> (...)
```

![Image](assets/image_000004_342f208eb1b069e6c3e0cc13d79566c2821e9c48fe68c93fa0351695faeea7a3.png)

&lt;/enderDest&gt; &lt;IE&gt;&lt;/IE&gt; &lt;/dest&gt;

As  notas  fiscais  que  forem  preenchidas  de  forma  diversa  do  estabelecido  serão rejeitadas.

Esta regra será aplicada a partir do dia 01/05/2011  em ambiente de homologação.

![Image](assets/image_000005_05fc05d3490fa3414f5a8bc52d53e219087e3e99d9f555ff850ae06b6fabd7b7.png)

## 2.  Novas regras de validação

## 2.1 Verificar a recepção de NF-e da versão 1.10 após 01 /04/2011

| #       | Campo   | Regra de Validação                                                                    | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                       |
|---------|---------|---------------------------------------------------------------------------------------|----------|-------|----------|--------------------------------------------------------------------------------------|
|         |         | B - Identificação da NF-e                                                             |          |       |          |                                                                                      |
| GB09.02 | B09     | Data de Emissão posterior à 31/03/2011 (NT 2011.002)                                  | Obrig.   |   595 | Rej.     | Rejeição: A versão do leiaute da NF-e utilizada não é mais válida                    |
| GB09.03 | B24     | Data de Recepção posterior à 31/03/2011 e tpAmb (B24) = 2 - homologação (NT 2011.002) | Obrig.   |   596 | Rej.     | Rejeição: Ambiente de homologação indisponível para recepção de NF-e da versão 1.10. |

## 2.2 Verificar o CNPJ, Razão Social e IE do destinatário  de NF-e emitida em ambiente de homologação

| #      | Campo   | Regra de Validação                                                                                                                            | Aplic.   |   Msg | Efeito   | Descrição Erro                                                                                                                                            |
|--------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
|        |         | E - Identificação do Destinatário                                                                                                             |          |       |          |                                                                                                                                                           |
| GE02.3 | E02     | Se tpAmb (B24) = 2: o CNPJ (E02) deve ser 99.999.999/0001-91 ou ter conteúdovazio (NT 2011.002)                                               | Facult.  |   597 | Rej.     | Rejeição: NF-e emitida em ambiente de homologação com CNPJ do destinatário diferente de 99999999000191                                                    |
| GE04   | E04     | Se tpAmb (B24) = 2: o xNome (E04) deve ser informado com a literal 'NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL' (NT 2011.002) | Obrig    |   598 | Rej.     | Rejeição: NF-e emitida em ambiente de homologação com Razão Social do destinatário diferente de NF-E EMITIDAEM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL |
| GE17.2 | E17     | Se tpAmb (B24) = 2: a IE (E17) deve ter conteúdo vazio (NT 2011.002)                                                                          | Facult.  |   599 | Rej.     | Rejeição: NF-e emitida em ambiente de homologação com IE do destinatário diferente de vazio                                                               |

![Image](assets/image_000006_05fc05d3490fa3414f5a8bc52d53e219087e3e99d9f555ff850ae06b6fabd7b7.png)

## 3.  Novas Mensagens de Rejeição

|   595 | Rejeição: A versão do leiaute da NF-e utilizada não é mais válida                                                                                            |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   596 | Rejeição: Ambiente de homologação indisponível para recepção de NF-e da versão 1.10.                                                                         |
|   597 | Rejeição: NF-e emitida em ambiente de homologação c om CNPJ do destinatário diferente de 99999999000191                                                      |
|   598 | Rejeição: NF-e emitida em ambiente de homologação c om Razão Social do destinatário diferente de NF-E E MITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL |
|   599 | Rejeição: NF-e emitida em ambiente de homologação c om IE do destinatário diferente de vazio                                                                 |