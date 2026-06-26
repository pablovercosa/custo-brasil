# Custo Brasil — Projeto

Base pública, versionada e rastreável de documentação técnico-normativa fiscal brasileira.

## Agents especializados

Agents em `agents/` para consulta fiscal, diff de versões, explicação de rejeições SEFAZ, análise de schemas XSD e reforma tributária. Use `@agent-name` no OpenCode ou carregue o arquivo correspondente:

- `agents/pesquisador-fiscal.md` — localiza evidência normativa no corpus
- `agents/auditor-diff-regulatorio.md` — compara versões de documentos
- `agents/explicador-rejeicao.md` — explica códigos de rejeição SEFAZ
- `agents/analisador-schema.md` — interpreta metadados de schemas XSD
- `agents/especialista-reforma-tributaria.md` — consultas IBS/CBS
- `agents/CORPUS.md` — referência completa da estrutura do corpus

Antes de usar qualquer agent, leia `agents/CORPUS.md` para entender a estrutura de diretórios, campos de front matter, categorias e localização de documentos.

## Skills operacionais

Skills em `skills/` fornecem passo-a-passo para tarefas específicas:

- `skills/consultar-regra-fiscal/`
- `skills/comparar-notas-tecnicas/`
- `skills/explicar-rejeicao-sefaz/`
- `skills/mapear-campo-xml/`
- `skills/localizar-regra-vigente/`
- `skills/reforma-tributaria/`
- `skills/navegar-corpus/`

## Corpus

Documentos convertidos em `corpus/` organizados por categoria fiscal: `nfe/`, `nfce/`, `nfag/`, `nfgas/`, `nfeabi/`, `reforma-tributaria/`, `combustiveis/`, `geral/`.

Cada documento contém:
- `document.md` ou `README.md` — conteúdo convertido para Markdown
- `metadata.json` — procedência, hash, fonte, status
- `assets/` — imagens referenciadas

Changelog em `changelog/` espelha a estrutura do corpus.

## Limites

Este projeto não substitui a fonte oficial, os schemas oficiais, a legislação aplicável ou a validação pelos órgãos competentes. Decisões fiscais e contábeis devem sempre ser confirmadas com as fontes oficiais e profissionais habilitados.
