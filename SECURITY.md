# Política de Segurança

O `modelo-tcc-depro-ufs` é um modelo de código aberto em LaTeX voltado à compilação local e em nuvem (Oleafly, linha de comando, Overleaf e GitHub Actions). Levamos a integridade dos arquivos-fonte, dos scripts de automação e do fluxo de compilação a sério.

## Relatando uma vulnerabilidade

**Por favor, não reporte problemas de segurança em *issues* públicas, discussões ou *pull requests*.**

Em vez disso, utilize o relato privado de vulnerabilidades do GitHub:

1. Acesse a aba **Security** do repositório → **Report a vulnerability** (ou abra diretamente <https://github.com/LucasReSilva/modelo-tcc-depro-ufs/security/advisories/new>).
2. Descreva o problema, o arquivo/versão afetada e os passos necessários para reprodução.

Buscamos acusar o recebimento do relato em até **72 horas** e publicar uma correção ou mitigação para problemas confirmados com a maior brevidade possível. Caso deseje, daremos os devidos créditos nas notas de versão (*release notes*); caso contrário, manteremos o anonimato.

## Escopo — o que merece atenção especial

Embora este repositório contenha primariamente código-fonte LaTeX e arquivos de compilação, interessam-nos especialmente relatos sobre:

- **Execução arbitrária de comandos / primitivas inseguras em TeX:** qualquer alteração, macro ou dependência proposta no modelo que exija `--shell-escape`, invoque `\write18` ou execute comandos externos durante a compilação sem consentimento explícito. Por padrão de segurança e compatibilidade, o modelo deve compilar integralmente em `pdfLaTeX` sem `--shell-escape`.
- **Segurança no fluxo de CI (GitHub Actions e `Makefile`):** permissões excessivas, exposição indevida de tokens, ações de terceiros não confiáveis ou possibilidade de injeção de comandos em [`.github/workflows/build.yml`](.github/workflows/build.yml) e [`Makefile`](Makefile).
- **Integridade de ativos e links externos:** arquivos vetoriais/PDF malformados em `figuras/`, arquivos CSV em `dados/` ou links maliciosos/comprometidos na documentação.

## Limitações conhecidas (por design)

- **Execução em compiladores TeX locais:** o repositório distribui apenas código-fonte `.tex`, `.bib`, `.csv` e ativos vetoriais. A segurança da compilação em máquina local depende da configuração da distribuição LaTeX instalada (TeX Live, MiKTeX ou TinyTeX). Recomenda-se nunca habilitar `--shell-escape` ao compilar arquivos de origem desconhecida.
- **Ausência de armazenamento de credenciais:** o projeto não gerencia segredos, bancos de dados ou serviços em execução.

## Versões suportadas

As correções de segurança e ajustes críticos são aplicados na branch `main` e publicados na versão seguinte. Apenas a série de lançamento mais recente recebe suporte ativo:

| Versão | Suportada |
| --- | --- |
| `1.0.x` (última release / `main`) | ✅ |
| Versões anteriores | ❌ |
