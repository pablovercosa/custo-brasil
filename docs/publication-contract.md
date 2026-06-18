# Contrato de publicação pública

Cada publicação documental deve ser atômica por documento ou revisão.

## Arquivos esperados por versão

```text
corpus/nfe/notas-tecnicas/nt-2025-002/v1.33/
├── NT_2025_002_v1_33.md
├── assets/
│   └── figure-001.png
└── provenance.json
```

## Conteúdo mínimo da procedência

- autoridade/fonte;
- URL da página-fonte;
- URL direta de download, quando houver;
- nome oficial do arquivo;
- data e hora do download;
- SHA-256 do original;
- versão e status;
- publicação e vigência quando conhecidas;
- relação com versão anterior/substituta.

## Stage permitido por documento

Somente paths em `sources/`, `corpus/`, `normalized/` e `changelog/` ligados ao documento atual. É proibido usar `git add .`.
