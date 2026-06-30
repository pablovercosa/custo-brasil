---
title: "Manual SVAN - Anexo II"
slug: "manual-svan-anexo-ii"
category: "manual"
source_family: "portal_nacional_nfe"
original_sha256: "6f514b60d58c92e804da4b943bc31c06efd71cabe57a2dfca03a0d0e2b116c04"
converted_at_utc: "2026-06-26T15:51:44.796377+00:00"
status: "published"
type: "manual"
---
**Anexo II**

Os endereços das URLs a partir das quais poderão ser obtidos os certificados digitais para os ambientes de homologação e de produção, são:

- Ambiente de Homologação:

> [**https://hom.nfe.fazenda.gov.br/NFeRetRecepcao/NFeRetRecepcao.asmx**](https://hom.sefazvirtual.fazenda.gov.br/NFeRetRecepcao/NFeRetRecepcao.asmx)

- Ambiente de Produção:

> [**https://www.sefazvirtual.fazenda.gov.br/NFeRetRecepcao/NFeRetRecepcao.asmx**](https://www.sefazvirtual.fazenda.gov.br/NFeRetRecepcao/NFeRetRecepcao.asmx)

Nas seções abaixo serão descritos os procedimentos para verificar a instalação do certificado digital e para obtenção e instalação deste.

No que diz respeito à obtenção do certificado digital, é apresentado somente o passo a passo para obtenção do certificado no ambiente de produção, pelo fato do procedimento diferir apenas quanto à URL a partir da qual ele será obtido.

1.  Verificar instalação do certificado digital

A seqüência de passos a ser adotada para confirmação da prévia instalação do referido certificado no navegador Internet Explorer, em sua versão 6.0.

a.  Acione a seqüência Ferramentas -\> Opções da Internet -\> Aba Conteúdo -\> Opção Certificados da seção Certificados.

![](/home/projetos/custo-brasil/runtime/work/nfe/manuais/manual-svan-anexo-ii/assets/media/image1.jpeg)

b.  Na aba "Outras pessoas" são enumerados os certificados digitais instalados no navegador. Na figura abaixo está representada a inexistência de quaisquer certificados confiáveis, de outras pessoas, instados no navegador.

![](/home/projetos/custo-brasil/runtime/work/nfe/manuais/manual-svan-anexo-ii/assets/media/image2.jpeg)

c.  No caso do certificado digital utilizado no ambiente de produção do SVAN, teria que estar relacionado um certificado com as seguintes informações:

- Emitido para: www.nfe.fazenda.gov.br, emitido pela: "Autoridade Certificadora do Serpro Final v1"

![](/home/projetos/custo-brasil/runtime/work/nfe/manuais/manual-svan-anexo-ii/assets/media/image3.jpeg)

Para confirmar se toda a cadeia de certificados está instalada:

1.  acione a aba "Autoridades de certificação intermediárias" e verifique se constam as seguintes informações:

- Emitido para : "Autoridade Certificadora do SERPRO v1", emitido pela "Autoridade Certificadora Raiz Brasileira".

- Emitido para : Autoridade Certificadora do SERPRO Final v1, emitido pela "Autoridade Certificadora do SERPRO v1".

2.  acione a aba "Autoridades de certificação raiz confiáveis" e verifique se constam as seguintes informações:

- Emitido para : "Autoridade Certificadora Raiz Brasileira", emitido pela "Autoridade Certificadora Raiz Brasileira".

Se já houver esse certificado instalado no seu navegador e toda a cadeia de certificados descrita acima, a primeira etapa para obtenção do certificado inicia-se no item *n* do procedimento abaixo descrito, na seção 6.2.2. Caso contrário, é necessário iniciar do item a para instalar o certificado no navegador e posteriormente realizar a sua exportação.

1.  Instalar e obter o certificado digital

Abaixo está descrito o procedimento para obtenção do certificado digital do ambiente de produção, de onde a empresa poderá extrair a cadeia de autorização a ser instalada no ambiente computacional da empresa. O procedimento descrito também é realizado a partir do navegador Internet Explorer, versão 6.0.

a.  Acesse o site do Portal da NF-e: <https://www.nfe.fazenda.gov.br/portal/>

![](/home/projetos/custo-brasil/runtime/work/nfe/manuais/manual-svan-anexo-ii/assets/media/image4.jpeg)

b.  Clique duas vezes sobre o ícone em formato de cadeado, localizado na barra de status do navegador, à direita do monitor. Será exibida uma janela para exibição dos dados do certificado digital.

Acione a opção "Instalar certificado".

![](/home/projetos/custo-brasil/runtime/work/nfe/manuais/manual-svan-anexo-ii/assets/media/image5.jpeg)

c.  Será exibida uma janela de boas vindas do "Assistente para importação de certificados".

Acione a opção "Avançar".

![](/home/projetos/custo-brasil/runtime/work/nfe/manuais/manual-svan-anexo-ii/assets/media/image6.jpeg)

d.  Selecione um local específico para armazenar o certificado ou deixe que o assistente selecione automaticamente o local de armazenamento do certificado de acordo com o tipo do certificado.

Acione a opção "Avançar".

![](/home/projetos/custo-brasil/runtime/work/nfe/manuais/manual-svan-anexo-ii/assets/media/image7.jpeg)

e.  Em seguida, acione a opção "Concluir".

![](/home/projetos/custo-brasil/runtime/work/nfe/manuais/manual-svan-anexo-ii/assets/media/image8.jpeg)

f.  Se a importação foi realizada com sucesso, será exibida uma janela similar à apresentada abaixo.

![](/home/projetos/custo-brasil/runtime/work/nfe/manuais/manual-svan-anexo-ii/assets/media/image9.jpeg)

g.  Verifique se toda a cadeia de certificados já está instalada no navegador. Para isso realize a seguinte seqüência de comandos:

Ferramentas -\> Opções da Internet -\> Aba Conteúdo -\> Opção Certificados -\> Aba Outras Pessoas -\> Selecione o certificado emitido para www.nfe.fazenda.gov.br -\> Acione a opção Exibir. Será aberta uma janela intitulada Certificado. Nesta janela, acione a aba "Caminho de certificação". Deverão estar relacionada a cadeia completa de certificados:

- Autoridade Certificadora Raiz Brasileira

- Autoridade Certificadora do SERPRO v1

- Autoridade Certificadora do SERPRO Final v1

- www.nfe.fazenda.gov.br

> Se a cadeia não estiver completa execute todos os itens seguintes desse procedimento. Caso a cadeia esteja completa, como na figura a seguir, você poderá iniciar o procedimento para exportação do certificado, descrito a partir do item *m* deste passo a passo.

![](/home/projetos/custo-brasil/runtime/work/nfe/manuais/manual-svan-anexo-ii/assets/media/image10.jpeg)

Para cada uma das entidades não instaladas no navegador, execute os procedimentos descritos nos itens h a m. Ao final, deverá estar instalada toda a cadeia de certificados, como mostrado na figura acima.

h.  Clique duas vezes sobre o ícone do cadeado localizado na barra de status do site do Portal da NF-e.

Acione a aba "Caminho de certificação".

![](/home/projetos/custo-brasil/runtime/work/nfe/manuais/manual-svan-anexo-ii/assets/media/image11.jpeg)

i.  Selecione uma das entidades que necessitam ser instaladas. Clique duas vezes sobre ela. Serão exibidos os dados relativos ao certificado selecionado.\
    Acione a opção "Instalar certificado".

![](/home/projetos/custo-brasil/runtime/work/nfe/manuais/manual-svan-anexo-ii/assets/media/image12.jpeg)

j.  Será exibida a tela de boas vindas do "Assistente para importação de certificados".\
    Acione a opção Avançar.

![](/home/projetos/custo-brasil/runtime/work/nfe/manuais/manual-svan-anexo-ii/assets/media/image13.jpeg)

k.  Selecione um local específico para armazenar o certificado ou deixe que o assistente selecione automaticamente o local de armazenamento do certificado de acordo com o tipo do certificado.

Acione a opção "Avançar".

![](/home/projetos/custo-brasil/runtime/work/nfe/manuais/manual-svan-anexo-ii/assets/media/image14.jpeg)

l.  Em seguida, acione a opção "Concluir".

![](/home/projetos/custo-brasil/runtime/work/nfe/manuais/manual-svan-anexo-ii/assets/media/image15.jpeg)

m.  Se a importação foi realizada com sucesso, será exibida uma janela similar à apresentada abaixo.

![](/home/projetos/custo-brasil/runtime/work/nfe/manuais/manual-svan-anexo-ii/assets/media/image16.jpeg)

n.  Agora iniciaremos o processo para exportação do certificado instalado em um formato de arquivo desse tipo.

Execute a seguinte seqüência de comandos: Ferramentas -\> Opções da Internet -\> Aba Conteúdo -\> Opção Certificados -\> Aba Outras Pessoas

![](/home/projetos/custo-brasil/runtime/work/nfe/manuais/manual-svan-anexo-ii/assets/media/image17.jpeg)

o.  Selecione o certificado emitido para www.nfe.fazenda.gov.br e acione a opção Exportar. Será exibida a tela de boas vindas do "Assistente para exportação de certificados".

![](/home/projetos/custo-brasil/runtime/work/nfe/manuais/manual-svan-anexo-ii/assets/media/image18.jpeg)

p.  Selecione a extensão do certificado digital.

Acione a opção Avançar.

![](/home/projetos/custo-brasil/runtime/work/nfe/manuais/manual-svan-anexo-ii/assets/media/image19.jpeg)

q.  Defina a localização e nome do arquivo que contém o certificado exportado. Para definir o local de armazenamento, acione a opção Procurar e defina o nome na janela de seleção aberta.

Em seguida, acione a opção Avançar.

![](/home/projetos/custo-brasil/runtime/work/nfe/manuais/manual-svan-anexo-ii/assets/media/image20.jpeg)

r.  Acione a opção "Concluir".

![](/home/projetos/custo-brasil/runtime/work/nfe/manuais/manual-svan-anexo-ii/assets/media/image21.jpeg)

s.  Se a importação foi realizada com sucesso, será exibida uma janela similar à apresentada abaixo.

![](/home/projetos/custo-brasil/runtime/work/nfe/manuais/manual-svan-anexo-ii/assets/media/image22.jpeg)

t.  No local definido e com o nome do arquivo especificado, estará salvo um arquivo com o certificado exportado.

![](/home/projetos/custo-brasil/runtime/work/nfe/manuais/manual-svan-anexo-ii/assets/media/image23.jpeg)

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Após instalar o certificado com toda a cadeia de certificados autorizados, recomenda-se fortemente que a empresa realize um teste simples para confirmar a correta realização do procedimento anterior.        |
|                                                                                                                                                                                                                |
| O procedimento consiste em acessar a URL dos serviços no ambiente de homologação/produção utilizando um navegador (Internet Explorer, Mozilla Firefox, dentre outros).                                         |
|                                                                                                                                                                                                                |
| Na seção 6 do documento "Orientações de Utilização do Sefaz Virtual Ambiente Nacional para as Empresas" estão apresentadas as URLs de todos os serviços disponibilizados pela Sefaz Virtual aos contribuintes. |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## Metadados
- [Metadados do corpus](metadata.json)
- [Fonte e procedência](../../../../sources/portal_nacional_nfe/nfe/manuais/manual-svan-anexo-ii/source.json)
- [Dados normalizados](../../../../normalized/nfe/manuais/manual-svan-anexo-ii/normalized.json)
- [Changelog](../../../../changelog/nfe/manuais/manual-svan-anexo-ii.md)
- [Proveniência resumida](../../../../sources/provenance/manual-svan-anexo-ii.json)


## Documentos relacionados

- [anexo-ii-manual-especifica-est-cnicas-danfe-c-digo-barras](../anexo-ii-manual-especifica-est-cnicas-danfe-c-digo-barras/document.md)
- [anexo-iii-manual-de-conting-ncia-nf-e](../anexo-iii-manual-de-conting-ncia-nf-e/document.md)
- [anexo-iv-manual-de-conting-ncia-nfc-e](../../../nfce/manuais/anexo-iv-manual-de-conting-ncia-nfc-e/document.md)
- [manual-svan-anexo-i](../manual-svan-anexo-i/document.md)
- [manual-svan-v1-00](../manual-svan-v1-00/document.md)
