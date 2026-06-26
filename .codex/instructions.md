# Custo Brasil — Instruções para Codex CLI

Este é o repositório público do projeto Custo Brasil: base de documentação técnico-normativa fiscal brasileira convertida para Markdown.

## Agents

Agents em `agents/` fornecem instruções especializadas para consulta ao corpus:

| Arquivo | Função |
|---------|--------|
| `agents/pesquisador-fiscal.md` | Localiza evidência normativa fiscal |
| `agents/auditor-diff-regulatorio.md` | Compara versões de documentos |
| `agents/explicador-rejeicao.md` | Explica códigos de rejeição SEFAZ |
| `agents/analisador-schema.md` | Interpreta metadados de schemas XSD |
| `agents/especialista-reforma-tributaria.md` | Consultas IBS/CBS |
| `agents/CORPUS.md` | Referência completa do corpus |

Carregue o agent desejado com `cat agents/<arquivo>` ou inclua-o nas instruções do seu projeto.

## Skills

Skills operacionais em `skills/` para tarefas específicas:

- `skills/consultar-regra-fiscal/`
- `skills/comparar-notas-tecnicas/`
- `skills/explicar-rejeicao-sefaz/`
- `skills/mapear-campo-xml/`
- `skills/localizar-regra-vigente/`
- `skills/reforma-tributaria/`
- `skills/navegar-corpus/`

## Corpus

Documentos convertidos para Markdown em `corpus/`. Metadata em `metadata.json` com procedência e hash.

## Limites

Não substitui fonte oficial, schema XML ou validação por órgão competente.
