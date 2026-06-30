---
title: "Manual SEFAZ Virtual para Empresas"
slug: "manual-svan-v1-00"
category: "manual"
source_family: "portal_nacional_nfe"
original_sha256: "b22555575763026a1318165447401f3efd64340d281600e79ef8dec55e09f647"
converted_at_utc: "2026-06-26T15:51:43.776024+00:00"
status: "published"
type: "manual"
---
**Projeto Nota Fiscal Eletrônica**

![](/home/projetos/custo-brasil/runtime/work/nfe/manuais/manual-svan-v1-00/assets/media/image1.jpeg)

Orientações de Utilização

do Sefaz Virtual Ambiente Nacional para as Empresas

Versão 1.0

##### Fevereiro 2008

Sumário:

[1. Introdução 3](#introdução)

[2. O que é o Sefaz Virtual 4](#o-que-é-o-sefaz-virtual)

[3. Benefícios e Vantagens do Sefaz Virtual 5](#benefícios-e-vantagens-do-sefaz-virtual)

[4. Orientações para as Empresas no Ambiente de Homologação 6](#orientações-para-as-empresas-no-ambiente-de-homologação)

[4.1. Cadastro da Empresa 6](#cadastro-da-empresa)

[4.2. Obter o certificado digital do ambiente de homologação 6](#obter-o-certificado-digital-do-ambiente-de-homologação)

[4.3. Experimentos necessários e indicados neste ambiente 7](#experimentos-necessários-e-indicados-neste-ambiente)

[4.4. Exclusão de cadastro de empresa no SVAN 7](#exclusão-de-cadastro-de-empresa-no-svan)

[5. Orientações para as Empresas no Ambiente de Produção 8](#orientações-para-as-empresas-no-ambiente-de-produção)

[5.1. Seguir Orientações para as Empresas no Ambiente de Homologação 8](#seguir-orientações-para-as-empresas-no-ambiente-de-homologação)

[5.2. Solicitar autorização para a empresa operar em ambiente de produção 8](#solicitar-autorização-para-a-empresa-operar-em-ambiente-de-produção)

[5.3. Obter o certificado digital do ambiente de produção 8](#obter-o-certificado-digital-do-ambiente-de-produção)

[6. Serviços do Sefaz Virtual 9](#serviços-do-sefaz-virtual)

[6.1. Recepção de Lote de NF-e 10](#recepção-de-lote-de-nf-e)

[6.2. Consulta ao Processamento de Lote de NF-e 10](#consulta-ao-processamento-de-lote-de-nf-e)

[6.3. Cancelamento de NF-e 11](#cancelamento-de-nf-e)

[6.4. Inutilização de Numeração de NF-e 11](#inutilização-de-numeração-de-nf-e)

[6.5. Consulta à Situação Atual da NF-e 11](#consulta-à-situação-atual-da-nf-e)

[6.6. Consulta ao Status do Serviço 12](#consulta-ao-status-do-serviço)

[7. Contatos 13](#contatos)

[8. Referências 14](#referências)

# Introdução

Este documento contém orientações para as Secretarias Estaduais de Fazenda e Empresas participantes do projeto Sefaz Virtual Ambiente Nacional (SVAN), no que se refere à definição das especificações e critérios técnicos adotados para os ambientes de homologação e de produção.

# O que é o Sefaz Virtual

O Sefaz Virtual Ambiente Nacional, ou apenas Sefaz Virtual, é um ambiente computacional seguro, de alta disponibilidade e de elevado desempenho que visa assumir as funcionalidades das Secretarias Estaduais de Fazenda (Sefaz), que optarem por utilizar a infra-estrutura necessária para participar do projeto da Nota Fiscal Eletrônica.

As principais funcionalidades identificadas para o ambiente de Sefaz Virtual são:

- Manter atualizada uma base de dados com o cadastro dos contribuintes autorizados a emitir NF-e, para cada Sefaz cujo ambiente está integralmente suportado por esta solução;

- Recepcionar notas fiscais eletrônicas e lotes de NF-e;

- Processar notas fiscais eletrônicas e lotes de NF-e;

- Autorizar notas fiscais eletrônicas e lotes de NF-e;

- Cancelar NF-e autorizadas;

- Inutilizar numeração de NF-e;

- Disponibilizar a consulta da situação atual de um documento de NF-e;

- Fornecer informações sobre o status de serviço.

# Benefícios e Vantagens do Sefaz Virtual

O projeto Sefaz Virtual viabiliza os seguintes benefícios e vantagens aos contribuintes e Secretarias Estaduais de Fazenda participantes:

- Redução de custos e entraves burocráticos, facilitando o cumprimento das obrigações tributárias e o pagamento de impostos e contribuições;

- Um melhor intercâmbio e compartilhamento de informações entre os fiscos;

- Disponibilizar um ambiente computacional seguro, de alta disponibilidade e de elevado desempenho;

- Viabilizar a participação no projeto de um número maior de empresas contribuintes, localizadas em todo o território nacional;

- Fornecer um ambiente único e padronizado para as Secretarias de Fazenda e empresas participantes do projeto.

# Orientações para as Empresas no Ambiente de Homologação



Para participar do Sefaz Virtual como empresa emissora de NF-e, o primeiro passo a ser realizado pela empresa é entrar em contato com a Secretaria Estadual de Fazenda correspondente à UF onde ela está situada.

Depois de confirmado seu cadastro junto á Sefaz Virtual, a empresa deverá preparar seu ambiente computacional para se comunicar com o SVAN.

Em seguida, a empresa poderá realizar, por tempo indeterminado, experimentos com sua solução tecnológica em um ambiente de testes, denominado ambiente de homologação. Este ambiente, em termos computacionais, é similar ao de produção.

Se a empresa optar por não mais participar do Sefaz Virtual, ela deverá solicitar a exclusão dos seus dados cadastrais junto á Sefaz.

Seguem as definições de cada uma dessas etapas a serem realizadas pelas empresas interessadas:

# Cadastro da Empresa

O cadastro de inclusão de empresas autorizadas a emitir NF-e, é realizado pela Secretaria Estadual de Fazenda correspondente à UF onde a empresa está situada.

Para o cadastro da empresa, a empresa deverá enviar um e-mail para Secretaria Estadual de Fazenda, conforme modelo apresentado no Anexo I deste documento. Este e-mail deverá conter:

> 1.      As informações solicitadas sobre a empresa emissora de NF-e (CNPJ, CNPJ matriz, IE e UF);
>
> 2.      Como anexo, os certificados digitais (chave pública, formato ".cer") de cada um dos aplicativos clientes que utilizarão as funcionalidades do Sefaz Virtual.

De possa das informações solicitadas, a Sefaz encaminhará o e-mail enviado pela empresa para a equipe do Sefaz Virtual efetivar o seu cadastro.

# Obter o certificado digital do ambiente de homologação

Para que a empresa inicie a efetiva comunicação com o ambiente de homologação do Sefaz Virtual, é necessário obter o certificado digital da Sefaz Virtual para o referido ambiente.

A partir do certificado digital obtido poderá ser extraída a cadeia de autorização a ser instalada no ambiente computacional da empresa.

O procedimento para obtenção do certificado digital está descrito no Anexo II deste documento.

# Experimentos necessários e indicados neste ambiente

Os experimentos indicados para serem realizados estão relacionados a seguir:

- Utilizar o serviço de Recepção de Lotes de NF-e em um número mínimo de dez (10) vezes;

- Utilizar o serviço de Cancelamento de NF-e em um número mínimo de dez (10) vezes;

- Utilizar o serviço de Inutilização de Faixa de Numeração de NF-e em um número mínimo de dez (10) vezes;

- Utilizar o serviço de Consulta ao Status do Serviço em um número mínimo de dez (10) vezes;

- Utilizar o serviço de Consulta à situação da NF-e em um número mínimo de dez (10) vezes.

A versão do XML dos arquivos de NF-e utilizado no SVAN é igual ou superior a 1.10.

# Exclusão de cadastro de empresa no SVAN

Caso a empresa não deseje mais utilizar os serviços da SVAN, deverá solicitar a exclusão de cadastro de contribuinte através do procedimento similar à inclusão, ou seja, enviar um e-mail para a Sefaz contendo seus dados cadastrais, solicitando a exclusão.

Ao solicitar a exclusão, os dados da empresa informada serão excluídos de ambos os ambientes: de homologação e de produção. O modelo para a solicitação de exclusão está apresentado no Anexo I deste documento.

De possa das informações solicitadas, a Sefaz encaminhará o e-mail enviado pela empresa para a equipe do Sefaz Virtual excluir o cadastro realizado anteriormente.

Importante ressaltar que a empresa será efetivamente excluída somente se não houver a obrigatoriedade da participação da mesma no projeto.

# Orientações para as Empresas no Ambiente de Produção

Seguem as definições de cada uma dessas etapas a serem realizadas pelas empresas interessadas em utilizar as funcionalidades do Sefaz Virtual, no ambiente de produção:

# Seguir Orientações para as Empresas no Ambiente de Homologação 

O ambiente de homologação tem uma estrutura computacional similar de produção. Após solicitar o cadastro no SVAN, por meio da Sefaz correspondente à UF onde a empresa está instalada, a empresa tem a possibilidade de realizar uma séries de experimentos em um ambiente de testes, o ambiente de homologação.

Na seção 4 estão descritos os passos sugeridos às empresas interessadas em atuar como emissor de NF-e. Após realizá-los, a empresa terá condições plenas para participar como emissor de NF-e no ambiente de produção.

# Solicitar autorização para a empresa operar em ambiente de produção

Quando a empresa contribuinte identificar sua completa aderência ao processo de emissão de NF-e e mitigação de dúvidas com relação aos serviços oferecidos pelo SVAN, ela deverá entrar em contato com a Secretaria Estadual de Fazenda informando a finalização dos experimentos e para solicitar sua autorização para operar no ambiente de produção.

A Sefaz, por sua vez, emitirá em seguida um e-mail para a equipe do Sefaz Virtual, conforme modelo apresentado no Anexo I, informando a autorização da referida empresa como emissora de NF-e, no ambiente de produção.

# Obter o certificado digital do ambiente de produção

Uma vez que a empresa foi autorizada, de forma similar ao procedimento realizado para o ambiente de homologação, ela deverá obter o certificado digital do Sefaz Virtual para o ambiente de produção para iniciar a efetiva comunicação com este ambiente.

A partir do certificado digital obtido deverá ser extraída a cadeia de autorização a ser instalada no ambiente computacional da empresa.

O procedimento para obtenção do certificado digital está descrito no Anexo II deste documento.

# Serviços do Sefaz Virtual

A Sefaz Virtual foi desenvolvida para fornecer os mesmos serviços que as Secretarias Estaduais de Fazenda. Para atingir tal objetivo, foram seguidas as especificações técnicas apresentadas no Manual de Integração do Contribuinte \[1\]. Dessa forma, o ambiente computacional da Sefaz Virtual disponibiliza os seguintes serviços:

a)  Recepção de NF-e;

<!-- -->

1.  Recepção de Lote;

2.  Consulta Processamento de Lote;

<!-- -->

b)  Cancelamento de NF-e;

c)  Inutilização de numeração de NF-e;

d)  Consulta à situação atual da NF-e;

e)  Consulta ao status do serviço.

A Figura 1 apresenta um esquema da estrutura e funcionamento da Sefaz Virtual.

![](/home/projetos/custo-brasil/runtime/work/nfe/manuais/manual-svan-v1-00/assets/media/image2.jpeg)

Figura 1 - Esquema de Funcionamento do SEFAZ Virtual

Para cada serviço oferecido, há um Web Service específico. Um Web Service (ou serviço Web) é uma aplicação baseada em mensagens XML publicada, localizada e chamada através da internet. Sua função é de encapsular, contratar funções e objetos remotos oferecidos via um protocolo padrão e reconhecido. 

Na Sefaz Virtual, o fluxo de comunicação é sempre iniciado pelo aplicativo do contribuinte através do envio de uma mensagem ao Web Service com a solicitação do serviço desejado. Em contrapartida, o Web Service sempre devolve uma mensagem de resposta confirmando o recebimento da solicitação de serviço ao aplicativo do contribuinte na mesma conexão.

A solicitação de serviço poderá ser atendida na mesma conexão ou ser armazenada em filas de processamento nos serviços mais críticos para um melhor aproveitamento dos recursos de comunicação e de processamento da Sefaz Virtual.

Os serviços podem ser síncronos ou assíncronos em função da forma de processamento da solicitação de serviços:

a)  Serviços síncronos -- o processamento da solicitação de serviço é concluído na mesma conexão, com a devolução de uma mensagem com o resultado do processamento do serviço solicitado;

b)  Serviços assíncronos -- o processamento da solicitação de serviço não é concluído na mesma conexão, havendo a devolução de uma mensagem de resposta com um recibo que apenas confirma o recebimento da solicitação de serviço. O aplicativo do contribuinte deverá realizar uma nova conexão para consultar o resultado do processamento do serviço solicitado anteriormente.

As subseções seguintes apresentam uma breve descrição sobre cada um dos serviços disponibilizados pela SVAN às empresas contribuintes participantes. Maiores detalhes quanto ao funcionamento e padrões de comunicação utilizados podem ser obtidos no Manual de Integração do Contribuinte \[1\], acessível a partir do Portal da NF-e \[2\].

Não faz parte do escopo do SEFAZ Virtual, oferecer o Web Service destinado à consulta ao cadastro de contribuintes do ICMS da unidade federada.

# Recepção de Lote de NF-e

- Função: serviço destinado à recepção de mensagens de lote de NF-e.

- Descrição do processo: esta funcionalidade é responsável por receber as mensagens de envio de lotes de NF-e e colocá-las na fila de entrada.

- URL deste serviço do Sefaz Virtual:

  - Ambiente de Homologação:

> <https://hom.nfe.fazenda.gov.br/NfeRecepcao/NfeRecepcao.asmx>

- Ambiente de Produção:

> <https://www.sefazvirtual.fazenda.gov.br/NfeRecepcao/NfeRecepcao.asmx>

# Consulta ao Processamento de Lote de NF-e

- Função: serviço destinado a retornar o resultado do processamento do lote de NF-e.

- Descrição do processo: este serviço é responsável por receber as mensagens de consulta do resultado do processamento do lote de NF-e, e retornar mensagem com o resultado da consulta.

- URL deste serviço do Sefaz Virtual:

  - Ambiente de Homologação:\
    <https://hom.nfe.fazenda.gov.br/NFeRetRecepcao/NFeRetRecepcao.asmx>

  - Ambiente de Produção:

> <https://www.sefazvirtual.fazenda.gov.br/NFeRetRecepcao/NFeRetRecepcao.asmx>

# Cancelamento de NF-e

- Função: serviço destinado ao atendimento de solicitações de cancelamento de Notas Fiscais Eletrônicas.

- Descrição do processo: esta funcionalidade é responsável por receber e processar as mensagens de cancelamento de NF-e, retornando mensagem como resultado do processamento.

- URL deste serviço do Sefaz Virtual:

  - Ambiente de Homologação:\
    <https://hom.nfe.fazenda.gov.br/NFeCancelamento/NFeCancelamento.asmx>

  - Ambiente de Produção:

> <https://www.sefazvirtual.fazenda.gov.br/NFeCancelamento/NFeCancelamento.asmx>

# Inutilização de Numeração de NF-e

- Função: serviço destinado ao atendimento de solicitações de inutilização de numeração.

- Descrição do processo: funcionalidade responsável por receber e processa as mensagens de inutilização de NF-e, retornando mensagem como resultado do processamento.

- URL deste serviço do Sefaz Virtual:

  - Ambiente de Homologação:

> <https://hom.nfe.fazenda.gov.br/NFeInutilizacao/NFeInutilizacao.asmx>

- Ambiente de Produção:

> <https://www.sefazvirtual.fazenda.gov.br/NFeInutilizacao/NFeInutilizacao.asmx>

# Consulta à Situação Atual da NF-e

- Função: serviço destinado ao atendimento de solicitações de consulta da situação atual da NF-e na Base de Dados do SEFAZ Virtual.

- Descrição do processo: funcionalidade responsável por receber as mensagens de consulta à situação atual da NF-e e retornar mensagem com o resultado da consulta.

- URL deste serviço do Sefaz Virtual:

  - Ambiente de Homologação:\
    <https://hom.nfe.fazenda.gov.br/nfeconsulta/nfeconsulta.asmx>

  - Ambiente de Produção:

> <https://www.sefazvirtual.fazenda.gov.br/nfeconsulta/nfeconsulta.asmx>

# Consulta ao Status do Serviço

- Função: serviço destinado à consulta do status do serviço prestado pelo Portal da Secretaria de Fazenda Estadual.

- Descrição do processo: funcionalidade responsável por receber as mensagens de consulta ao status do serviço e retornar mensagem com o resultado da consulta.

- URL deste serviço do Sefaz Virtual:

  - Ambiente de Homologação:\
    [https://hom.nfe.fazenda.gov.br/NFeStatusServico/NFeStatusServico.asmx](https://hom.sefazvirtual.fazenda.gov.br/NFeStatusServico/NFeStatusServico.asmx)

  - Ambiente de Produção: <https://www.sefazvirtual.fazenda.gov.br/NFeStatusServico/NFeStatusServico.asmx>

# Contatos

# 

A central de atendimento do projeto Nota Fiscal Eletrônica está disponível no contato 0800 9782338.

#  Referências

\[1\] Manual de Integração -- Contribuinte. Padrões Técnicos de Comunicação.

> Versão 2.02 -- Junho de 2007.
>
> Disponível em: <http://www.nfe.fazenda.gov.br/portal/integracao.aspx>.

\[2\] Portal da NF-e\
Disponível em: <http://www.nfe.fazenda.gov.br/portal>

## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/manuais/manual-svan-v1-00/source.json)
- [Dados normalizados](../../../../normalized/nfe/manuais/manual-svan-v1-00/normalized.json)
- [Changelog](../../../../changelog/nfe/manuais/manual-svan-v1-00.md)
- [Proveniência resumida](../../../../sources/provenance/manual-svan-v1-00.json)


## Documentos relacionados

- [manual-svan-anexo-i](../manual-svan-anexo-i/document.md)
- [manual-svan-anexo-ii](../manual-svan-anexo-ii/document.md)
