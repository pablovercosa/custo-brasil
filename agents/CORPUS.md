# Referência do Corpus Público — Custo Brasil

Este documento descreve a estrutura e os padrões do corpus público de documentos fiscais brasileiros. Agents e skills devem consultar esta referência para navegar, localizar e interpretar corretamente os documentos.

## Estrutura de diretórios

O corpus está organizado em **8 categorias temáticas** sob `corpus/`:

```
corpus/
├── nfe/                      # NF-e (modelo 55) + NFAg + NFGas + NFeABI
│   ├── notas-tecnicas/       # Notas Técnicas (ex: nt-2023-001)
│   ├── informes-tecnicos/    # Informes Técnicos (ex: it-2024-002)
│   ├── manuais/              # Manuais (ex: manual-de-orienta-o-ao-contribuinte)
│   ├── schema/               # Schemas XSD por PL
│   └── Estado de <UF>/       # Documentos estaduais (SP, RS, ES, DF, GO, PR, RJ)
├── nfce/                     # NFC-e (modelo 65)
├── nfag/                     # NF de Água e Saneamento Eletrônica
├── nfgas/                    # NF de Gás Eletrônica
├── nfeabi/                   # NF ABI Eletrônica
├── reforma-tributaria/       # IBS/CBS/Reforma Tributária do Consumo
├── combustiveis/             # Tributação Monofásica de Combustíveis
├── geral/                    # Tabelas transversais e CNPJ Alfanumérico
│   ├── tabelas-federais/     # Tabelas de CFOP, NCM, municípios, etc.
│   ├── notas-tecnicas/       # NTs conjuntas (ex: dfe-ntcj-cnpj-alfa)
│   └── informes-tecnicos/    # Informes gerais (NCM, municípios)
├── cte/                      # CT-e (reservado para expansão)
├── mdfe/                     # MDF-e (reservado para expansão)
└── nfse/                     # NFS-e (reservado para expansão)
```

## Estrutura de um documento

Cada documento segue um dos dois formatos:

### Documento narrativo (PDF convertido)
```
corpus/{categoria}/{subdir}/{slug}/
├── document.md       # Conteúdo Markdown com front matter YAML
├── metadata.json     # Metadados estruturados
└── assets/           # Imagens extraídas (PNG, referenciadas via paths relativos)
```

### Documento tabular (planilha convertida)
```
corpus/{categoria}/{subdir}/{slug}/
├── README.md         # Descrição e contexto (com front matter YAML)
├── metadata.json     # Metadados estruturados
└── csv/              # Dados tabulares (CSV, um por aba)
```

### Schema XML
```
corpus/{categoria}/schema/{PL}/
├── {arquivo}.xsd
└── ...
```

## Front Matter YAML

Todo `document.md` e `README.md` inicia com front matter YAML. Campos disponíveis:

```yaml
---
slug: nt-2023-001
title: Título completo do documento
canonical_id: nt-2023-001
category: nota_tecnica     # ver tabela abaixo
status: published
source_family: portal_nacional_nfe
source_url: https://www.nfe.fazenda.gov.br/...
authority: Portal Nacional da Nota Fiscal Eletrônica
converted_at: 2026-06-25T14:52:45+00:00
original_sha256: abc123def456...
original_filename: NT_2023_001.pdf
---

...
```

### Categorias de documento

| Categoria | Uso |
|-----------|-----|
| `nota_tecnica` | Notas Técnicas do ENCAT / Portal NF-e |
| `informe_tecnico` | Informes Técnicos (tabelas, atualizações) |
| `manual` | Manuais de especificação técnica |
| `tabela` | Tabelas federais (CFOP, NCM, municípios, etc.) |
| `cbenef` | Códigos de Benefícios Fiscais estaduais |

### Campos úteis para consulta

- `status`: sempre `published` para documentos publicados
- `source_url`: URL oficial de onde o documento foi obtido
- `original_sha256`: hash SHA-256 do arquivo original (para verificação de integridade)
- `converted_at`: data/hora UTC da conversão para Markdown
- `original_filename`: nome do arquivo original na fonte

### Validação do documento

O `metadata.json` contém a seção `validation`:

```json
{
  "validation": {
    "asset_count": 42,
    "image_refs_count": 42,
    "missing_image_refs_count": 0,
    "contains_base64_images": false,
    "contains_data_image": false,
    "assets_validated": true,
    "links_validated": true,
    "schema_validated": true,
    "valid": true
  }
}
```

## Changelog

O histórico de cada documento está em:

```
changelog/{categoria}/{subdir}/{slug}.md
```

Cada changelog contém:
- Slug e descrição
- Categoria e fonte
- SHA-256 do original
- Histórico cronológico de versões com timestamps
- Descrição de cada alteração (publicação, correção de metadados, etc.)

## Convenção de slugs

| Tipo | Padrão | Exemplo |
|------|--------|---------|
| Nota Técnica | `nt-{ano}-{numero}[-{sufixo}]` | `nt-2023-001`, `nt-2018-004-cancelamento-por-substitui-o-da-nfc-e` |
| Informe Técnico | `it{ano}-{numero}[-{sufixo}]` | `it2024-002v1-11`, `it-2025-002-v-1-50` |
| Manual | `{prefixo-descritivo}` | `manual-de-orienta-o-ao-contribuinte`, `anexo-i-leiaute-e-regra-de-valida-o` |
| Tabela | `tabela-{assunto}` | `tabela-cfop-2023`, `tabela-ncm-2022` |
| cBenef | `cbenef-{uf}` | `cbenef-sp`, `cbenef-rs` |
| NT Conjunta | `dfe-ntcj-{ano}-{numero}` | `dfe-ntcj-2025-001-cnpj-alfa-v1-00` |
| NFAg | `moc-nfag-{assunto}` | `moc-nfag-visaogeral-v1-00k` |
| NFGas | `moc-nfgas-{assunto}` | `moc-nfgas-anexo-i-leiaute-v1-00f` |
| NFeABI | `moc-nfeabi-{assunto}` | `moc-nfeabi-anexo-i-leiaute-e-rv-v2-00` |

## Documentos estaduais

Documentos de âmbito estadual estão sob `corpus/nfe/Estado de <UF>/`:

```
nfe/Estado de SP/   → cbenef-sp, cbenef-sp-ods, cbenef-sp-html
nfe/Estado de RS/   → cbenef-rs, validacoes-cbenef-rs
nfe/Estado de ES/   → cbenef-es
nfe/Estado de DF/   → edital-transacao-pgdf
nfe/Estado de GO/   → cbenef-go-html
nfe/Estado de PR/   → cbenef-pr-html
nfe/Estado de RJ/   → cbenef-rj-html
```

Estes documentos pertencem às respectivas SEFAZs estaduais (`source_family: sefaz_sp`, `sefaz_rs`, etc.) e podem conter regras específicas daquele estado.

## Schemas XSD

Schemas XML estão organizados por categoria e versão de PL:

```
corpus/nfe/schema/PL_009n/
corpus/nfe/schema/PL_009o/
corpus/nfe/schema/PL_009v/
corpus/nfe/schema/PL_010/
corpus/nfe/schema/PL_010v/
corpus/nfce/schema/PL_009n/
corpus/nfce/schema/PL_009o/
corpus/nfag/schema/PL_001a/
corpus/nfgas/schema/PL_001a/
corpus/reforma-tributaria/schema/PL_IBS_001/
corpus/geral/schema/PL_CTE_001/
corpus/geral/schema/PL_MDFE_001/
corpus/geral/schema/PL_NFSE_001/
```

## Como localizar documentos

### Por tipo e ano
Navegue por `corpus/{categoria}/{subdir}/` e filtre pelo slug:
- NTs de 2023 → `corpus/nfe/notas-tecnicas/` → slugs começando com `nt-2023` ou `nt2023`
- Informes → `corpus/nfe/informes-tecnicos/` ou categoria equivalente
- Manuais NF-e → `corpus/nfe/manuais/`
- Tabelas federais → `corpus/geral/tabelas-federais/`

### Por slug exato
O slug corresponde ao nome do diretório do documento.
Ex: `slug: nt-2023-001` → `corpus/nfe/notas-tecnicas/nt-2023-001/`

### Por hash SHA-256
O campo `original_sha256` no front matter de cada documento permite verificar integridade e encontrar a versão exata de um original.

### Por categoria + estado
Documentos estaduais → `corpus/nfe/Estado de <UF>/<slug>/`

## Observações importantes

1. **Imagens**: Todos os Markdown usam imagens referenciadas (`assets/image_NNNNN_hash.png`), nunca Base64.
2. **Links**: Links entre documentos usam caminhos relativos compatíveis com Obsidian e GitHub.
3. **Documentos tabulares** (categoria `tabela`) usam `README.md` em vez de `document.md`.
4. **Documentos vazios**: As categorias `cte/`, `mdfe/`, `nfse/` estão reservadas sem documentos.
5. **Reforma Tributária**: Documentos sobre IBS/CBS estão em `corpus/reforma-tributaria/`.
6. **Combustíveis**: Documentos sobre tributação monofásica estão em `corpus/combustiveis/`.
