# Registro de alterações (*Changelog*)

Todas as alterações notáveis deste projeto são documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
e este projeto adota o [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [Não lançado]

### Adicionado
- Exemplo ativo de código-fonte nos anexos ([`pos-textuais/anexos.tex`](pos-textuais/anexos.tex)) referenciando o arquivo externo [`codigos/exemplo-eficiencia.py`](codigos/exemplo-eficiencia.py) via `\lstinputlisting`, com `pre-textuais/lista-de-codigos.tex` habilitado em [`tcc-depro-ufs.tex`](tcc-depro-ufs.tex).
- Link direto e selo no [`README.md`](README.md) para abrir a última versão da branch `main` diretamente no Overleaf (com `pdfLaTeX` e `tcc-depro-ufs.tex` pré-selecionados).
- Instruções detalhadas no [`README.md`](README.md) sobre como abrir e configurar o repositório no [Oleafly](https://oleafly.com/) (via arquivo `.zip`, `git clone` / `oleafly open` ou integração com o GitHub).
- Arquivos de documentação, governança e metadados na raiz do repositório: [`CHANGELOG.md`](CHANGELOG.md), [`CITATION.cff`](CITATION.cff), [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md), [`SECURITY.md`](SECURITY.md) e [`THIRD_PARTY_LICENSES.md`](THIRD_PARTY_LICENSES.md), além da ampliação do guia [`CONTRIBUTING.md`](CONTRIBUTING.md).

## [1.0.0] - 2026-11-15

### Adicionado
- Estrutura inicial completa do modelo LaTeX (`abnTeX2`) para TCC do DEPRO/UFS (`tcc-depro-ufs.tex`, `pre-textuais/`, `capitulos/`, `pos-textuais/`, `referencias.bib` e `dados/exemplo-tabela.csv`).
- Logotipos vetoriais da UFS (`figuras/logo-ufs.pdf`), do DEPRO (`figuras/logo-depro.pdf`, acompanhado do vetor editável `figuras/logo-depro.svg`) e identidade visual do repositório (`figuras/logo-projeto.svg`).
- Ambiente flutuante `quadro` e `Lista de quadros` própria, separados de `table` (`booktabs`).
- Suporte nativo a códigos-fonte via `listings` (compatível com `pdfLaTeX` sem `--shell-escape`, acentos UTF-8 em português, estilos pré-configurados para `Python`, `R`, `SQL`, `Matlab` e `VBA`, macro `\fontecodigo` e `pre-textuais/lista-de-codigos.tex` opcional).
- Importação de tabelas externas via CSV (`csvsimple`), fluxograma metodológico nativo em TikZ (`capitulos/procedimentos-metodologicos.tex`) e suporte opcional à ficha catalográfica (`pdfpages`).
- Automação de compilação com `.latexmkrc`, `Makefile` e workflow de integração contínua no GitHub Actions (`.github/workflows/build.yml`).

### Corrigido e aprimorado em relação ao modelo DOCX original
- Posicionamento do Sumário como último elemento pré-textual (ABNT NBR 14724).
- Contagem sequencial oculta a partir da folha de rosto e numeração arábica visível a partir da Introdução.
- Folha de rosto limpa e nomenclatura oficial para `REFERÊNCIAS` e `LISTA DE ABREVIATURAS E SIGLAS` (ordenada alfabeticamente).
- Correção da equação de exemplo e unificação dos símbolos ($A = \pi r^2$), formatação de alíneas (ABNT NBR 6024) e metadados básicos de acessibilidade no PDF.

[Não lançado]: https://github.com/LucasReSilva/modelo-tcc-depro-ufs/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/LucasReSilva/modelo-tcc-depro-ufs/releases/tag/v1.0.0
