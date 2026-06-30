![](cabecalho.jpg)


# Custo Brasil

Base pública, versionada e rastreável de documentação técnico-normativa fiscal brasileira, organizada para leitura em Markdown, Obsidian e ferramentas de IA.

Deixar que a IA leia os PDFs disponibilizados pela Receita Federal consome muitos tokens. Utilizá-los em formato Markdown fará bem ao seu bolso.

Cada documento publicado preserva procedência, fonte, nome oficial, data de download, hash e status de versão. Versões históricas não são apagadas.

O projeto não substitui a fonte oficial, os schemas oficiais, a legislação aplicável ou a validação pelos órgãos competentes.

## Instalação

### OpenCode

1. Clone o repositório:
   ```bash
   git clone git@github.com:pablovercosa/custo-brasil.git
   cd custo-brasil
   ```

2. O `opencode.json` na raiz já configura automaticamente:
   - Agents como subagentes selecionáveis via `@` (ex: `@pesquisador-fiscal`)
   - Skills públicas em `skills/` carregadas automaticamente
   - `agents/CORPUS.md` como instrução de base

3. Use `@agent-nome` no chat para ativar o agent desejado, ou carregue a skill via `/skill`.

### Claude Code (Anthropic)

1. Clone e entre no diretório.
2. O `CLAUDE.md` na raiz é carregado automaticamente. Ele descreve agents, skills e estrutura do corpus.
3. Para usar um agent específico, inclua o arquivo no prompt:
   ```
   Leia e siga agents/pesquisador-fiscal.md e agents/CORPUS.md como instruções.
   ```

### Codex CLI (OpenAI)

1. Clone e entre no diretório.
2. O `.codex/instructions.md` é carregado automaticamente.
3. Para usar um agent, carregue o arquivo como instrução adicional:
   ```
   cat agents/pesquisador-fiscal.md agents/CORPUS.md | codex --instructions -
   ```

### Obsidian (visualização do corpus)

1. Abra a pasta do repositório como um cofre do Obsidian.
2. Navegue por `corpus/` para ler os documentos convertidos.
3. Links relativos entre documentos funcionam nativamente.

## Fórmulas

`formulas/` reúne fórmulas para cálculos tributários (ICMS próprio, ICMS-ST, PIS/COFINS não cumulativo, IBS/CBS) referenciadas aos documentos normativos do corpus. Cada fórmula contém front matter com `sources` ligando aos slugs dos documentos que a fundamentam.

## Agents e Skills

Agents especializados em `agents/` para consulta fiscal, diff de versões, análise de schemas, explicação de rejeições SEFAZ e reforma tributária. Skills operacionais em `skills/` com passo-a-passo para cada tarefa.

## Estrutura

```
formulas/
├── icms/               # ICMS próprio e ST
├── pis-cofins/         # PIS/COFINS não cumulativo
├── reforma-tributaria/ # IBS e CBS
├── ipi/                # (reservado)
└── iss/                # (reservado)

corpus/
├── nfe/                    # NF-e (modelo 55) + NFAg + NFGas + NFeABI
├── nfce/                   # NFC-e (modelo 65)
├── nfag/                   # NF de Água e Saneamento Eletrônica
├── nfgas/                  # NF de Gás Eletrônica
├── nfeabi/                 # NF ABI Eletrônica
├── reforma-tributaria/     # IBS/CBS/Reforma Tributária
├── combustiveis/           # Tributação Monofásica de Combustíveis
├── geral/                  # Tabelas transversais (CFOP, NCM, municípios, etc.)
├── cte/                    # CT-e (reservado)
├── mdfe/                   # MDF-e (reservado)
└── nfse/                   # NFS-e (reservado)
```

Cada documento contém `document.md` (ou `README.md` para dados tabulares), `metadata.json` com procedência e hash, e `assets/` com imagens referenciadas.

## Pastas públicas

| Pasta | Conteúdo |
|-------|----------|
| `corpus/` | Documentos convertidos (Markdown + assets + metadados), organizados por categoria fiscal |
| `changelog/` | Histórico de versões de cada documento, com timestamps e descrição de cada alteração |
| `sources/` | Metadados de origem e procedência: manifesto global, registros de proveniência por documento, e páginas-fonte organizadas por família |
| `normalized/` | Dados normalizados extraídos dos documentos, índices por autoridade/categoria/status, e artefatos estruturados (tabelas, campos, regras, rejeições, diffs de versão) |
| `formulas/` | Fórmulas para cálculos tributários referenciadas aos documentos normativos do corpus |
| `agents/` | Agents especializados para consulta fiscal (pesquisador, diff de versões, análise de schema, rejeição SEFAZ, reforma tributária) |
| `skills/` | Skills operacionais com passo-a-passo para cada tarefa |
| `docs/` | Documentação complementar (ex: contrato de publicação) |

## Documentos incluídos

- **169 documentos** convertidos: 136 PDFs (Docling), 28 planilhas (XLSX/XLS/ODS → CSV), 5 páginas HTML
- **8 categorias fiscais** ocupadas, 3 reservadas para expansão
- **239 schemas XSD** organizados por PL
- **3.415 imagens** extraídas e referenciadas como assets

## Licença

Este projeto é fornecido apenas para consulta. Consulte sempre as fontes oficiais para validação de informações fiscais.
